"""Parse PEP RST with explicit string/regex rules, then export a typed graph."""
from collections import Counter
import json
from pathlib import Path
import re
import networkx as nx
from rules import CONCEPTS, OBJECTIONS, OBJECTION_SECTIONS, keyword_matches

ROOT = Path(__file__).resolve().parent
# Include plain prose, :pep:`484` roles, and common PEP-0484 links.
REFERENCE_RE = re.compile(r'\bPEP[\s-]+0*(\d+)\b|:pep:`0*(\d+)`', re.I)


def pep_references(text):
    return sorted({int(a or b) for a, b in REFERENCE_RE.findall(text)})


def parse_header(text):
    headers, current = {}, None
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            return headers, '\n'.join(lines[index+1:])
        if line[:1].isspace() and current:
            headers[current] += ' ' + line.strip()
        elif ':' in line:
            current, value = line.split(':', 1)
            current = current.strip()
            headers[current] = value.strip()
    return headers, ''


def split_sections(body):
    """Track nested RST headings so objections in subsections retain parent context."""
    lines, sections, stack, levels = body.splitlines(), [], [], {}
    buffer = []
    def flush():
        if buffer:
            sections.append((' / '.join(title for _, title in stack) or 'Preamble',
                             '\n'.join(buffer)))
            buffer.clear()
    index = 0
    while index < len(lines):
        if index+1 < len(lines):
            title, underline = lines[index].strip(), lines[index+1].strip()
            if (title and len(underline) >= len(title) and len(set(underline)) == 1
                    and underline[0] in '=-~^"`:+*#' and not lines[index][:1].isspace()):
                flush()
                level = levels.setdefault(underline[0], len(levels))
                while stack and stack[-1][0] >= level:
                    stack.pop()
                stack.append((level, title))
                index += 2
                continue
        buffer.append(lines[index])
        index += 1
    flush()
    return sections


def authors(value):
    # Remove email addresses before splitting comma-separated, folded Author fields.
    return [name.strip() for name in re.split(r',|\s+and\s+',
            re.sub(r'<[^>]*>', '', value)) if name.strip()]


def build_graph(data_dir=None):
    graph = nx.MultiDiGraph()
    documents = []
    for path in sorted(Path(data_dir or ROOT / 'data' / 'peps').glob('pep-*.rst')):
        header, body = parse_header(path.read_text(encoding='utf-8'))
        number = int(header['PEP'])
        year = re.search(r'\b(?:19|20)\d{2}\b', header.get('Created', ''))
        graph.add_node(f'pep:{number}', node_type='PEP', number=number,
                       title=header.get('Title', ''), status=header.get('Status', 'Unknown'),
                       type=header.get('Type', ''), created_year=int(year[0]) if year else '',
                       python_version=header.get('Python-Version', ''), in_scope=True)
        documents.append((number, header, body))
    if not documents:
        raise ValueError('No PEP files found; run fetch_data.py first.')

    def ensure_pep(number):
        node = f'pep:{number}'
        if node not in graph:
            graph.add_node(node, node_type='PEP', number=number, title=f'PEP {number} (external)',
                           status='Unknown', type='', created_year='', python_version='',
                           in_scope=False)
        return node

    def edge(source, target, relation, evidence, **extra):
        graph.add_edge(source, target, key=relation, relation=relation,
                       evidence=evidence, **extra)

    for number, header, body in documents:
        source = f'pep:{number}'
        for field, relation in [('Requires', 'REQUIRES'), ('Replaces', 'SUPERSEDES'),
                                ('Superseded-By', 'SUPERSEDES')]:
            for target in re.findall(r'\d+', header.get(field, '')):
                other = ensure_pep(int(target))
                left, right = (other, source) if field == 'Superseded-By' else (source, other)
                edge(left, right, relation, f'{field}: {header[field]}')
        for name in authors(header.get('Author', '')):
            person = 'person:' + name
            graph.add_node(person, node_type='Person', name=name)
            edge(source, person, 'AUTHORED_BY', f'Author: {name}')
        for match in REFERENCE_RE.finditer(body):
            target = int(match.group(1) or match.group(2))
            if target != number and not graph.has_edge(source, f'pep:{target}', 'REFERENCES'):
                edge(source, ensure_pep(target), 'REFERENCES',
                     ' '.join(body[max(0, match.start()-60):match.end()+100].split()))
        sections = split_sections(body)
        abstract = '\n'.join(content for section, content in sections
                             if section.split(' / ')[-1].lower() == 'abstract')
        introduced = keyword_matches(header.get('Title', '') + '\n' + abstract)
        mentioned = keyword_matches(body)
        for concept in sorted(set(introduced) | set(mentioned)):
            node = 'concept:' + concept
            graph.add_node(node, node_type='Concept', name=concept)
            relation = 'INTRODUCES' if concept in introduced else 'MENTIONS'
            match = introduced.get(concept, mentioned.get(concept))
            edge(source, node, relation, match['snippet'], keyword=match['keyword'])
        for section, content in sections:
            if any(cue in section.lower() for cue in OBJECTION_SECTIONS):
                for objection, match in keyword_matches(content, OBJECTIONS).items():
                    node = 'objection:' + objection
                    graph.add_node(node, node_type='Objection', name=objection)
                    # Parallel section evidence is stored in one JSON string for GraphML.
                    if graph.has_edge(source, node, 'FACED_OBJECTION'):
                        old = json.loads(graph[source][node]['FACED_OBJECTION']['evidence'])
                    else:
                        old = []
                    old.append({'section': section, 'snippet': match['snippet']})
                    edge(source, node, 'FACED_OBJECTION', json.dumps(old, ensure_ascii=False))
    return graph


def save_graph(graph, output_dir=ROOT):
    output_dir = Path(output_dir)
    state = {'nodes': [dict(id=node, **attributes) for node, attributes in sorted(graph.nodes(data=True))],
             'edges': [dict(source=left, target=right, **attributes)
                       for left, right, _, attributes in sorted(graph.edges(keys=True, data=True))]}
    (output_dir / 'knowledge_state.json').write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    nx.write_graphml(graph, output_dir / 'knowledge_state.graphml')


def main():
    graph = build_graph()
    save_graph(graph)
    print(f'Nodes: {graph.number_of_nodes()} {dict(Counter(a["node_type"] for _, a in graph.nodes(data=True)))}')
    print(f'Edges: {graph.number_of_edges()} {dict(Counter(a["relation"] for *_, a in graph.edges(data=True)))}')


if __name__ == '__main__':
    main()

"""Deterministic concept scoring and graph reasoning over the saved state."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import networkx as nx
from rules import keyword_matches

ROOT = Path(__file__).resolve().parent


def load_graph(path=None):
    state = json.loads(Path(path or ROOT / 'knowledge_state.json').read_text(encoding='utf-8'))
    graph = nx.MultiDiGraph()
    for node in state['nodes']:
        attributes = dict(node)
        graph.add_node(attributes.pop('id'), **attributes)
    for edge in state['edges']:
        attributes = dict(edge)
        left, right = attributes.pop('source'), attributes.pop('target')
        graph.add_edge(left, right, key=attributes['relation'], **attributes)
    return graph


def reading_order(graph, selected):
    """Invert dependent->prerequisite edges before topological sorting."""
    order_graph = nx.DiGraph()
    pending, visited = list(selected), set()
    while pending:
        node = pending.pop()
        if node in visited:
            continue
        visited.add(node)
        order_graph.add_node(node)
        for _, target, attributes in graph.out_edges(node, data=True):
            if attributes['relation'] == 'REQUIRES':
                order_graph.add_edge(target, node)
                pending.append(target)
    key = lambda node: graph.nodes[node]['number']
    if nx.is_directed_acyclic_graph(order_graph):
        return list(nx.lexicographical_topological_sort(order_graph, key=key)), False
    # Keep all nodes and order SCCs; no valid internal order exists within a cycle.
    condensed = nx.condensation(order_graph)
    ordered = []
    for component in nx.lexicographical_topological_sort(
            condensed, key=lambda c: min(key(n) for n in condensed.nodes[c]['members'])):
        ordered.extend(sorted(condensed.nodes[component]['members'], key=key))
    return ordered, True


def query(text, graph=None, limit=5):
    graph = graph if graph is not None else load_graph()
    concepts = sorted(keyword_matches(text))
    scores, reasons, overlaps = {}, defaultdict(list), {}
    for node, attributes in graph.nodes(data=True):
        if attributes['node_type'] != 'PEP' or not attributes.get('in_scope', False):
            continue
        matched = set()
        score = 0.0
        for _, target, edge in graph.out_edges(node, data=True):
            concept = target.removeprefix('concept:')
            if concept in concepts and edge['relation'] in ('INTRODUCES', 'MENTIONS'):
                weight = 3.0 if edge['relation'] == 'INTRODUCES' else 1.0
                matched.add(concept)
                score += weight
                reasons[node].append(f'{edge["relation"]} {concept} (+{weight:g}): {edge["evidence"]}')
        if score:
            scores[node], overlaps[node] = score, matched
    direct = dict(scores)
    # One hop from five strongest direct matches. Never propagate boosts recursively.
    seeds = sorted(direct, key=lambda n: (-direct[n], graph.nodes[n]['number']))[:5]
    boosts = defaultdict(float)
    weights = {'REQUIRES': 0.6, 'SUPERSEDES': 0.9, 'REFERENCES': 0.3}
    used = set()
    for seed in seeds:
        for left, right, edge in list(graph.out_edges(seed, data=True)) + list(graph.in_edges(seed, data=True)):
            relation = edge['relation']
            neighbor = right if left == seed else left
            if (relation not in weights or neighbor == seed or
                    not graph.nodes[neighbor].get('in_scope', False) or
                    (seed, neighbor, relation) in used):
                continue
            used.add((seed, neighbor, relation))
            gain = min(weights[relation], 1.5 - boosts[neighbor])
            if gain > 0:
                boosts[neighbor] += gain
                scores[neighbor] = scores.get(neighbor, 0) + gain
                reasons[neighbor].append(
                    f'Graph neighbor of PEP {graph.nodes[seed]["number"]}: '
                    f'PEP {graph.nodes[left]["number"]} {relation} PEP '
                    f'{graph.nodes[right]["number"]} (+{gain:g}); {edge["evidence"]}')

    warnings = []
    supersession = nx.DiGraph()
    supersession.add_nodes_from(n for n, a in graph.nodes(data=True) if a['node_type'] == 'PEP')
    supersession.add_edges_from((l, r) for l, r, a in graph.edges(data=True)
                               if a['relation'] == 'SUPERSEDES')
    resolved = {}
    replacement_warnings = defaultdict(list)
    for node in sorted(scores, key=lambda n: (-scores[n], graph.nodes[n]['number'])):
        newer = nx.ancestors(supersession, node)
        terminals = [n for n in newer if supersession.in_degree(n) == 0]
        destinations = terminals or [node]
        for destination in destinations:
            if newer:
                replacement_warnings[destination].append({'kind': 'superseded',
                    'pep': graph.nodes[node]['number'],
                    'newer_peps': sorted(graph.nodes[n]['number'] for n in newer)})
                if graph.nodes[node]['status'].lower() in ('rejected', 'withdrawn'):
                    replacement_warnings[destination].append({
                        'kind': graph.nodes[node]['status'].lower(), 'pep': graph.nodes[node]['number']})
            if newer and not terminals:
                replacement_warnings[destination].append({'kind': 'supersession_cycle',
                                                         'pep': graph.nodes[node]['number']})
            candidate_reasons = list(reasons[node])
            if destination != node:
                candidate_reasons.append(f'Supersedes matched PEP {graph.nodes[node]["number"]}; '
                                         'followed SUPERSEDES chain to its newest endpoint')
            # Merge by max rather than inflating score from many obsolete versions.
            if destination not in resolved or scores[node] > resolved[destination][0]:
                resolved[destination] = (scores[node], candidate_reasons)
    ranked = sorted(resolved, key=lambda n: (-resolved[n][0], graph.nodes[n]['number']))[:limit]
    closest = []
    for node in ranked:
        attributes = graph.nodes[node]
        warnings.extend(replacement_warnings[node])
        closest.append({'pep': attributes['number'], 'title': attributes['title'],
                        'status': attributes['status'], 'score': round(resolved[node][0], 3),
                        'why': resolved[node][1]})
        if attributes['status'].lower() in ('rejected', 'withdrawn', 'superseded'):
            warnings.append({'kind': attributes['status'].lower(), 'pep': attributes['number']})
        if not attributes.get('in_scope'):
            warnings.append({'kind': 'external_metadata_missing', 'pep': attributes['number']})
    # Preserve concerns from matched predecessors as well as recommended successors.
    concern_nodes = set(ranked)
    for node in ranked:
        concern_nodes.update(n for n in nx.descendants(supersession, node) if n in direct)
    objections = {}
    for node in sorted(concern_nodes, key=lambda n: graph.nodes[n]['number']):
        for _, target, edge in graph.out_edges(node, data=True):
            if edge['relation'] == 'FACED_OBJECTION':
                name = graph.nodes[target]['name']
                item = objections.setdefault(name, {'objection': name, 'peps': [], 'evidence': []})
                number = graph.nodes[node]['number']
                item['peps'].append(number)
                item['evidence'].extend(dict(pep=number, **entry)
                                        for entry in json.loads(edge['evidence']))
    ordered, cycle = reading_order(graph, ranked)
    if cycle:
        warnings.append({'kind': 'requires_cycle', 'message': 'No valid prerequisite order inside a cycle.'})
    if not concepts:
        novelty = 'No concepts detected; novelty cannot be assessed with this vocabulary.'
    elif not any(set(concepts) <= matched for matched in overlaps.values()):
        novelty = 'No single PEP in the selected corpus matches this concept combination; this is not proof of novelty.'
    else:
        novelty = 'This concept combination appears in at least one selected PEP; this does not establish that the specific idea already exists.'
    # Deduplicate warnings generated through multiple matches.
    warnings = list({json.dumps(w, sort_keys=True): w for w in warnings}.values())
    return {'input': text, 'detected_concepts': concepts, 'closest_peps': closest,
            'outcomes_summary': {'status_counts': dict(Counter(p['status'] for p in closest)),
                'note': 'Header status describes proposal outcome, not support for the input idea. Scores are rule weights, not probabilities.'},
            'past_objections': [objections[n] for n in sorted(objections)],
            'read_first': [graph.nodes[n]['number'] for n in ordered],
            'warnings': warnings, 'novelty_note': novelty}


def pretty(result):
    lines = [f'Input: {result["input"]}', 'Concepts: ' + (', '.join(result['detected_concepts']) or '(none)')]
    for pep in result['closest_peps']:
        lines.append(f'PEP {pep["pep"]}: {pep["title"]} [{pep["status"]}] score={pep["score"]}')
        lines.extend('  ' + reason for reason in pep['why'])
    lines.append('Outcomes: ' + json.dumps(result['outcomes_summary']))
    lines.append('Read first: ' + ' -> '.join(map(str, result['read_first'])))
    for objection in result['past_objections']:
        lines.append(f'Possible objection: {objection["objection"]} (PEPs {objection["peps"]})')
        for evidence in objection['evidence']:
            lines.append(f'  PEP {evidence["pep"]}, {evidence["section"]}: {evidence["snippet"]}')
    lines.extend('Warning: ' + json.dumps(w) for w in result['warnings'])
    lines.append(result['novelty_note'])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='A new feature idea in plain English')
    view = parser.add_mutually_exclusive_group()
    view.add_argument('--pretty', action='store_true')
    view.add_argument('--json', action='store_true', help='Structured JSON (default)')
    arguments = parser.parse_args()
    try:
        result = query(arguments.input)
    except FileNotFoundError:
        parser.error('knowledge_state.json is missing; run python build_graph.py')
    print(pretty(result) if arguments.pretty else json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

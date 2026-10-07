import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import networkx as nx
from build_graph import authors, build_graph, parse_header, pep_references, save_graph, split_sections
from query import load_graph, query, reading_order

ROOT = Path(__file__).resolve().parents[1]


class ParserTests(unittest.TestCase):
    def test_folded_header_and_authors(self):
        header, body = parse_header('PEP: 999\nTitle: A title: with colon\n'
            'Author: Alice <a@example.org>,\n    Bob <b@example.org>\n\nAbstract\n========\nText')
        self.assertEqual(header['Title'], 'A title: with colon')
        self.assertEqual(authors(header['Author']), ['Alice', 'Bob'])
        self.assertTrue(body.startswith('Abstract'))

    def test_references(self):
        self.assertEqual(pep_references('PEP 484, PEP-0589, :pep:`649`, PEP 484; PEP 4840'),
                         [484, 589, 649, 4840])

    def test_nested_sections(self):
        sections = split_sections('Rejected Ideas\n==============\nIntro\n\nAlternative\n-----------\ncomplexity')
        self.assertEqual(sections[-1][0], 'Rejected Ideas / Alternative')


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = build_graph()

    def test_expected_features(self):
        for idea, expected in [('add a way to mark a method as overriding a parent method', 698),
                               ('let users declare a dict with fixed keys', 589)]:
            with self.subTest(idea=idea):
                self.assertEqual(query(idea, self.graph)['closest_peps'][0]['pep'], expected)

    def test_lazy_supersession_and_prerequisite(self):
        result = query('make type hints evaluated lazily', self.graph)
        peps = [p['pep'] for p in result['closest_peps']]
        self.assertIn(649, peps)
        self.assertIn(749, peps)
        self.assertNotIn(563, peps)
        self.assertTrue(any(w['kind'] == 'superseded' and w['pep'] == 563 for w in result['warnings']))
        self.assertLess(result['read_first'].index(649), result['read_first'].index(749))

    def test_graph_schema_and_roundtrip(self):
        graph = self.graph
        self.assertEqual({a['node_type'] for _, a in graph.nodes(data=True)},
                         {'PEP', 'Person', 'Concept', 'Objection'})
        self.assertEqual(sum(a.get('in_scope', False) for _, a in graph.nodes(data=True)), 28)
        self.assertTrue(all(a.get('evidence') for *_, a in graph.edges(data=True)))
        self.assertEqual({a['relation'] for *_, a in graph.edges(data=True)},
            {'REQUIRES', 'SUPERSEDES', 'AUTHORED_BY', 'REFERENCES', 'INTRODUCES', 'MENTIONS', 'FACED_OBJECTION'})
        with tempfile.TemporaryDirectory() as directory:
            save_graph(graph, directory)
            loaded = load_graph(Path(directory) / 'knowledge_state.json')
            exported = nx.read_graphml(Path(directory) / 'knowledge_state.graphml', force_multigraph=True)
            self.assertEqual(graph.number_of_edges(), exported.number_of_edges())
            self.assertEqual(query('fixed keys', graph), query('fixed keys', loaded))

    def test_no_match(self):
        result = query('make the coffee warmer', self.graph)
        self.assertEqual(result['closest_peps'], [])
        self.assertEqual(result['detected_concepts'], [])
        self.assertIn('cannot be assessed', result['novelty_note'])

    def test_cli_from_other_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            output = subprocess.check_output([sys.executable, str(ROOT / 'query.py'),
                'fixed keys', '--json'], cwd=directory, text=True, encoding='utf-8')
            self.assertEqual(json.loads(output)['closest_peps'][0]['pep'], 589)


class ReasoningTests(unittest.TestCase):
    def fixture(self):
        graph = nx.MultiDiGraph()
        for number in range(1, 5):
            graph.add_node(f'pep:{number}', node_type='PEP', number=number,
                           title=f'Test {number}', status='Final', in_scope=True)
        graph.add_node('concept:generics', node_type='Concept', name='generics')
        def edge(left, right, relation):
            graph.add_edge(left, right, key=relation, relation=relation, evidence='Synthetic evidence')
        edge('pep:1', 'concept:generics', 'INTRODUCES')
        edge('pep:2', 'pep:1', 'SUPERSEDES')
        edge('pep:3', 'pep:2', 'SUPERSEDES')
        edge('pep:3', 'pep:4', 'REQUIRES')
        edge('pep:4', 'pep:1', 'REFERENCES')
        return graph

    def test_transitive_supersession_and_neighbor_boost(self):
        result = query('generics', self.fixture())
        self.assertEqual(result['closest_peps'][0]['pep'], 3)
        self.assertNotIn(1, [p['pep'] for p in result['closest_peps']])
        self.assertLess(result['read_first'].index(4), result['read_first'].index(3))
        self.assertTrue(any('Graph neighbor' in why for p in result['closest_peps'] for why in p['why']))

    def test_cycle_does_not_drop_nodes(self):
        graph = self.fixture()
        graph.add_edge('pep:4', 'pep:3', relation='REQUIRES', evidence='Cycle')
        ordered, cycle = reading_order(graph, ['pep:3'])
        self.assertTrue(cycle)
        self.assertEqual(set(ordered), {'pep:3', 'pep:4'})


if __name__ == '__main__':
    unittest.main()

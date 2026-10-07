# Typing PEP knowledge graph

A small, offline, explainable knowledge graph for new Python typing feature ideas.
All entity and relationship extraction is hand-written Python string handling,
regular expressions, and keyword dictionaries. **No NLP, entity-extraction library,
model, LLM API, or automatic graph transformer is used.** NetworkX only stores,
traverses, and exports the graph.

## Setup

Python 3.10+ is required. NetworkX is the sole package dependency; tests use unittest.
Git and internet access are needed only when fetching fresh source files.

```sh
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

If activation is unavailable, use `.venv\Scripts\python.exe` on Windows or
`.venv/bin/python` on macOS/Linux in place of `python`.

## Build and regenerate

The repository includes 28 raw PEP files and the generated knowledge state.
No network access is needed to build or query them:

```sh
python build_graph.py
python -m unittest discover -s tests -v
```

To update the data deliberately:

```sh
python fetch_data.py
python build_graph.py
```

`fetch_data.py` shallow-clones [python/peps](https://github.com/python/peps)
into an automatically cleaned temporary directory, copies the chosen RST files,
skips missing files, and records the upstream revision in `data/source.json`.
It does not copy the entire source repository into this project. Updating upstream
can change status, edges, and query outputs. The bundled snapshot is reproducible
without fetching. The raw PEPs retain their upstream copyright/license statements.

## Query a new idea

`query.py` loads the existing `knowledge_state.json`; it never rebuilds or fetches.
JSON is the default, and `--json` explicitly selects it. `--pretty` provides a
readable text view of the same results.

```sh
python query.py "make type hints evaluated lazily" --json
python query.py "add a way to mark a method as overriding a parent method" --pretty
python query.py "let users declare a dict with fixed keys"
```

The output includes `input`, `detected_concepts`, `closest_peps`,
`outcomes_summary`, `past_objections`, `read_first`, `warnings`, and `novelty_note`.
Each closest PEP includes its number, title, status, numeric score, and evidence-based
reasons. `past_objections` contains possible concern categories with PEP numbers,
section names, and snippets. These are lexical cues and require developer review.
Scores are transparent weights, not probabilities. A missing concept combination
only means it was not detected in this small corpus.

Use the saved graph directly from Python:

```python
from query import load_graph, query
graph = load_graph()  # NetworkX MultiDiGraph, existing JSON only
result = query("optional runtime type checking of function arguments", graph)
```

Files are resolved relative to their scripts, so the CLI works from other working
directories. No API keys or configuration are needed. Edit `rules.py` to expand
the vocabulary; rebuild after changing graph extraction rules.

## Structure

| File | Purpose |
| --- | --- |
| `fetch_data.py` | Select and copy upstream PEP source files |
| `data/peps/` | 28 bundled raw RST documents |
| `data/source.json` | Source repository, exact commit, copied/missing numbers |
| `rules.py` | Commented, manually chosen concept and objection vocabulary |
| `build_graph.py` | Header/section parser, graph construction and export |
| `knowledge_state.json` | Inspectable typed nodes and evidence-carrying edges |
| `knowledge_state.graphml` | The same graph for external graph viewers |
| `query.py` | Concept matching, graph scoring, successor and prerequisite traversal |
| `tests/test_basic.py` | Parser, CLI, serialization, and reasoning tests |
| `examples/sample_outputs.md` | Complete JSON captured from four actual CLI runs |
| `approach.md` | Design, scoring, tradeoffs, and honest limitations |

The verified snapshot has 94 nodes: 28 full PEPs, 14 external PEP stubs,
30 people, 16 concepts, and 6 objections. It has 370 typed edges.
External PEP stubs preserve references without claiming their contents were parsed.

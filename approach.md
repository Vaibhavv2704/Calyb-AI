# Approach

## 1. What subset of data I chose and why

I chose the 25 requested typing PEPs: 483, 484, 526, 544, 563, 585, 586,
589, 591, 593, 604, 612, 613, 646, 647, 649, 655, 673, 675, 681, 692,
695, 696, 698, and 705. I added 724 and 742 to capture the evolution of
type narrowing, and 749 to capture implementation of deferred annotation
evaluation and a real prerequisite relationship to 649. All 28 exist in the
bundled source snapshot. The upstream revision is in `data/source.json`.

Typing is a bounded topic with self-contained proposals, rich cross-references,
and explicit proposal statuses. Accepted/final, rejected, withdrawn, or superseded
statuses provide useful outcomes when present; the code uses actual headers
rather than assigning an outcome based on a feature idea. Broader typing PEPs
provide background, while narrowly focused PEPs support actionable recommendations.

## 2. Entities and relationships modeled and the reasoning for each

The graph is a directed multigraph, allowing different relationships between the
same pair of nodes. Stable namespaced IDs distinguish entity classes.

| Node | Attributes and purpose |
| --- | --- |
| PEP | `id=pep:number`, `number`, `title`, `status`, `type`, `created_year`, `python_version`, `in_scope`; identity, outcome and version context |
| Person | `id=person:name`, `name`; identifies authors without inferring affiliations |
| Concept | `id=concept:name`, `name`; connects documents around explicit typing topics |
| Objection | `id=objection:name`, `name`; groups possible design concerns for review |

Missing referenced PEPs become explicit `in_scope=false` stubs with Unknown status,
empty metadata and an external title. Only the 28 bundled documents have full
metadata. Stubs never earn direct concept scores or graph-neighbor boosts.

| Relationship | Direction and extraction |
| --- | --- |
| REQUIRES | Dependent PEP -> prerequisite PEP, from Requires header |
| SUPERSEDES | Newer PEP -> older PEP, from Replaces or reversed Superseded-By |
| AUTHORED_BY | PEP -> Person, from unfolded Author header |
| REFERENCES | PEP -> PEP, from body regex mentions |
| INTRODUCES | PEP -> Concept, phrase in Title or Abstract |
| MENTIONS | PEP -> Concept, phrase elsewhere when no Title/Abstract hit exists |
| FACED_OBJECTION | PEP -> Objection, cue in a selected discussion section |

Every edge carries nonempty `evidence`. Header edges contain the field and value;
references and concepts carry short source snippets. Objection evidence includes
both section and snippet. It is a JSON-encoded list string on the edge so it remains
a valid scalar in GraphML; the query decodes it into structured JSON objects.
Repeated evidence from objection subsections is retained; repeated body references
use the first snippet. Duplicate header assertions collapse to one typed edge.

Concepts include generics, protocols, runtime_typing, type_aliases, literal_types,
typeddict, variadic_generics, forward_references, annotations_evaluation, type_guards,
final_qualifiers, decorators_typing, method_overrides, union_types, self_types, and
readonly_items. Objections are backward_compat, runtime_performance, complexity,
ambiguity_with_existing_syntax, tooling_burden, and not_enough_use_cases.

## 3. How the knowledge representation was built and the tradeoffs

The header parser splits lines on the first colon up to the first blank line and
unfolds indented continuation lines. Authors are split after removing bracketed
email addresses. Year is read from Created. RST sections use title/underline pairs
and a hierarchy of encountered adornment styles; nested sections keep their parent
names, so a rejected-idea subsection remains eligible for objection matching.

Body references recognize `PEP 123`, `PEP-0123`, and the actual upstream RST role
`:pep:` followed by a backtick-delimited number. Self-references are excluded.
Handwritten phrase rules use case-insensitive word boundaries and flexible
whitespace. The same concept vocabulary handles documents and new feature ideas.
Rules never consult an external model or extraction tool.

JSON stores `{ "nodes": [...], "edges": [...] }`, including explicit IDs,
source/target, relation, and evidence. It is easy to inspect, review, and load
without a database service. GraphML supports graph viewers. NetworkX provides only
storage, traversal, topological sorting, and export; no extraction algorithm is used.
Handwritten vocabulary is deterministic and transparent but misses synonyms and
cannot understand claims. Evidence helps a developer check each inference.

The verified build has 94 nodes (42 PEPs including 14 stubs, 30 people, 16 concepts,
6 objections) and 370 edges: 52 AUTHORED_BY, 87 REFERENCES, 36 INTRODUCES,
123 MENTIONS, 68 FACED_OBJECTION, 3 SUPERSEDES, and 1 REQUIRES.
The low REQUIRES count reflects explicit source metadata: references are not
invented prerequisites. This is a relational graph, not a collection of documents:
PEPs share authors, concepts, objections, and explicit inter-PEP relationships.

## 4. How the system works when a new input arrives

1. Load only the saved JSON into a MultiDiGraph. No rebuild or network call occurs.
2. Match the feature idea against the concept dictionary, including a few manually
   chosen paraphrases such as evaluated lazily, overriding, and fixed keys.
3. For every in-scope PEP, add 3 per overlapping INTRODUCES concept and 1 per
   overlapping MENTIONS concept. Count each concept once; retain edge evidence in why.
4. Select the five strongest direct matches, breaking ties by PEP number. Inspect
   incoming and outgoing REQUIRES, SUPERSEDES, and REFERENCES edges. Neighbors gain
   0.6, 0.9, or 0.3 respectively, capped at 1.5 total per PEP. Boosts do not recursively
   propagate. Each explanation names the edge direction and source evidence.
5. Traverse SUPERSEDES in reverse to find newer endpoints, including transitive
   chains and multiple successors. Replace obsolete recommendations with the
   endpoint. Scores inherited from multiple predecessors are merged by maximum,
   not summed. The score may therefore reflect a predecessor rather than direct
   overlap with the successor; why states that explicitly. External successors
   are labeled with a metadata warning. Cycles receive warnings.
6. Rank the resolved PEPs and return at most five. Report their actual statuses,
   plus superseded/rejected/withdrawn warnings applicable to recommendations or
   their replaced matches. Collect possible objections from the selected PEPs
   and directly matched predecessors, including section/snippet evidence.
7. Recursively collect REQUIRES prerequisites. Invert dependent->prerequisite edges
   and topologically sort, using PEP number to break unrelated ties. If a cycle
   exists, sort strongly connected components and warn that no valid order exists
   within the cycle. Never silently discard prerequisite nodes.
8. Report whether any single in-scope PEP has all detected concepts. An unmatched
   combination means only absence under these rules, not proven research novelty.
   With no detected concepts return empty recommendations and an honest note.
9. Emit actionable structured JSON, or a readable rendering with --pretty.

The sample outputs were captured from actual CLI runs. Tests cover folded headers,
reference forms, nested sections, expected first matches, supersession, graph
neighbor boosts, prerequisite order/cycles, unknown ideas, full schema, GraphML
roundtrip, and CLI loading from another directory.

## 5. What I chose NOT to build and why

No web UI, graph database, embeddings, LLM calls, NLP package, automatic extractor,
or semantic search. No automatic judgment that a new idea should be accepted or 
rejected: proposal status is evidence about history, not a verdict on a different idea. 
No inferred prerequisites from ordinary references, because a citation alone does not 
establish a dependency.

## 6. What I would build next and why

Expand the manually curated vocabulary using missed queries, while preserving
auditable mappings. Add sentence-level objection rules with negation and explicit
concern cues to reduce false positives. Link CPython issue tracker and commit
history for implementation outcomes, and discussion threads for objections not
present in final PEPs. Build a labeled evaluation set of feature ideas with expected
PEPs and objection spans to measure precision, recall, and ranking quality before
changing weights. Improve source spans to include line numbers and multiple
reference snippets for easier evidence review.

## 7. Limitations

INTRODUCES is the assignment's lexical Title/Abstract proxy. An Abstract can discuss
an existing concept, so this edge does not prove historical invention. A body hit
can be a negative statement (for example, variable annotations are not designed
for runtime type checking); the matcher cannot understand that distinction.

FACED_OBJECTION is also heuristic. A performance passage may say overhead is zero,
type checker mentions may describe benefits, and use cases may justify a feature
rather than criticize it. Compatibility sections are not necessarily objections.
These edges identify possible concerns with evidence, not verified opposition.
The dictionaries have narrow and broad cues: Final can describe a proposal status
in body prose rather than a qualifier; decorators can be incidental examples;
dict with may match ordinary dictionary prose. The runtime vocabulary intentionally
avoids bare runtime type, which falsely matched runtime type aliases.

RST parsing is deliberately partial: unusual overline-only titles or adornment
ordering, embedded code, escaped roles, and split reference syntax can be missed
or misclassified. People are normalized by spelling only, with no alias resolution.
Only explicit headers establish supersession or prerequisites. Neighbor boosts
can elevate a general background PEP; they are contextual signals, not similarity
proof. Scores and the five-result cutoff are manually chosen, not calibrated.

The corpus is small, frozen, and typing-focused. Stub metadata and other PEP
contents are unavailable. Status is captured at the recorded commit, and a Final
PEP may have later canonical specifications outside the corpus. Novelty checks
ignore undetected concepts and cannot establish that an idea has never been tried.

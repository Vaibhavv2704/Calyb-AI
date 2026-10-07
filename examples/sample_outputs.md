# Sample CLI outputs

Complete JSON captured from actual CLI runs against the bundled snapshot.
Scores are rule weights; objections are possible concerns, not semantic judgments.

## make type hints evaluated lazily

```sh
python query.py "make type hints evaluated lazily" --json
```

```json
{
  "input": "make type hints evaluated lazily",
  "detected_concepts": [
    "annotations_evaluation"
  ],
  "closest_peps": [
    {
      "pep": 649,
      "title": "Deferred Evaluation Of Annotations Using Descriptors",
      "status": "Final",
      "score": 4.5,
      "why": [
        "INTRODUCES annotations_evaluation (+3): Postponed Evaluation of Annotations :pep:`3107` introduced syntax for function annotations, but the semantics were deli",
        "Graph neighbor of PEP 649: PEP 649 REFERENCES PEP 563 (+0.3); rcular-reference problems. Python solved this by accepting :pep:`563`, incorporating a new approach called \"stringized annotations\" in which annotations were automatical",
        "Graph neighbor of PEP 649: PEP 649 SUPERSEDES PEP 563 (+0.9); Replaces: 563",
        "Graph neighbor of PEP 604: PEP 604 REFERENCES PEP 563 (+0.3); ---------------------------------------------------------- :pep:`563` (Postponed Evaluation of Annotations) is enough to accept this proposition, if we accept to not be",
        "Supersedes matched PEP 563; followed SUPERSEDES chain to its newest endpoint"
      ]
    },
    {
      "pep": 749,
      "title": "Implementing PEP 649",
      "status": "Final",
      "score": 4.5,
      "why": [
        "INTRODUCES annotations_evaluation (+3): Postponed Evaluation of Annotations :pep:`3107` introduced syntax for function annotations, but the semantics were deli",
        "Graph neighbor of PEP 649: PEP 649 REFERENCES PEP 563 (+0.3); rcular-reference problems. Python solved this by accepting :pep:`563`, incorporating a new approach called \"stringized annotations\" in which annotations were automatical",
        "Graph neighbor of PEP 649: PEP 649 SUPERSEDES PEP 563 (+0.9); Replaces: 563",
        "Graph neighbor of PEP 604: PEP 604 REFERENCES PEP 563 (+0.3); ---------------------------------------------------------- :pep:`563` (Postponed Evaluation of Annotations) is enough to accept this proposition, if we accept to not be",
        "Supersedes matched PEP 563; followed SUPERSEDES chain to its newest endpoint"
      ]
    },
    {
      "pep": 695,
      "title": "Type Parameter Syntax",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS annotations_evaluation (+1): x, these attributes become lazily evaluated, as discussed under `Lazy Evaluation`_ below. Generic Type Alias ------------------ We propose to introduce a new statement for decla",
        "Graph neighbor of PEP 563: PEP 695 REFERENCES PEP 563 (+0.3); close such expressions in quotes to prevent runtime errors. :pep:`563` and :pep:`649` detail the problems with this situation for type annotations. To prevent a similar",
        "Graph neighbor of PEP 649: PEP 695 REFERENCES PEP 649 (+0.3); essions in quotes to prevent runtime errors. :pep:`563` and :pep:`649` detail the problems with this situation for type annotations. To prevent a similar situation with",
        "Graph neighbor of PEP 749: PEP 749 REFERENCES PEP 695 (+0.3); d type parameter bounds and defaults (which were added by :pep:`695` and :pep:`696`) using PEP 649-like semantics. * The ``SOURCE`` format is renamed to ``STRING`` to i"
      ]
    },
    {
      "pep": 604,
      "title": "Allow writing union types as ``X | Y``",
      "status": "Final",
      "score": 1.3,
      "why": [
        "MENTIONS annotations_evaluation (+1): --------------------------------------------------- :pep:`563` (Postponed Evaluation of Annotations) is enough to accept this proposition, if we accept to not be compatible with the dy",
        "Graph neighbor of PEP 563: PEP 604 REFERENCES PEP 563 (+0.3); ---------------------------------------------------------- :pep:`563` (Postponed Evaluation of Annotations) is enough to accept this proposition, if we accept to not be"
      ]
    },
    {
      "pep": 484,
      "title": "Type Hints",
      "status": "Final",
      "score": 1.2,
      "why": [
        "Graph neighbor of PEP 563: PEP 563 REFERENCES PEP 484 (+0.3); tions, but the semantics were deliberately left undefined. :pep:`484` introduced a standard meaning to annotations: type hints. :pep:`526` defined variable annotations,",
        "Graph neighbor of PEP 649: PEP 649 REFERENCES PEP 484 (+0.3); static type information, called *type hints,* as defined in :pep:`484`. Python 3.5 shipped with a new :mod:`typing` module which quickly became very popular. Python 3.6",
        "Graph neighbor of PEP 604: PEP 604 REFERENCES PEP 484 (+0.3); stance`` and ``issubclass`` calls. Motivation ========== :pep:`484` and :pep:`526` propose a generic syntax to add typing to variables, parameters and function returns",
        "Graph neighbor of PEP 695: PEP 695 REFERENCES PEP 484 (+0.3); tement for declaring type aliases. Motivation ========== :pep:`484` introduced type variables into the language. :pep:`612` built upon this concept by introducing para"
      ]
    }
  ],
  "outcomes_summary": {
    "status_counts": {
      "Final": 5
    },
    "note": "Header status describes proposal outcome, not support for the input idea. Scores are rule weights, not probabilities."
  },
  "past_objections": [
    {
      "objection": "ambiguity_with_existing_syntax",
      "peps": [
        695
      ],
      "evidence": [
        {
          "pep": 695,
          "section": "Specification / Compatibility with Traditional TypeVars",
          "snippet": "checkers. This is necessary because the type parameter order is ambiguous. It is OK to combine traditional type variables with new-style type parameters if the class, funct"
        }
      ]
    },
    {
      "objection": "backward_compat",
      "peps": [
        484,
        563,
        649,
        695,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotatio"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "ns in function annotations. The new proposal is then considered incompatible with the specification of PEP 3107. Our response to this is that, first of all, the current propos"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The problem of forward declarations",
          "snippet": "evaluated at runtime at all). This of course would run afoul of backwards compatibility, since the Python interpreter doesn't actually know whether a particular annotation is meant to be"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals / Non-typing usage of annotations",
          "snippet": "d enhancements require. With this in mind, uses for annotations incompatible with the aforementioned PEPs should be considered deprecated."
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility",
          "snippet": "This is a backwards incompatible change. Applications depending on arbitrary objects to be directly present in annotations will bre"
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility / Deprecation policy",
          "snippet": "e, use of annotations that depend upon their eager evaluation is incompatible with both proposals and is no longer supported."
        },
        {
          "pep": 563,
          "section": "Rejected Ideas / Introducing a new dictionary for the string literal form instead",
          "snippet": "ns_text__`` just-in-time. This idea is supposed to solve the backwards compatibility issue, removing the need for a new ``__future__`` import. Sadly, this is not enough. Postponed ev"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With Stock Semantics",
          "snippet": "'int'>`` when this PEP is active. This is therefore a backwards-incompatible change. However, this example is poor programming style, so this change seems acceptable. There"
        },
        {
          "pep": 695,
          "section": "Specification / Compatibility with Traditional TypeVars",
          "snippet": "``TypeVar``, ``TypeVarTuple``, and ``ParamSpec`` is retained for backward compatibility. However, these \"traditional\" type variables should not be combined with type parameters allocated"
        },
        {
          "pep": 749,
          "section": "Backwards Compatibility",
          "snippet": ":pep:`649` provides a thorough discussion of the backwards compatibility implications on existing code that uses either stock or :pep:`563` semantics. However, there is an"
        }
      ]
    },
    {
      "objection": "complexity",
      "peps": [
        484,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rejected Alternatives / Which brackets for generic type parameters?",
          "snippet": "such cases, but to most users the rules would feel arbitrary and complex. It would also require us to dramatically change the CPython parser (and every other parser for Py"
        },
        {
          "pep": 749,
          "section": "Annotations and metaclasses / Rejected alternatives",
          "snippet": "the known edge cases with metaclasses, it introduces significant complexity to all classes, including a new built-in type (for the annotations descriptor) with unusual behavio"
        }
      ]
    },
    {
      "objection": "not_enough_use_cases",
      "peps": [
        484,
        563,
        649,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "e hinting <gvr-artima_>`_, which is listed as the first possible use case in said PEP. This PEP aims to provide a standard syntax for type annotations, opening up Python co"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "A number of existing or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a stat"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals",
          "snippet": "tion time. This creates a number of issues for the type hinting use case: * forward references: when a type hint contains names that have not been defined yet, that defi"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals / Non-typing usage of annotations",
          "snippet": "and :pep:`526`), is predominantly motivated by the type hinting use case. In Python 3.8 :pep:`484` will graduate from provisional status. Other enhancements to the Python"
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility",
          "snippet": "ll be successfully statically analyzed, which is the predominant use case for annotations. Annotations using nested classes and their respective state are still valid. The"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With PEP 563 Semantics",
          "snippet": "omatically-generated documentation. Users experimented with this use case, and Python's ``pydoc`` has expressed some interest in this technique. This PEP supports this use"
        },
        {
          "pep": 749,
          "section": "New ``annotationlib`` module / Rejected alternatives",
          "snippet": "already quite large, and its import time is prohibitive for some use cases. *Add the functionality to the typing module*: While annotations are mostly used for typing, they"
        }
      ]
    },
    {
      "objection": "runtime_performance",
      "peps": [
        484
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "r example using decorators or metaclasses. Using type hints for performance optimizations is left as an exercise for the reader. It should also be emphasized that **Python wi"
        }
      ]
    },
    {
      "objection": "tooling_burden",
      "peps": [
        484,
        563,
        649,
        695
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "lysis is the most important. This includes support for off-line type checkers such as mypy, as well as providing a standard notation that can be used by IDEs for code completion"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotations have no runtime behavior (other than evaluation of the an"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "function or class decorated with the latter to be ignored by the type checker. There are also ``# type: ignore`` comments, and static checkers should support configuration opti"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The double colon",
          "snippet": "ilt on top of type hints. * It catches mistakes even when the type checker is not run. Since it is a separate program, users may choose not to run it (or even instal"
        },
        {
          "pep": 563,
          "section": "Rejected Ideas / Passing string literals in annotations verbatim to ``__annotations__``",
          "snippet": "annotations__``. This was meant to simplify support for runtime type checkers. Mark Shannon pointed out this idea was flawed since it wasn't handling situations where strings a"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With Stock Semantics",
          "snippet": "one happy. Note that these are both also pain points for static type checkers, and are unsupported by those tools. It seems reasonable to declare that both are at the very leas"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With PEP 563 Semantics",
          "snippet": "n an ``if typing.TYPE_CHECKING`` block. This allowed the static type checkers to import the modules and the type definitions inside, but they wouldn't be imported at runtime. So"
        },
        {
          "pep": 695,
          "section": "Specification / Compatibility with Traditional TypeVars",
          "snippet": ": K = TypeVar(\"K\") class ClassA[V](dict[K, V]): ... # Type checker error class ClassB[K, V](dict[K, V]): ... # OK class ClassC[V]: # The use of K a"
        }
      ]
    }
  ],
  "read_first": [
    484,
    604,
    649,
    695,
    749
  ],
  "warnings": [
    {
      "kind": "superseded",
      "pep": 563,
      "newer_peps": [
        649,
        749
      ]
    }
  ],
  "novelty_note": "This concept combination appears in at least one selected PEP; this does not establish that the specific idea already exists."
}
```

## add a way to mark a method as overriding a parent method

```sh
python query.py "add a way to mark a method as overriding a parent method" --json
```

```json
{
  "input": "add a way to mark a method as overriding a parent method",
  "detected_concepts": [
    "method_overrides"
  ],
  "closest_peps": [
    {
      "pep": 698,
      "title": "Override Decorator for Static Typing",
      "status": "Final",
      "score": 3.0,
      "why": [
        "INTRODUCES method_overrides (+3): Override Decorator for Static Typing This PEP proposes adding an ``@override`` decorator to the Python type"
      ]
    },
    {
      "pep": 483,
      "title": "The Theory of Type Hints",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS method_overrides (+1): sed under control of the type checker, because in Python one can override attributes in an incompatible way:: class Base: answer = '42' # type: str class Derived",
        "Graph neighbor of PEP 484: PEP 484 REFERENCES PEP 483 (+0.3); g. Gradual typing and the full type system are explained in :pep:`483`. Other approaches from which we have borrowed or to which ours can be compared and contrasted are",
        "Graph neighbor of PEP 544: PEP 544 REFERENCES PEP 483 (+0.3); ently of its actual runtime class. However, as discussed in :pep:`483`, both nominal and structural subtyping have their strengths and weaknesses. Therefore, in this PEP",
        "Graph neighbor of PEP 589: PEP 589 REFERENCES PEP 483 (+0.3); o support the ``Any`` type. It is defined more formally in :pep:`483`. This section introduces the new, non-trivial rules needed to support type consistency for TypedDi"
      ]
    },
    {
      "pep": 484,
      "title": "Type Hints",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS method_overrides (+1): rt Mapping, Set def notify_by_email(employees: Set[Employee], overrides: Mapping[str, str]) -> None: ... Generics can be parameterized by using a new factory available in",
        "Graph neighbor of PEP 483: PEP 483 REFERENCES PEP 484 (+0.3); stract ======== This PEP lays out the theory referenced by :pep:`484`. Introduction ============ This document lays out the theory of the new type hinting proposal fo",
        "Graph neighbor of PEP 544: PEP 544 REFERENCES PEP 484 (+0.3); ing.Protocol` Abstract ======== Type hints introduced in :pep:`484` can be used to specify type metadata for static type checkers and other third party tools. However,",
        "Graph neighbor of PEP 589: PEP 589 REFERENCES PEP 484 (+0.3); :py:class:`typing.TypedDict` Abstract ======== :pep:`484` defines the type ``Dict[K, V]`` for uniform dictionaries, where each value has the same type, and a"
      ]
    },
    {
      "pep": 544,
      "title": "Protocols: Structural subtyping (static duck typing)",
      "status": "Final",
      "score": 1.6,
      "why": [
        "MENTIONS method_overrides (+1): n it is not strictly compatible, such as when it has an unsafe override. Covariant subtyping of mutable attributes ----------------------------------------- Rejected be",
        "Graph neighbor of PEP 483: PEP 544 REFERENCES PEP 483 (+0.3); ently of its actual runtime class. However, as discussed in :pep:`483`, both nominal and structural subtyping have their strengths and weaknesses. Therefore, in this PEP",
        "Graph neighbor of PEP 484: PEP 544 REFERENCES PEP 484 (+0.3); ing.Protocol` Abstract ======== Type hints introduced in :pep:`484` can be used to specify type metadata for static type checkers and other third party tools. However,"
      ]
    },
    {
      "pep": 589,
      "title": "TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys",
      "status": "Final",
      "score": 1.6,
      "why": [
        "MENTIONS method_overrides (+1): ult, all keys must be present in a TypedDict. It is possible to override this by specifying *totality*. Here is how to do this using the class-based syntax:: class Mo",
        "Graph neighbor of PEP 483: PEP 589 REFERENCES PEP 483 (+0.3); o support the ``Any`` type. It is defined more formally in :pep:`483`. This section introduces the new, non-trivial rules needed to support type consistency for TypedDi",
        "Graph neighbor of PEP 484: PEP 589 REFERENCES PEP 484 (+0.3); :py:class:`typing.TypedDict` Abstract ======== :pep:`484` defines the type ``Dict[K, V]`` for uniform dictionaries, where each value has the same type, and a"
      ]
    }
  ],
  "outcomes_summary": {
    "status_counts": {
      "Final": 5
    },
    "note": "Header status describes proposal outcome, not support for the input idea. Scores are rule weights, not probabilities."
  },
  "past_objections": [
    {
      "objection": "ambiguity_with_existing_syntax",
      "peps": [
        544
      ],
      "evidence": [
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Protocols subclassing normal classes",
          "snippet": ". This situation would be really weird. In addition, there is an ambiguity about whether attributes of ``Base`` should become protocol members of ``Proto``."
        }
      ]
    },
    {
      "objection": "backward_compat",
      "peps": [
        484,
        544,
        589,
        698
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotatio"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "ns in function annotations. The new proposal is then considered incompatible with the specification of PEP 3107. Our response to this is that, first of all, the current propos"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The problem of forward declarations",
          "snippet": "evaluated at runtime at all). This of course would run afoul of backwards compatibility, since the Python interpreter doesn't actually know whether a particular annotation is meant to be"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols interoperable with other approaches",
          "snippet": "conceptually a superset of protocols defined here, but using an incompatible syntax to define them, because before :pep:`526` there was no straightforward way to annotate attri"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Use assignments to check explicitly that a class implements a protocol",
          "snippet": "Error: A.__len__ doesn't conform to 'Sized' # (Incompatible return type 'float') This approach moves the check away from the class definition and it almost re"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Prohibit explicit subclassing of protocols by non-protocols",
          "snippet": "This was rejected for the following reasons: * Backward compatibility: People are already using ABCs, including generic ABCs from ``typing`` module. If we prohibit exp"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols special objects at runtime rather than normal ABCs",
          "snippet": "Making protocols non-ABCs will make the backwards compatibility problematic if possible at all. For example, ``collections.abc.Iterable`` is already an ABC, and lo"
        },
        {
          "pep": 589,
          "section": "Backwards Compatibility",
          "snippet": "To retain backwards compatibility, type checkers should not infer a TypedDict type unless it is sufficiently clear that this is desir"
        },
        {
          "pep": 589,
          "section": "Rejected Alternatives",
          "snippet": "potentially extended later. These are rejected on principle, as incompatible with the spirit of this proposal: * TypedDict isn't extensible, and it addresses only a specific u"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Mark a base class to force explicit overrides on subclasses",
          "snippet": "a strict mode where explicit ``@override`` is required (see the Backward Compatibility section) provides more benefits than a way to mark base classes. Moreover we believe that authors"
        }
      ]
    },
    {
      "objection": "complexity",
      "peps": [
        484,
        544,
        698
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rejected Alternatives / Which brackets for generic type parameters?",
          "snippet": "such cases, but to most users the rules would feel arbitrary and complex. It would also require us to dramatically change the CPython parser (and every other parser for Py"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "e protocols non-optional in the future. To reiterate, providing complex runtime semantics for protocol classes is not a goal of this PEP, the main goal is to provide a sup"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make every class a protocol by default",
          "snippet": "otocols anyway, mainly because their interfaces are too large, complex or implementation-oriented (for example, they may include de facto private attributes and metho"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Overriding inferred variance of protocol classes",
          "snippet": "king for protocol implementations in MROs but this will be too complex in a general case, and this \"cure\" requires abandoning simple idea of purely structural subtyping"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Include the name of the ancestor class being overridden",
          "snippet": "er. We decided against it because: - Supporting this would add complexity to the implementation of both ``@override`` and type checker support for it, so there would need"
        }
      ]
    },
    {
      "objection": "not_enough_use_cases",
      "peps": [
        484,
        544,
        589,
        698
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "e hinting <gvr-artima_>`_, which is listed as the first possible use case in said PEP. This PEP aims to provide a standard syntax for type annotations, opening up Python co"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "A number of existing or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a stat"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Support optional protocol members",
          "snippet": "y they are pretty commonly used. The current realistic potential use cases for protocols in Python don't require these. In the interest of simplicity, we propose to not suppo"
        },
        {
          "pep": 589,
          "section": "Rejected Alternatives",
          "snippet": "* TypedDict isn't extensible, and it addresses only a specific use case. TypedDict objects are regular dictionaries at runtime, and TypedDict cannot be used with other"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Mark a base class to force explicit overrides on subclasses",
          "snippet": "ge codebases will benefit most from ``@override``, and for these use cases having a strict mode where explicit ``@override`` is required (see the Backward Compatibility secti"
        }
      ]
    },
    {
      "objection": "runtime_performance",
      "peps": [
        484,
        698
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "r example using decorators or metaclasses. Using type hints for performance optimizations is left as an exercise for the reader. It should also be emphasized that **Python wi"
        },
        {
          "pep": 698,
          "section": "Rationale / Precedent in Other Languages and Runtime Libraries / Runtime Override Checks in Python",
          "snippet": "be caught earlier, often in-editor. - Static checks come with no performance overhead, unlike runtime checks. - Bugs will be caught quickly even in rarely-used modules, whereas"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Runtime enforcement",
          "snippet": "t clear this brings any benefits. - There would be at least some performance overhead, leading to projects importing slower with runtime enforcement. We estimate the ``@ove"
        }
      ]
    },
    {
      "objection": "tooling_burden",
      "peps": [
        484,
        544,
        589,
        698
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "lysis is the most important. This includes support for off-line type checkers such as mypy, as well as providing a standard notation that can be used by IDEs for code completion"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotations have no runtime behavior (other than evaluation of the an"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "function or class decorated with the latter to be ignored by the type checker. There are also ``# type: ignore`` comments, and static checkers should support configuration opti"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The double colon",
          "snippet": "ilt on top of type hints. * It catches mistakes even when the type checker is not run. Since it is a separate program, users may choose not to run it (or even instal"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals",
          "snippet": "ered a subtype of both ``Sized`` and ``Iterable[int]`` by static type checkers using structural [wiki-structural]_ subtyping:: from typing import Iterator, Iterable class B"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "otocol class. * Any checks will be performed only by third-party type checkers and other tools. * Programmers are free to not use them even if they use type annotations. * Ther"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Allow only protocol methods and force use of getters and setters",
          "snippet": "large code bases is partially due to previous absence of static type checkers for Python, the problem that :pep:`484` and this PEP are aiming to solve. For example:: # withou"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols interoperable with other approaches",
          "snippet": "` might potentially adopt the ``Protocol`` syntax. In this case, type checkers could be taught to recognize interfaces as protocols and make simple structural checks with respect"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Provide a special intersection type construct",
          "snippet": "yet clear how popular/useful it will be and implementing this in type checkers for non-protocol classes could be difficult. Finally, it will be very easy to add this later if nee"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Prohibit explicit subclassing of protocols by non-protocols",
          "snippet": "lar protocol, making subtyping relationships easier to see. * Type checkers can warn about missing protocol members or members with incompatible types more easily, without h"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Overriding inferred variance of protocol classes",
          "snippet": "variance will make impossible more detailed error messages in type checkers citing particular conflicts in member type signatures. * Finally, explicit is better than implic"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Support adapters and adaptation",
          "snippet": "e there is a reasonable alternative for such cases with existing tooling, it is therefore proposed not to include adaptation in this PEP."
        },
        {
          "pep": 589,
          "section": "Backwards Compatibility",
          "snippet": "y start generating errors once TypedDict support is added to the type checker, since TypedDict types are more restrictive than dictionary types. In particular, they aren't subt"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Rely on Integrated Development Environments for safety",
          "snippet": "will not help and the bug appears when upgrading dependencies. Type checkers are a fast way to catch breaking changes in dependencies. - Not all developers use such IDEs. And"
        },
        {
          "pep": 698,
          "section": "Rejected Alternatives / Include the name of the ancestor class being overridden",
          "snippet": "add complexity to the implementation of both ``@override`` and type checker support for it, so there would need to be considerable benefits. - We believe that it would be ra"
        }
      ]
    }
  ],
  "read_first": [
    483,
    484,
    544,
    589,
    698
  ],
  "warnings": [],
  "novelty_note": "This concept combination appears in at least one selected PEP; this does not establish that the specific idea already exists."
}
```

## let users declare a dict with fixed keys

```sh
python query.py "let users declare a dict with fixed keys" --json
```

```json
{
  "input": "let users declare a dict with fixed keys",
  "detected_concepts": [
    "typeddict"
  ],
  "closest_peps": [
    {
      "pep": 589,
      "title": "TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys",
      "status": "Final",
      "score": 4.2,
      "why": [
        "INTRODUCES typeddict (+3): TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys :pep:`484` defines the type ``Dict[K, V]`` f",
        "Graph neighbor of PEP 655: PEP 655 REFERENCES PEP 589 (+0.3); :py:data:`typing.NotRequired` Abstract ======== :pep:`589` defines notation for declaring a TypedDict with all required keys and notation for defining a Typed",
        "Graph neighbor of PEP 692: PEP 692 REFERENCES PEP 589 (+0.3); `__ in the popular ``httpx`` library. Rationale ========= :pep:`589` introduced the ``TypedDict`` type constructor that supports dictionary types consisting of string k",
        "Graph neighbor of PEP 705: PEP 705 REFERENCES PEP 589 (+0.3); :external+py3.13:data:`typing.ReadOnly` Abstract ======== :pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys. A",
        "Graph neighbor of PEP 484: PEP 589 REFERENCES PEP 484 (+0.3); :py:class:`typing.TypedDict` Abstract ======== :pep:`484` defines the type ``Dict[K, V]`` for uniform dictionaries, where each value has the same type, and a"
      ]
    },
    {
      "pep": 655,
      "title": "Marking individual TypedDict items as required or potentially-missing",
      "status": "Final",
      "score": 3.9,
      "why": [
        "INTRODUCES typeddict (+3): Marking individual TypedDict items as required or potentially-missing :pep:`589` defines notation for declaring a TypedDict wit",
        "Graph neighbor of PEP 589: PEP 655 REFERENCES PEP 589 (+0.3); :py:data:`typing.NotRequired` Abstract ======== :pep:`589` defines notation for declaring a TypedDict with all required keys and notation for defining a Typed",
        "Graph neighbor of PEP 692: PEP 692 REFERENCES PEP 655 (+0.3); he dictionary's ``total`` parameter as ``False``. Moreover, :pep:`655` introduced new type qualifiers - ``typing.Required`` and ``typing.NotRequired`` - that enable speci",
        "Graph neighbor of PEP 705: PEP 705 REFERENCES PEP 655 (+0.3); ] # OK This is consistent with the behavior introduced in :pep:`655`. Inheritance ----------- Subclasses can redeclare read-only items as non-read-only, allowing them"
      ]
    },
    {
      "pep": 692,
      "title": "Using TypedDict for more precise \\*\\*kwargs typing",
      "status": "Final",
      "score": 3.9,
      "why": [
        "INTRODUCES typeddict (+3): Using TypedDict for more precise \\*\\*kwargs typing Currently ``**kwargs`` can be type hinted as long as all of the",
        "Graph neighbor of PEP 589: PEP 692 REFERENCES PEP 589 (+0.3); `__ in the popular ``httpx`` library. Rationale ========= :pep:`589` introduced the ``TypedDict`` type constructor that supports dictionary types consisting of string k",
        "Graph neighbor of PEP 655: PEP 692 REFERENCES PEP 655 (+0.3); he dictionary's ``total`` parameter as ``False``. Moreover, :pep:`655` introduced new type qualifiers - ``typing.Required`` and ``typing.NotRequired`` - that enable speci",
        "Graph neighbor of PEP 705: PEP 705 REFERENCES PEP 692 (+0.3); e absent. Keyword argument typing ----------------------- :pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the ite"
      ]
    },
    {
      "pep": 705,
      "title": "TypedDict: Read-only items",
      "status": "Final",
      "score": 3.9,
      "why": [
        "INTRODUCES typeddict (+3): TypedDict: Read-only items :pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionarie",
        "Graph neighbor of PEP 589: PEP 705 REFERENCES PEP 589 (+0.3); :external+py3.13:data:`typing.ReadOnly` Abstract ======== :pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys. A",
        "Graph neighbor of PEP 655: PEP 705 REFERENCES PEP 655 (+0.3); ] # OK This is consistent with the behavior introduced in :pep:`655`. Inheritance ----------- Subclasses can redeclare read-only items as non-read-only, allowing them",
        "Graph neighbor of PEP 692: PEP 705 REFERENCES PEP 692 (+0.3); e absent. Keyword argument typing ----------------------- :pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the ite"
      ]
    },
    {
      "pep": 484,
      "title": "Type Hints",
      "status": "Final",
      "score": 1.3,
      "why": [
        "MENTIONS typeddict (+1): on or method. Given a function or method object, it returns a dict with the same format as ``__annotations__``, but evaluating forward references (which are given as str",
        "Graph neighbor of PEP 589: PEP 589 REFERENCES PEP 484 (+0.3); :py:class:`typing.TypedDict` Abstract ======== :pep:`484` defines the type ``Dict[K, V]`` for uniform dictionaries, where each value has the same type, and a"
      ]
    }
  ],
  "outcomes_summary": {
    "status_counts": {
      "Final": 5
    },
    "note": "Header status describes proposal outcome, not support for the input idea. Scores are rule weights, not probabilities."
  },
  "past_objections": [
    {
      "objection": "ambiguity_with_existing_syntax",
      "peps": [
        705
      ],
      "evidence": [
        {
          "pep": 705,
          "section": "Rejected alternatives / A readonly flag",
          "snippet": "current type. The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a so"
        }
      ]
    },
    {
      "objection": "backward_compat",
      "peps": [
        484,
        589,
        655
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotatio"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "ns in function annotations. The new proposal is then considered incompatible with the specification of PEP 3107. Our response to this is that, first of all, the current propos"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The problem of forward declarations",
          "snippet": "evaluated at runtime at all). This of course would run afoul of backwards compatibility, since the Python interpreter doesn't actually know whether a particular annotation is meant to be"
        },
        {
          "pep": 589,
          "section": "Backwards Compatibility",
          "snippet": "To retain backwards compatibility, type checkers should not infer a TypedDict type unless it is sufficiently clear that this is desir"
        },
        {
          "pep": 589,
          "section": "Rejected Alternatives",
          "snippet": "potentially extended later. These are rejected on principle, as incompatible with the spirit of this proposal: * TypedDict isn't extensible, and it addresses only a specific u"
        },
        {
          "pep": 655,
          "section": "Backwards Compatibility",
          "snippet": "No backward incompatible changes are made by this PEP."
        }
      ]
    },
    {
      "objection": "complexity",
      "peps": [
        484,
        692,
        705
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rejected Alternatives / Which brackets for generic type parameters?",
          "snippet": "such cases, but to most users the rules would feel arbitrary and complex. It would also require us to dramatically change the CPython parser (and every other parser for Py"
        },
        {
          "pep": 692,
          "section": "Rejected Ideas / ``TypedDict`` unions",
          "snippet": "*kwargs`` with a union of typed dicts would greatly increase the complexity of the implementation of this PEP and there seems to be no compelling use case to justify the suppo"
        },
        {
          "pep": 705,
          "section": "Rejected alternatives / A TypedMapping protocol type",
          "snippet": "ict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity."
        }
      ]
    },
    {
      "objection": "not_enough_use_cases",
      "peps": [
        484,
        589,
        692
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "e hinting <gvr-artima_>`_, which is listed as the first possible use case in said PEP. This PEP aims to provide a standard syntax for type annotations, opening up Python co"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "A number of existing or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a stat"
        },
        {
          "pep": 589,
          "section": "Rejected Alternatives",
          "snippet": "* TypedDict isn't extensible, and it addresses only a specific use case. TypedDict objects are regular dictionaries at runtime, and TypedDict cannot be used with other"
        },
        {
          "pep": 692,
          "section": "Rationale",
          "snippet": "the purposes described in this PEP does not interfere with the use cases described in :pep:`646`."
        },
        {
          "pep": 692,
          "section": "Rejected Ideas / ``TypedDict`` unions",
          "snippet": "e implementation of this PEP and there seems to be no compelling use case to justify the support for this. Therefore, using unions of typed dictionaries to type ``**kwargs``"
        }
      ]
    },
    {
      "objection": "runtime_performance",
      "peps": [
        484
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "r example using decorators or metaclasses. Using type hints for performance optimizations is left as an exercise for the reader. It should also be emphasized that **Python wi"
        }
      ]
    },
    {
      "objection": "tooling_burden",
      "peps": [
        484,
        589,
        655,
        692,
        705
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "lysis is the most important. This includes support for off-line type checkers such as mypy, as well as providing a standard notation that can be used by IDEs for code completion"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotations have no runtime behavior (other than evaluation of the an"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "function or class decorated with the latter to be ignored by the type checker. There are also ``# type: ignore`` comments, and static checkers should support configuration opti"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The double colon",
          "snippet": "ilt on top of type hints. * It catches mistakes even when the type checker is not run. Since it is a separate program, users may choose not to run it (or even instal"
        },
        {
          "pep": 589,
          "section": "Backwards Compatibility",
          "snippet": "y start generating errors once TypedDict support is added to the type checker, since TypedDict types are more restrictive than dictionary types. In particular, they aren't subt"
        },
        {
          "pep": 655,
          "section": "Rejected Ideas / Marking absence of a value with a special constant",
          "snippet": "to implement '''''''''''''''''''''' Eric Traut from the Pyright type checker team has stated that implementing a ``Union[..., Missing]``-style notation would be difficult. [2]_"
        },
        {
          "pep": 692,
          "section": "Rejected Ideas / Changing the meaning of ``**kwargs`` annotations",
          "snippet": "**kwargs`` annotations is well-established in the ecosystem, and type checkers would have to introduce new errors for code that is currently legal."
        },
        {
          "pep": 705,
          "section": "Rejected alternatives / A readonly flag",
          "snippet": "b: B = { \"key1\": 1, \"key2\": 2 } b[\"key1\"] = 4 # Accepted by type checker: \"key1\" is not read-only It would be reasonable for someone familiar with ``frozen`` (from :mod:`d"
        }
      ]
    }
  ],
  "read_first": [
    484,
    589,
    655,
    692,
    705
  ],
  "warnings": [],
  "novelty_note": "This concept combination appears in at least one selected PEP; this does not establish that the specific idea already exists."
}
```

## I want optional runtime type checking of function arguments

```sh
python query.py "I want optional runtime type checking of function arguments" --json
```

```json
{
  "input": "I want optional runtime type checking of function arguments",
  "detected_concepts": [
    "runtime_typing"
  ],
  "closest_peps": [
    {
      "pep": 649,
      "title": "Deferred Evaluation Of Annotations Using Descriptors",
      "status": "Final",
      "score": 2.5,
      "why": [
        "MENTIONS runtime_typing (+1): ey use as input to runtime behavior. Specific use cases include runtime type verification (Pydantic) and glue logic to expose Python APIs in another domain (FastAPI, Typer). The annotation",
        "Graph neighbor of PEP 484: PEP 649 REFERENCES PEP 484 (+0.3); static type information, called *type hints,* as defined in :pep:`484`. Python 3.5 shipped with a new :mod:`typing` module which quickly became very popular. Python 3.6",
        "Graph neighbor of PEP 526: PEP 649 REFERENCES PEP 526 (+0.3); utes, and module attributes, using the approach proposed in :pep:`526`. Static type analysis continued to grow in popularity. However, static type analysis users were i",
        "Graph neighbor of PEP 563: PEP 563 REFERENCES PEP 649 (+0.3); ced with deferred evaluation of annotations, as proposed by :pep:`649` and :pep:`749`. Abstract ======== :pep:`3107` introduced syntax for function annotations, but th",
        "Graph neighbor of PEP 563: PEP 649 SUPERSEDES PEP 563 (+0.6); Replaces: 563"
      ]
    },
    {
      "pep": 749,
      "title": "Implementing PEP 649",
      "status": "Final",
      "score": 2.2,
      "why": [
        "MENTIONS runtime_typing (+1): in ``__annotations__``. This was meant to simplify support for runtime type checkers. Mark Shannon pointed out this idea was flawed since it wasn't handling situations where strings a",
        "Graph neighbor of PEP 484: PEP 484 REFERENCES PEP 563 (+0.3); or other uses of annotations. For the updated schedule see :pep:`563`.) Another possible outcome would be that type hints will eventually become the default meaning for",
        "Graph neighbor of PEP 526: PEP 563 REFERENCES PEP 526 (+0.3); introduced a standard meaning to annotations: type hints. :pep:`526` defined variable annotations, explicitly tying them with the type hinting use case. This PEP propo",
        "Graph neighbor of PEP 544: PEP 563 REFERENCES PEP 544 (+0.3); Other enhancements to the Python programming language like :pep:`544`, :pep:`557`, or :pep:`560`, are already being built on this basis as they depend on type annotation",
        "Graph neighbor of PEP 585: PEP 585 REFERENCES PEP 563 (+0.3); tch Importing those from ``typing`` is deprecated. Due to :pep:`563` and the intention to minimize the runtime impact of typing, this deprecation will not generate Depr",
        "Supersedes matched PEP 563; followed SUPERSEDES chain to its newest endpoint"
      ]
    },
    {
      "pep": 484,
      "title": "Type Hints",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS runtime_typing (+1): Python code to easier static analysis and refactoring, potential runtime type checking, and (perhaps, in some contexts) code generation utilizing type information. Of these goals, stati",
        "Graph neighbor of PEP 526: PEP 526 REFERENCES PEP 484 (+0.3); ted_>`_ listed at the end of this PEP. Abstract ======== :pep:`484` introduced type hints, a.k.a. type annotations. While its main focus was function annotations, it",
        "Graph neighbor of PEP 544: PEP 544 REFERENCES PEP 484 (+0.3); ing.Protocol` Abstract ======== Type hints introduced in :pep:`484` can be used to specify type metadata for static type checkers and other third party tools. However,",
        "Graph neighbor of PEP 563: PEP 563 REFERENCES PEP 484 (+0.3); tions, but the semantics were deliberately left undefined. :pep:`484` introduced a standard meaning to annotations: type hints. :pep:`526` defined variable annotations,"
      ]
    },
    {
      "pep": 526,
      "title": "Syntax for Variable Annotations",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS runtime_typing (+1): rieval of annotations, variable annotations are not designed for runtime type checking. Third party packages will have to be developed to implement such functionality. It should also be",
        "Graph neighbor of PEP 484: PEP 484 REFERENCES PEP 526 (+0.3); without giving it an initial value. This can be done using :pep:`526` variable annotation syntax:: from typing import IO stream: IO[str] The above syntax is accep",
        "Graph neighbor of PEP 544: PEP 544 REFERENCES PEP 526 (+0.3); the logic of :pep:`484`. As well, following :pep:`484` and :pep:`526` we state that protocols are **completely optional**: * No runtime semantics will be imposed for va",
        "Graph neighbor of PEP 563: PEP 563 REFERENCES PEP 526 (+0.3); introduced a standard meaning to annotations: type hints. :pep:`526` defined variable annotations, explicitly tying them with the type hinting use case. This PEP propo"
      ]
    },
    {
      "pep": 544,
      "title": "Protocols: Structural subtyping (static duck typing)",
      "status": "Final",
      "score": 1.9,
      "why": [
        "MENTIONS runtime_typing (+1): other introspection tools this give a reasonable perspective for runtime type checking tools. .. _PEP 544 rejected: Rejected/Postponed Ideas ======================== The ideas in thi",
        "Graph neighbor of PEP 484: PEP 544 REFERENCES PEP 484 (+0.3); ing.Protocol` Abstract ======== Type hints introduced in :pep:`484` can be used to specify type metadata for static type checkers and other third party tools. However,",
        "Graph neighbor of PEP 526: PEP 544 REFERENCES PEP 526 (+0.3); the logic of :pep:`484`. As well, following :pep:`484` and :pep:`526` we state that protocols are **completely optional**: * No runtime semantics will be imposed for va",
        "Graph neighbor of PEP 563: PEP 563 REFERENCES PEP 544 (+0.3); Other enhancements to the Python programming language like :pep:`544`, :pep:`557`, or :pep:`560`, are already being built on this basis as they depend on type annotation"
      ]
    }
  ],
  "outcomes_summary": {
    "status_counts": {
      "Final": 5
    },
    "note": "Header status describes proposal outcome, not support for the input idea. Scores are rule weights, not probabilities."
  },
  "past_objections": [
    {
      "objection": "ambiguity_with_existing_syntax",
      "peps": [
        526,
        544
      ],
      "evidence": [
        {
          "pep": 526,
          "section": "Rejected/Postponed Proposals",
          "snippet": "for example in:: x: int = y = 1 z = w: int = 1 it is ambiguous, what should the types of ``y`` and ``z`` be? Also the second line is difficult to parse. - **A"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Protocols subclassing normal classes",
          "snippet": ". This situation would be really weird. In addition, there is an ambiguity about whether attributes of ``Base`` should become protocol members of ``Proto``."
        }
      ]
    },
    {
      "objection": "backward_compat",
      "peps": [
        484,
        544,
        563,
        649,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotatio"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "ns in function annotations. The new proposal is then considered incompatible with the specification of PEP 3107. Our response to this is that, first of all, the current propos"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The problem of forward declarations",
          "snippet": "evaluated at runtime at all). This of course would run afoul of backwards compatibility, since the Python interpreter doesn't actually know whether a particular annotation is meant to be"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols interoperable with other approaches",
          "snippet": "conceptually a superset of protocols defined here, but using an incompatible syntax to define them, because before :pep:`526` there was no straightforward way to annotate attri"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Use assignments to check explicitly that a class implements a protocol",
          "snippet": "Error: A.__len__ doesn't conform to 'Sized' # (Incompatible return type 'float') This approach moves the check away from the class definition and it almost re"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Prohibit explicit subclassing of protocols by non-protocols",
          "snippet": "This was rejected for the following reasons: * Backward compatibility: People are already using ABCs, including generic ABCs from ``typing`` module. If we prohibit exp"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols special objects at runtime rather than normal ABCs",
          "snippet": "Making protocols non-ABCs will make the backwards compatibility problematic if possible at all. For example, ``collections.abc.Iterable`` is already an ABC, and lo"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals / Non-typing usage of annotations",
          "snippet": "d enhancements require. With this in mind, uses for annotations incompatible with the aforementioned PEPs should be considered deprecated."
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility",
          "snippet": "This is a backwards incompatible change. Applications depending on arbitrary objects to be directly present in annotations will bre"
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility / Deprecation policy",
          "snippet": "e, use of annotations that depend upon their eager evaluation is incompatible with both proposals and is no longer supported."
        },
        {
          "pep": 563,
          "section": "Rejected Ideas / Introducing a new dictionary for the string literal form instead",
          "snippet": "ns_text__`` just-in-time. This idea is supposed to solve the backwards compatibility issue, removing the need for a new ``__future__`` import. Sadly, this is not enough. Postponed ev"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With Stock Semantics",
          "snippet": "'int'>`` when this PEP is active. This is therefore a backwards-incompatible change. However, this example is poor programming style, so this change seems acceptable. There"
        },
        {
          "pep": 749,
          "section": "Backwards Compatibility",
          "snippet": ":pep:`649` provides a thorough discussion of the backwards compatibility implications on existing code that uses either stock or :pep:`563` semantics. However, there is an"
        }
      ]
    },
    {
      "objection": "complexity",
      "peps": [
        484,
        526,
        544,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rejected Alternatives / Which brackets for generic type parameters?",
          "snippet": "such cases, but to most users the rules would feel arbitrary and complex. It would also require us to dramatically change the CPython parser (and every other parser for Py"
        },
        {
          "pep": 526,
          "section": "Rejected/Postponed Proposals",
          "snippet": "tion. In contrast, the PEP implies that if the target is more complex than a single name, its \"left-hand part\" should be evaluated at the point where it occurs in the"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "e protocols non-optional in the future. To reiterate, providing complex runtime semantics for protocol classes is not a goal of this PEP, the main goal is to provide a sup"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make every class a protocol by default",
          "snippet": "otocols anyway, mainly because their interfaces are too large, complex or implementation-oriented (for example, they may include de facto private attributes and metho"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Overriding inferred variance of protocol classes",
          "snippet": "king for protocol implementations in MROs but this will be too complex in a general case, and this \"cure\" requires abandoning simple idea of purely structural subtyping"
        },
        {
          "pep": 749,
          "section": "Annotations and metaclasses / Rejected alternatives",
          "snippet": "the known edge cases with metaclasses, it introduces significant complexity to all classes, including a new built-in type (for the annotations descriptor) with unusual behavio"
        }
      ]
    },
    {
      "objection": "not_enough_use_cases",
      "peps": [
        484,
        544,
        563,
        649,
        749
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "e hinting <gvr-artima_>`_, which is listed as the first possible use case in said PEP. This PEP aims to provide a standard syntax for type annotations, opening up Python co"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "A number of existing or potential use cases for function annotations exist, which are incompatible with type hinting. These may confuse a stat"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Support optional protocol members",
          "snippet": "y they are pretty commonly used. The current realistic potential use cases for protocols in Python don't require these. In the interest of simplicity, we propose to not suppo"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals",
          "snippet": "tion time. This creates a number of issues for the type hinting use case: * forward references: when a type hint contains names that have not been defined yet, that defi"
        },
        {
          "pep": 563,
          "section": "Rationale and Goals / Non-typing usage of annotations",
          "snippet": "and :pep:`526`), is predominantly motivated by the type hinting use case. In Python 3.8 :pep:`484` will graduate from provisional status. Other enhancements to the Python"
        },
        {
          "pep": 563,
          "section": "Backwards Compatibility",
          "snippet": "ll be successfully statically analyzed, which is the predominant use case for annotations. Annotations using nested classes and their respective state are still valid. The"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With PEP 563 Semantics",
          "snippet": "omatically-generated documentation. Users experimented with this use case, and Python's ``pydoc`` has expressed some interest in this technique. This PEP supports this use"
        },
        {
          "pep": 749,
          "section": "New ``annotationlib`` module / Rejected alternatives",
          "snippet": "already quite large, and its import time is prohibitive for some use cases. *Add the functionality to the typing module*: While annotations are mostly used for typing, they"
        }
      ]
    },
    {
      "objection": "runtime_performance",
      "peps": [
        484,
        526
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "r example using decorators or metaclasses. Using type hints for performance optimizations is left as an exercise for the reader. It should also be emphasized that **Python wi"
        },
        {
          "pep": 526,
          "section": "Rejected/Postponed Proposals",
          "snippet": "roblems such as readability and it introduces possible runtime overhead. - **Allow type annotations for tuple unpacking:** This causes ambiguity: it's not clear what th"
        }
      ]
    },
    {
      "objection": "tooling_burden",
      "peps": [
        484,
        526,
        544,
        563,
        649
      ],
      "evidence": [
        {
          "pep": 484,
          "section": "Rationale and Goals",
          "snippet": "lysis is the most important. This includes support for off-line type checkers such as mypy, as well as providing a standard notation that can be used by IDEs for code completion"
        },
        {
          "pep": 484,
          "section": "Compatibility with other uses of function annotations",
          "snippet": "are incompatible with type hinting. These may confuse a static type checker. However, since type hinting annotations have no runtime behavior (other than evaluation of the an"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / What about existing uses of annotations?",
          "snippet": "function or class decorated with the latter to be ignored by the type checker. There are also ``# type: ignore`` comments, and static checkers should support configuration opti"
        },
        {
          "pep": 484,
          "section": "Rejected Alternatives / The double colon",
          "snippet": "ilt on top of type hints. * It catches mistakes even when the type checker is not run. Since it is a separate program, users may choose not to run it (or even instal"
        },
        {
          "pep": 526,
          "section": "Rationale / Non-goals",
          "snippet": "type metadata for third party tools. This PEP does not require type checkers to change their type checking rules. It merely provides a more readable syntax to replace type comm"
        },
        {
          "pep": 526,
          "section": "Rejected/Postponed Proposals",
          "snippet": "way to distinguish between class and instance variables. But a type checker can do useful things with the extra information, for example flag accidental assignments to a c"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals",
          "snippet": "ered a subtype of both ``Sized`` and ``Iterable[int]`` by static type checkers using structural [wiki-structural]_ subtyping:: from typing import Iterator, Iterable class B"
        },
        {
          "pep": 544,
          "section": "Rationale and Goals / Non-goals",
          "snippet": "otocol class. * Any checks will be performed only by third-party type checkers and other tools. * Programmers are free to not use them even if they use type annotations. * Ther"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Allow only protocol methods and force use of getters and setters",
          "snippet": "large code bases is partially due to previous absence of static type checkers for Python, the problem that :pep:`484` and this PEP are aiming to solve. For example:: # withou"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Make protocols interoperable with other approaches",
          "snippet": "` might potentially adopt the ``Protocol`` syntax. In this case, type checkers could be taught to recognize interfaces as protocols and make simple structural checks with respect"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Provide a special intersection type construct",
          "snippet": "yet clear how popular/useful it will be and implementing this in type checkers for non-protocol classes could be difficult. Finally, it will be very easy to add this later if nee"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Prohibit explicit subclassing of protocols by non-protocols",
          "snippet": "lar protocol, making subtyping relationships easier to see. * Type checkers can warn about missing protocol members or members with incompatible types more easily, without h"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Overriding inferred variance of protocol classes",
          "snippet": "variance will make impossible more detailed error messages in type checkers citing particular conflicts in member type signatures. * Finally, explicit is better than implic"
        },
        {
          "pep": 544,
          "section": "Rejected/Postponed Ideas / Support adapters and adaptation",
          "snippet": "e there is a reasonable alternative for such cases with existing tooling, it is therefore proposed not to include adaptation in this PEP."
        },
        {
          "pep": 563,
          "section": "Rejected Ideas / Passing string literals in annotations verbatim to ``__annotations__``",
          "snippet": "annotations__``. This was meant to simplify support for runtime type checkers. Mark Shannon pointed out this idea was flawed since it wasn't handling situations where strings a"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With Stock Semantics",
          "snippet": "one happy. Note that these are both also pain points for static type checkers, and are unsupported by those tools. It seems reasonable to declare that both are at the very leas"
        },
        {
          "pep": 649,
          "section": "Backwards Compatibility / Backwards Compatibility With PEP 563 Semantics",
          "snippet": "n an ``if typing.TYPE_CHECKING`` block. This allowed the static type checkers to import the modules and the type definitions inside, but they wouldn't be imported at runtime. So"
        }
      ]
    }
  ],
  "read_first": [
    484,
    526,
    544,
    649,
    749
  ],
  "warnings": [
    {
      "kind": "superseded",
      "pep": 563,
      "newer_peps": [
        649,
        749
      ]
    }
  ],
  "novelty_note": "This concept combination appears in at least one selected PEP; this does not establish that the specific idea already exists."
}
```

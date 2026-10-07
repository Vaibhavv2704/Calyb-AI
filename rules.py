"""Auditable vocabulary; no model, NLP library, or automatic extraction.

Patterns match words/phrases, ignoring case and treating whitespace uniformly.
These are topical cues, not proof that a PEP actually introduced a feature.
"""
import re

# Each group includes canonical technical terms and a few feature-idea paraphrases.
CONCEPTS = {
    'generics': ('generic', 'generics', 'type parameter', 'type parameters', 'typevar'),
    'protocols': ('protocol', 'protocols', 'structural subtyping', 'duck typing'),
    'runtime_typing': ('runtime type checking', 'runtime checking', 'runtime type verification',
                       'runtime type checkers', 'check function arguments', 'runtime validation'),
    'type_aliases': ('type alias', 'type aliases', 'typealias'),
    'literal_types': ('literal type', 'literal types', 'literalstring'),
    'typeddict': ('typeddict', 'typed dictionary', 'fixed keys', 'fixed-key', 'dict with'),
    'variadic_generics': ('variadic', 'typevartuple', 'parameter packs'),
    'forward_references': ('forward reference', 'forward references'),
    'annotations_evaluation': ('annotation evaluation', 'annotations evaluation',
        'deferred evaluation', 'postponed evaluation', 'lazy evaluation',
        'evaluated lazily', 'lazy annotations', 'type hints evaluated lazily'),
    'type_guards': ('typeguard', 'type guard', 'type guards', 'type narrowing', 'typeis'),
    'final_qualifiers': ('final', 'final qualifier', 'prevent subclassing'),
    'decorators_typing': ('decorator', 'decorators', 'paramspec', 'dataclass_transform'),
    # Separate override concept avoids ranking every decorator ahead of PEP 698.
    'method_overrides': ('override', 'overriding', 'overrides', 'parent method'),
    'union_types': ('union', 'unions', 'union types'),
    'self_types': ('self type', 'self types', 'return own type'),
    'readonly_items': ('read-only', 'readonly', 'read only'),
}

# Objection cues are intentionally restricted to discussion/compatibility sections.
# They identify possible concerns, not attributed arguments or acceptance outcomes.
OBJECTIONS = {
    'backward_compat': ('backward compatibility', 'backwards compatibility',
                      'incompatible', 'break existing', 'breaking change'),
    'runtime_performance': ('performance', 'overhead', 'slow', 'memory usage'),
    'complexity': ('complex', 'complexity', 'complicated'),
    'ambiguity_with_existing_syntax': ('ambiguous', 'ambiguity', 'confusing syntax'),
    'tooling_burden': ('type checker', 'type checkers', 'tooling', 'implementation burden'),
    'not_enough_use_cases': ('use cases', 'use case', 'not needed', 'too rare'),
}
OBJECTION_SECTIONS = ('rationale', 'rejected', 'backward', 'backwards',
                      'compatibility', 'drawback', 'disadvantage')


def keyword_matches(text, dictionary=CONCEPTS):
    """Return first matching literal phrase and short source evidence per category."""
    result = {}
    for category, phrases in dictionary.items():
        for phrase in phrases:
            pattern = r'(?<!\w)' + r'\s+'.join(re.escape(w) for w in phrase.split()) + r'(?!\w)'
            match = re.search(pattern, text, flags=re.I)
            if match:
                snippet = ' '.join(text[max(0, match.start()-65):match.end()+100].split())
                result[category] = {'keyword': phrase, 'snippet': snippet}
                break
    return result

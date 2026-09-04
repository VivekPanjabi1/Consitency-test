"""Project coding standards loaded as a Python module."""

STANDARDS = {
    "general": {
        "max_line_length": 100,
        "indent": "4 spaces (2 for JS)",
        "no_tabs": True,
        "no_trailing_whitespace": True,
        "no_dead_code": True,
        "no_magic_numbers": True,
    },
    "naming": {
        "python_functions_vars": "snake_case",
        "python_classes": "PascalCase",
        "python_constants": "UPPER_SNAKE_CASE",
        "java_methods_vars": "camelCase",
        "java_classes": "PascalCase",
        "java_constants": "UPPER_SNAKE_CASE",
        "js_functions_vars": "camelCase",
        "js_classes": "PascalCase",
        "js_constants": "UPPER_SNAKE_CASE",
    },
    "python": {
        "type_hints_required": True,
        "docstrings_required": True,
        "no_bare_except": True,
        "no_mutable_default_args": True,
        "use_is_none_not_eq_none": True,
        "f_strings_only": True,
    },
    "java": {
        "braces_always_required": True,
        "brace_style": "K&R",
        "no_wildcard_imports": True,
        "javadoc_on_public": True,
        "one_top_level_class_per_file": True,
        "no_system_out_in_library": True,
    },
    "javascript": {
        "no_var": True,
        "strict_equality_only": True,
        "no_console_log_in_library": True,
        "arrow_functions_for_callbacks": True,
    },
    "error_handling": {
        "catch_specific_exceptions": True,
        "never_swallow_silently": True,
        "handle_at_right_boundary": True,
    },
    "functions": {
        "single_responsibility": True,
        "max_cyclomatic_complexity": 10,
        "max_lines": 50,
        "max_nesting_depth": 3,
    },
    "git": {
        "conventional_commits": True,
        "subject_imperative_mood": True,
        "subject_max_chars": 72,
        "one_change_per_pr": True,
    },
}


def get_standard(category: str) -> dict:
    """Return the standards for a given category."""
    return STANDARDS.get(category, {})

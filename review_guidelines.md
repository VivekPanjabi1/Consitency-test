# Code Review Guidelines

## What to check
- Code follows `standard.py` rules
- No magic numbers — use named constants
- No dead code or unused imports
- Functions do one thing, under 50 lines
- Error handling at the right boundary

## Naming
- Python: `snake_case` functions/vars, `PascalCase` classes
- Java: `camelCase` methods/vars, `PascalCase` classes
- JS: `camelCase` functions/vars, `PascalCase` classes

## Python
- Type hints on all public functions
- Docstrings on public functions/classes
- No bare `except:`
- Use `is None`, not `== None`
- f-strings only

## Java
- Braces always required (K&R)
- No wildcard imports
- Javadoc on public classes and methods
- No `System.out` in library code

## JavaScript
- Use `const`/`let`, never `var`
- Use `===` / `!==`, never `==` / `!=`
- No `console.log` in library code

## PR rules
- One logical change per PR
- Conventional Commits
- Reviewer verifies lint passes with no new warnings

# Coding Standards

## General
- Line length: max 100 chars
- 4-space indent, no tabs
- No trailing whitespace; files end with one newline
- No dead code or unused imports

## Naming
- Python: `snake_case` functions/vars, `PascalCase` classes, `UPPER_SNAKE` constants
- Java: `camelCase` methods/vars, `PascalCase` classes, `UPPER_SNAKE` constants

## Python
- Type hints on all public functions
- Docstrings (Google style) on public functions/classes
- No bare `except:` — catch specific exceptions
- No mutable default args (`def f(x=[])`)
- Use `is None`, never `== None`
- f-strings only (no `%` / `.format()`)

## Java
- Braces required even for single-statement blocks (K&R style)
- No wildcard imports (`import java.util.*`)
- Javadoc on public classes and methods
- One top-level class per file
- No magic numbers — use named constants
- No `System.out` in library code — use a logger

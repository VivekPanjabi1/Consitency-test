# Coding Standards & Rules

## General
- Line length: max 100 chars
- 4-space indent (2-space for JS), no tabs
- No trailing whitespace; files end with one newline
- No dead code or unused imports
- No magic numbers — use named constants

## Naming
- Python: `snake_case` functions/vars, `PascalCase` classes, `UPPER_SNAKE` constants
- Java: `camelCase` methods/vars, `PascalCase` classes, `UPPER_SNAKE` constants
- JS: `camelCase` functions/vars, `PascalCase` classes, `UPPER_SNAKE` constants

## Python
- Type hints on all public functions
- Docstrings on public functions/classes
- No bare `except:` — catch specific exceptions
- No mutable default args
- Use `is None`, never `== None`
- f-strings only

## Java
- Braces required even for single-statement blocks (K&R style)
- No wildcard imports
- Javadoc on public classes and methods
- One top-level class per file
- No `System.out` in library code — use a logger

## JavaScript
- Use `const`/`let`, never `var`
- Use `===` / `!==`, never `==` / `!=`
- No `console.log` in library code — use a logger
- Arrow functions for callbacks

## Error Handling
- Handle errors at the right boundary
- Never swallow exceptions silently
- Log the error with context before re-raising

## Functions
- One responsibility per function
- Max cyclomatic complexity: 10
- Max function length: ~50 lines
- Avoid deep nesting (max 3 levels)

## Comments
- Comments explain why, not what
- No commented-out code
- TODOs must include owner + issue link

## Security
- Never hardcode secrets or API keys
- Never log sensitive data
- Validate all external input

## Git
- Conventional Commits: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- Subject in imperative mood, lowercase, max 72 chars
- One logical change per PR

# Coding Principles

## SOLID
- **Single Responsibility** — each class/function does one thing
- **Open/Closed** — open for extension, closed for modification
- **Liskov Substitution** — subclasses must be substitutable for their base
- **Interface Segregation** — no fat interfaces; split into small ones
- **Dependency Inversion** — depend on abstractions, not concretions

## DRY
- Don't Repeat Yourself — extract shared logic into functions/modules

## KISS
- Keep It Simple, Stupid — prefer simple solutions over clever ones

## Naming
- Python: `snake_case` functions/vars, `PascalCase` classes, `UPPER_SNAKE` constants
- Java: `camelCase` methods/vars, `PascalCase` classes, `UPPER_SNAKE` constants
- JS: `camelCase` functions/vars, `PascalCase` classes, `UPPER_SNAKE` constants

## Formatting
- Line length: max 100 chars
- 4-space indent (2-space for JS), no tabs
- No trailing whitespace; files end with one newline

## Error Handling
- Catch specific exceptions, never bare `except`
- Never swallow exceptions silently
- Handle errors at the right boundary

## Java-specific
- Braces required even for single-statement blocks (K&R)
- No wildcard imports
- Javadoc on public classes and methods
- One top-level class per file
- No magic numbers — use named constants
- No `System.out` in library code — use a logger

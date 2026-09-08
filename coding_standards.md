# Coding Standards

This repository follows a simple but strict standard for code quality.

## General

- Max line length: 100 characters
- Indent: 4 spaces (2 for JS)
- No tabs; no trailing whitespace
- No dead code or unused imports
- No magic numbers — use named constants

## Naming

- Python functions/vars: `snake_case`
- Python classes: `PascalCase`
- Python constants: `UPPER_SNAKE_CASE`
- Java methods/vars: `camelCase`
- Java classes: `PascalCase`
- Java constants: `UPPER_SNAKE_CASE`
- JS functions/vars: `camelCase`
- JS classes: `PascalCase`
- JS constants: `UPPER_SNAKE_CASE`

## Python

- Type hints required on all public functions
- Docstrings required on public functions/classes
- No bare `except:`
- No mutable default arguments
- Use `is None`, not `== None`
- f-strings only

## Java

- Braces always required (K&R style)
- No wildcard imports
- Javadoc on public classes and methods
- One top-level class per file
- No `System.out` in library code

## JavaScript

- Use `const`/`let`, never `var`
- Use `===` / `!==`, never `==` / `!=`
- No `console.log` in library code
- Arrow functions for callbacks

## Error Handling

- Catch specific exceptions
- Never swallow errors silently
- Handle at the right boundary

## Functions

- Single responsibility
- Max cyclomatic complexity: 10
- Max 50 lines
- Max nesting depth: 3

## Principles

- **SOLID** — SRP, OCP, LSP, ISP, DIP
- **DRY** — Don't Repeat Yourself
- **KISS** — Keep It Simple, Stupid
- **YAGNI** — You Aren't Gonna Need It
- **Boy Scout Rule** — Leave the code cleaner than you found it
- **Fail Fast** — Validate input early and fail loudly
- **Separation of Concerns** — Split logic into distinct layers
- **Composition Over Inheritance** — Prefer composing small units

## Git

- Conventional Commits
- Subject in imperative mood, max 72 chars
- One logical change per PR
- Reviewer verifies lint passes with no new warnings

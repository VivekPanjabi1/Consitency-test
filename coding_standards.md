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

## SOLID Principles

- **S** — Single Responsibility: one reason to change
- **O** — Open/Closed: open for extension, closed for modification
- **L** — Liskov Substitution: subtypes substitutable for base types
- **I** — Interface Segregation: small client-specific interfaces
- **D** — Dependency Inversion: depend on abstractions, not concretions

## Git

- Conventional Commits
- Subject in imperative mood, max 72 chars
- One logical change per PR
- Reviewer verifies lint passes with no new warnings

# Repository Rules

## Branching

- `main` is the default branch
- Create feature branches as `feat/<name>` or `fix/<name>`
- Delete branches after merge

## Commits

- Use Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`)
- Subject in imperative mood, max 72 chars
- One logical change per commit

## Pull Requests

- One logical change per PR
- Link related issues in the PR description
- Reviewer must verify lint passes with no new warnings
- No direct pushes to `main` without review (except for docs)

## Code Quality

- All code must pass the rules in `coding_standards.md`
- No new violations introduced — fix existing ones when you touch a file
- Run lint before requesting review

## File Organization

- One top-level class per file (Java)
- Keep files under 300 lines
- Group related modules in folders when the repo grows

## Enforcement

- Violations in `bad_example.py` and `bad_small.py` are intentional for testing
- All other files must be compliant
- CI should fail on new violations

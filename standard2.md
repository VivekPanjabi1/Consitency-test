# Coding Standards (Supplementary)

Additional rules complementing `standard.md`.

## Comments & Documentation
- Comments explain *why*, not *what*
- No commented-out code in committed files
- TODOs must include owner + issue: `// TODO(vivek): refactor (#42)`

## Functions & Methods
- One responsibility per function
- Max cyclomatic complexity: 10
- Max function length: ~50 lines

## Error Handling
- Handle errors at the right boundary; don't wrap every line in try/catch
- Never swallow exceptions silently

## Testing
- Test files: `*_test.py` (Python), `*Test.java` (Java)
- Every public function/method has at least one test
- Test names describe behavior: `test_greet_returns_none_for_non_positive_times`

## Git
- Conventional Commits: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
- Subject in imperative mood, lowercase, max 72 chars
- Branches: `feature/<desc>`, `fix/<desc>`, `docs/<desc>`
- One logical change per PR

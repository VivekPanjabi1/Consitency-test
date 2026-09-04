# Best Practices

## Error Handling
- Handle errors at the right boundary
- Never swallow exceptions silently
- No bare `except:` — catch specific exceptions
- Log the error with context before re-raising

## Code Organization
- One responsibility per function
- Keep functions under 50 lines
- Avoid deep nesting (max 3 levels)
- Group related functions in modules

## Security
- Never hardcode secrets or API keys
- Never log sensitive data
- Validate all external input
- Use parameterized queries for SQL

## Performance
- Avoid premature optimization
- Use appropriate data structures
- Batch database and API calls when possible
- Cache expensive computations

## Collaboration
- Keep PRs small and focused
- Review every PR before merge
- Write clear commit messages (Conventional Commits)
- Document public APIs

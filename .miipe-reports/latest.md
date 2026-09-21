# MIIPE Local Scan Report

- Scan: `6a8331b3-48d7-4e2d-928c-6f7a8e85f0ff`
- Commit: `de7e00159f166d3f47aec03c5fd3d83cc7b2d296`
- Status: completed
- Generated: 2026-09-21T19:54:45.413726+00:00
- Findings: 12

## Coverage

- Scanners: bandit unknown
- Files scanned: 0
- Files not scanned: 0

## Security Review

### 1. Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal stri

- Severity: warning
- Status: open
- Location: `app.py:6`
- CWE: CWE-798
- Validation: needs_review

Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal string 'admin123' at module level. This credential is committed to version control, visible to anyone with repository access, and trivially guessable. It is also used directly in the __main__ block to call login_user(), meaning it is exercised at runtime.

**Triage:** The literal string 'admin123' is assigned to ADMIN_PASSWORD at line 6 and used at line 38. This is a hardcoded credential in version-controlled source. The scanner was unavailable; agent-found issue.

**Recommendation:** Remove all hardcoded credentials from source code. Load secrets from environment variables (os.environ) or a secrets manager (e.g. AWS Secrets Manager, HashiCorp Vault). Rotate the exposed credential immediately.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-798 (Use of Hard-coded Credentials).”

### 2. Authentication bypass risk: login_user() returns raw database rows but performs 

- Severity: warning
- Status: open
- Location: `app.py:9`
- CWE: CWE-306
- Validation: needs_review

Authentication bypass risk: login_user() returns raw database rows but performs no authorisation check on the result. The caller receives whatever rows the (injectable) query returns and there is no check that the result is non-empty, that the returned user is active/non-locked, or that the password is verified against a stored hash. Combined with the SQL injection at line 11-15, an attacker can bypass authentication entirely without knowing any valid password.

**Triage:** The function returns raw rows with no post-query authorisation logic. The SQL injection vulnerability means the WHERE clause can be trivially bypassed. No access-control check exists between the query result and the caller. Agent-found A01 issue.

**Recommendation:** Enforce authentication at the application layer: (1) use parameterised queries, (2) store passwords as bcrypt/argon2 hashes and verify with a constant-time comparison, (3) check that exactly one row is returned and that the account is in an active state before granting access, (4) implement account lockout after repeated failures.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-306 (Missing Authentication for Critical Function).”

### 3. SQL injection via string interpolation in login_user(). The query is built by di

- Severity: warning
- Status: open
- Location: `app.py:11`
- CWE: CWE-89
- Validation: needs_review

SQL injection via string interpolation in login_user(). The query is built by directly embedding the 'username' and 'password' parameters into an f-string SQL statement. An attacker can supply a value such as `' OR '1'='1` to bypass authentication entirely or exfiltrate arbitrary data.

**Triage:** The query string is constructed with f-string interpolation of raw function parameters (username, password) with no sanitisation, escaping, or parameterisation. This is a textbook SQL injection pattern. The scanner was unavailable so no scanner finding exists; this is an agent-found issue.

**Recommendation:** Replace string interpolation with parameterised queries: `cursor.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', (username, password))`. Never concatenate or interpolate user-controlled values into SQL strings.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-89 (Improper Neutralisation of Special Elements used in an SQL Command).”

### 4. OS command injection via shell=True in fetch_remote_url(). The user-supplied 'us

- Severity: warning
- Status: open
- Location: `app.py:21`
- CWE: CWE-78
- Validation: needs_review

OS command injection via shell=True in fetch_remote_url(). The user-supplied 'user_input' value is interpolated directly into a shell command string and executed with `subprocess.run(..., shell=True)`. An attacker can inject arbitrary shell commands (e.g. `; rm -rf /` or backtick subshells) through the URL argument.

**Triage:** The command string is built with an f-string embedding the raw 'user_input' parameter, then executed with shell=True. This allows shell metacharacter injection. The scanner was unavailable; agent-found issue.

**Recommendation:** Never pass shell=True with user-controlled input. Use a list-form invocation: `subprocess.run(['curl', '-fsSL', user_input, '-o', '/tmp/user_data.txt'], shell=False, check=True)`. Additionally, validate and allowlist the URL scheme and host before passing it to any subprocess.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-78 (Improper Neutralisation of Special Elements used in an OS Command).”

### 5. Weak cryptographic algorithm (MD5) used for session token generation in create_s

- Severity: warning
- Status: open
- Location: `app.py:26`
- CWE: CWE-327
- Validation: needs_review

Weak cryptographic algorithm (MD5) used for session token generation in create_session_token(). MD5 is cryptographically broken, collision-prone, and trivially reversible via rainbow tables. Using it to derive session tokens makes those tokens predictable and forgeable.

**Triage:** hashlib.md5() is called to produce a session token. MD5 is a broken algorithm for security use. The scanner was unavailable; agent-found issue.

**Recommendation:** Use a cryptographically secure token generator such as `secrets.token_hex(32)` for session tokens. If a hash is required, use SHA-256 or SHA-3 at minimum. Never use MD5 or SHA-1 for security-sensitive purposes.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-327 (Use of a Broken or Risky Cryptographic Algorithm).”

### 6. OS command injection via os.system() in remove_user(). The 'user_name' parameter

- Severity: warning
- Status: open
- Location: `app.py:31`
- CWE: CWE-78
- Validation: needs_review

OS command injection via os.system() in remove_user(). The 'user_name' parameter is interpolated directly into a shell command string passed to os.system(). An attacker controlling 'user_name' can inject shell metacharacters (e.g. `; cat /etc/passwd`) or path-traversal sequences (e.g. `../../etc`) to execute arbitrary commands or delete unintended files.

**Triage:** os.system() is called with an f-string embedding the raw 'user_name' parameter. This is a direct OS command injection vector. The scanner was unavailable; agent-found issue.

**Recommendation:** Replace os.system() with `shutil.rmtree()` or `os.remove()` operating on a validated, canonicalised path. Verify the resolved path is within the expected directory before deletion. Never pass user-controlled strings to os.system().

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-78 (Improper Neutralisation of Special Elements used in an OS Command).”

### 7. Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal stri

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:11`
- CWE: CWE-798
- Validation: needs_review

Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal string 'admin123' at module level in owasp_violation_push.py, identical to app.py. This credential is committed to version control and trivially guessable.

**Triage:** Literal 'admin123' assigned to ADMIN_PASSWORD at line 11 and used at line 49. Hardcoded credential in version-controlled source. Agent-found issue.

**Recommendation:** Remove all hardcoded credentials. Load secrets from environment variables or a secrets manager. Rotate the exposed credential immediately.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-798 (Use of Hard-coded Credentials).”

### 8. SQL injection via string interpolation in login_user() (owasp_violation_push.py)

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:18`
- CWE: CWE-89
- Validation: needs_review

SQL injection via string interpolation in login_user() (owasp_violation_push.py). Identical pattern to app.py: username and password are interpolated directly into an f-string SQL query with no parameterisation. An attacker can bypass authentication or exfiltrate data.

**Triage:** Identical SQL injection pattern to app.py. Raw f-string interpolation of function parameters into a SQL query. The scanner was unavailable; agent-found issue.

**Recommendation:** Use parameterised queries: `cursor.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', (username, password))`. Never interpolate user-controlled values into SQL strings.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-89 (Improper Neutralisation of Special Elements used in an SQL Command).”

### 9. OS command injection via shell=True in fetch_user_data(). The 'url' parameter is

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:28`
- CWE: CWE-78
- Validation: needs_review

OS command injection via shell=True in fetch_user_data(). The 'url' parameter is interpolated into a shell command string and executed with subprocess.run(..., shell=True). An attacker controlling the URL can inject arbitrary shell commands.

**Triage:** Identical shell injection pattern to app.py fetch_remote_url(). User-controlled 'url' embedded in f-string command with shell=True. Agent-found issue.

**Recommendation:** Use list-form subprocess invocation with shell=False: `subprocess.run(['curl', '-fsSL', url, '-o', '/tmp/remote_data.txt'], shell=False, check=True)`. Validate and allowlist the URL before use.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-78 (Improper Neutralisation of Special Elements used in an OS Command).”

### 10. Weak cryptographic algorithm (MD5) used for session token generation in create_s

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:34`
- CWE: CWE-327
- Validation: needs_review

Weak cryptographic algorithm (MD5) used for session token generation in create_session_token() (owasp_violation_push.py). Identical pattern to app.py: MD5 is cryptographically broken and unsuitable for session tokens.

**Triage:** hashlib.md5() used to produce a session token. Identical broken-crypto pattern to app.py. Agent-found issue.

**Recommendation:** Use `secrets.token_hex(32)` for session tokens. If hashing is required, use SHA-256 or SHA-3.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-327 (Use of a Broken or Risky Cryptographic Algorithm).”

### 11. OS command injection via os.system() in delete_temp_files(). The 'username' para

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:39`
- CWE: CWE-78
- Validation: needs_review

OS command injection via os.system() in delete_temp_files(). The 'username' parameter is interpolated directly into a shell command string passed to os.system(). An attacker can inject shell metacharacters or path-traversal sequences.

**Triage:** os.system() called with f-string embedding raw 'username'. Identical OS command injection pattern to app.py remove_user(). Agent-found issue.

**Recommendation:** Replace os.system() with `shutil.rmtree()` or `os.remove()` on a validated, canonicalised path. Confirm the resolved path is within the expected directory before deletion.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-78 (Improper Neutralisation of Special Elements used in an OS Command).”

### 12. Log injection via unsanitised user input in debug_log(). The 'message' parameter

- Severity: warning
- Status: open
- Location: `owasp_violation_push.py:44`
- CWE: CWE-117
- Validation: needs_review

Log injection via unsanitised user input in debug_log(). The 'message' parameter is written directly into /tmp/debug.log with no sanitisation. An attacker can inject newlines or control characters to forge log entries, obscure audit trails, or exploit log-parsing tools downstream.

**Triage:** Raw 'message' parameter written directly to a log file via f-string with no sanitisation. Enables log injection / log forging. Agent-found issue.

**Recommendation:** Sanitise log input by stripping or escaping newline characters (`\n`, `\r`) and other control characters before writing. Use a structured logging library (e.g. Python's `logging` module with a formatter) rather than raw file writes. Avoid logging raw user-controlled data.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard KB documents were found for this organisation. Finding is reported on the basis of agent semantic analysis and CWE-117 (Improper Output Neutralisation for Logs).”

## Code Consistency

- Findings: 23
- Files: 3

### 1. Hardcoded magic string used as a credential constant

- Severity: critical
- Location: `app.py:7`

`ADMIN_PASSWORD = "admin123"` embeds a literal password directly in source code. The standards prohibit magic numbers/strings — named constants must not themselves be raw secret literals baked into the codebase. Credentials must be sourced from environment variables or a secrets manager, not committed as string literals.

**Citations:**
- `coding_standards.md`: “No magic numbers — use named constants”

### 2. Public function missing type hints

- Severity: critical
- Location: `app.py:9`

`login_user(username, password)` declares no parameter or return type hints. All public functions must carry type hints per the Python section of the coding standards. Fix: annotate as `def login_user(username: str, password: str) -> list:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 3. Public function missing docstring

- Severity: critical
- Location: `app.py:9`

`login_user` has no docstring. The coding standards require docstrings on all public functions and classes. A docstring describing the function's purpose, parameters, and return value must be added.

**Citations:**
- `coding_standards.md`: “Docstrings required on public functions/classes”

### 4. Function violates Single Responsibility Principle

- Severity: warning
- Location: `app.py:9`

`login_user` both constructs a database connection AND executes a query AND returns results — multiple distinct responsibilities in one function. Per the SOLID/SRP rule, each function should have one reason to change. Database connection management should be separated from query execution.

**Citations:**
- `coding_standards.md`: “S — Single Responsibility: one reason to change”

### 5. Public function missing type hints

- Severity: critical
- Location: `app.py:20`

`fetch_remote_url(user_input)` declares no parameter or return type hints. Fix: annotate as `def fetch_remote_url(user_input: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 6. Public function missing docstring

- Severity: critical
- Location: `app.py:20`

`fetch_remote_url` has no docstring. A docstring describing the function's purpose, parameters, and return value must be added.

**Citations:**
- `coding_standards.md`: “Docstrings required on public functions/classes”

### 7. Public function missing type hints

- Severity: critical
- Location: `app.py:26`

`create_session_token(secret_value)` declares no parameter or return type hints. Fix: annotate as `def create_session_token(secret_value: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 8. Public function missing docstring

- Severity: critical
- Location: `app.py:26`

`create_session_token` has no docstring. A docstring describing the function's purpose, parameters, and return value must be added.

**Citations:**
- `coding_standards.md`: “Docstrings required on public functions/classes”

### 9. Public function missing type hints

- Severity: critical
- Location: `app.py:30`

`write_debug_log(user_name)` declares no parameter or return type hints. Fix: annotate as `def write_debug_log(user_name: str) -> None:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 10. Public function missing docstring

- Severity: critical
- Location: `app.py:30`

`write_debug_log` has no docstring. A docstring describing the function's purpose, parameters, and return value must be added.

**Citations:**
- `coding_standards.md`: “Docstrings required on public functions/classes”

### 11. Public function missing type hints

- Severity: critical
- Location: `app.py:35`

`remove_user(user_name)` declares no parameter or return type hints. Fix: annotate as `def remove_user(user_name: str) -> bool:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 12. Public function missing docstring

- Severity: critical
- Location: `app.py:35`

`remove_user` has no docstring. A docstring describing the function's purpose, parameters, and return value must be added.

**Citations:**
- `coding_standards.md`: “Docstrings required on public functions/classes”

### 13. Magic number used instead of a named constant

- Severity: critical
- Location: `ex.py:1`

The literal `10` on line 1 is a magic number assigned directly to `a`. Per the coding standards, all magic numbers must be replaced with named constants (e.g., `A_VALUE = 10` using UPPER_SNAKE_CASE for a module-level constant).

**Citations:**
- `coding_standards.md`: “No magic numbers — use named constants”

### 14. Python constants at module level must use UPPER_SNAKE_CASE

- Severity: warning
- Location: `ex.py:1`

The module-level names `a` and `b` appear to be constants (they are bare assignments at module scope with no enclosing function or class). The naming standard requires Python constants to use `UPPER_SNAKE_CASE`. They should be renamed to descriptive `UPPER_SNAKE_CASE` identifiers (e.g., `BASE_VALUE`, `RESULT`).

**Citations:**
- `coding_standards.md`: “Python constants: `UPPER_SNAKE_CASE`”

### 15. Magic number used instead of a named constant

- Severity: critical
- Location: `ex.py:2`

The literal `2` on line 2 is a magic number used directly in an expression. It must be extracted into a named constant with an `UPPER_SNAKE_CASE` name that communicates its intent.

**Citations:**
- `coding_standards.md`: “No magic numbers — use named constants”

### 16. Dead code — assigned value is never used before being overwritten

- Severity: critical
- Location: `ex.py:2`

`b` is assigned on line 2 (`b = 2 + a`) but is immediately overwritten on line 3 (`b = a + b`) without the line-2 value ever being read in between. The line-2 assignment is therefore dead code and must be removed or corrected.

**Citations:**
- `coding_standards.md`: “No dead code or unused imports”

### 17. Hardcoded magic string used as a credential constant

- Severity: critical
- Location: `owasp_violation_push.py:11`

`ADMIN_PASSWORD = "admin123"` embeds a literal password directly in source code. Credentials must be sourced from environment variables or a secrets manager, not committed as string literals.

**Citations:**
- `coding_standards.md`: “No magic numbers — use named constants”

### 18. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:14`

`login_user(username, password)` has a docstring but no parameter or return type hints. Fix: annotate as `def login_user(username: str, password: str) -> list:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 19. Function violates Single Responsibility Principle

- Severity: warning
- Location: `owasp_violation_push.py:14`

`login_user` manages a DB connection, builds a query, executes it, and returns results — multiple responsibilities. Connection management should be separated from query logic.

**Citations:**
- `coding_standards.md`: “S — Single Responsibility: one reason to change”

### 20. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:27`

`fetch_user_data(url)` has a docstring but no parameter or return type hints. Fix: annotate as `def fetch_user_data(url: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 21. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:33`

`create_session_token(secret_value)` has a docstring but no parameter or return type hints. Fix: annotate as `def create_session_token(secret_value: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 22. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:38`

`delete_temp_files(username)` has a docstring but no parameter or return type hints. Fix: annotate as `def delete_temp_files(username: str) -> bool:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 23. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:44`

`debug_log(message)` has a docstring but no parameter or return type hints. Fix: annotate as `def debug_log(message: str) -> None:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

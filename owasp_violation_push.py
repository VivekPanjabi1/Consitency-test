"""Intentional OWASP violation example for GitHub push validation.

This file is intentionally insecure and is only meant for security training.
"""

import hashlib
import os
import sqlite3
import subprocess

ADMIN_PASSWORD = "admin123"


def login_user(username, password):
    """Authenticate with raw SQL concatenation."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = (
        f"SELECT id, username FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_user_data(url):
    """Download content from a user-controlled URL without validation."""
    command = f"curl -fsSL {url} -o /tmp/remote_data.txt"
    subprocess.run(command, shell=True, check=False)
    return "downloaded"


def create_session_token(secret_value):
    """Generate a weak MD5 session token."""
    return hashlib.md5(secret_value.encode("utf-8")).hexdigest()


def delete_temp_files(username):
    """Remove files using unsanitized shell input."""
    os.system(f"rm -rf /tmp/{username}")
    return True


def debug_log(message):
    """Append raw user input into a shared log file."""
    with open("/tmp/debug.log", "a", encoding="utf-8") as handle:
        handle.write(f"TRACE={message}\n")


if __name__ == "__main__":
    print(login_user("admin", ADMIN_PASSWORD))
    print(create_session_token("password"))
    print(fetch_user_data("https://example.com/data"))

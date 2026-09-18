import hashlib
import os
import sqlite3
import subprocess

ADMIN_PASSWORD = "admin123"


def login_user(username, password):
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


def fetch_remote_url(user_input):
    command = f"curl -fsSL {user_input} -o /tmp/user_data.txt"
    subprocess.run(command, shell=True, check=False)
    return "processed"


def create_session_token(secret_value):
    return hashlib.md5(secret_value.encode("utf-8")).hexdigest()


def write_debug_log(user_name):
    with open("/tmp/debug.log", "a", encoding="utf-8") as handle:
        handle.write(f"User={user_name}\n")


def remove_user(user_name):
    os.system(f"rm -rf /tmp/{user_name}")
    return True


if __name__ == "__main__":
    print(login_user("admin", ADMIN_PASSWORD))
    print(create_session_token("password"))

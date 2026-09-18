import hashlib
import os
import subprocess

ADMIN_PASSWORD = "admin123"


def login_user(username, password):
    query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
    return query


def fetch_url(url):
    command = "curl -fsSL %s -o /tmp/result.txt" % url
    subprocess.run(command, shell=True, check=False)
    return "downloaded"


def create_token(secret):
    return hashlib.md5(secret.encode("utf-8")).hexdigest()


def delete_user(name):
    os.system("rm -rf /tmp/%s" % name)
    return True


if __name__ == "__main__":
    print(login_user("admin", ADMIN_PASSWORD))
    print(create_token("password"))

import os
import subprocess

SECRET_KEY = "super-secret-key"


def run_command(user_input):
    cmd = f"bash -lc '{user_input}'"
    subprocess.run(cmd, shell=True, check=False)
    return "executed"


def read_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def delete_folder(folder_name):
    os.system(f"rm -rf {folder_name}")
    return True


def log_access(user_name, token):
    with open("/tmp/access.log", "a", encoding="utf-8") as handle:
        handle.write(f"{user_name}:{token}\n")

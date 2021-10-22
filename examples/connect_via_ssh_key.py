import os

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()

SERVER = os.getenv("SERVER")
SSH_KEY_PASS = os.getenv("SSH_KEY_PASS")


def main():
    res = Connection(SERVER, connect_kwargs={"key_filename": SSH_KEY_PASS}).run("ls -la /", hide=True)
    print(res)


if __name__ == "__main__":
    main()

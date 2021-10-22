import os

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()

SERVER = os.getenv("SERVER")


def main():
    res = Connection(SERVER).run("ls -la /fe3f", hide=True)
    print(res.exited)


if __name__ == "__main__":
    main()

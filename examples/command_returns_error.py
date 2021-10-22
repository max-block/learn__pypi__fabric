import os

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()

SERVER = os.getenv("SERVER")


def main():
    result = Connection(SERVER).run("ls -la /fe3f", hide=True, warn=True)
    print(result.ok)  # False
    print(result.exited)  # 2
    print(result.stdout)  #
    print(result.stderr)  # ls: cannot access '/fe3f': No such file or directory


if __name__ == "__main__":
    main()

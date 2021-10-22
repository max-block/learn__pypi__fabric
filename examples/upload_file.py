import os
from pathlib import Path

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()

SERVER = os.getenv("SERVER")


def main():
    local_file = Path(__file__).parent.joinpath("../README.txt").absolute()
    Connection(SERVER).put(local_file, remote="/tmp2")


if __name__ == "__main__":
    main()

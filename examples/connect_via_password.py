import os

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()

SERVER = os.getenv("SERVER")
PASSWORD = os.getenv("PASSWORD")


def main():
    res = Connection(SERVER, connect_kwargs={"password": PASSWORD}).run("ls -la /", hide=True)
    print(res)


if __name__ == "__main__":
    main()

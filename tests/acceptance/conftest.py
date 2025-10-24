import os
import subprocess
import time
from pathlib import Path
from threading import Thread
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

import httpx
import pytest


def attempt_connect():
    try:
        print("testing connection")
        return httpx.get("http://localhost:8000")
    except (httpx.ConnectError, httpx.ReadError):
        attempt_connect()

def start_docker():
    subprocess.call(["docker", "compose", "up"])


@pytest.fixture
def start_service():
    docker = Thread(target=start_docker)
    docker.start()
    attempt_connect()
    yield
    subprocess.call(["docker", "compose", "down"], shell=True)


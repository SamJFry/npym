import subprocess
from pathlib import Path
from threading import Thread
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

import httpx
import pytest


def attempt_connect():
    try:
        return httpx.get("http://localhost:8000")
    except:
        attempt_connect()

def start_docker():
    subprocess.call(["docker", "compose", "up"])


@pytest.fixture
def start_service():
    docker = Thread(target=start_docker)
    docker.start()
    attempt_connect()
    yield
    docker._delete()

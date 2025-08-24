import os
import subprocess
from pathlib import Path

import httpx
import pytest


def attempt_connect():
    try:
        return httpx.get("http://localhost:8080")
    except httpx.ConnectError:
        attempt_connect()

@pytest.fixture
def start_service():
    os.chdir(Path(__name__).parent.parent)
    print(os.getcwd())
    subprocess.call(["cmd", "/c", "sudo",  "docker",  "compose", "up"], shell=True)
    attempt_connect()
    yield
    subprocess.call(["cmd", "/c", "sudo", "docker", "compose", "down"], shell=True)


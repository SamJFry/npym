import os
import subprocess
from pathlib import Path

import httpx
import pytest


@pytest.fixture
def start_service():
    os.chdir(Path(__name__).parent.parent)
    print(os.getcwd())
    subprocess.call(
        ["cmd", "/c", "sudo",  "docker",  "compose", "up"],
        shell=True
    )
    service_status = httpx.get("http://localhost:8000")
    while service_status.status_code != 200:
        service_status = httpx.get("http://localhost:8000")

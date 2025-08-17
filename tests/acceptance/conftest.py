import os
import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def start_service():
    os.chdir(Path(__file__).parents()[2])
    subprocess.run("sudo docker compose up")


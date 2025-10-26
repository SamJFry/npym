import pytest
from fastapi.testclient import TestClient

from npym.main import app


@pytest.fixture()
def client():
    return TestClient(app)


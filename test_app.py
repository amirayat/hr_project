import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def replace_do_something():
    raise Exception()


national_code = "1234567890"
def test_employee_arrived(monkeypatch: pytest.MonkeyPatch):
    response = client.get("/arrival_departure/{national_code}/arrivced/")
    assert response.status_code == 200
    assert response.json() == {"detail": "done."}
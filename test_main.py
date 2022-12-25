import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def replace_do_something():
    raise Exception()


def test_employee_arrived(monkeypatch: pytest.MonkeyPatch):
    response = client.put("/arrival_departure/1234567890/arrived")
    assert response.status_code == 200
    assert response.json() == {"detail": "done."}


def test_employee_departure(monkeypatch: pytest.MonkeyPatch):
    response = client.put("/arrival_departure/1234567890/departured")
    assert response.status_code == 200
    assert response.json() == {"detail": "done."}
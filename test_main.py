from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

national_code = "1234567890"


def test_employee_arrived():
    response = client.put(f"/arrival_departure/{national_code}/arrived")
    assert response.status_code == 200
    assert response.json() == {"detail": "done."}


def test_employee_departure():
    response = client.put(f"/arrival_departure/{national_code}/departured")
    assert response.status_code == 200
    assert response.json() == {"detail": "done."}
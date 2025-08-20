from http import HTTPStatus

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health() -> None:
    r = client.get("/health")
    assert r.status_code == HTTPStatus.OK
    assert r.json()["status"] == "ok"

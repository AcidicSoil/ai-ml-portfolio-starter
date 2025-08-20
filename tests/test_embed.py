from http import HTTPStatus

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

EXPECTED_EMBEDDING_DIM = 384


def test_embed() -> None:
    r = client.post("/embed", json={"text": "hello"})
    assert r.status_code == HTTPStatus.OK
    data = r.json()
    assert data["dim"] == EXPECTED_EMBEDDING_DIM

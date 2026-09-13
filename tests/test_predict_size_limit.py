"""TDD round (Etapa 2): tests written BEFORE the size-limit feature exists.
Feature: /predict should reject uploads larger than a maximum size, with a
clear error, instead of silently accepting arbitrarily large files."""
import io

from fastapi.testclient import TestClient

from src.inference_service.main import app, MAX_UPLOAD_BYTES
from tests.conftest import authenticate

client = TestClient(app)


def _upload(client, size_bytes: int, content_type: str = "image/jpeg", filename: str = "leaf.jpg"):
    return client.post(
        "/predict",
        files={"file": (filename, io.BytesIO(b"x" * size_bytes), content_type)},
    )


def test_predict_rejects_file_over_max_size():
    authenticate(client)
    response = _upload(client, MAX_UPLOAD_BYTES + 1)
    assert response.status_code == 413
    assert "too large" in response.json()["detail"].lower()


def test_predict_accepts_file_at_max_size_if_otherwise_valid(monkeypatch):
    """A file exactly at the size limit must not be rejected for size alone
    (it may still fail decoding if it isn't a real image - that's a separate
    concern, so we bypass decoding here to isolate the size check)."""
    authenticate(client)

    def fake_predict(self, image_bytes):
        return {
            "label": "healthy",
            "confidence": 0.9,
            "probabilities": {"healthy": 0.9, "cssvd": 0.05, "anthracnose": 0.05},
        }

    monkeypatch.setattr("src.inference_service.model.LeafClassifier.predict", fake_predict)
    response = _upload(client, MAX_UPLOAD_BYTES)
    assert response.status_code == 200


def test_predict_rejects_empty_file_with_clear_message():
    authenticate(client)
    response = _upload(client, 0)
    assert response.status_code == 400
    assert "no file" in response.json()["detail"].lower()

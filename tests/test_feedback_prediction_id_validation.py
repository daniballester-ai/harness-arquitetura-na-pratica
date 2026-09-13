"""Tests written AFTER the feature (no-TDD round, Etapa 2): prediction_id
must be a positive integer in POST /predict/{prediction_id}/feedback."""
from fastapi.testclient import TestClient

from src.inference_service.main import app
from tests.conftest import authenticate

client = TestClient(app)


def test_feedback_rejects_zero_prediction_id():
    authenticate(client)
    response = client.post("/predict/0/feedback", json={"label": "healthy"})
    assert response.status_code == 400


def test_feedback_rejects_negative_prediction_id():
    authenticate(client)
    response = client.post("/predict/-1/feedback", json={"label": "healthy"})
    assert response.status_code == 400

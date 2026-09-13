from fastapi.testclient import TestClient

from src.inference_service.main import app

client = TestClient(app)


def test_version_reports_api_version_and_model_architecture():
    response = client.get("/version")
    assert response.status_code == 200
    body = response.json()
    assert body["api_version"] == "1.0.0"
    assert body["model_architecture"] == "efficientnet_b0"

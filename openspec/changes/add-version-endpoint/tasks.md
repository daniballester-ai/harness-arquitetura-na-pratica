## 1. Expose model architecture

- [ ] 1.1 In `src/inference_service/model.py`, add `self.architecture = mapping["architecture"]` in `LeafClassifier.__init__` (right after `self.classes = mapping["classes"]`) and verify it's readable as `classifier.architecture`

## 2. Add the endpoint

- [ ] 2.1 In `src/inference_service/main.py`, add a `GET /version` route (right after `/health`) returning `{"api_version": "1.0.0", "model_architecture": classifier.architecture}` and verify it responds 200 via `TestClient`

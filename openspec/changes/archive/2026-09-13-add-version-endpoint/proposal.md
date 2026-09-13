## Why

There is no way for a client (or an operator debugging a deployment) to check which API version and model architecture are actually running behind an instance of this service, short of reading the source code. A simple, read-only `/version` endpoint closes that gap.

## What Changes

- Add a new `GET /version` endpoint that returns the API version and the model architecture currently loaded.
- Expose `architecture` as a public attribute on `LeafClassifier` (currently read locally in `__init__` only for validation, then discarded).

## Capabilities

### New Capabilities
- `leaf-inference-service-version`: reports the running API version and the loaded model's architecture via a read-only endpoint.

### Modified Capabilities
(none — this is a new, additive capability; no existing requirement changes)

## Impact

- `src/inference_service/main.py`: new `GET /version` route.
- `src/inference_service/model.py`: `LeafClassifier.__init__` now stores `self.architecture`.
- No new dependencies, no breaking changes, no auth required (read-only, non-sensitive metadata).

# leaf-inference-service-version Specification

## Purpose

Lets a client or operator confirm which API version and model architecture are actually running behind a given deployment of the service.

## Requirements

### Requirement: Version endpoint
The service SHALL expose a read-only `GET /version` endpoint that returns the running API version and the architecture of the currently loaded model, without requiring authentication.

#### Scenario: Version reported
- **WHEN** a client sends `GET /version`
- **THEN** the service returns 200 with the API version string and the model architecture (e.g. `"efficientnet_b0"`)

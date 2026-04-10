🔹 Task 3: MLOps Workflow (Docker + CI/CD)
🎯 Objective

Create a reproducible and automated workflow for building and deploying the model.

🐳 Dockerization
Containerized inference service
Ensures environment consistency across systems
Includes:
Dependencies
Model artifacts
API server
🔄 CI/CD Pipeline

Implemented using GitHub Actions:

Pipeline Steps:
Code linting
Unit testing
Docker image build
(Extendable) Deployment
📦 Model Versioning Strategy
Version control via:
Git (code)
Model artifacts stored with version tags
Suggested improvements:
Use MLflow or DVC for full lifecycle tracking
🔁 Automated Retraining (Conceptual Design)

To handle model drift:

Monitor performance metrics (accuracy, F1, etc.)
Trigger retraining when performance drops below threshold
Retrain pipeline runs automatically
Deploy updated model
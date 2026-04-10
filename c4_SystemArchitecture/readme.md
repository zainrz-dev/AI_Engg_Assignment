🔹 Task 4: System Architecture (AWS)
🎯 Objective

Design a scalable cloud architecture for training and serving the model.

🏗️ Architecture Components
Amazon S3 → Data storage
AWS SageMaker → Model training & hosting
API Gateway + Lambda / EC2 → Inference API
CloudWatch → Monitoring and logging
🔄 System Flow
Raw data stored in S3
PySpark pipeline processes data
Model trained using SageMaker
Model deployed as an endpoint
API layer serves predictions
📈 Scalability & Reliability
Auto-scaling endpoints for inference
Load balancing via API Gateway
Fault tolerance using managed AWS services
🔍 Monitoring & Drift Detection
Track:
Prediction distributions
Input data changes
Trigger alerts when drift detected
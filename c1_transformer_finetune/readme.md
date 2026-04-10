🔹 Task 1: Transformer Optimization & Inference Service
🎯 Objective

Build and deploy a transformer-based NLP model with an emphasis on efficient inference.

⚙️ Implementation
Fine-tuned a pretrained transformer model using Hugging Face
Built an inference API using FastAPI
Structured separation between:
Training pipeline
Model loading
Inference service

## Steps

1. Install dependencies
pip install -r requirements.txt

2. Add your dataset to data/dataset.csv

3. Run training
cd src
python train.py

4. Model will be saved in /model

📡 API Endpoints
Endpoint	Method	Description
/predict	POST	Accepts text input and returns model prediction
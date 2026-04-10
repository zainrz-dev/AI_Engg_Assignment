from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from schema import TextRequest

app = FastAPI()

# Load model + tokenizer
MODEL_PATH = "../model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Model API is running 🚀"}

# Prediction endpoint
@app.post("/predict")
def predict(request: TextRequest):
    inputs = tokenizer(
        request.text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()

    sentiment = "positive" if prediction == 1 else "negative"

    return {
        "text": request.text,
        "prediction": prediction,
        "sentiment": sentiment
    }
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from datasets import load_dataset

MODEL_NAME = "distilbert-base-uncased"

# 1. Load IMDB dataset
dataset = load_dataset("imdb")

# 2. Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# 3. Tokenization function
def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )

# 4. Apply tokenization
dataset = dataset.map(tokenize, batched=True)

# 5. Load model
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

# 6. Training arguments
training_args = TrainingArguments(
    output_dir="../model",
    learning_rate=2e-5,
    per_device_train_batch_size=8,   # smaller for safety
    num_train_epochs=1,              # keep 1 for faster run
    logging_dir="../logs"
)

# 7. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"].shuffle(seed=42).select(range(2000)),  # small subset
    eval_dataset=dataset["test"].select(range(500))
)

# 8. Train
trainer.train()

# 9. Save model
trainer.save_model("../model")
tokenizer.save_pretrained("../model")
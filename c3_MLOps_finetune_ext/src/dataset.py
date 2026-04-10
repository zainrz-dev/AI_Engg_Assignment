import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import AutoTokenizer
from config import MODEL_NAME, MAX_LENGTH

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def load_data(path):
    df = pd.read_csv(path)
    train_df, val_df = train_test_split(df, test_size=0.1)
    
    return Dataset.from_pandas(train_df), Dataset.from_pandas(val_df)

def tokenize_function(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH
    )
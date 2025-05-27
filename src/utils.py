import os

def ensure_dirs():
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("models", exist_ok=True)
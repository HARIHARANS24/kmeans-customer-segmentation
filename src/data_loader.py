import pandas as pd
from src.config import RAW_DATA_PATH

def load_data(path=RAW_DATA_PATH):
    return pd.read_csv(path)
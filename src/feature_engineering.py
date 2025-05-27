from sklearn.preprocessing import StandardScaler
import joblib
from src.config import SCALER_PATH

def select_features(df):
    return df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

def scale_features(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, SCALER_PATH)
    return X_scaled

def load_scaler():
    return joblib.load(SCALER_PATH)
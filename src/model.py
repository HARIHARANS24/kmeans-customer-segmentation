from sklearn.cluster import KMeans
import joblib
from src.config import MODEL_PATH, N_CLUSTERS

def train_kmeans(X):
    model = KMeans(n_clusters=N_CLUSTERS, random_state=42)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    return joblib.load(MODEL_PATH)
from src.model import train_kmeans
import numpy as np

def test_kmeans():
    X = np.array([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
    model = train_kmeans(X)
    assert hasattr(model, "predict")
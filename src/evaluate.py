from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def evaluate_model(X, model):
    score = silhouette_score(X, model.labels_)
    print(f"Silhouette Score: {score:.2f}")

def visualize_clusters(X, model):
    plt.scatter(X[:, 0], X[:, 1], c=model.labels_, cmap='viridis')
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=300, c='red')
    plt.title('Customer Segments')
    plt.show()
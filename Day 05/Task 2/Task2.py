import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(42)
X = np.vstack([
    np.random.normal(loc=[2, 2], scale=0.5, size=(50, 2)),
    np.random.normal(loc=[8, 3], scale=0.5, size=(50, 2)),
    np.random.normal(loc=[5, 8], scale=0.5, size=(50, 2))
])

initializations = [0, 10, 42]
plt.figure(figsize=(18, 6))

for i, seed in enumerate(initializations, 1):
    kmeans = KMeans(n_clusters=3, random_state=seed, init='k-means++')
    kmeans.fit(X)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    plt.subplot(1, 3, i)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.title(f'K-means Clustering (Seed={seed})')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

print("Different random initializations can lead to different clustering results.")

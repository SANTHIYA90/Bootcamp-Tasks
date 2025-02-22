import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(42)
X= np.vstack([
 np.random.normal(loc=[2, 2],scale=0.5,size=(50, 2)),
 np.random.normal(loc=[8, 3],scale=0.5,size=(50, 2)),
 np.random.normal(loc=[5, 8],scale=0.5,size=(50, 2))])
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(X)
labels=kmeans.labels_
centroids=kmeans.cluster_centers_

plt.figure(figsize=(10,7))
plt.scatter(X[:, 0],X[:, 1],c=labels,cmap='viridis',s=50)
plt.scatter(centroids[:, 0],centroids[:, 1],c='red',marker=X,s=200,label='centroids')
plt.title('k means clustering')
plt.legend()
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.grid(True)
plt.show()
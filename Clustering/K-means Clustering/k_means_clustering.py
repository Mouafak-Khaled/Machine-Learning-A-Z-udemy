# -*- coding: utf-8 -*-
"""K-means-Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N33H7esi8p_C4JpsIRYFGvJc9yYxtLuh

##Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""##Importing The Dataset"""

dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, 3:].values

print(X)

"""##Using The Elbow Method to Find The Optimal Number of Clusters"""

from sklearn.cluster import KMeans
WCSS = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, init ="k-means++", random_state = 42)
  kmeans.fit(X)
  WCSS.append(kmeans.inertia_)

"""##Visualizing The WCSS Vs N_Clusters



"""

plt.plot(range(1,11), WCSS)
plt.title("The Elbow Method")
plt.xlabel("Numbers of Clusters")
plt.ylabel("WCSS")
plt.show()

"""##Training The K-means Model on The Dataset"""

# From the elbow method, we conclude that the optimal number of cluster is 5.
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
y_pred = kmeans.fit_predict(X)

print(y_pred)

"""##Visualizing The Clusters"""

plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1], color='red', label = 'Cluster 1')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], color='yellow', label = 'Cluster 2')
plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], color='green', label = 'Cluster 3')
plt.scatter(X[y_pred == 3, 0], X[y_pred == 3, 1], color='cyan', label = 'Cluster 4')
plt.scatter(X[y_pred == 4, 0], X[y_pred == 4, 1], color='magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker=",", s=100, color='blue', label = "Centroids")
plt.title("Clusters of Customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
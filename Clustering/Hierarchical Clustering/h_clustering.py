# -*- coding: utf-8 -*-
"""H-Clustering.ipynb

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

"""##Using The Dendrogram to Find the Optimal Number of Clusters"""

import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distances")
plt.show()

"""##Training The Hierarchial Clustering Model on The Dataset"""

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_pred = hc.fit_predict(X)

print(y_pred)

"""##Visualizing The Clusters"""

plt.scatter(X[y_pred == 0, 0], X[y_pred == 0, 1], color='red', label = 'Cluster 1')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], color='blue', label = 'Cluster 2')
plt.scatter(X[y_pred == 2, 0], X[y_pred == 2, 1], color='green', label = 'Cluster 3')
plt.scatter(X[y_pred == 3, 0], X[y_pred == 3, 1], color='cyan', label = 'Cluster 4')
plt.scatter(X[y_pred == 4, 0], X[y_pred == 4, 1], color='magenta', label = 'Cluster 5')
plt.title("Clusters of Customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
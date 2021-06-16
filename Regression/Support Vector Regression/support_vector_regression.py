# -*- coding: utf-8 -*-
"""Support-Vector-Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ekCUVAgIbFWqzgO49dFbo8ZDDzdwRiO

##Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""##Importing Dataset"""

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
y = y.reshape(len(y), 1)

print(X)

print(y)

"""##Feature Scaling"""

from sklearn.preprocessing import StandardScaler
x_sc = StandardScaler()
y_sc = StandardScaler()
X = x_sc.fit_transform(X)
y = y_sc.fit_transform(y)

print(X)

print(y)

"""##Training The SVR model on The Whole Dataset"""

from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf') # using Radial Base Function as a kernel
svr_regressor.fit(X, y)

"""##Predict a New Point"""

y_pred = y_sc.inverse_transform(svr_regressor.predict(x_sc.transform([[6.5]])))
print("The predicted salary for a scaled level of 6.5 is ", y_pred[0])

"""##Visualizing The SVR Results"""

plt.scatter(x_sc.inverse_transform(X), y_sc.inverse_transform(y), color="red")
plt.plot(x_sc.inverse_transform(X), y_sc.inverse_transform(svr_regressor.predict(X)))
plt.title("Truth or Bluff (Support Vector Regression")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

"""##Visualizing The SVR Results for Higher Resolution and Smoother Curve"""

X_grid = np.arange(min(x_sc.inverse_transform(X)), max(x_sc.inverse_transform(X)), 0.1)
X_grid = np.reshape(X_grid, (len(X_grid), 1))
plt.scatter(x_sc.inverse_transform(X), y_sc.inverse_transform(y), color="red")
plt.plot(X_grid, y_sc.inverse_transform(svr_regressor.predict(x_sc.transform(X_grid))))
plt.title("Truth or Bluff (Support Vector Regression")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
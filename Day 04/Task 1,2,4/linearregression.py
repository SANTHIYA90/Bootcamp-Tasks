import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

california = fetch_california_housing()
x = california.data
y = california.target
columns = california.feature_names

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_pred,y_test)
rmse  = np.sqrt(mse)
r2 = r2_score(y_pred,y_test)

print(f"mean squared error: {mse}")
print(f"root mean squared error:{rmse}")
print(f"r2 score:{r2}")

plt.scatter(y_pred,y_test)
plt.xlabel("y_pred")
plt.ylabel("y_test")
plt.title("y_pred vs y_test")
plt.show()
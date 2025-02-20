import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1000,2000,3000,4000,5000,])

poly = PolynomialFeatures(degree=4)
X_poly=poly.fit_transform(X)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)

poly_reg=LinearRegression()
poly_reg.fit(X_poly,y)

plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.scatter(X,y,color='blue')
plt.plot(X,lin_reg.predict(X),color='red')
plt.title(LinearRegression)
plt.xlabel('position level')
plt.ylabel('salary')

plt.subplot(1,2,2)
plt.scatter(X,y,color='green')
plt.plot(X,poly_reg.predict(poly.fit_transform(X)),color='blue')
plt.title("PolynomialFeatures")
plt.xlabel('position level')
plt.ylabel('salary')

plt.tight_layout()
plt.show()


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error,r2_score

data = fetch_california_housing()

df= pd.DataFrame(data=data.data,columns=data.feature_names)
df['target']=data.target
x=df.drop('target',axis=1)
y=df['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

mse = mean_squared_error(y_pred,y_test)
r2 = r2_score(y_test,y_pred)
print(f"mean squared error:{mse}")
print(f"r2 score{r2}")

print("model coefficients")
for feature,coef in zip(data.feature_names,model.coef_):
     print(f"{feature},{coef}")

            

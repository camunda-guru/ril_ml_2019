# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('F:/citi_ml_jun2018/day3/LinearRegression/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/6, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = np.array(y_train).reshape(-1,1)
y_train = sc_y.fit_transform(y_train)
y_test = np.array(y_test).reshape(-1,1)
y_test = sc_y.transform(y_test)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#print interceptor
print("Interceptor=",regressor.intercept_)
#slope
print("Slope=", regressor.coef_)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
#Mean Sqaured Error
MSE=np.mean((y_test-y_pred)**2)
print("Mean Sqaured Error %r" %(MSE))
#Sum of Sqaured Error
SSE=np.sum((y_test-y_pred)**2)
print("SUM of Sqaured Error %r" %(SSE))

#Evaluating algorithm
from sklearn import metrics

print(" Mean Absolute Error", metrics.mean_absolute_error(y_test,y_pred))
print(" Mean Squared Error", metrics.mean_squared_error(y_test,y_pred))
print(" Root Mean Squared Error", np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
'''
import statsmodels.api as sm

est = sm.OLS(y_train, X_train) #ordinary least square method 
est2 = est.fit()
print("Summary.....")
print(est2.summary())
'''

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, regressor.predict(X_test), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

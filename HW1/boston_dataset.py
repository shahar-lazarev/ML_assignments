# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the Boston dataset (must use this method since other method is depracated)
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
boston_X = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
boston_y = raw_df.values[1::2, 2]

# Use only one feature
boston_X = boston_X[:, np.newaxis, 2]

# Split the data into training/testing sets
boston_X_train = boston_X[:-20]
boston_X_test = boston_X[-20:]

# Split the targets into training/testing sets
boston_y_train = boston_y[:-20]
boston_y_test = boston_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(boston_X_train, boston_y_train)

# Make predictions using the testing set
boston_y_pred = regr.predict(boston_X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(boston_y_test, boston_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(boston_y_test, boston_y_pred))

# Plot outputs
plt.scatter(boston_X_test, boston_y_test, color="black")
plt.plot(boston_X_test, boston_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression()
model.fit(x, y)
print("Model trained successfully!")

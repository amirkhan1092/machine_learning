import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
# model = LinearRegression()
# odel.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)
# intercept: 5.633333333333329
print('slope:', model.coef_)
# slope: [0.54]

# simple as simple
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)
# 1.0
print(reg.coef_)
# array([1., 2.])
print(reg.intercept_) # doctest: +ELLIPSIS
# 3.0000../.
print(reg.predict(np.array([[3, 5]])))
# array([16.])

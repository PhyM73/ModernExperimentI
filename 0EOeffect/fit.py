import numpy as np

# Seed the random number generator for reproducibility
np.random.seed(0)

x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)

# And plot it
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)

from scipy import optimize


def test_func(x, a, b):
    return a * np.sin(b * x)


params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])

print(params)
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Generate 100 random values between 0 and 2
y = 5 * X**2 + np.random.randn(100, 1)  # Quadratic relationship with some noise

# Fit polynomial regression model
X_poly = np.c_[X, X**2]  # Add polynomial features (X and X^2)
X_poly = sm.add_constant(X_poly)  # Add constant term for the intercept
model = sm.OLS(y, X_poly).fit()

# View model summary
print(model.summary())

# Predictions
y_pred = model.predict(X_poly)

# Plot actual vs. predicted values
plt.scatter(X, y, label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.title('Actual vs. Predicted Values (Polynomial Regression)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

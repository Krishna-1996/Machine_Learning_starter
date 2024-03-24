# 1. Install Required Libraries:
# pip install statsmodels pandas.

# 2. Import Libraries:
import pandas as pd
import statsmodels.api as sm
import matplotlib as plt

# 3. Load Data:
data = pd.read_csv('data.csv')

# 4. Prepare Data:
# Assume 'X' contains independent variables and 'y' contains the dependent variable
X = data[['independent_var1', 'independent_var2', ...]]
y = data['dependent_var']

# 5. Fit Linear Model:
# Add constant term to the independent variables (for intercept)
X = sm.add_constant(X)

# Fit the linear model
model = sm.OLS(y, X).fit()

# 6. View Model Summary:
print(model.summary())

# 7. Predictions:
# Assume 'new_data' contains new observations
X_new = sm.add_constant(new_data[['independent_var1', 'independent_var2', ...]])
predictions = model.predict(X_new)

# 8. Visualization
# Plot actual vs. predicted values
plt.scatter(y, predictions)
plt.plot(y, y, color='red')  # Identity line (y = x)
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.show()








































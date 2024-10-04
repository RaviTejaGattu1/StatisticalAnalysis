import numpy as np
from scipy.stats import chi2_contingency

# Example data: Contingency table for Day of the Week and Flight Delay Status
# Rows: Days (Monday, Tuesday, Wednesday)
# Columns: On Time, Delayed
observed = np.array([[50, 20],
                     [45, 25],
                     [55, 15]])

# Perform Chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(observed)

# Print the results
print(f"Chi-square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies: \n{expected}")

# Conclusion based on p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (There is an association between the variables).")
else:
    print("Fail to reject the null hypothesis (No significant association between the variables).")

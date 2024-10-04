import numpy as np
from scipy import stats

# Sample data for two independent groups (Group A and Group B)
group_A = [3.4, 2.9, 4.1, 3.5, 3.2]
group_B = [4.0, 4.5, 3.9, 4.2, 4.3]

# Perform independent t-test
t_statistic, p_value = stats.ttest_ind(group_A, group_B)

# Print the results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

# Conclusion: Compare p-value to alpha (0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (significant difference between groups).")
else:
    print("Fail to reject the null hypothesis (no significant difference between groups).")

import numpy as np
from scipy import stats

# Sample data for three groups
group1 = [23, 20, 22, 21, 19]
group2 = [31, 29, 35, 32, 30]
group3 = [35, 37, 36, 33, 34]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

# Interpret p-value
if p_value < 0.05:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. No significant difference between the groups.")

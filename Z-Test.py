import numpy as np
from statsmodels.stats.weightstats import ztest

# Sample data
sample_data = [102, 110, 105, 98, 100, 108, 112, 104, 106]
population_mean = 100

# Perform Z-test (One-sample Z-test)
z_stat, p_value = ztest(sample_data, value=population_mean)

print(f"Z-Statistic: {z_stat}")
print(f"P-Value: {p_value}")

# Interpret p-value
if p_value < 0.05:
    print("Reject the null hypothesis. The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis. The sample mean is not significantly different from the population mean.")

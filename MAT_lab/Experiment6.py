# Probability Density Function

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
# probability function
np.set_printoptions(precision = 4)
t_dist = stats.t(20)
t_values = np.linspace(-4, 4, 1000)
# Pdf
plt.plot(t_values, t_dist.pdf(t_values))
plt.xlabel("t_values")
plt.ylabel("probability for t_values")
plt.title("PDF for t distribution with df = 20")
plt.show()
# cdf
plt.plot(t_values, t_dist.cdf(t_values))
plt.xlabel("t_values")
plt.ylabel("probability for t_values<=t")
plt.title("  CDF for t distribution with df = 20")
plt.show()

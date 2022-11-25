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


# ------------------------------Moment Generating Functions ------------------------------

from scipy import stats
data = [[3, 4, 6, 7, 9],
       [21, 34, 43, 2, 67],
       [4, 7, 5, 27, 1]]
print("")
print("Moment Generating Function")
print("0th Moment=", stats.moment(data, moment=0,axis=1))
print("1st  Moment=", stats.moment(data, moment=1,axis=1))
print("2nd  Moment=", stats.moment(data, moment=2,axis=1))
print("3rd  Moment=", stats.moment(data, moment=3,axis=1))
print("4th  Moment=", stats.moment(data, moment=4,axis=1))
print("5th  Moment=", stats.moment(data, moment=5,axis=1))


# 7 oct


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,30,10)
y = x**2
z = x**2
plt.plot(x,z,color='red')
plt.plot(x,y,'*')
plt.xlabel('x-value')
plt.ylabel('y-value')
plt.title('Line-Plot')
plt.grid(True)
plt.show()
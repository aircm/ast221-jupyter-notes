import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 1, 1000)
y = 1.8*(x-x**3)

plt.plot(x, y, color="red")
plt.plot(x, x)
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.axhline(y=0.675,  xmax=0.5, linestyle="--")
plt.axvline(x=0.5, ymax=0.675, linestyle="--")


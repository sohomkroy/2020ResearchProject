import matplotlib.pyplot as plt

with open('final_wing.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

import numpy as np
for i in range(0, len(x)):
    x[i] = float(x[i])

for i in range(0, len(y)):
    y[i] = float(y[i])


plt.xlim(-.2, 1.2)
plt.ylim(-1, 1)

plt.plot(x, y)
plt.show()
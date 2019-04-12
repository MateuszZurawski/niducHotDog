import numpy as np
import matplotlib.pyplot as plt


filename = "results/AVERAGE_REPAIR_TIME.csv"

file_handle = open(filename)

x = []
y = []


counter = 0
for line in file_handle:
    counter+=1
    x.append(counter)
    y.append(float(line.replace('\n', '')))


x = np.array(x)
y = np.array(y)

z = np.polyfit(x, y, 3)
p = np.poly1d(z)
p30 = np.poly1d(np.polyfit(x, y, 30))

xp = np.linspace(-100, 100, 100)
_ = plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
plt.ylim(-2,2)

plt.show()
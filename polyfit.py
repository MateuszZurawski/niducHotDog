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


polynomial = np.poly1d(np.polyfit(x, y, 5))

xp = np.linspace(-1, 10, 1000)
_ = plt.plot(x, y, '.',xp, polynomial(xp), '--')
plt.ylim(90,110)

plt.show()
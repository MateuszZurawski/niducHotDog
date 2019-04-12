import numpy as np
import matplotlib.pyplot as plt


#filename = "results/PROBABILITY_OF_FAILURE.csv"
filename = "results/REPAIR_TIME_VARIANCE.csv"

file_handle = open(filename)

'''
x = []
y = []


counter = 0
for line in file_handle:
    counter+=1
    x.append(counter)
    y.append(float(line.replace('\n', '')))


x = np.array(x)
y = np.array(y)
'''
data = np.loadtxt(open(filename, "rb"), delimiter=",")
x = data[:,0]
y = data[:,1]

#exit()
print(x)

polynomial = np.poly1d(np.polyfit(x, y, 5))

xp = np.linspace(min(x), max(x), 100)
_ = plt.plot(x, y, '.',xp, polynomial(xp), '--')
plt.ylim(min(y)-1, max(y)+1)

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='wykresy lel')

parser.add_argument('--file', type=str, required=True)


filename = parser.parse_args().file
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
q1 = data[:, 2]
q3 = data[:, 3]

yerr = [
    [abs(x_val - q1_val) for x_val, q1_val in zip(y, q1)],
    [abs(x_val - q3_val) for x_val, q3_val in zip(y, q3)]
]

print(yerr)

#exit()

polynomial = np.poly1d(np.polyfit(x, y, 5))

xp = np.linspace(min(x), max(x), 100)

_ = plt.errorbar(x, y, yerr=yerr, ecolor='r', color='#00000000')

_ = plt.plot(x, y, '.', xp, polynomial(xp), '--')
plt.ylim(min(y)-1 - yerr[0][0], max(y)+1 + yerr[-1][0])

plt.xlabel('Wartości badanej zmiennej')
plt.ylabel('Niezawodność [%]')

plt.show()
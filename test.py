import matplotlib.pyplot as plt


data = [True,True,True,True,True,True,True,True,True,True]

plt.fill_between([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], y1=2, y2=3, where=data)


plt.show()
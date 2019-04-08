import parameters
import random
from numpy.random import normal, weibull

import numpy as np

import math
import matplotlib.pyplot as plt

from elevator import Elevator

def plot_elevators(elevators):

    y = 0
    plt.figure(num=None, figsize=[15, 5])

    for e in elevators:
        y+=1
        for data in e.journal:
            plt.fill_between(data, y1=y-0.2, y2=y+0.2, color=parameters.COLORS[y])

    plt.axes().get_yaxis().set_visible(False)
    plt.show()


elevators = [Elevator() for i in range(parameters.HOW_MANY_ELEVATORS)]

global_downtime = 0

for i in range (parameters.LIFETIME_OF_ELEVATOR):
    
    not_working = 0
    for e in elevators:
        e.simulate_1_day()
        if not e.is_working:
            not_working +=1

    if not_working == len(elevators):
        global_downtime+=1

    #if sum([int(elevator.is_working) for elevator in elevators] ) == len(elevators):
    #    global_downtime += 1


for e in elevators:
    e.finalize_simulation()


print(f'{global_downtime} downtime')
plot_elevators(elevators)


import parameters
import random
from numpy.random import normal, weibull

import numpy as np

import math
import matplotlib.pyplot as plt

from elevator import Elevator
import parameters

import plots

elevators = [Elevator() for i in range(parameters.HOW_MANY_ELEVATORS)]

global_downtime = []

for i in range (parameters.LIFETIME_OF_ELEVATOR):
    
    not_working = 0
    for e in elevators:
        e.simulate_1_day()
        if not e.is_working:
            not_working +=1

    if not_working != len(elevators):
        global_downtime.append(1)
    else:
        global_downtime.append(0)


for e in elevators:
    e.finalize_simulation()


print(f'{global_downtime} downtime')
plots.plot_elevators(elevators, global_downtime)


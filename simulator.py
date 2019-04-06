import parameters
import random

from numpy.random import normal, weibull
import numpy as np

import math
import matplotlib.pyplot as plt

class Malfunction:
    def __init__(self):
        self.repair_time =  math.ceil( abs( normal(
            parameters.AVERAGE_REPAIR_TIME,
            parameters.REPAIR_TIME_VARIANCE
        ) ) )


        self.is_fixed = False

    def one_day_repair(self):
        self.repair_time -= 1
        if self.repair_time <= 0:
            self.is_fixed = True
    

class Elevator:
    def __init__(self):
        self.uptime_without_failure_days = 0
        self.downtime = 0
        self.malfunction = None
        self.failures = 0


    def random_failure(self): # TODO: maths, not random guesses
        if weibull(self.uptime_without_failure_days / 50 + 1) < 0.01:
            self.failures += 1
            self.malfunction = Malfunction()

    @property
    def is_working(self):
        return self.malfunction is None

    def simulate_1_day(self):
        if self.is_working == False:
            self.downtime += 1
            self.malfunction.one_day_repair()
            if self.malfunction.is_fixed:
                self.malfunction = None
        else:
            self.random_failure()

elevators = [Elevator(), Elevator()]

global_downtime = 0

for i in range (parameters.LIFETIME_OF_ELEVATOR*3):
    
    not_working = 0
    for e in elevators:
        e.simulate_1_day()
        if not e.is_working:
            not_working +=1

    if not_working == len(elevators):
        global_downtime+=1

    #if sum([int(elevator.is_working) for elevator in elevators] ) == len(elevators):
    #    global_downtime += 1


print(f'{global_downtime} downtime')



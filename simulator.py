import parameters
import random
from numpy.random import normal, weibull

import numpy as np

import math
import matplotlib.pyplot as plt

from elevator import Elevator
import parameters

import plots

class Simulator:    
    
    def run(self):
        elevators = [Elevator() for i in range(int(parameters.HOW_MANY_ELEVATORS))]

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


        uptime = sum(global_downtime)/parameters.LIFETIME_OF_ELEVATOR*100

        return uptime

    def average_uptime(self, number_of_runs):
        uptimes = self.uptimes_for_histogram(number_of_runs)

        return sum(uptimes)/len(uptimes)

    def uptimes_for_histogram(self, number_of_runs):
        uptimes = [self.run() for _ in range(number_of_runs)]

        return uptimes
    #plots.plot_elevators(elevators, global_downtime)


if __name__ == '__main__':
    s = Simulator()
    uptime =  s.run()
    print(f'Uptime: {uptime}')
    

import parameters
import random
from numpy.random import normal, weibull

import numpy as np
from numpy import percentile


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

        #plots.plot_elevators(elevators, global_downtime)


        return uptime

    def average_uptime_stats(self, number_of_runs):
        uptimes = self.uptimes_for_histogram(number_of_runs)
        minimum, q1, median, q3, maximum = get_5_point_summary(uptimes)

        return sum(uptimes)/len(uptimes), q1, q3

    def uptimes_for_histogram(self, number_of_runs):
        uptimes = [self.run() for _ in range(number_of_runs)]
        return uptimes


def get_5_point_summary(data):
    data = np.array(data)

    # calculate quartiles
    quartiles = percentile(data, [25, 50, 75]) # to so centyle
    # calculate min/max
    data_min, data_max = data.min(), data.max()
    # print 5-number summary
    
    return data_min, quartiles[0], quartiles[1], quartiles[2], data_max


if __name__ == '__main__':
    s = Simulator()
    uptime =  s.run()
    print(f'Uptime: {uptime}')
    

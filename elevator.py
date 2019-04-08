from numpy.random import normal, weibull
from malfunction import Malfunction
import math
import parameters

class Elevator:
    def __init__(self):
        self.uptime_without_failure_days = 0
        self.downtime = 0
        self.malfunction = None
        self.failures = 0

        self.current_day = 0
        self.journal = [ [0] ]# [[0, 19], [21, 100], [103, 205]]


    def random_failure(self): # TODO: maths, not random guesses
        if weibull(self.uptime_without_failure_days / 50 + 1) < parameters.PROBABILITY_OF_FAILURE:
            self.failures += 1
            self.malfunction = Malfunction()
            self.journal[-1].append(self.current_day)

    @property
    def is_working(self):
        return self.malfunction is None

    def simulate_1_day(self):
        self.current_day+=1

        if self.is_working == False:
            self.downtime += 1
            self.malfunction.one_day_repair()
            if self.malfunction.is_fixed:
                self.malfunction = None
                self.journal.append([self.current_day])
        else:
            self.random_failure()

    def finalize_simulation(self):
        if len(self.journal[-1]) == 1:
            self.journal[-1].append(self.current_day)


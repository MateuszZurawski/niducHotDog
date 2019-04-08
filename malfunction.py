import parameters
import math
from numpy.random import normal, weibull

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
      

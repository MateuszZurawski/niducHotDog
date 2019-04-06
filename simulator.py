import parameters
import random

from numpy.random import normal, weibull
import numpy as np

import math
import matplotlib.pyplot as plt



averages = []

for i in range(100, 200):
    samples = [weibull(i/100) for j in range(1000)]
    averages.append( sum(samples) / len(samples) )

plt.plot( averages )
plt.show()

class Malfunction:
    def __init__(self):
        self.repair_time =  math.ceil( math.abs( normal(
            parameters.AVERAGE_REPAIR_TIME,
            parameters.REPAIR_TIME_VARIANCE
        ) ) )

        self.is_fixed = False

    def one_day_repair(self):
        self.repair_time -= 1
        if self.repair_time == 0:
            self.is_fixed = True
    

class Elevator:
    def __init__(self):
        self.uptime_without_failure_days = 0
        self.malfunction = None

    def random_failure(self):
        pass


exit(0)



#elevators= [0]*parameters.HOW_MANY_ELEVATORS []

#more elevators down lel 

for i in range (parameters.LIFETIME_OF_ELEVATOR):
    for j in range (parameters.HOW_MANY_ELEVATORS):
        radom=random.uniform(0,1)
        if radom<=parameters.PROBABILITY_OF_FAILURE:
            down+=1
    elevators[down]+=1

    down=0


print(elevators)



# print(parameters.ANNUAL_CHECK_COST)
# class Doggo:
#     def __init__(self):
#         self.name = 'Azor'
#         self.ilosc_zagryzionych_niemowlat = 5

#     def bark(self):
#         print('hau hau')

#     def zagryz_niemowle(self, imie_niemowlecia):
#         self.ilosc_zagryzionych_niemowlat += 1
#         print('Zagryzlem ' + imie_niemowlecia)


#     def zagryz_niemowleta(self, lista_niemowlat):
#         for niemowle in lista_niemowlat:
#             self.zagryz_niemowle(niemowle)

        
#         # SAME SHIT
#         #for i in range(len(lista_niemowlat)):
#         #    self.zagryz_niemowle(lista_niemowlat[i])

# azor = Doggo()
# azor.bark()

# niemowleta_do_zagryzienia = ['Mateusz', 'Biernat', 'Bobowska <3']
# azor.zagryz_niemowleta(niemowleta_do_zagryzienia)
# azor.zagryz_niemowle('Jonasz')
# azor.bark()

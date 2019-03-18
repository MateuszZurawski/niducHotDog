import parameters
import random


oneElevatorDown=0
twoElevatorsDown=0
randomVariable = 0
#more elevators down lel 

for i in range (parameters.LIFETIME_OF_ELEVATOR):
    for j in range (parameters.HOW_MANY_ELEVATORS):
        radom=random.uniform(0,1)
        if radom<=parameters.PROBABILITY_OF_FAILURE:
            randomVariable+=1
    if randomVariable==1:
            oneElevatorDown+=1
    if randomVariable==2:
            twoElevatorsDown+=1     
    randomVariable=0


print(oneElevatorDown,'          ',twoElevatorsDown)




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

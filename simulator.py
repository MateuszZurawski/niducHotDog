import parameters
print(parameters.)
class Doggo:
    def __init__(self):
        self.name = 'Azor'
        self.ilosc_zagryzionych_niemowlat = 5

    def bark(self):
        print('hau hau')

    def zagryz_niemowle(self, imie_niemowlecia):
        self.ilosc_zagryzionych_niemowlat += 1
        print('Zagryzlem ' + imie_niemowlecia)


    def zagryz_niemowleta(self, lista_niemowlat):
        for niemowle in lista_niemowlat:
            self.zagryz_niemowle(niemowle)

        
        # SAME SHIT
        #for i in range(len(lista_niemowlat)):
        #    self.zagryz_niemowle(lista_niemowlat[i])

azor = Doggo()
azor.bark()

niemowleta_do_zagryzienia = ['Mateusz', 'Biernat', 'Bobowska <3']
azor.zagryz_niemowleta(niemowleta_do_zagryzienia)
azor.zagryz_niemowle('Jonasz')
azor.bark()

import obiekty as obiekt
import miod, parsuj

import random
from threading import Thread, Lock

class poprzedni_ruch():
    def __init__(self):
        self.x = 11
        self.y = 11
        self.czytrafiono = False


class wrog:
    def __init__(self):
        self.poleGry = obiekt.Tablica()
        self.wstawStatki()
        self.poprzednie = []
        #self.poleGry.drukujTablice()
        pass

    def wstawStatki(self):
        listadlug = [4, 4, 3, 2, 2, 1]

        for dlugosc in listadlug:
            statekX = random.randint(0, 10)
            statekY = random.randint(0, 10)

            while statekX + dlugosc > 10:
                statekX = random.randint(0, 10)

            while statekY + dlugosc > 10:
                statekY = random.randint(0, 10) #zmieniamy, jesli wypada

            self.poleGry.tablicaStatkow.append(obiekt.Statek(dlugosc, int(statekX), int(statekY),
                                                                         self.poleGry.tablicaStatkow.__len__()))
            self.poleGry.piszTablice()


        for i in range(len(listadlug)):
            if random.randint(0, 10)>7:
                self.poleGry.tablicaStatkow[i].obrot("-", "w")
                self.poleGry.odswiezTablice()

    def strzel(self):
        if poprzedni_ruch.czytrafiono:
            if random.randint(0, 2) > 2:
                x = poprzedni_ruch.x + 1
                y = poprzedni_ruch.y
            else:
                y = poprzedni_ruch.y + 1
                x = poprzedni_ruch.x        #albo jakos inaczej zmodyfikuj
        else:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
        return [x, y]

    def dostan(self, x, y):

        for statek in self.poleGry.tablicaStatkow:
            i = 0
            for czlon in statek.pozycjaCzlonu:
                if czlon[0] == y and czlon[1] == x:
                    statek.stan[i] = 2
                i = i + 1

        self.poleGry.drukujTablice()






wrog()
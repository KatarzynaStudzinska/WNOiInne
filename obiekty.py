import numpy as np

class Statek():

            def __init__(self, jakaDlug, dajX, dajY, n):
                self.czyRuszamy = False
                self.dlugosc = jakaDlug
                self.x = dajX
                self.y = dajY
                # self.imie = dajImie
                self.numer = n
                self.stan = [1]*jakaDlug
                self.pozycjaCzlonu = []

            def getCzyRuszamy(self):
                return self.czyRuszamy

            def setCzyRuszamy(self):
                self.czyRuszamy = False

            def zmienPozycjaCzlonu(self, x, y):
                self.pozycjaCzlonu.append([x, y])

            def czyWyjedziemy(self, ruch, orientacja):      # W sumie to dla jednego i drugiego to samo
                if ruch == "o":
                    if self.pozycjaCzlonu[self.dlugosc-1][1] + self.dlugosc-1 < 11:
                        return False
                    return True

            def obrot(self, znak, orientacja):
                if self.dlugosc != 1:                        #  Nalezy  uzwglednic przypadek dla statku pojedynczego - dla niego nie ma obrotu
                   # if self.czyWyjedziemy("o", znak):
                    #    print "Statek opuscilby mape. Nie wykonujesz ruchu."
                    #else:
                        if ((znak == "+" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0] == -1)) or
                             (znak == "-" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == 1)):
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0], self.pozycjaCzlonu[0][1]-i]

                        elif ((znak == "+" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == 1) or
                              (znak == "-" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == -1)):
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0]-i, self.pozycjaCzlonu[0][1]]

                        elif ((znak == "+" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == 1) or
                              (znak == "-" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == -1)):
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0], self.pozycjaCzlonu[0][1]+i]

                        elif ((znak == "+" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == -1) or
                              (znak == "-" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == 1)):
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0]+i, self.pozycjaCzlonu[0][1]]

            def przesun(self, znak, orientacja):

                if znak == "+":
                    trasa = 1
                else:
                    trasa = -1

                if orientacja == "h":
                    for i in range(self.dlugosc):
                        pozx, pozy = self.pozycjaCzlonu[i]
                        if not pozx + trasa < 0 and not pozx + trasa > 9:
                            self.pozycjaCzlonu[i] = [pozx + trasa, pozy]
                        else:
                            print "Wyjezdzasz statkiem poza mape!"
                else:
                    for i in range(self.dlugosc):
                        pozx, pozy = self.pozycjaCzlonu[i]
                        if not pozy + trasa < 0 and not pozy + trasa > 9:
                            self.pozycjaCzlonu[i] = [pozx, pozy + trasa]
                        else:
                            print "Wyjezdzasz statkiem poza mape!"


class Tablica():

        def __init__(self):
            self.dlugoscTablicy = 10
            self.mojaTablica = [[0 for col in range(self.dlugoscTablicy)] for row in range(self.dlugoscTablicy)]
            self.tablicaStatkow = []

        def dajMojaTablica(self):
            return self.mojaTablica

        def drukujTablice(self):
            for i in range(self.mojaTablica.__len__()):
                print self.mojaTablica[i]

        def piszTablice(self):
            for statek in self.tablicaStatkow:
                statek.pozycjaCzlonu = []
                for i in range(statek.dlugosc):
                    self.mojaTablica[statek.x + i][statek.y] = statek.stan[i]
                    statek.zmienPozycjaCzlonu(statek.x + i, statek.y)

        def odswiezTablice(self):
            self.mojaTablica = [[0 for col in range(self.dlugoscTablicy)] for row in range(self.dlugoscTablicy)]
            for statek in self.tablicaStatkow:
                for i in range(statek.dlugosc):
                    statx, staty = statek.pozycjaCzlonu[i]
                    self.mojaTablica[statx][staty] = statek.stan[i]

        def piszStany(self):
            for statek in self.tablicaStatkow:
                print statek.stan

        def czyWrogTrafil(self, xWrog, yWrog):
            for statek in self.tablicaStatkow:          # dla kazdego statku
                for i in range(statek.stan.__len__()):
                    pozycja = statek.pozycjaCzlonu[i]
                    if pozycja[0] == xWrog and pozycja[1] == yWrog:
                        statek.stan[i] = 2
                        return True
            return False


class Dane():
        Wyslane = []
        Przyjete = []

        def get(self):
            return self.Wyslane

        def set(self, data):
            self.Wyslane = data

        def clr(self):
            self.Wyslane = []

        def ustawWyslane(self, dane):
            self.Wyslane = dane

        def printuj(self):
            print "Uwazamy ze stan wyslanych to :", self.Wyslane




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
                    if ((znak == "+" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0] == -1)) or      # Godzina 3 obrot ze wskazowkami
                            (znak == "-" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == 1)):    # Godzina 9 obrot przeciwnie do wskazowek
                        if self.pozycjaCzlonu[0][1] - self.dlugosc + 1 >= 0:
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0], self.pozycjaCzlonu[0][1]-i]
                        else:
                            print 'Nie mozna wykonac obrotu!'

                    elif ((znak == "+" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == 1) or     # Godzina 6, obrot ze wskazowkami zegara
                              (znak == "-" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == -1)): # Godzina 12, obrot przeciwnie do wskazowek
                        if self.pozycjaCzlonu[0][0] - self.dlugosc + 1 >= 0:
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0]-i, self.pozycjaCzlonu[0][1]]
                        else:
                            print 'Nie mozna wykonac obrotu!'

                    elif ((znak == "+" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == 1) or     # Godzina 9, obrot ze wskazowkami
                              (znak == "-" and (self.pozycjaCzlonu[0][0]-self.pozycjaCzlonu[1][0]) == -1)): # Godzina 3, obrot przeciwnie do wskazowek
                        if self.pozycjaCzlonu[0][1] + self.dlugosc - 1 <= 9:
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0], self.pozycjaCzlonu[0][1]+i]
                        else:
                            print 'Nie mozna wykonac obrotu!'

                    elif ((znak == "+" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == -1) or    # Godzina 12, obrot ze wskazowkam zegara
                              (znak == "-" and (self.pozycjaCzlonu[0][1]-self.pozycjaCzlonu[1][1]) == 1)):  # Godzina 6,  obrot przeciwnie do wskazowek
                        if self.pozycjaCzlonu[0][0] + self.dlugosc - 1 <= 9:
                            for i in range(self.dlugosc):
                                self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[0][0]+i, self.pozycjaCzlonu[0][1]]
                        else:
                            print 'Nie mozna wykonac obrotu!'

            def przesun(self, znak, orientacja):

                if znak == "+":
                    trasa = 1
                elif znak == "-":
                    trasa = -1

                pozx, pozy = self.pozycjaCzlonu[0]                                  # Wspolrzedne pierwszego czlonu
                pozx1, pozy1 = self.pozycjaCzlonu[1]                                # Wspolrzedne drugiego czlonu

                if orientacja == "h":                                               # Przesuwajac poziomo  statki
                    if (pozx + trasa >= 0) and (pozx + self.dlugosc + trasa < 11) and (pozx - pozx1) == -1:     # Ustawiony poziomo normalnie
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0] + trasa, self.pozycjaCzlonu[i][1]]
                    elif (self.pozycjaCzlonu[self.dlugosc-1][0] + trasa >= 0) and (self.pozycjaCzlonu[self.dlugosc-1][0] + self.dlugosc + trasa < 11) and (pozx - pozx1) == 1:     # Ustawiony poziomo odwrocony
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0] + trasa, self.pozycjaCzlonu[i][1]]
                    elif (pozx + trasa >= 0) and (pozx + trasa < 10) and np.absolute(pozy - pozy1) == 1:     # Ustawiony pionowo
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0] + trasa, self.pozycjaCzlonu[i][1]]
                    else:
                        print "Wyjezdzasz statkiem poza mape!"
                else:                                                                                     # Przesuwanie statku w pionie, jezeli
                    if(pozy + trasa - self.dlugosc + 1 >= 0) and (pozy + trasa < 10) and (pozy - pozy1) == 1:           # Jezeli statki ustawione sa pionowo - od pol. pocz. zgodnie z ruchem wskazowek zegara
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0], self.pozycjaCzlonu[i][1] + trasa]
                    elif (self.pozycjaCzlonu[self.dlugosc-1][1] + trasa - self.dlugosc + 1 >= 0) and (self.pozycjaCzlonu[self.dlugosc-1][1] + trasa < 10) and (pozy - pozy1) == -1:            # Jezeli statki ustawione sa pionowo - od pol. pocz. przeciwnie do ruchu wskazowek zegara
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0], self.pozycjaCzlonu[i][1] + trasa]
                    elif (pozy + trasa >= 0) and (pozy + trasa < 10) and np.absolute(pozx - pozx1) == 1:  # Jezeli statki ustawione sa poziomo
                        for i in range(self.dlugosc):
                            self.pozycjaCzlonu[i] = [self.pozycjaCzlonu[i][0], self.pozycjaCzlonu[i][1] + trasa]
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




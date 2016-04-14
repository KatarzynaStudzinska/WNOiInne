import obiekty as obiekt
import miod, parsuj
import socket
import sys
import numpy as np
import json
from random import random
from threading import Thread, Lock
from PyQt4 import QtCore, QtGui
from RAZ import Ui_Widget
import os

global PORT, HOST, RECV_BUFFER, killall

CZCIONKA = 23

HOST = '127.0.0.1'              # Adresem labolatoryjnym jest '153.19.54.27'
PORT = 8888                     # Portem labolatoryjnym jest 50002
RECV_BUFFER = 2048
killall = False


class Komiwojazer(QtGui.QWidget):
    _aktualneKliki = []
    _obrot = 0
    _tabkrawedzi = []
    _tabwezlow = []
    _gen = []
    _data = []

    def onclick(self, event):

        x = event.xdata
        y = event.ydata
        srodki = miod.rysujMiod(self.ui.sc.axes)
        self.ui.textEdit.clear()
        for i in range(srodki.__len__()):
            xs, ys = srodki[i]
            if np.absolute(xs - x) < 1:
                if np.absolute(ys - y) < 1:
                    ikomorki = i % 10
                    jkomorki = (i - ikomorki)/10
                    self._aktualneKliki = [ikomorki, jkomorki]
                    self.ui.textEdit.insertPlainText(str(ikomorki) + " " + str(jkomorki))

                    miod.miodStatek(xs, ys, self.ui.sc.axes, 3)
        self.ui.sc.draw()

    def zapisz(self):
        self.poleGry.drukujTablice()

        if not self.ostatniStatek:
            self.ui.textEdit.clear()
            self.ui.textEdit.insertPlainText("Nie mozna zapisac przed polozeniem wszyskich statkow.")

        else:
            sender = self.sender()
            wcisniete = sender.text()
            if wcisniete =="ZAPIS":             # Zapis do pliku wpisanego przez uzytkownika
                nazwa = self.ui.textEdit.toPlainText() + ".txt"
            else:                               # Zapis do pliku do odtwarzania ruchu
                nazwa = "my_json.txt"

            self.ui.textEdit.clear()
            self.ui.textEdit.insertPlainText("Zapisano!")
            tablicaCzlonow = []
            tablicaStanuStatku = []
            tablicaGdzieStatki = []
            tablicaDlugosci = []


            for statek in (self.poleGry.tablicaStatkow):
                tablicaCzlonow.append(statek.pozycjaCzlonu)
                tablicaStanuStatku.append(statek.stan)
                tablicaGdzieStatki.append(statek.pozycjaCzlonu[0])
                tablicaDlugosci.append(statek.dlugosc)

            data = {'plansza': self.poleGry.dajMojaTablica(), 'gdzieStatki':tablicaGdzieStatki, 'zniszczenie':tablicaStanuStatku,
                    'dlugosc':tablicaDlugosci, 'czlony':tablicaCzlonow}

            with open(nazwa, 'a') as fp:
                json.dump(data, fp)
                fp.write('\n')
            pass

    def odczyt(self):   

        self.ostatniStatek = True

        sender = self.sender()
        wcisniete = sender.text()

        if wcisniete =="CO INNEGO":             # Zapis do pliku wpisanego przez uzytkownika
            nazwa = "my_json.txt"
        else:                               # Zapis do pliku do odtwarzania ruchu
            nazwa = self.ui.textEdit.toPlainText() + ".txt"

        with open(nazwa, 'rb') as fh:       # Czytanie ostatniej linijki zapisanego ruchu
            fh.seek(-660, os.SEEK_END)
            last = fh.readlines()[-1].decode()

        with open(nazwa, 'rb+') as ft:
            ft.seek(-660, os.SEEK_END)
            ft.truncate()

        print ("ostatni")
        print (last)
        data = json.loads(last)

        poprzedniaPlansza = data["plansza"]
        poprzedniePozycja = data["gdzieStatki"]
        czlony = data["czlony"]
        dlugosc = data["dlugosc"]
        self.poleGry = obiekt.Tablica()
        for (pozycja, dlug, czlon) in zip(poprzedniePozycja, dlugosc, czlony):
            print pozycja[0], pozycja[1]
            statek = obiekt.Statek(dlug, pozycja[0], pozycja[1], self.poleGry.tablicaStatkow.__len__())
            statek.pozycjaCzlonu = czlon
            self.poleGry.tablicaStatkow.append(statek)
            self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.poleGry.drukujTablice()

    def naKtoryStatekKliknelismy(self):
        for i in range(self.poleGry.tablicaStatkow.__len__()):
            for j in range(self.poleGry.tablicaStatkow[i].pozycjaCzlonu.__len__()):
                xk, yk = self.poleGry.tablicaStatkow[i].pozycjaCzlonu[j]
                print xk, yk
                ikomorki, jkomorki = self._aktualneKliki
                if ikomorki == yk and jkomorki == xk:
                    print self.poleGry.tablicaStatkow[i].dlugosc
                    return self.poleGry.tablicaStatkow[i]
                    break

    def initClient(self):                   # Laczymy sie z serwerem
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        print 'You have connected to server!'
        # sending name

        name = str(random())                # Aby wpisac swoje imie: str(raw_input("Enter your name: "))
        print "Klient " + name
        self.client_socket.send(name)
        response = self.client_socket.recv(RECV_BUFFER)
        # "0" means error
        if response == "0":
            print'User %s already logged in! Connection terminated!' % name
            return
        # "1" means everything's fine
        if response == "1":
            print 'User connected!'
            print 'Welcome ' + name + ' to the game! Please type "q" to quit!'
            self.lock = Lock()
            Thread(target=self.strzel).start()              #, args=(self.client_socket, self.lock)).start()
            Thread(target=self.oberwij).start()             #, args=(client_socket, lock)).start()

    def __init__(self, parent=None):
        self.ostatniStatek = False
        self._aktualneKliki = [0, 0]
        self.dane = obiekt.Dane()
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Statki")
        self.initClient()

        miod.rysujMiod(self.ui.sc.axes)

        def dlugosciStatku():
            listadlug = [4, 4, 3, 2, 2, 1]                  # Dlugosci statkow
            idx = {'i': 0}

            def jakadlugosc():
                if idx.get('i') < listadlug.__len__():
                    dlugosc = listadlug[idx.get('i')]
                    idx['i'] += 1
                else:
                    dlugosc = 0
                return dlugosc
            return jakadlugosc

        self.dlugoscstatku = dlugosciStatku()
        self.poleGry = obiekt.Tablica()

        QtCore.QObject.connect(self.ui.STRZELAJ, QtCore.SIGNAL("clicked()"), self.strzel)
        QtCore.QObject.connect(self.ui.WSTAW, QtCore.SIGNAL("clicked()"), self.wstawStatki)
        #self.ui.PRZESUN.connect("clicked()", self.przesun)
        #self.ui.PRZESUN.clicked.connect(self.przesun)
        self.ui.STRZELAJ.clicked.connect(self.kur)
        self.ui.ZAPIS.clicked.connect(self.zapisz)
        self.ui.INNY.clicked.connect(self.odczyt)
        self.ui.ODCZYTZPLIKU.clicked.connect(self.odczyt)
        self.ui.sc.mpl_connect('button_press_event', self.onclick)

        self.ui.OBROTZEGAR.clicked.connect(self.obrot_zgodny)
        self.ui.OBROTPRZECIWNIE.clicked.connect(self.obrot_przeciwny)
        self.ui.PRAWO.clicked.connect(self.prawo)
        self.ui.LEWO.clicked.connect(self.lewo)
        self.ui.DOL.clicked.connect(self.dol)
        self.ui.GORA.clicked.connect(self.gora)

        self.ui.sc.mpl_connect('button_press_event', self.onclick)


    def przesun(self):

        statek = self.naKtoryStatekKliknelismy()
        znak, orient = self.ui.textEdit.toPlainText()

        if orient == "o":
            print "Obracamy sie"
            statek.obrot(znak, orient)
        else:
            print "Przesuwamy sie"
            statek.przesun(znak, orient)

        self.zapisz()

        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()

    def obrot_zgodny(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.obrot("+", "o")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()
    def obrot_przeciwny(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.obrot("-", "o")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()
    def prawo(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.przesun("+", "h")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()
    def lewo(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.przesun("-", "h")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()
    def gora(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.przesun("+", "g")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()
    def dol(self):
        statek = self.naKtoryStatekKliknelismy()
        statek.przesun("-", "d")
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()
        self.zapisz()


    def rysujStatki(self):
        self.poleGry.odswiezTablice()
        self.ui.sc.czysc()
        srodki = miod.rysujMiod(self.ui.sc.axes)

        for i in range(self.poleGry.dlugoscTablicy):
            for j in range(self.poleGry.dlugoscTablicy):
                if self.poleGry.mojaTablica[i][j] == 1:
                    x, y = srodki[i*10+j] #[i*10+j]  [j*10+i] moze i tak trzeba
                    miod.miodStatek(x, y, self.ui.sc.axes, 1)
                if self.poleGry.mojaTablica[i][j] == 2:
                    x, y = srodki[i*10+j] #[i*10+j]  [j*10+i] moze i tak trzeba
                    miod.miodStatek(x, y, self.ui.sc.axes, 2)
        self.ui.sc.draw()

    def wstawStatki(self):
            if not self.ostatniStatek:
                dlugosc = self.dlugoscstatku()              # Pobieramy dlugosc statku z listy dlugosci statkow

                if dlugosc  == 0:
                    self.ostatniStatek = True
                    nazwa = "my_json.txt"

                    with open(nazwa, 'rb+') as ft:          # Jezeli dodalismy wszystkie statki, to czyscimy prace krokowa
                        ft.truncate()

                    self.zapisz()                           # I dodajemy aktualne polozenie

                if dlugosc == 0:
                    self.ui.textEdit.clear()
                    self.ui.textEdit.insertPlainText("Skonczyly ci sie statki")
                else:
                    statekY, statekX = self._aktualneKliki #self.ui.textEdit.toPlainText()

                    if int(statekX) + dlugosc > 10:
                        self.ui.textEdit.clear()
                        self.ui.textEdit.insertPlainText( "Nie zmiesciles sie w polu walki. Statek wypadl ze swiata. Nie mozesz go uzywac.")
                    else:
                        self.poleGry.tablicaStatkow.append(obiekt.Statek(dlugosc, int(statekX), int(statekY),
                                                                         self.poleGry.tablicaStatkow.__len__()))
                        self.poleGry.piszTablice()
                       # self.ui.sc._tab = self.poleGry.mojaTablica
                self.poleGry.drukujTablice()
                self.rysujStatki()
                self.ui.sc.draw()
                pass

    def strzel(self):
        data = str(self._aktualneKliki[0])+str( self._aktualneKliki[1])#self.ui.textEdit.toPlainText()#str(raw_input())
        self.client_socket.send(data)
        self.ui.textEdit.clear()
        self.dane.set(data)
        #print self.dane.get(), "tutaj nadajemy"
        pass

    def czyXYwStatku(self):
        x = self._aktualneKliki[0]
        y = self._aktualneKliki[1]
        for i in self.poleGry.tablicaStatkow.pozycjaCzlonu:
            print i[0]
        for statek in self.poleGry.tablicaStatkow:
            pass

    def kur(self):
        x, y = parsuj.parsuj(self._data)
        for statek in self.poleGry.tablicaStatkow:
            i = 0
            for czlon in statek.pozycjaCzlonu:

                if czlon[0] == y and czlon[1] == x:
                    data = "Przed chwila trafiles!"
                    self.client_socket.send(data)
                    self.ui.textEdit.clear()
                    self.dane.set(data)
                    statek.stan[i] = 2
                i = i + 1
        self.rysujStatki()



    def oberwij(self):
        data = ""
        while True:
            if killall:
                break
            try:
                data = self.client_socket.recv(RECV_BUFFER)
                if not self.dane.get() == data:
                    if data == "Przed chwila trafiles!":
                        #self.ui.textEdit.insertPlainText(" ")
                        #self.ui.textEdit.insertPlainText("Ktos zostal trafiony.")
                        pass
                    else:
                        print data
                        self._data = data

                #x, y = parsuj(data)
                #print x
                if self.dane.get() == data:
                    print data
                    self.dane.clr()
            except:
                break
            if not data:
                break



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komiwojazer()
    myapp.show()
    sys.exit(app.exec_())


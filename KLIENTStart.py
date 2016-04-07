import obiekty as obiekt
import miod, parsuj
import socket
import sys
import numpy as np

from random import random
from threading import Thread, Lock
from PyQt4 import QtCore, QtGui
from RAZ import Ui_Widget

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

        for i in range(srodki.__len__()):
            xs, ys = srodki[i]
            if np.absolute(xs - x) < 1:
                if np.absolute(ys - y) < 1:
                    ikomorki = i % 10
                    jkomorki = (i - ikomorki)/10
                    self._aktualneKliki = [ikomorki, jkomorki]

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
        self._aktualneKliki = [0,0]
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
        self.ui.PRZESUN.clicked.connect(self.przesun)
        self.ui.STRZELAJ.clicked.connect(self.kur)
        self.ui.sc.mpl_connect('button_press_event', self.onclick)


    '''def przesun(self):

        print "KOLO"
        znak, orient = self.ui.textEdit.toPlainText()
        statek = self.naKtoryStatekKliknelismy()
        statek.przesun(znak, orient)
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()'''

    def przesun(self):


        statek = self.naKtoryStatekKliknelismy()
        znak, orient = self.ui.textEdit.toPlainText()

        if (orient == "o"):
            statek.obrot(znak, orient)
        else:
            statek.przesun(znak, orient)

        self.poleGry.odswiezTablice()

        self.rysujStatki()
        self.ui.sc.draw()

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
        dlugosc = self.dlugoscstatku()              # Pobieramy dlugosc statku z listy dlugosci statkow

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
                self.ui.sc._tab = self.poleGry.mojaTablica

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
                        self.ui.textEdit.insertPlainText(" ")
                        self.ui.textEdit.insertPlainText("Rozbitkowie donosza, ze przed chwila rozbiles statek wroga!")
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

    def datuj(self):
        print self._data


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komiwojazer()
    myapp.show()
    sys.exit(app.exec_())


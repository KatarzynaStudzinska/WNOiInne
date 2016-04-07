import obiekty as obiekt
import miod
import numpy as np
import socket
import sys

from random import random
from PyQt4 import QtCore, QtGui
from RAZ import Ui_Widget
from threading import Thread, Lock

global PORT, HOST, RECV_BUFFER, killall

HOST = 'localhost'                          # Labolatoryjnym adresem jest '153.19.54.27'
PORT = 8888                                 # Labolatoryjnym portem jest 50002
RECV_BUFFER = 2048
killall = False
CZCIONKA = 23


class Komiwojazer(QtGui.QWidget):
    _aktualneKliki = []
    _obrot = 0
    _tabkrawedzi = []
    _tabwezlow = []
    _gen = []

    def onclick(self, event):
        print (event.xdata, event.ydata)
        x = event.xdata
        y = event.ydata
        srodki = miod.rysujMiod(self.ui.sc.axes)

        for i in range(srodki.__len__()):
            xs, ys = srodki[i]
            if np.absolute(xs - x) < 1:
                if np.absolute(ys - y) < 1:
                    ikomorki = i%10
                    jkomorki = (i - ikomorki)/10
                    self._aktualneKliki = [ikomorki, jkomorki]

    def naKtoryStatekKliknelismy(self):
        for i in range(self.poleGry.tablicaStatkow.__len__()):
            for j in range(self.poleGry.tablicaStatkow[i].pozycjaCzlonu.__len__()):
                xk, yk = self.poleGry.tablicaStatkow[i].pozycjaCzlonu[j]
                print xk, yk
                ikomorki, jkomorki = self._aktualneKliki
                if ikomorki == yk and jkomorki == xk:
                    return self.poleGry.tablicaStatkow[i]
                    break

    def initClient(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        print 'You have connected to server!'
        # sending name

        name = "Klient " + str(random())           #str(raw_input("Enter your name: "))
        print name
        self.client_socket.send(name)
        response = self.client_socket.recv(RECV_BUFFER)
        # "0" means error
        if response == "0":
            print'User %s alraedy logged in! Connection terminated!' % name
            return
        # "1" means everything's fine
        if response == "1":
            print 'User connected!'
            print 'Welcome ' + name + ' to our chat! Please type "q" to quit!'
            self.lock = Lock()
            Thread(target=self.strzel).start()          #, args=(self.client_socket, self.lock)).start()
            Thread(target=self.oberwij).start()         #, args=(client_socket, lock)).start()

    def __init__(self, parent=None):
        self.dane = obiekt.Dane()
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Wrog")
        self.initClient()

        miod.rysujMiod(self.ui.sc.axes)

        def dlugosciStatku():
            listadlug = [4, 4, 3, 2, 2, 1]
            idx = {'i': 0}

            def jakadlugosc():
                if idx.get('i')< listadlug.__len__():
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
        self.ui.PRZESUN.clicked.connect(self.przesun)
        self.ui.sc.mpl_connect('button_press_event', self.onclick)
        self.show()

    def przesun(self):

        znak, orient = self.ui.textEdit.toPlainText()
        statek = self.naKtoryStatekKliknelismy()
        print statek.przesun(znak, orient)
        self.poleGry.odswiezTablice()
        self.rysujStatki()
        self.ui.sc.draw()

    def rysujStatki(self):
        self.ui.sc.czysc()
        srodki = miod.rysujMiod(self.ui.sc.axes)
        for i in range(self.poleGry.dlugoscTablicy):
            for j in range(self.poleGry.dlugoscTablicy):
                if self.poleGry.mojaTablica[i][j] == 1:
                    x, y = srodki[i*10+j]                        #[i*10+j]  [j*10+i] moze i tak trzeba
                    miod.miodStatek(x, y, self.ui.sc.axes, 1)

    def wstawStatki(self):
        dlugosc = self.dlugoscstatku()                           #pobieramy dlugosc statku z listy dlugosci statkow

        if dlugosc == 0:
            self.ui.textEdit.clear()
            self.ui.textEdit.insertPlainText("Skonczyly ci sie statki")
        else:
            statekY, statekX = self._aktualneKliki              #self.ui.textEdit.toPlainText()


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
        global killall
        data = self.ui.textEdit.toPlainText()                   #str(raw_input())
        self.client_socket.send(data)
        self.ui.textEdit.clear()
        self.dane.set(data)
        pass

    def oberwij(self):

        global killall
        while True:
            if killall:
                break
            try:
                data = self.client_socket.recv(RECV_BUFFER)
                print(data)
                if self.dane.get() == data:
                    self.dane.clr()
                else:
                    if data.__len__() == 2 and data.isdigit():
                        x = int(data[0])
                        y = int(data[1])
                        for statek in self.poleGry.tablicaStatkow:
                            for (czlon, i) in (statek.pozycjaCzlonu, statek.pozycjaCzlonu.__len__()):
                                if x == czlon[0] and y == czlon[1]:
                                    statek.stan[i] = 2
                            self.poleGry.drukujTablice()
                    else:
                        pass
            except:
                break
            if not data:
                break


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Komiwojazer()
    myapp.show()
    sys.exit(app.exec_())


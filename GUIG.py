# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from __future__ import unicode_literals
import sys
import os
import pyglet

from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
progname = os.path.basename(sys.argv[0])
progversion = "0.1"

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MyMplCanvas(FigureCanvas):
    _info = []
    _lista = []
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def onpick(self, event):
        ind = event.ind[0]
        x, y, z = event.artist._offsets3d
        self._info = [x[ind], y[ind], z[ind]]
        self._lista.append(self._info)
        x[ind], y[ind], z[ind]
        music = pyglet.resource.media('b5.wav')
        music.play()

    def czysclisty(self):
        self._info = []
        self._lista = []

    def __init__(self, parent):
        fig = plt.figure()
        self.axes = fig.add_subplot(111, projection='3d')
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)

        #self.compute_initial_figure()

        self.axes.view_init(30, 5)
        self.axes.set_xlabel('X Label')
        self.axes.set_ylabel('Y Label')
        self.axes.set_zlabel('Z Label')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


        fig.canvas.mpl_connect('pick_event', self.onpick)

    def czysc(self):
        plt.cla()


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def russia(self, tab):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(tab, s)


class MyMplCanvas2d(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent):
        fig = plt.figure()
        self.axes = fig.add_subplot(111)

        self.axes.set_xlabel('X Label')
        self.axes.set_ylabel('Y Label')

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def czysc(self):
        plt.cla()



class MyStaticMplCanvas2d(MyMplCanvas2d):
    """Simple canvas with a sine plot."""

    def russia(self, tab):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(tab, s)




class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(1346, 1988)
        self.WciskPatrz = QtGui.QPushButton(Widget)
        self.WciskPatrz.setGeometry(QtCore.QRect(30, 330, 111, 51))
        self.WciskPatrz.setObjectName(_fromUtf8("WciskPatrz"))
        self.WciskLicz = QtGui.QPushButton(Widget)
        self.WciskLicz.setGeometry(QtCore.QRect(30, 280, 111, 51))
        self.WciskLicz.setObjectName(_fromUtf8("WciskLicz"))
        self.WciskKrzycz = QtGui.QPushButton(Widget)
        self.WciskKrzycz.setGeometry(QtCore.QRect(30, 380, 111, 51))
        self.WciskKrzycz.setObjectName(_fromUtf8("WciskKrzycz"))

        self.lcdNumber = QtGui.QLCDNumber(Widget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 30, 161, 81))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_mutacji = QtGui.QLCDNumber(Widget)
        self.lcdNumber_mutacji.setGeometry(QtCore.QRect(230, 30, 161, 81))
        self.lcdNumber_mutacji.setObjectName(_fromUtf8("lcdNumber_mutacji"))

        self.suwak = QtGui.QSlider(Widget)
        self.suwak.setGeometry(QtCore.QRect(30, 180, 281, 22))
        self.suwak.setOrientation(QtCore.Qt.Horizontal)
        self.suwak.setObjectName(_fromUtf8("suwak"))
        self.suwak_mutacji = QtGui.QSlider(Widget)
        self.suwak_mutacji.setGeometry(QtCore.QRect(30, 250, 281, 22))
        self.suwak_mutacji.setOrientation(QtCore.Qt.Horizontal)
        self.suwak_mutacji.setObjectName(_fromUtf8("suwak_mutacji"))

        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(30, 130, 131, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 204, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(30, 420, 204, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))



        self.sc = MyStaticMplCanvas(Widget)
        self.sc.setGeometry(QtCore.QRect(430, 30, 861, 881))



        self.retranslateUi(Widget)
        QtCore.QObject.connect(Widget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), self.WciskLicz.click)
        QtCore.QObject.connect(Widget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), self.WciskPatrz.click)
        #QtCore.QObject.connect(Widget, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), self.WciskLicz.click)
        QtCore.QObject.connect(Widget, QtCore.SIGNAL(_fromUtf8("objectNameChanged(QString)")), self.suwak.setWindowTitle)

        self.suwak.setMinimum(3)
        self.suwak.setMaximum(50)
        self.suwak.valueChanged.connect(self.lcdNumber.display)
        self.suwak_mutacji.setMinimum(70)
        self.suwak_mutacji.setMaximum(100)
        self.suwak_mutacji.valueChanged.connect(self.lcdNumber_mutacji.display)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.WciskLicz.setText(_translate("Widget", "Przejdź graf", None))
        self.WciskPatrz.setText(_translate("Widget", "Zmień Widok", None))
        self.WciskKrzycz.setText(_translate("Widget", "Rysuj Wybrane", None))
        self.label.setText(_translate("Widget", "Podaj liczbę węzłów:", None))
        self.label_2.setText(_translate("Widget", "Podaj prawdopodobieństwo mutacji:", None))



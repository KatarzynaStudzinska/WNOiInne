# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RAZ.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import miod
progversion = "0.1"




class MyMplCanvas(FigureCanvas):
    _info = []
    _lista = []
    _tab = []

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

        self.axes = fig.add_subplot(111)#, projection='2d')
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)

        #self.srodki = miod.rysujMiod(self.axes)
        #print self.srodki
        #self.axes.view_init(30, 5)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)


        fig.canvas.mpl_connect('pick_event', self.onpick)

    def rysuj(self):
        self.axes.imshow(self._tab, interpolation='nearest')


    def czysc(self):
        plt.cla()


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(698, 749)
        self.widget = QtGui.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 651, 441))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textEdit = QtGui.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 460, 651, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayoutWidget = QtGui.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 550, 651, 135))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.STRZELAJ = QtGui.QPushButton(self.verticalLayoutWidget)
        self.STRZELAJ.setObjectName(_fromUtf8("STRZELAJ"))
        self.verticalLayout.addWidget(self.STRZELAJ)
        self.PRZESUN = QtGui.QPushButton(self.verticalLayoutWidget)
        self.PRZESUN.setObjectName(_fromUtf8("PRZESUN"))
        self.verticalLayout.addWidget(self.PRZESUN)
        self.WSTAW = QtGui.QPushButton(self.verticalLayoutWidget)
        self.WSTAW.setObjectName(_fromUtf8("WSTAW"))
        self.verticalLayout.addWidget(self.WSTAW)
        self.INNY = QtGui.QPushButton(self.verticalLayoutWidget)
        self.INNY.setObjectName(_fromUtf8("INNY"))
        self.verticalLayout.addWidget(self.INNY)
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 700, 651, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.sc = MyMplCanvas(Widget)
        self.sc.setGeometry(QtCore.QRect(20, 30, 301, 301))


        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.STRZELAJ.setText(_translate("Widget", "STRZELAJ", None))
        self.PRZESUN.setText(_translate("Widget", "PRZESUN", None))
        self.WSTAW.setText(_translate("Widget", "WSTAW STATEK", None))
        self.INNY.setText(_translate("Widget", "CO INNEGO", None))
        self.label.setText(_translate("Widget", "+o/-o - obrot +w/-h -przesuwanie", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())


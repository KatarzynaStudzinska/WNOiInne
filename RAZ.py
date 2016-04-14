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
        self.textEdit.setGeometry(QtCore.QRect(20, 500, 651, 60))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayoutWidget = QtGui.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(15, 560, 670, 195))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(10)
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
        self.ZAPIS = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ZAPIS.setObjectName(_fromUtf8("ZAPIS"))
        self.verticalLayout.addWidget(self.ZAPIS)
        self.ODCZYTZPLIKU = QtGui.QPushButton(self.verticalLayoutWidget)
        self.ODCZYTZPLIKU.setObjectName(_fromUtf8("ODCZYTZPLIKU"))
        self.verticalLayout.addWidget(self.ODCZYTZPLIKU)


#-----------------------------------------------------------------------------------------------

        self.verticalLayoutWidgetLEWO = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetLEWO.setGeometry(QtCore.QRect(100, 330, 50, 150))
        self.verticalLayoutWidgetLEWO.setObjectName(_fromUtf8("verticalLayoutWidgetLEWO"))
        self.verticalLayoutLEWO = QtGui.QVBoxLayout(self.verticalLayoutWidgetLEWO)

        self.LEWO = QtGui.QPushButton(self.verticalLayoutWidgetLEWO)
        self.LEWO.setObjectName(_fromUtf8("LEWO"))
        self.verticalLayoutLEWO.addWidget(self.LEWO)

        self.verticalLayoutWidgetPRAWO = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetPRAWO.setGeometry(QtCore.QRect(190, 330, 50, 150))
        self.verticalLayoutWidgetPRAWO.setObjectName(_fromUtf8("verticalLayoutWidgetPRAWO"))
        self.verticalLayoutPRAWO = QtGui.QVBoxLayout(self.verticalLayoutWidgetPRAWO)

        self.PRAWO = QtGui.QPushButton(self.verticalLayoutWidgetPRAWO)
        self.PRAWO.setObjectName(_fromUtf8("PRAWO"))
        self.verticalLayoutPRAWO.addWidget(self.PRAWO)

        self.verticalLayoutWidgetGORA = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetGORA.setGeometry(QtCore.QRect(145, 285, 50, 150))
        self.verticalLayoutWidgetGORA.setObjectName(_fromUtf8("verticalLayoutWidgetPRAWO"))
        self.verticalLayoutPRAWO = QtGui.QVBoxLayout(self.verticalLayoutWidgetGORA)

        self.GORA = QtGui.QPushButton(self.verticalLayoutWidgetGORA)
        self.GORA.setObjectName(_fromUtf8("GORA"))
        self.verticalLayoutPRAWO.addWidget(self.GORA)
        '''self.verticalLayoutWidgetGORA = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetGORA.setGeometry(QtCore.QRect(145, 305, 50, 150))
        self.verticalLayoutWidgetGORA.setObjectName(_fromUtf8("verticalLayoutWidgetGORA"))
        self.verticalLayoutGORA = QtGui.QVBoxLayout(self.verticalLayoutWidgetGORA)

        self.GORA = QtGui.QPushButton(self.verticalLayoutWidgetGORA)
        self.GORA.setObjectName(_fromUtf8("GORA"))
        self.verticalLayoutGORA.addWidget(self.GORA)'''

        self.verticalLayoutWidgetDOL = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetDOL.setGeometry(QtCore.QRect(145, 375, 50, 150))
        self.verticalLayoutWidgetDOL.setObjectName(_fromUtf8("verticalLayoutWidgetDOL"))
        self.verticalLayoutDOL = QtGui.QVBoxLayout(self.verticalLayoutWidgetDOL)

        self.DOL = QtGui.QPushButton(self.verticalLayoutWidgetDOL)
        self.DOL.setObjectName(_fromUtf8("DOL"))
        self.verticalLayoutDOL.addWidget(self.DOL)

        self.verticalLayoutWidgetOBROTZEGAR = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetOBROTZEGAR.setGeometry(QtCore.QRect(235, 330, 50, 150))
        self.verticalLayoutWidgetOBROTZEGAR.setObjectName(_fromUtf8("verticalLayoutWidgetOBROTZEGAR"))
        self.verticalLayoutOBROTZEGAR = QtGui.QVBoxLayout(self.verticalLayoutWidgetOBROTZEGAR)

        self.OBROTZEGAR = QtGui.QPushButton(self.verticalLayoutWidgetOBROTZEGAR)
        self.OBROTZEGAR.setObjectName(_fromUtf8("OBROTZEGAR"))
        self.verticalLayoutOBROTZEGAR.addWidget(self.OBROTZEGAR)

        self.verticalLayoutWidgetOBROTPRZECIWNIE = QtGui.QWidget(Widget)
        self.verticalLayoutWidgetOBROTPRZECIWNIE.setGeometry(QtCore.QRect(55, 330, 50, 150))
        self.verticalLayoutWidgetOBROTPRZECIWNIE.setObjectName(_fromUtf8("verticalLayoutWidgetOBROTPRZECIWNIE"))
        self.verticalLayoutOBROTPRZECIWNIE = QtGui.QVBoxLayout(self.verticalLayoutWidgetOBROTPRZECIWNIE)

        self.OBROTPRZECIWNIE = QtGui.QPushButton(self.verticalLayoutWidgetOBROTPRZECIWNIE)
        self.OBROTPRZECIWNIE.setObjectName(_fromUtf8("OBROTPRZECIWNIE"))
        self.verticalLayoutOBROTPRZECIWNIE.addWidget(self.OBROTPRZECIWNIE)


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
        self.ZAPIS.setText(_translate("Widget", "ZAPIS", None))
        self.ODCZYTZPLIKU.setText(_translate("Widget", "ODCZYT PLIKU", None))
        #self.label.setText(_translate("Widget", "+o/-o - obrot +w/-h -przesuwanie", None))
        self.LEWO.setText(_translate("Widget", chr(27), None))
        self.PRAWO.setText(_translate("Widget", chr(26), None))
        self.GORA.setText(_translate("Widget", chr(24), None))
        self.DOL.setText(_translate("Widget", unichr(8595), None))
        self.OBROTZEGAR.setText(_translate("Widget", unichr(10549), None))
        self.OBROTPRZECIWNIE.setText(_translate("Widget", unichr(10548), None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())


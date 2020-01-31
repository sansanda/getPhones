# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo_MDI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Ejercicios.recursos.recursos_1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(-1, -1, 781, 541))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        self.menuInsertar = QtWidgets.QMenu(self.menubar)
        self.menuInsertar.setObjectName("menuInsertar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNueva_Ventana = QtWidgets.QAction(MainWindow)
        self.actionNueva_Ventana.setObjectName("actionNueva_Ventana")
        self.actionDistribuir_Cascada = QtWidgets.QAction(MainWindow)
        self.actionDistribuir_Cascada.setObjectName("actionDistribuir_Cascada")
        self.actionDistribuir_Mosaico = QtWidgets.QAction(MainWindow)
        self.actionDistribuir_Mosaico.setObjectName("actionDistribuir_Mosaico")
        self.menuInsertar.addAction(self.actionNueva_Ventana)
        self.menuInsertar.addAction(self.actionDistribuir_Cascada)
        self.menuInsertar.addAction(self.actionDistribuir_Mosaico)
        self.menubar.addAction(self.menuInsertar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuInsertar.setTitle(_translate("MainWindow", "MDI"))
        self.actionNueva_Ventana.setText(_translate("MainWindow", "Nueva Ventana"))
        self.actionDistribuir_Cascada.setText(_translate("MainWindow", "Distribuir Cascada"))
        self.actionDistribuir_Mosaico.setText(_translate("MainWindow", "Distribuir Mosaico"))


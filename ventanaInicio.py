# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaInicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import self as self
from PyQt5 import QtCore, QtGui, QtWidgets

from ventanaListadoClientes import ListadoClientes
from ventanaNuevaReserva import NuevaReserva
from ventanaListadoReservas import ListadoReservas
from ventanaClientes import Clientes

class Inicio(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Principal")
        MainWindow.resize(450, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNuevaReserva = QtWidgets.QPushButton(self.centralwidget)
        self.btnNuevaReserva.setGeometry(QtCore.QRect(40, 30, 110, 40))
        self.btnNuevaReserva.setObjectName("btnNuevaReserva")
        self.btnListadoReservas = QtWidgets.QPushButton(self.centralwidget)
        self.btnListadoReservas.setGeometry(QtCore.QRect(250, 30, 110, 40))
        self.btnListadoReservas.setObjectName("btnListadoReservas")
        self.btnListadoClientes = QtWidgets.QPushButton(self.centralwidget)
        self.btnListadoClientes.setGeometry(QtCore.QRect(40, 110, 110, 40))
        self.btnListadoClientes.setObjectName("btnClienteMes")
        self.btnClientes = QtWidgets.QPushButton(self.centralwidget)
        self.btnClientes.setGeometry(QtCore.QRect(250, 110, 110, 40))
        self.btnClientes.setObjectName("btnClientes")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(150, 190, 110, 40))
        self.btnSalir.setObjectName("btnSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        #Asignamos funciones a los botones
        self.btnNuevaReserva.clicked.connect(self.mostrarNuevaReserva)
        self.btnListadoReservas.clicked.connect(self.mostrarListadoReservas)
        self.btnListadoClientes.clicked.connect(self.mostrarListadoClientes)
        self.btnClientes.clicked.connect(self.mostrarClientes)
        self.btnSalir.clicked.connect(self.salir)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def mostrarNuevaReserva(self):
        self.ventanaNuevaReserva = QtWidgets.QMainWindow()
        self.nuevaReserva = NuevaReserva()
        self.nuevaReserva.setupUi(self.ventanaNuevaReserva)
        self.ventanaNuevaReserva.show()

    def mostrarListadoReservas(self):
        self.ventanaListadoReservas = QtWidgets.QMainWindow()
        self.listadoReservas = ListadoReservas()
        self.listadoReservas.setupUi(self.ventanaListadoReservas)
        self.ventanaListadoReservas.show()

    def mostrarListadoClientes(self):
        self.ventanaListadoClientes = QtWidgets.QMainWindow()
        self.listadoClientes = ListadoClientes()
        self.listadoClientes.setupUi(self.ventanaListadoClientes)
        self.ventanaListadoClientes.show()

    def mostrarClientes(self):
        self.ventanaClientes = QtWidgets.QMainWindow()
        self.clientes = Clientes()
        self.clientes.setupUi(self.ventanaClientes)
        self.ventanaClientes.show()

    def salir(self):
        exit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnNuevaReserva.setText(_translate("MainWindow", "Nueva Reserva"))
        self.btnListadoReservas.setText(_translate("MainWindow", "Listado Reservas"))
        self.btnListadoClientes.setText(_translate("MainWindow", "Listado Clientes"))
        self.btnClientes.setText(_translate("MainWindow", "Clientes"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    inicio = Inicio()
    inicio.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaNuevaReserva.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import datetime

from PyQt5 import QtCore, QtWidgets
import mysql.connector

class NuevaReserva(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Nueva Reserva")
        MainWindow.resize(869, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textFecInicial = QtWidgets.QLineEdit(self.centralwidget)
        self.textFecInicial.setGeometry(QtCore.QRect(249, 32, 116, 22))
        self.textFecInicial.setObjectName("textFecInicial")
        self.textFecFinal = QtWidgets.QLineEdit(self.centralwidget)
        self.textFecFinal.setGeometry(QtCore.QRect(629, 32, 116, 22))
        self.textFecFinal.setObjectName("textFecFinal")
        self.textLitros = QtWidgets.QLineEdit(self.centralwidget)
        self.textLitros.setGeometry(QtCore.QRect(629, 78, 116, 22))
        self.textLitros.setObjectName("textLitros")
        self.textCodReserva = QtWidgets.QLineEdit(self.centralwidget)
        self.textCodReserva.setGeometry(QtCore.QRect(249, 78, 116, 22))
        self.textCodReserva.setObjectName("textCodReserva")
        self.labelFechaInicial = QtWidgets.QLabel(self.centralwidget)
        self.labelFechaInicial.setGeometry(QtCore.QRect(45, 35, 192, 16))
        self.labelFechaInicial.setObjectName("labelFechaInicial")
        self.labelFechaFinal = QtWidgets.QLabel(self.centralwidget)
        self.labelFechaFinal.setGeometry(QtCore.QRect(438, 35, 179, 16))
        self.labelFechaFinal.setObjectName("labelFechaFinal")
        self.labelLitros = QtWidgets.QLabel(self.centralwidget)
        self.labelLitros.setGeometry(QtCore.QRect(438, 81, 152, 16))
        self.labelLitros.setObjectName("labelLitros")
        self.labelCodigoReserva = QtWidgets.QLabel(self.centralwidget)
        self.labelCodigoReserva.setGeometry(QtCore.QRect(45, 81, 167, 16))
        self.labelCodigoReserva.setObjectName("labelCodigoReserva")
        self.comboBox_Coches = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Coches.setGeometry(QtCore.QRect(320, 180, 421, 20))
        self.comboBox_Coches.setObjectName("comboBox_Coches")
        self.comboBox_Clientes = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Clientes.setGeometry(QtCore.QRect(50, 180, 196, 20))
        self.comboBox_Clientes.setObjectName("comboBox_Clientes")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(130, 340, 93, 28))
        self.okButton.setObjectName("pushButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(610, 340, 93, 28))
        self.cancelButton.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.okButton.clicked.connect(self.consultaBDNombre)
        #Añadimos función al botón cancel
        self.cancelButton.clicked.connect(self.mostrarInicio)


    def consultaBDNombre(self):
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='castelao',
            db='UD02BDReservaCoches')

        cur=conexion.cursor()
        cur.execute("SELECT * FROM clientes WHERE clNif=12131414P")
        result = cur.fetchall()
        for x in result:
            print(x)
        conexion.close()

    def mostrarInicio(self):
        from ventanaInicio import Inicio
        self.ventanaInicio = QtWidgets.QMainWindow()
        self.inicio = Inicio()
        self.inicio.setupUi(self.ventanaInicio)
        self.ventanaInicio.show()

    def capturarDatos(self):
        self.fechaInicial = self.textFecInicial.text()
        self.fechaFinal = self.textFecFinal.text()
        self.litros = self.textLitros.text()
        self.codigoReserva = self.textCodReserva.text()

        self.fechaInicialDate = datetime.strptime(self.fechaInicial, '%dd/%mm/%Y')
        self.fechaFinalDate = datetime.strptime(self.fechaFinal, '%dd/%mm/%Y')
        self.litrosInt = int(self.litros)
        self.codigoReservaInt = int(self.codigoReserva)


    def insertarRegistroBD(self):
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='castelao',
            db='UD02BDReservaCoches')
        cur = conexion.cursor()
        sql = "INSERT INTO reservas (reCodigo, reFecInicio, reFecFinal) VALUES ('{}', '{}', '{}')".format(self.codigoReservaInt, self.fechaInicialDate, self.fechaFinalDate)
        #val = (self.codigoReservaInt, self.fechaInicialDate, self.fechaFinalDate)
        cur.execute(sql)

        conexion.commit()
        print(cur.rowcount, "registro insertado")

        conexion.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFechaInicial.setText(_translate("MainWindow", "Fecha Inicial (DD/MM/AAAA):"))
        self.labelFechaFinal.setText(_translate("MainWindow", "Fecha Final (DD/MM/AAAA):"))
        self.labelLitros.setText(_translate("MainWindow", "Litros Consumidos:"))
        self.labelCodigoReserva.setText(_translate("MainWindow", "Código Reserva:"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))

        self.okButton.clicked.connect(self.capturarDatos)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = NuevaReserva()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

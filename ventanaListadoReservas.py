# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListadoReservas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ListadoReservas(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Listado Reservas")
        MainWindow.resize(884, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textPrecioMedio = QtWidgets.QLineEdit(self.centralwidget)
        self.textPrecioMedio.setGeometry(QtCore.QRect(340, 30, 116, 22))
        self.textPrecioMedio.setObjectName("textPrecioMedio")
        self.textDiasMedia = QtWidgets.QLineEdit(self.centralwidget)
        self.textDiasMedia.setGeometry(QtCore.QRect(500, 30, 116, 22))
        self.textDiasMedia.setObjectName("textDiasMedia")
        self.textTotalMes = QtWidgets.QLineEdit(self.centralwidget)
        self.textTotalMes.setGeometry(QtCore.QRect(670, 30, 116, 22))
        self.textTotalMes.setObjectName("textTotalMes")
        self.textNumAlquileres = QtWidgets.QLineEdit(self.centralwidget)
        self.textNumAlquileres.setGeometry(QtCore.QRect(170, 30, 116, 22))
        self.textNumAlquileres.setObjectName("textNumAlquileres")
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(170, 350, 93, 28))
        self.btnOk.setObjectName("btnOk")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(600, 350, 93, 28))
        self.btnAtras.setObjectName("btnAtras")
        self.comboBoxMesesAnho = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMesesAnho.setGeometry(QtCore.QRect(20, 30, 106, 20))
        self.comboBoxMesesAnho.setObjectName("comboBox")
        self.labelNumAlquileres = QtWidgets.QLabel(self.centralwidget)
        self.labelNumAlquileres.setGeometry(QtCore.QRect(174, 0, 111, 20))
        self.labelNumAlquileres.setObjectName("labelNumAlquileres")
        self.labelPrecioMedio = QtWidgets.QLabel(self.centralwidget)
        self.labelPrecioMedio.setGeometry(QtCore.QRect(360, 0, 81, 20))
        self.labelPrecioMedio.setObjectName("labelPrecioMedio")
        self.labelDiasMedia = QtWidgets.QLabel(self.centralwidget)
        self.labelDiasMedia.setGeometry(QtCore.QRect(520, 0, 81, 20))
        self.labelDiasMedia.setObjectName("labelDiasMedia")
        self.labelTotalMes = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalMes.setGeometry(QtCore.QRect(700, 0, 55, 16))
        self.labelTotalMes.setObjectName("labelTotalMes")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(120, 90, 650, 221))
        self.tableView.setObjectName("tableView")

        for i in range(5):
            self.tableView.setColumnWidth(i, 150)

         #labels = ["Nombre Cliente", "Matrícula vehículo", "Precio", "Días", "Precio Total"]

         #for i in range(len(labels)):
             #self.tableView.setHorizontalHeaderLabels(labels[i])

        self.tableView.setHorizontalHeaderLabels(["Nombre Cliente", "Matrícula vehículo", "Precio", "Días", "Precio Total"])
        # self.tableView.setHorizontalHeader("Matrícula Vehículo")
        # self.tableView.setHorizontalHeader(["Precio"])
        # self.tableView.setHorizontalHeader(["Días"])
        # self.tableView.setHorizontalHeader(["Precio Total"])



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Rellenamos comboBox con los meses del año
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                 "Noviembre", "Diciembre"]

        for m in meses:
            self.comboBoxMesesAnho.addItem(m)

        #Añadimos funciones a botones ok y cancel
        self.btnOk.clicked.connect(self.mostrarDatos)
        self.btnAtras.clicked.connect(lambda: self.ejecutarFunciones(MainWindow))


    def ejecutarFunciones(self, MainWindow):
        self.mostrarInicio()
        MainWindow.close()
        
    def mostrarInicio(self):
        from ventanaInicio import Inicio
        self.ventanaInicio = QtWidgets.QMainWindow()
        self.inicio = Inicio()
        self.inicio.setupUi(self.ventanaInicio)
        self.ventanaInicio.show()

    def mostrarDatos(self):
        self.textNumAlquileres.setText("7")
        self.textTotalMes.setText("1000")
        self.textDiasMedia.setText("5")
        self.textPrecioMedio.setText("200")


    def borrarDatos(self):
        self.textNumAlquileres.clear()
        self.textTotalMes.clear()
        self.textDiasMedia.clear()
        self.textPrecioMedio.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listado Reservas"))
        self.btnOk.setText(_translate("MainWindow", "OK"))
        self.btnAtras.setText(_translate("MainWindow", "Atrás"))
        self.labelNumAlquileres.setText(_translate("MainWindow", "Numero Alquileres"))
        self.labelPrecioMedio.setText(_translate("MainWindow", "Precio Medio"))
        self.labelDiasMedia.setText(_translate("MainWindow", "Media días"))
        self.labelTotalMes.setText(_translate("MainWindow", "Total Mes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ListadoReservas()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

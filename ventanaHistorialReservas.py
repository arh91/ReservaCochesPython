# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListadoReservas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from datetime import datetime
import mysql.connector

mesesAnho = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
numerosMeses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
fechaActual = datetime.now().date()
stringFechaActual = str(fechaActual)
fecha = stringFechaActual.split("-")


class CenterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class HistorialReservas(object):

    selected_index = 0
    
    # Construye la ventana con todos sus elementos
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Historial Reservas")
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
        self.btnMostrarDatos = QtWidgets.QPushButton(self.centralwidget)
        self.btnMostrarDatos.setGeometry(QtCore.QRect(170, 350, 93, 28))
        self.btnMostrarDatos.setObjectName("btnMostrarDatos")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(600, 350, 93, 28))
        self.btnAtras.setObjectName("btnAtras")
        self.comboBoxMesesAnho = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMesesAnho.setGeometry(QtCore.QRect(20, 30, 106, 20))
        self.comboBoxMesesAnho.setObjectName("comboBox")
        self.comboBoxAnhos = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxAnhos.setGeometry(QtCore.QRect(20, 230, 106, 20))
        self.comboBoxAnhos.setObjectName("comboBoxAnhos")
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
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(170, 90, 650, 221))
        self.tableView.setObjectName("tableView")


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

        self.rellenarComboAnhos(self.comboBoxAnhos)
        self.rellenarComboMesesAnteriores(self.comboBoxMesesAnho)
        
        global selected_index
        selected_index = self.comboBoxMesesAnho.currentIndex() 

        #Añadimos funciones a botones ok y cancel
        self.comboBoxMesesAnho.currentIndexChanged.connect(lambda index: self.Cargar_Datos_Tabla(index, self.comboBoxAnhos))
        self.comboBoxAnhos.currentIndexChanged.connect(lambda index: self.mostrarMeses(index))
        self.btnMostrarDatos.clicked.connect(self.mostrarDatos)
        self.btnAtras.clicked.connect(lambda: self.ejecutarFunciones(MainWindow))


    def ejecutarFunciones(self, MainWindow):
        self.mostrarListadoReservas()
        MainWindow.close()


    # Función que rellena el comboBox meses con los meses que correspondan en función del año seleccionado por el usuario
    def mostrarMeses(self, index):
        if index==0:
            self.rellenarComboMesesAnteriores(self.comboBoxMesesAnho)
        elif index == 5:
            self.rellenarComboMesesSiquientes(self.comboBoxMesesAnho)
        else:
            self.rellenarComboMeses(self.comboBoxMesesAnho)


    # Función para conectar con la base de datos
    def establecerConexionBD(self):
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='castelao',
            db='UD02BDReservaCoches')
        
        return conexion
    

    # Función que construye una tabla para listar las reservas del historial por mes y año, accede a la base de datos, 
    # obtiene los datos correspondientes y carga dichos datos en la tabla
    def Cargar_Datos_Tabla(self, index, comboAnhos):    
        modelo = QStandardItemModel(MainWindow)
        self.tableView.setModel(modelo)

        # Establecer el delegate para centrar todos los datos en la tabla
        delegate = CenterDelegate()
        self.tableView.setItemDelegate(delegate)


        nombreColumnas = ["Cliente", "Vehículo", "Precio", "Días", "Total"]  # Nombres de las columnas
        modelo.setHorizontalHeaderLabels(nombreColumnas)

        anchoTabla = self.tableView.viewport().width()
        numeroColumnas = 5
        anchoColumna = anchoTabla / numeroColumnas

        for col in range(numeroColumnas):
            self.tableView.setColumnWidth(col, anchoColumna)  

        index+=1

        if(index<10):
            month = "0"+str(index)
        else:
            month = str(index)
        
        year = comboAnhos.currentText()

        conexion = self.establecerConexionBD()
        if not conexion:
            return
        
        query = ("select clNombre, inMatricula, coPrecio, DateDiff(reFecFinal, reFecInicio), coPrecio*DateDiff(reFecFinal, reFecInicio)"
                +" from historialInvolucra join Clientes on inCliente = clNif"
                +" join historialReservas on inReserva = reCodigo"
                +" join Coches on inMatricula = coMatricula"
                +" where month(reFecInicio) = "+ month
                +" and year(reFecInicio) = "+ year)
        cur=conexion.cursor()
        cur.execute(query)

        row = 0
        for data_row in cur.fetchall():
            for col, value in enumerate(data_row):
                item = QStandardItem(str(value))
                self.tableView.model().setItem(row, col, item)
            row += 1

        cur.close()
        conexion.close()
        

    # Función que muestra la ventana para el listado de reservas en curso
    def mostrarListadoReservas(self):
        from ventanaListadoReservas import ListadoReservas
        self.ventanaListadoReservas = QtWidgets.QMainWindow()
        self.listaReservas = ListadoReservas()
        self.listaReservas.setupUi(self.ventanaListadoReservas)
        self.ventanaListadoReservas.show()


    def mostrarDatos(self):
        self.textNumAlquileres.setText("7")
        self.textTotalMes.setText("1000")
        self.textDiasMedia.setText("5")
        self.textPrecioMedio.setText("200")


    # Deja en blanco los campos de la interfaz
    def borrarDatos(self):
        self.textNumAlquileres.clear()
        self.textTotalMes.clear()
        self.textDiasMedia.clear()
        self.textPrecioMedio.clear()


    def rellenarComboMeses(self, combo):
        combo.clear()
        for m in mesesAnho:
            combo.addItem(m)


    # Rellena el combo Meses con el mes actual más los meses anteriores
    def rellenarComboMesesAnteriores(self, combo):
        combo.clear()
        mesActual = fecha[1]
        indice = 0

        for n in numerosMeses:
            if n==mesActual:
                break
            indice+=1

        #ultimoMes = mesesAnho[indice]
        #print(ultimoMes) 

        indiceMes = 0
        for m in mesesAnho:
            if indiceMes>indice:
                break
            combo.addItem(m)
            indiceMes+=1
            


    # Rellena el combo Meses con los meses posteriores al mes actual
    def rellenarComboMesesSiquientes(self, combo):
        combo.clear()
        mesActual = fecha[1]
        indice = 0

        for n in numerosMeses:
            if n==mesActual:
                break
            indice+=1

        indiceMes = 0
        for m in mesesAnho:
            if indiceMes<=indice:
                indiceMes+=1
                continue
            combo.addItem(m)
            indiceMes+=1 


    # Rellena el combo Anhos con el año actual más los cinco años anteriores al mismo
    def rellenarComboAnhos(self, combo):
        combo.clear()

        anho = fecha[0]
        anhoActual = int(anho)
        for a in range(6):
            combo.addItem(str(anhoActual))
            anhoActual-=1


    # Configuramos el título de nuestra ventana y el texto para los botones y para los label
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Historial Reservas"))
        self.btnMostrarDatos.setText(_translate("MainWindow", "Mostrar Datos"))
        self.btnAtras.setText(_translate("MainWindow", "Atrás"))
        self.labelNumAlquileres.setText(_translate("MainWindow", "Numero Alquileres"))
        self.labelPrecioMedio.setText(_translate("MainWindow", "Precio Medio"))
        self.labelDiasMedia.setText(_translate("MainWindow", "Media días"))
        self.labelTotalMes.setText(_translate("MainWindow", "Total Mes"))


# Arranca la clase, construye la ventana y la muestra
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HistorialReservas()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

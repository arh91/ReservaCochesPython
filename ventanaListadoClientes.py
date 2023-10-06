# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaListadoClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import mysql.connector


class CenterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class ListadoClientes(object):

    direcciones = []
    localidades = []
    localidadesFinal = []


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxCiudades = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCiudades.setGeometry(QtCore.QRect(70, 30, 161, 22))
        self.comboBoxCiudades.setObjectName("comboBoxCiudades")
        self.btnMostrarDatos = QtWidgets.QPushButton(self.centralwidget)
        self.btnMostrarDatos.setGeometry(QtCore.QRect(320, 480, 161, 28))
        self.btnMostrarDatos.setObjectName("btnMostrarDatos")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(631,480, 93, 28))
        self.btnAtras.setObjectName("btnAtras")
        self.tablaClientes = QtWidgets.QTableView(self.centralwidget)
        self.tablaClientes.setGeometry(QtCore.QRect(100, 110, 641, 301))
        self.tablaClientes.setObjectName("tablaClientes")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(600, 30, 141, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        global selected_index
        selected_index = self.comboBoxCiudades.currentIndex()

        self.comboBoxCiudades.currentIndexChanged.connect(lambda index: self.load_data(index))
        self.btnMostrarDatos.clicked.connect(self.cargarDatos)
        self.btnAtras.clicked.connect(lambda: self.ejecutarFunciones(MainWindow))

        self.obtenerDirecciones()

        for lf in ListadoClientes.localidadesFinal:
            self.comboBoxCiudades.addItem(lf)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # Función para conectar con la base de datos
    def establecerConexionBD(self):
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='castelao',
            db='UD02BDReservaCoches')
        
        return conexion
    

    def ejecutarFunciones(self, MainWindow):
        self.mostrarInicio()
        MainWindow.close()

    def mostrarInicio(self):
        from ventanaInicio import Inicio
        self.ventanaInicio = QtWidgets.QMainWindow()
        self.inicio = Inicio()
        self.inicio.setupUi(self.ventanaInicio)
        self.ventanaInicio.show()

    def cargarDatos(self):
        item = self.comboBoxCiudades.currentText()
        self.load_data(item)


    def load_data(self, selected_item):
        try:
            modelo = QStandardItemModel(MainWindow)
            self.tableView.setModel(modelo)

            # Establecer el delegate para centrar todos los datos en la tabla
            delegate = CenterDelegate()
            self.tableView.setItemDelegate(delegate)


            nombreColumnas = ["NIF", "Nombre", "Dirección", "Teléfono"]  # Nombres de las columnas
            modelo.setHorizontalHeaderLabels(nombreColumnas)

            anchoTabla = self.tableView.viewport().width()
            numeroColumnas = 4
            anchoColumna = anchoTabla / numeroColumnas

            for col in range(numeroColumnas):
                self.tableView.setColumnWidth(col, anchoColumna)

            conexion = self.establecerConexionBD()
            cur = conexion.cursor()
            sql = "SELECT * FROM clientes WHERE clDireccion LIKE %s"
            ciudad = f"%{selected_item}%"
            cur.execute(sql, (ciudad,))

            row = 0
            for data_row in cur.fetchall():
                for col, value in enumerate(data_row):
                    item = QStandardItem(str(value))
                    self.tableView.model().setItem(row, col, item)
                row += 1
        except:
            print("Error al obtener los datos")
        finally:
            cur.close()
            conexion.close()
        


        """ query = QSqlQueryModel()
        query.setQuery(f"SELECT * FROM clientes WHERE clDireccion LIKE %s")

        if query.lastError().isValid():
            print("Error en la consulta:", query.lastError().text())
            return

        self.tablaClientes.setModel(query) """


    def obtenerDirecciones(self):
        """ global direcciones
        global localidades
        global localidadesFinal
 """
        self.obtenerDireccionesClientes(ListadoClientes.direcciones)
        for d in ListadoClientes.direcciones:
            arrayLocalidades = d.split(",")
            localidad = arrayLocalidades[arrayLocalidades.length-1]
            ListadoClientes.localidades.append(localidad)

        for l in ListadoClientes.localidades:
            if l in ListadoClientes.localidadesFinal:
                continue
            else:
                ListadoClientes.localidadesFinal.append(l)



    def obtenerDireccionesClientes(self, list):
        conexion = self.establecerConexionBD()
        try:
            cur = conexion.cursor()
            sql = "SELECT clDireccion FROM clientes"
            cur.execute(sql)
            #conexion.commit()

            for row in cur.fetchall():
                print(row)
                value = row[2]
                list.append(value)
            
            print(list)
            conexion.commit()
        except:
            print("Error: no se han podido obtener los datos")
        finally:
            # Cierra la conexión a la base de datos
            cur.close()
            conexion.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listado Clientes"))
        self.btnMostrarDatos.setText(_translate("MainWindow", "Mostrar Clientes"))
        self.btnAtras.setText(_translate("MainWindow", "Atrás"))
        self.checkBox.setText(_translate("MainWindow", "Por orden alfabético"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ListadoClientes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

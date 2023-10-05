import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
#from ventanaMasOpciones import masOpciones
from PyQt5.QtCore import pyqtSlot
import mysql.connector


class modificarCliente(QMainWindow):

    existeDni = "false"
    dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8 = "1", "2", "3", "4", "5", "6", "7", "8"
    nifIntro = "nif"
    nombreIntro = "nombre"
    primerApellidoIntro = "primerApellido"
    segundoApellidoIntro = "segundoApellido"
    calleIntro = "calle"
    numeroIntro = "numero"
    municipioIntro = "municipio"
    telefonoIntro = "telefono"
    nombreCompletoIntro = "nc"
    direccionIntro = "d"

    # Construye la ventana con todos sus elementos
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditNif = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNif.setGeometry(QtCore.QRect(200, 30, 113, 22))
        self.lineEditNif.setObjectName("lineEdit")
        self.lineEditNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNombre.setGeometry(QtCore.QRect(200, 80, 111, 22))
        self.lineEditNombre.setObjectName("lineEdit_2")
        self.labelNif = QtWidgets.QLabel(self.centralwidget)
        self.labelNif.setGeometry(QtCore.QRect(60, 30, 55, 16))
        self.labelNif.setObjectName("label")
        self.labelNombre = QtWidgets.QLabel(self.centralwidget)
        self.labelNombre.setGeometry(QtCore.QRect(60, 80, 55, 16))
        self.labelNombre.setObjectName("label_2")
        self.labelPrimerApellido = QtWidgets.QLabel(self.centralwidget)
        self.labelPrimerApellido.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.labelPrimerApellido.setObjectName("label_3")
        self.labelSegundoApellido = QtWidgets.QLabel(self.centralwidget)
        self.labelSegundoApellido.setGeometry(QtCore.QRect(60, 180, 111, 16))
        self.labelSegundoApellido.setObjectName("label_4")
        self.labelCalle = QtWidgets.QLabel(self.centralwidget)
        self.labelCalle.setGeometry(QtCore.QRect(60, 230, 55, 16))
        self.labelCalle.setObjectName("label_5")
        self.labelNumero = QtWidgets.QLabel(self.centralwidget)
        self.labelNumero.setGeometry(QtCore.QRect(60, 280, 55, 16))
        self.labelNumero.setObjectName("label_6")
        self.labelMunicipio = QtWidgets.QLabel(self.centralwidget)
        self.labelMunicipio.setGeometry(QtCore.QRect(60, 330, 55, 16))
        self.labelMunicipio.setObjectName("label_7")
        self.labelTelefono = QtWidgets.QLabel(self.centralwidget)
        self.labelTelefono.setGeometry(QtCore.QRect(60, 380, 55, 16))
        self.labelTelefono.setObjectName("label_8")
        self.lineEditPrimerApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPrimerApellido.setGeometry(QtCore.QRect(200, 130, 113, 22))
        self.lineEditPrimerApellido.setObjectName("lineEdit_3")
        self.lineEditSegundoApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSegundoApellido.setGeometry(QtCore.QRect(200, 180, 113, 22))
        self.lineEditSegundoApellido.setObjectName("lineEdit_4")
        self.lineEditCalle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCalle.setGeometry(QtCore.QRect(200, 220, 113, 22))
        self.lineEditCalle.setObjectName("lineEdit_5")
        self.lineEditNumero = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNumero.setGeometry(QtCore.QRect(200, 280, 113, 22))
        self.lineEditNumero.setObjectName("lineEdit_6")
        self.lineEditMunicipio = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMunicipio.setGeometry(QtCore.QRect(200, 330, 113, 22))
        self.lineEditMunicipio.setObjectName("lineEdit_7")
        self.lineEditTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTelefono.setGeometry(QtCore.QRect(200, 380, 113, 22))
        self.lineEditTelefono.setObjectName("lineEdit_8")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(500, 240, 131, 28))
        self.btnModificar.setObjectName("btnModificar")
        self.btnAtras = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtras.setGeometry(QtCore.QRect(460, 480, 93, 28))
        self.btnAtras.setObjectName("btnAtras")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.btnBuscar.clicked.connect(self.buscarClienteBD)
        #self.btnEliminar.clicked.connect(self.eliminarCliente)
        self.btnModificar.clicked.connect(self.modificarCliente)
        self.btnAtras.clicked.connect(lambda: self.ejecutarMasOpciones(MainWindow))

        self.rellenarCampos()
        self.desactivarNif()

        
    # Función para conectar con la base de datos
    def establecerConexionBD(self):
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='castelao',
            db='UD02BDReservaCoches')
        
        return conexion
    
    
    # Captura los datos introducidos por el usuario en los distintos campos de texto de la interfaz
    def capturarDatos(self):
        global nifIntro, nombreIntro, primerApellidoIntro, segundoApellidoIntro, calleIntro, numeroIntro, municipioIntro, telefonoIntro, nombreCompleto, direccion

        nifIntro = self.lineEditNif.text()
        nombreIntro = self.lineEditNombre.text()
        primerApellidoIntro = self.lineEditPrimerApellido.text()
        segundoApellidoIntro = self.lineEditSegundoApellido.text()
        calleIntro = self.lineEditCalle.text()
        numeroIntro = self.lineEditNumero.text()
        municipioIntro = self.lineEditMunicipio.text()
        telefonoIntro = self.lineEditTelefono.text()

        nombreCompleto = nombreIntro + " " + primerApellidoIntro + " " + segundoApellidoIntro
        direccion = calleIntro + ", " + numeroIntro + ", " + municipioIntro


    # Deja en blanco todos los campos de texto de la interfaz
    def limpiarCampos(self):
        self.lineEditNif.clear()
        self.lineEditNombre.clear()
        self.lineEditPrimerApellido.clear()
        self.lineEditSegundoApellido.clear()
        self.lineEditCalle.clear()
        self.lineEditNumero.clear()
        self.lineEditMunicipio.clear()
        self.lineEditTelefono.clear()


    def desactivarNif(self):
        self.lineEditNif.setEnabled(False)


    def modificarCliente(self):
        global nombreCompleto, direccion, telefonoIntro, nifIntro
        self.capturarDatos()
        if nombreIntro==dato2 and primerApellidoIntro==dato3 and segundoApellidoIntro==dato4 and calleIntro==dato5 and numeroIntro==dato6 and municipioIntro==dato7 and telefonoIntro==dato8:
            self.lanzarPanelInformativo("No ha modificado ningún dato")
        else:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Confirmar operación')
            box.setText('¿Está seguro de que desea modificar éste cliente?')
            box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            buttonY = box.button(QMessageBox.Yes)
            buttonY.setText('Continuar')
            buttonN = box.button(QMessageBox.No)
            buttonN.setText('Cancelar')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.modificarDatos()


    def modificarDatos(self):
        try:
            conexion = self.establecerConexionBD()
            cur = conexion.cursor()
            sql = "UPDATE clientes SET clNombre = %s, clDireccion = %s, clTelefono = %s WHERE clNif = %s"
            cur.execute(sql, (nombreCompleto, direccion, telefonoIntro, nifIntro))
            conexion.commit()
            self.lanzarPanelInformativo("Se han actualizado los datos correctamente")
        except:
            self.lanzarPanelInformativo("Error al modiicar datos:")
        finally:
            # Cierra la conexión a la base de datos
            cur.close()
            conexion.close()


    # Recibe los datos enviados desde la ventana MasOpciones
    @pyqtSlot(str, str, str, str, str, str, str, str)
    def recibirDatos(self, nif, nombre, primerApellido, segundoApellido, calle, numero, municipio, telefono):
        global dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8

        dato1 = nif
        dato2 = nombre
        dato3 = primerApellido
        dato4 = segundoApellido
        dato5 = calle
        dato6 = numero
        dato7 = municipio
        dato8 = telefono
        """ self.lineEditNif.setText(nif)
        self.lineEditNombre.setText(nombre)
        self.lineEditPrimerApellido.setText(primerApellido)
        self.lineEditSegundoApellido.setText(segundoApellido)
        self.lineEditCalle.setText(calle)
        self.lineEditNumero.setText(numero)
        self.lineEditMunicipio.setText(municipio)
        self.lineEditTelefono.setText(telefono) """


    def verificarEnMySQL(self):
        global existeDni
        nif = self.lineEditNif.text()
        conexion = self.establecerConexionBD()

        try:
            cur = conexion.cursor()
            consulta = "SELECT * FROM clientes WHERE clNif = %s"
            cur.execute(consulta, (nif,))
            resultado = cur.fetchone()

            if resultado:
                existeDni = "true"
            else:
                existeDni = "false"
            
            cur.close()
            conexion.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al consultar la base de datos: {str(e)}")


    def rellenarCampos(self):
        global dato1, dato2, dato3
        self.lineEditNif.setText(dato1)
        self.lineEditNombre.setText(dato2)
        self.lineEditPrimerApellido.setText(dato3)
        self.lineEditSegundoApellido.setText(dato4)
        self.lineEditCalle.setText(dato5)
        self.lineEditNumero.setText(dato6)
        self.lineEditMunicipio.setText(dato7)
        self.lineEditTelefono.setText(dato8)


    # Muestra la ventana MasOpciones
    def mostrarMasOpciones(self):
        from ventanaMasOpciones import masOpciones
        self.ventanaMasOpciones = QtWidgets.QMainWindow()
        self.masOpciones = masOpciones()
        self.masOpciones.setupUi(self.ventanaMasOpciones)
        self.ventanaMasOpciones.show()


    # Muestra la ventana MasOpciones y cierra la anterior
    def ejecutarMasOpciones(self, MainWindow):
        self.mostrarMasOpciones()
        MainWindow.close()


    # Función que lanza un panel para informar u orientar al usuario en lo necesario
    def lanzarPanelInformativo(self, mensaje):
        msgBox = QtWidgets.QMessageBox(self.centralwidget)
        msgBox.setWindowTitle("Información")
        msgBox.setText(mensaje)
        msgBox.exec()


    # Configuramos el título de nuestra ventana y el texto para los botones y para los label
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modificar cliente"))
        self.labelNif.setText(_translate("MainWindow", "NIF"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre"))
        self.labelPrimerApellido.setText(_translate("MainWindow", "Primer apellido"))
        self.labelSegundoApellido.setText(_translate("MainWindow", "Segundo apellido"))
        self.labelCalle.setText(_translate("MainWindow", "Calle"))
        self.labelNumero.setText(_translate("MainWindow", "Número"))
        self.labelMunicipio.setText(_translate("MainWindow", "Municipio"))
        self.labelTelefono.setText(_translate("MainWindow", "Teléfono"))
        #self.btnNuevo.setText(_translate("MainWindow", "Registrar Cliente"))
        #self.btnBuscar.setText(_translate("MainWindow", "Buscar Cliente"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar Cliente"))
        #self.btnEliminar.setText(_translate("MainWindow", "Eliminar Cliente"))
        #self.btnMasOpciones.setText(_translate("MainWindow", "Más Opciones"))
        self.btnAtras.setText(_translate("MainWindow", "Atrás"))


# Arranca la clase, construye la ventana y la muestra
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = modificarCliente()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
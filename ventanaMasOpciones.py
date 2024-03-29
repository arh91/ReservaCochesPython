import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ventanaModificarCliente import modificarCliente
import mysql.connector


class masOpciones(QMainWindow):

    existeDni = False
    botonBuscarClickado = False
    #camposRellenados = False
    data_signal = pyqtSignal(str, str, str, str, str, str, str, str)

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
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(500, 160, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(500, 240, 131, 28))
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(500, 320, 131, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(500, 400, 131, 28))
        self.btnLimpiar.setObjectName("btnLimpiar")
        """ self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(200, 480, 93, 28))
        self.btnOk.setObjectName("btnOk") """
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

        self.btnBuscar.clicked.connect(self.buscarClienteBD)
        self.btnEliminar.clicked.connect(self.eliminarCliente)
        self.btnModificar.clicked.connect(lambda: self.ejecutarFuncionesModificar(MainWindow))
        self.btnAtras.clicked.connect(lambda: self.ejecutarClientes(MainWindow))
        self.btnLimpiar.clicked.connect(self.limpiarCampos)

        self.ventana_modificar = modificarCliente()
        self.data_signal.connect(self.ventana_modificar.recibirDatos)

        
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
        self.nif = self.lineEditNif.text()
        self.nombre = self.lineEditNombre.text()
        self.primerApellido = self.lineEditPrimerApellido.text()
        self.segundoApellido = self.lineEditSegundoApellido.text()
        self.calle = self.lineEditCalle.text()
        self.numero = self.lineEditNumero.text()
        self.municipio = self.lineEditMunicipio.text()
        self.telefono = self.lineEditTelefono.text()

        self.nombreCompleto = self.nombre+(" ")+self.primerApellido+(" ")+self.segundoApellido
        self.direccion = self.calle+(",")+self.numero+(",")+self.municipio
        self.telefonoInt = int(self.telefono)


    # Deja en blanco todos los campos de texto de la interfaz
    def limpiarCampos(self):
        global botonBuscarClickado
        botonBuscarClickado = False
        self.lineEditNif.clear()
        self.lineEditNombre.clear()
        self.lineEditPrimerApellido.clear()
        self.lineEditSegundoApellido.clear()
        self.lineEditCalle.clear()
        self.lineEditNumero.clear()
        self.lineEditMunicipio.clear()
        self.lineEditTelefono.clear()


    # Deshabilita la edición de los campos de texto de la interfaz
    def desactivarCampos(self):
        self.lineEditNif.setEnabled(False)
        self.lineEditNombre.setEnabled(False)
        self.lineEditPrimerApellido.setEnabled(False)
        self.lineEditSegundoApellido.setEnabled(False)
        self.lineEditCalle.setEnabled(False)
        self.lineEditNumero.setEnabled(False)
        self.lineEditMunicipio.setEnabled(False)
        self.lineEditTelefono.setEnabled(False)


    # Habilita la edición de los campos de texto de la interfaz
    def activarCampos(self):
        self.lineEditNif.setEnabled(True)
        self.lineEditNombre.setEnabled(True)
        self.lineEditPrimerApellido.setEnabled(True)
        self.lineEditSegundoApellido.setEnabled(True)
        self.lineEditCalle.setEnabled(True)
        self.lineEditNumero.setEnabled(True)
        self.lineEditMunicipio.setEnabled(True)
        self.lineEditTelefono.setEnabled(True)


    # Función que muestra los datos de un cliente a partir del nif introducido por el usuario
    def buscarClienteBD(self):
        global botonBuscarClickado
        botonBuscarClickado=False
        nif = self.lineEditNif.text()
        if not nif.strip():
            self.lanzarPanelInformativo("Error: no ha introducido el nif del cliente que desea buscar.")
            return
        self.verificarEnMySQL()
        if existeDni == False:
            self.lanzarPanelInformativo("Error: el nif introducido no existe en nuestra base de datos.")
            return
        conexion = self.establecerConexionBD()
        cur = conexion.cursor()
        sql="select * from clientes where clNif = %s"
        cur.execute(sql, (nif,))
        result = cur.fetchall()
        for x in result:
            nombre = x[1]
            direccion = x[2]
            telefono = x[3]
        cur.close()
        conexion.close() 

        separadorNombre = ' '
        separadorDireccion = ','
        nombreCompleto = nombre.split(separadorNombre)
        direccionCompleta = direccion.split(separadorDireccion)

        if len(nombreCompleto) == 2:
            self.lineEditNombre.setText(nombreCompleto[0])
            self.lineEditPrimerApellido.setText(nombreCompleto[1])
            self.lineEditSegundoApellido.setText("")
        else:
            self.lineEditNombre.setText(nombreCompleto[0])
            self.lineEditPrimerApellido.setText(nombreCompleto[1])
            self.lineEditSegundoApellido.setText(nombreCompleto[2])
        
        self.lineEditCalle.setText(direccionCompleta[0])
        self.lineEditNumero.setText(direccionCompleta[1])
        self.lineEditMunicipio.setText(direccionCompleta[2])
        self.lineEditTelefono.setText(str(telefono))
        self.desactivarCampos()
        botonBuscarClickado=True


    # Función que elimina un cliente de la base de datos cuyo dni haya sido introducido por el usuario
    def eliminarCliente(self):
        global botonBuscarClickado
        botonBuscarClickado = False
        nif = self.lineEditNif.text()
        if not nif.strip():
            self.lanzarPanelInformativo("Error: no ha introducido el nif del cliente que desea eliminar!")
            return
        self.verificarEnMySQL()
        if existeDni == "false":
            self.lanzarPanelInformativo("Error: el nif introducido no existe en nuestra base de datos.")
            return
        else:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Confirmar operación')
            box.setText('¿Está seguro de que desea eliminar éste cliente?')
            box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            buttonY = box.button(QMessageBox.Yes)
            buttonY.setText('Continuar')
            buttonN = box.button(QMessageBox.No)
            buttonN.setText('Cancelar')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.eliminar()


    def eliminar(self):
        try:
            conexion = self.establecerConexionBD()
            cur = conexion.cursor()
            sql="delete from clientes where clNif = %s"
            nif= self.lineEditNif.text()
            print(nif)
            cur.execute(sql, (nif,))
            conexion.commit()
            self.lanzarPanelInformativo("El cliente ha sido eliminado de la base de datos")
        except:
            self.lanzarPanelInformativo("Error al eliminar cliente:")
        finally:
            # Cierra la conexión a la base de datos
            cur.close()
            conexion.close()
        

    # Muestra la ventana Clientes y cierra la anterior
    def ejecutarClientes(self, MainWindow):
        global botonBuscarClickado
        botonBuscarClickado = False
        self.mostrarVentanaClientes()
        MainWindow.close()


    def ejecutarFuncionesModificar(self, MainWindow):
        global botonBuscarClickado
        #global camposRellenados
        #self.comprobarCamposRellenados()
        if botonBuscarClickado==True:
            self.enviarDatos()
            self.mostrarVentanaModificar()
            MainWindow.close()
            botonBuscarClickado = False
        else:
            self.lanzarPanelInformativo("Primero busque los datos del cliente que desea modificar, introduciendo su nif y haciendo click en botón Buscar")
            botonBuscarClickado = False


    # Muestra la ventana para modificar datos de clientes
    def mostrarVentanaModificar(self):
        from ventanaModificarCliente import modificarCliente
        self.ventanaModificarCliente = QtWidgets.QMainWindow()
        self.modificarCliente = modificarCliente()
        self.modificarCliente.setupUi(self.ventanaModificarCliente)
        self.ventanaModificarCliente.show()


    # Muestra la ventana Clientes
    def mostrarVentanaClientes(self):
        from ventanaClientes import Clientes
        self.ventanaClientes = QtWidgets.QMainWindow()
        self.clientes = Clientes()
        self.clientes.setupUi(self.ventanaClientes)
        self.ventanaClientes.show()


    # Función que lee el dni introducido por el usuario, luego accede a la base de datos y comprueba que dicho dni exista en la misma
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
                existeDni = True
            else:
                existeDni = False
            
            cur.close()
            conexion.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al consultar la base de datos: {str(e)}")


    # Comprueba que todos los campos de texto estén rellenados
    """ def comprobarCamposRellenados(self):
        global camposRellenados
        # Comprobar si todos los QLineEdit están rellenados
        nif = self.lineEditNif.text()
        nombre = self.lineEditNombre.text()
        primerApellido = self.lineEditPrimerApellido.text()
        segundoApellido = self.lineEditSegundoApellido.text()
        calle = self.lineEditCalle.text()
        numero = self.lineEditNumero.text()
        municipio = self.lineEditMunicipio.text()
        telefono = self.lineEditTelefono.text()

        if nif.strip() and nombre.strip() and primerApellido.strip() and segundoApellido.strip() and calle.strip() and numero.strip() and municipio.strip() and telefono.strip():
            camposRellenados = True
        else:
            camposRellenados = False """


    # Función que lanza un panel para informar u orientar al usuario en lo necesario
    def lanzarPanelInformativo(self, mensaje):
        msgBox = QtWidgets.QMessageBox(self.centralwidget)
        msgBox.setWindowTitle("Información")
        msgBox.setText(mensaje)
        msgBox.exec()


    # Envía los datos de la busqueda a la interfaz de modificarCliente
    def enviarDatos(self):
        nif = self.lineEditNif.text()
        nombre = self.lineEditNombre.text()
        primerApellido = self.lineEditPrimerApellido.text()
        segundoApellido = self.lineEditSegundoApellido.text()
        calle = self.lineEditCalle.text()
        numero = self.lineEditNumero.text()
        municipio = self.lineEditMunicipio.text()
        telefono = self.lineEditTelefono.text()

        self.data_signal.emit(nif, nombre, primerApellido, segundoApellido, calle, numero, municipio, telefono)

    
    # Deja en blanco todos los campos de texto de la interfaz
    def limpiarCampos(self):
        global botonBuscarClickado
        botonBuscarClickado = False
        self.lineEditNif.clear()
        self.lineEditNombre.clear()
        self.lineEditPrimerApellido.clear()
        self.lineEditSegundoApellido.clear()
        self.lineEditCalle.clear()
        self.lineEditNumero.clear()
        self.lineEditMunicipio.clear()
        self.lineEditTelefono.clear()
        self.activarCampos()


    # Configuramos el título de nuestra ventana y el texto para los botones y para los label
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Más Opciones"))
        self.labelNif.setText(_translate("MainWindow", "NIF"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre"))
        self.labelPrimerApellido.setText(_translate("MainWindow", "Primer apellido"))
        self.labelSegundoApellido.setText(_translate("MainWindow", "Segundo apellido"))
        self.labelCalle.setText(_translate("MainWindow", "Calle"))
        self.labelNumero.setText(_translate("MainWindow", "Número"))
        self.labelMunicipio.setText(_translate("MainWindow", "Municipio"))
        self.labelTelefono.setText(_translate("MainWindow", "Teléfono"))
        #self.btnNuevo.setText(_translate("MainWindow", "Registrar Cliente"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar Cliente"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar Cliente"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar Cliente"))
        #self.btnMasOpciones.setText(_translate("MainWindow", "Más Opciones"))
        self.btnAtras.setText(_translate("MainWindow", "Atrás"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar Campos"))


# Arranca la clase, construye la ventana y la muestra
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = masOpciones()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


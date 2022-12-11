from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import threading
from datetime import datetime
import sys
import string

# setting path
sys.path.append('TPFinalMakkBettucci')

# importing

from routers import *

# Esta clase es para ejecutar la opcion 3,4 y 5
class Ui_FormVerConexPorUbicacion(QtWidgets.QMainWindow):   
    valueChanged = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        self.ubicacion = None

    def setupUi(self, Form, ubicacion,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        
        self.ubicacion = ubicacion

        Form.setObjectName("Form")
        Form.resize(559, 323)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.backButton = QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConTexto(self))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        self.backButton.setText(_translate("Form", "Volver"))

        QtCore.QMetaObject.connectSlotsByName(Form)

        if ubicacion == 'provincia':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(40, 160, 151, 16))
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese una provincia:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorProvincia)

        elif ubicacion == 'departamento':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un departamento:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)

        elif ubicacion == 'municipio':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un municipio:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorMunicipio)

        self.valueChanged.connect(self.on_value_changed)
        self.pushButton.clicked.connect(self.on_clicked)

        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    @QtCore.pyqtSlot()
    def on_clicked(self):
        #self.textEdit.clear()
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 140, 100))

        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia, daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento, daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio, daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEdit.append("Conexion: {}".format(value))

    #Funcion que muestra las conexiones por provincia dada
    def mostrarConexionesPorProvincia(self):
        idProvinciaIngresado  = self.textEdit.toPlainText().strip()
        if idProvinciaIngresado not in Provincia.diccionarioProv:
            msg = QMessageBox()
            msg.setInformativeText("No existe la provincia ingresada")
            msg.exec_()
        
        for router in Router.diccionarioRouter.keys():
            if idProvinciaIngresado == Router.diccionarioRouter[router].provinciaID:
                for conexion in Router.diccionarioRouter[router].conexiones:
                    self.valueChanged.emit(conexion)

    #Funcion que muestra las conexiones por departamento dado             
    def mostrarConexionesPorDepartamento(self):
        idDepartamentoIngresado  = self.textEdit.toPlainText().strip()
        if idDepartamentoIngresado not in Departamento.diccionarioDptos:
            msg = QMessageBox()
            msg.setInformativeText("No existe el departamento ingresado")
            msg.exec_()
        
        for router in Router.diccionarioRouter.keys():
            if idDepartamentoIngresado == Router.diccionarioRouter[router].departamentoID:
                for conexion in Router.diccionarioRouter[router].conexiones:
                    self.valueChanged.emit(conexion)
   
    #Funcion que muestra las conexiones por municipio dado
    def mostrarConexionesPorMunicipio(self):
        idMunicipioIngresado = self.textEdit.toPlainText().strip()
        if idMunicipioIngresado not in Municipio.diccionarioMunicipios:
            msg = QMessageBox()
            msg.setInformativeText("No existe el municipio ingresado")
            msg.exec_()
        
        for router in Router.diccionarioRouter.keys():
            if idMunicipioIngresado == Router.diccionarioRouter[router].municipioID:
                for conexion in Router.diccionarioRouter[router].conexiones:
                    self.valueChanged.emit(conexion)

# Para que validar que no pueda apretar el boton seleccionar con un numero (prov, depto, muni)
def botonSeleccionar_enableConTexto(self):  
    text = self.textEdit.toPlainText().strip()
    texto = quitarTildes(text)
    textoFinal = string.capwords(texto)
    #quitar tildes, hacer capitalize
    if len(textoFinal) != 0:
        try:
            #El setProvincias/setDeptos/setMunicipios es extraido de la base de datos nuestra, o sea de las prov que existen en nuestro sistema por el momento
            if textoFinal.isnumeric() == False and (textoFinal in Provincia.setProvincias or textoFinal in Departamento.setDepartamentos or textoFinal in Municipio.setMunicipios):
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
    else:
        self.pushButton.setEnabled(False)

# Funcion para quitar tildes
def quitarTildes(texto):
        replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
        for a, b in replacements:
            texto = texto.replace(a, b).replace(a.upper(), b.upper())
        return texto


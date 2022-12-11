from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import threading
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

    def setupUi(self, Form, ubicacion, secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        self.ubicacion = ubicacion

        Form.setObjectName("Form")
        Form.resize(628, 649)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 550, 50))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout_9")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Seleccionar")

        if ubicacion == 'provincia':
            self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.label.setObjectName("label")
            self.label.setText("Ingrese una provincia:")
            self.horizontalLayout.addWidget(self.label)
            self.pushButton.clicked.connect(self.mostrarConexionesPorProvincia)

            self.verticalLayout.addLayout(self.horizontalLayout)

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(133, 100, 357, 150)

            self.backButton = QPushButton(self.centralwidget)
            self.backButton.setObjectName("backButton")
            self.backButton.setGeometry(133, 260, 357, 30)
            self.backButton.setText("Volver")

            self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEdit.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEdit)
            self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConTexto(self))

            self.horizontalLayout.addWidget(self.pushButton)

        elif ubicacion == 'departamento':
            self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.label.setObjectName("label")
            self.label.setText("Ingrese un departamento:")
            self.horizontalLayout.addWidget(self.label)
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)

            self.verticalLayout.addLayout(self.horizontalLayout)

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(152, 100, 337, 150)

            self.backButton = QPushButton(self.centralwidget)
            self.backButton.setObjectName("backButton")
            self.backButton.setGeometry(152, 260, 337, 30)
            self.backButton.setText("Volver")

            self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEdit.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEdit)
            self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConTexto(self))

            self.horizontalLayout.addWidget(self.pushButton)

        elif ubicacion == 'municipio':
            self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.label.setObjectName("label")
            self.label.setText("Ingrese un municipio:")
            self.horizontalLayout.addWidget(self.label)
            self.pushButton.clicked.connect(self.mostrarConexionesPorMunicipio)

            self.verticalLayout.addLayout(self.horizontalLayout)

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(128, 100, 361, 150)

            self.backButton = QPushButton(self.centralwidget)
            self.backButton.setObjectName("backButton")
            self.backButton.setGeometry(128, 260, 361, 30)
            self.backButton.setText("Volver")

            self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEdit.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEdit)
            self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConTexto(self))

            self.horizontalLayout.addWidget(self.pushButton)

            

        Form.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.valueChanged.connect(self.on_value_changed)
        self.pushButton.clicked.connect(self.on_clicked)

        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    @QtCore.pyqtSlot()
    def on_clicked(self):
        #self.textEdit.clear()
        # self.textEdit.setGeometry(QtCore.QRect(210, 150, 140, 100))

        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia, daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento, daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio, daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEditOutput.append("Conexion: {}".format(value))

    #Funcion que muestra las conexiones por provincia dada
    def mostrarConexionesPorProvincia(self):
        idProvinciaIngresada  = self.textEdit.toPlainText().strip()
        if idProvinciaIngresada not in Provincia.diccionarioProv:
            msg = QMessageBox()
            msg.setInformativeText("No existe la provincia ingresada")
            msg.exec_()
        else:
            for router in Router.diccionarioRouter.keys():
                if idProvinciaIngresada == Router.diccionarioRouter[router].provinciaID:
                    for conexion in Router.diccionarioRouter[router].conexiones.items():
                        self.valueChanged.emit(str(conexion[1].routerID))


    #Funcion que muestra las conexiones por departamento dado             
    def mostrarConexionesPorDepartamento(self):
        idDepartamentoIngresado  = self.textEdit.toPlainText().strip()
        # for provincia in Provincia.diccionarioProv.items():
        #     if idDepartamentoIngresado not in provincia[1].diccionarioDptos.keys():
        if idDepartamentoIngresado not in Departamento.setDepartamentos:
            msg = QMessageBox()
            msg.setInformativeText("No existe el departamento ingresado")
            msg.exec_()
        else:
            for router in Router.diccionarioRouter.keys():
                if idDepartamentoIngresado == Router.diccionarioRouter[router].departamentoID:
                    for conexion in Router.diccionarioRouter[router].conexiones.items():
                        self.valueChanged.emit(str(conexion[1].routerID))

    #Funcion que muestra las conexiones por municipio dado
    def mostrarConexionesPorMunicipio(self):
        idMunicipioIngresado = self.textEdit.toPlainText().strip()
        if idMunicipioIngresado not in Municipio.setMunicipios:
            msg = QMessageBox()
            msg.setInformativeText("No existe el municipio ingresado")
            msg.exec_()
        else:    
            for router in Router.diccionarioRouter.keys():
                if idMunicipioIngresado == Router.diccionarioRouter[router].municipioID:
                    for conexion in Router.diccionarioRouter[router].conexiones.items():
                        self.valueChanged.emit(str(conexion[1].routerID))

# Para que validar que no pueda apretar el boton seleccionar con un numero (prov, depto, muni)
def botonSeleccionar_enableConTexto(self):  
    text = self.textEdit.toPlainText().strip()
    # texto = quitarTildes(text)
    # textoFinal = string.capwords(texto)
    #quitar tildes, hacer capitalize
    if len(text) != 0:
        try:
            #El setProvincias/setDeptos/setMunicipios es extraido de la base de datos nuestra, o sea de las prov que existen en nuestro sistema por el momento
            if text.isnumeric() == False and (text in Provincia.diccionarioProv.keys() or text in Departamento.setDepartamentos or text in Municipio.setMunicipios):
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
    else:
        self.pushButton.setEnabled(False)

# Funcion para quitar tildes
# def quitarTildes(texto):
#         replacements = (
#         ("á", "a"),
#         ("é", "e"),
#         ("í", "i"),
#         ("ó", "o"),
#         ("ú", "u"),
#         )
#         for a, b in replacements:
#             texto = texto.replace(a, b).replace(a.upper(), b.upper())
#         return texto
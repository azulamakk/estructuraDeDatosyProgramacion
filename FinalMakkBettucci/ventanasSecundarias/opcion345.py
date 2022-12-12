from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import threading
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')

# importing

from routers import Router
from municipios import Provincia, Departamento, Municipio

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

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProv")
            self.horizontalLayout.addWidget(self.textEditProv)
            self.textEditProv.textChanged.connect(self.botonSeleccionar_enableConTextoProv)

            self.horizontalLayout.addWidget(self.pushButton)

        elif ubicacion == 'departamento':
            labelProv = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelProv.setObjectName("labelProv")
            labelProv.setText("Ingrese una provincia:")
            self.horizontalLayout.addWidget(labelProv)

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProv")
            self.textEditProv.textChanged.connect(self.botonSeleccionar_enableConTextoDpto)
            self.horizontalLayout.addWidget(self.textEditProv)

            labelDepto = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelDepto.setObjectName("labelDepto")
            labelDepto.setText("Ingrese un departamento:")
            self.horizontalLayout.addWidget(labelDepto)
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)

            self.verticalLayout.addLayout(self.horizontalLayout)

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(152, 100, 337, 150)

            self.backButton = QPushButton(self.centralwidget)
            self.backButton.setObjectName("backButton")
            self.backButton.setGeometry(152, 260, 337, 30)
            self.backButton.setText("Volver")

            self.textEditDepto = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditDepto.setObjectName("textEditDepto")
            self.horizontalLayout.addWidget(self.textEditDepto)
            self.textEditDepto.textChanged.connect(self.botonSeleccionar_enableConTextoDpto)

            self.horizontalLayout.addWidget(self.pushButton)
        elif ubicacion == 'municipio':
            labelProv = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelProv.setObjectName("labelProv")
            labelProv.setText("Ingrese una provincia:")
            self.horizontalLayout.addWidget(labelProv)

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProv")
            self.textEditProv.textChanged.connect(self.botonSeleccionar_enableConTextoMuni)
            self.horizontalLayout.addWidget(self.textEditProv)

            labelDepto = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelDepto.setObjectName("labelDepto")
            labelDepto.setText("Ingrese un departamento:")
            self.horizontalLayout.addWidget(labelDepto)

            self.textEditDepto = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditDepto.setObjectName("textEditDepto")
            self.horizontalLayout.addWidget(self.textEditDepto)
            self.textEditDepto.textChanged.connect(self.botonSeleccionar_enableConTextoMuni)

            labelMuni = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelMuni.setObjectName("label")
            labelMuni.setText("Ingrese un municipio:")
            self.horizontalLayout.addWidget(labelMuni)
            self.pushButton.clicked.connect(self.mostrarConexionesPorMunicipio)

            self.verticalLayout.addLayout(self.horizontalLayout)

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(128, 100, 361, 150)

            self.backButton = QPushButton(self.centralwidget)
            self.backButton.setObjectName("backButton")
            self.backButton.setGeometry(128, 260, 361, 30)
            self.backButton.setText("Volver")

            self.textEditMuni = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditMuni.setObjectName("textEdit")
            self.horizontalLayout.addWidget(self.textEditMuni)
            self.textEditMuni.textChanged.connect(self.botonSeleccionar_enableConTextoMuni)

            self.horizontalLayout.addWidget(self.pushButton)


        Form.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.valueChanged.connect(self.on_value_changed)
        self.pushButton.clicked.connect(self.on_clicked)
        self.pushButton.setEnabled(False)


        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    @QtCore.pyqtSlot()
    def on_clicked(self):
        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia, daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento, daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio, daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEditOutput.append(value)
        

    #Funcion que muestra las conexiones por provincia dada
    def mostrarConexionesPorProvincia(self):
        idProvinciaIngresada = self.textEditProv.toPlainText().strip()
        if idProvinciaIngresada not in Provincia.diccionarioProv:
            msg = QMessageBox()
            msg.setInformativeText("No existe la provincia ingresada")
            msg.exec_()
            return

        for router in Router.diccionarioRouter:
            if idProvinciaIngresada == Router.diccionarioRouter[router].provinciaID:
                for (_, conexion) in Router.diccionarioRouter[router].conexiones.items():
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))


    #Funcion que muestra las conexiones por departamento dado             
    def mostrarConexionesPorDepartamento(self):
        idProvIngresada = self.textEditProv.toPlainText().strip()

        if idProvIngresada not in Provincia.diccionarioProv:
            msg = QMessageBox()
            msg.setInformativeText("No existe la provincia ingresada")
            msg.exec_()
            return
        
        prov = Provincia.diccionarioProv[idProvIngresada]
        idDepartamentoIngresado = self.textEditDepto.toPlainText().strip()
        if idDepartamentoIngresado not in prov.diccionarioDptos:
            msg = QMessageBox()
            msg.setInformativeText("No existe el departamento ingresado")
            msg.exec_()
            return

        for routerId in Router.diccionarioRouter:
            router = Router.diccionarioRouter[routerId]
            if idDepartamentoIngresado == router.departamentoID and idProvIngresada == router.provinciaID:
                for (_, conexion) in router.conexiones.items():
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))

    #Funcion que muestra las conexiones por municipio dado
    def mostrarConexionesPorMunicipio(self):
        idProvIngresada = self.textEditProv.toPlainText().strip()
        if idProvIngresada not in Provincia.diccionarioProv:
            msg = QMessageBox()
            msg.setInformativeText("No existe la provincia ingresada")
            msg.exec_()
            return
        
        prov = Provincia.diccionarioProv[idProvIngresada]
        idDepartamentoIngresado = self.textEditDepto.toPlainText().strip()
        if idDepartamentoIngresado not in prov.diccionarioDptos:
            msg = QMessageBox()
            msg.setInformativeText("No existe el departamento ingresado")
            msg.exec_()
            return
        
        depto = prov.diccionarioDptos[idDepartamentoIngresado]
        idMunicipioIngresado = self.textEditMuni.toPlainText().strip()
        if idMunicipioIngresado not in depto.diccionarioMunicipios:
            msg = QMessageBox()
            msg.setInformativeText("No existe el municipio ingresado")
            msg.exec_()
            return
          
        for routerId in Router.diccionarioRouter.keys():
            router = Router.diccionarioRouter[routerId]
            if idMunicipioIngresado == router.municipioID and idDepartamentoIngresado == router.departamentoID and idProvIngresada == router.provinciaID:
                for (_, conexion) in router.conexiones.items():
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))

    # Para que validar que no pueda apretar el boton seleccionar con un numero (prov, depto, muni)
    def botonSeleccionar_enableConTextoProv(self):  
        text = self.textEditProv.toPlainText().strip()
        if len(text) != 0:
            try:
                if text in Provincia.diccionarioProv:
                    self.pushButton.setEnabled(True)
                else:
                    self.pushButton.setEnabled(False)
            except:
                self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(False)

    def botonSeleccionar_enableConTextoDpto(self):  
        idProv = self.textEditProv.toPlainText().strip()
        try:
            if idProv in Provincia.diccionarioProv:
                prov = Provincia.diccionarioProv[idProv]
                idDepto = self.textEditDepto.toPlainText().strip()
                if idDepto in prov.diccionarioDptos:
                    self.pushButton.setEnabled(True)
                    return
            
            self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)

    def botonSeleccionar_enableConTextoMuni(self):  
        idProv = self.textEditProv.toPlainText().strip()
        try:
            if idProv in Provincia.diccionarioProv:
                prov = Provincia.diccionarioProv[idProv]
                idDepto = self.textEditDepto.toPlainText().strip()
                if idDepto in prov.diccionarioDptos:
                    depto = prov.diccionarioDptos[idDepto]
                    idMuni = self.textEditMuni.toPlainText().strip()
                    if idMuni in depto.diccionarioMunicipios:
                        self.pushButton.setEnabled(True)
                        return
            
            self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
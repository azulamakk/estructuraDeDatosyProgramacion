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

        if ubicacion == 'provincia':

            self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 550, 50))
            self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
            
            self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setObjectName("verticalLayout")

            ### DENTRO DEL LAYOUT ###
            self.horizontalLayoutProvincia = QtWidgets.QHBoxLayout()
            self.horizontalLayoutProvincia.setObjectName("horizontalLayoutProvincia")

            self.labelProvincia = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.labelProvincia.setObjectName("labelProvincia")
            self.labelProvincia.setText("Ingrese una provincia:")
            self.horizontalLayoutProvincia.addWidget(self.labelProvincia)

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProvincia")
            self.textEditProv.setPlaceholderText('AR-[A-Z]')
            self.textEditProv.setTabChangesFocus(True)
            self.horizontalLayoutProvincia.addWidget(self.textEditProv)

            self.verticalLayout.addLayout(self.horizontalLayoutProvincia)

            ## FUERA DEL LAYOUT ###

            self.pushButtonProvincia = QtWidgets.QPushButton(self.centralwidget)
            self.pushButtonProvincia.setObjectName("pushButtonProvincia")
            self.pushButtonProvincia.setGeometry(133, 100, 357, 25)
            self.pushButtonProvincia.setText("Seleccionar")
            
            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setPlaceholderText('Output textbox')
            self.textEditOutput.setTabChangesFocus(True)
            self.textEditOutput.setGeometry(133, 140, 357, 150)

            self.backButtonProvincia = QPushButton(self.centralwidget)
            self.backButtonProvincia.setObjectName("backButtonProvincia")
            self.backButtonProvincia.setGeometry(133, 305, 357, 25)
            self.backButtonProvincia.setText("Volver")

            Form.setCentralWidget(self.centralwidget)

            ## CONNECTS ##
            QtCore.QMetaObject.connectSlotsByName(Form)
            self.textEditProv.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoProv(self.pushButtonProvincia))

            self.valueChanged.connect(self.on_value_changed)
            self.pushButtonProvincia.clicked.connect(self.on_clicked)

            self.backButtonProvincia.clicked.connect(lambda: self.secondWidgetWindow.close())
            
        elif ubicacion == 'departamento':

            self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 550, 100))
            self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
            
            self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setObjectName("verticalLayout")

            ### DENTRO DEL LAYOUT ###

            # PRIMERO ARMAMOS EL HORIZONTAL LAYOUT CON EL INGRESO DE PROVINCIA #
            self.horizontalLayoutProv= QtWidgets.QHBoxLayout()
            self.horizontalLayoutProv.setObjectName("horizontalLayoutDepartamento")

            labelProv = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelProv.setObjectName("labelProv")
            labelProv.setText("Ingrese una provincia:")
            self.horizontalLayoutProv.addWidget(labelProv)

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProv")
            self.textEditProv.setPlaceholderText('AR-[A-Z]')
            self.textEditProv.setTabChangesFocus(True)
            self.horizontalLayoutProv.addWidget(self.textEditProv)

            # SEGUNDO ARMAMOS EL HORIZONTAL LAYOUT CON EL INGRESO DE DEPARTAMENTO #

            self.horizontalLayoutDepartamento = QtWidgets.QHBoxLayout()
            self.horizontalLayoutDepartamento.setObjectName("horizontalLayoutDepartamento")

            labelDepto = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelDepto.setObjectName("labelDepto")
            labelDepto.setText("Ingrese un departamento:")
            self.horizontalLayoutDepartamento.addWidget(labelDepto)

            self.textEditDepto = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditDepto.setObjectName("textEditDepto")
            self.textEditDepto.setPlaceholderText('0000')
            self.textEditDepto.setTabChangesFocus(True)
            self.horizontalLayoutDepartamento.addWidget(self.textEditDepto)

            # AÑADIMOS EL HORIZONTAL LAYOUT DE  DEPARTAMENTO Y PROVINCIA AL VERTICAL LAYOUT #

            self.verticalLayout.addLayout(self.horizontalLayoutProv)
            self.verticalLayout.addLayout(self.horizontalLayoutDepartamento)

            ### FUERA DEL LAYOUT ###

            self.pushButtonDepartamento = QtWidgets.QPushButton(self.centralwidget)
            self.pushButtonDepartamento.setObjectName("pushButtonDepartamento")
            self.pushButtonDepartamento.setGeometry(152, 150, 337, 30)
            self.pushButtonDepartamento.setText("Seleccionar")

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(152, 190, 337, 150)
            self.textEditOutput.setPlaceholderText('Output textbox')
            self.textEditOutput.setTabChangesFocus(True)

            self.backButtonDepartamento = QPushButton(self.centralwidget)
            self.backButtonDepartamento.setObjectName("backButton")
            self.backButtonDepartamento.setGeometry(152, 350, 337, 30)
            self.backButtonDepartamento.setText("Volver")

            Form.setCentralWidget(self.centralwidget)

            ## CONNECTS ##
            QtCore.QMetaObject.connectSlotsByName(Form)

            self.textEditProv.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoProv(self.pushButtonDepartamento))
            self.textEditDepto.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoDpto(self.pushButtonDepartamento))
            
            self.valueChanged.connect(self.on_value_changed)
            self.pushButtonDepartamento.clicked.connect(self.on_clicked)

            self.backButtonDepartamento.clicked.connect(lambda: self.secondWidgetWindow.close())

        elif ubicacion == 'municipio':

            self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 550, 120))
            self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
            
            self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setObjectName("verticalLayout")
            
            ### DENTRO DEL LAYOUT ###

            # PRIMERO ARMAMOS EL HORIZONTAL LAYOUT CON EL INGRESO DE PROVINCIA #

            self.horizontalLayoutProvincia = QtWidgets.QHBoxLayout()
            self.horizontalLayoutProvincia.setObjectName("horizontalLayout_9")
            
            labelProv = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelProv.setObjectName("labelProv")
            labelProv.setText("Ingrese una provincia:")
            self.horizontalLayoutProvincia.addWidget(labelProv)

            self.textEditProv = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditProv.setObjectName("textEditProv")
            self.textEditProv.setPlaceholderText('AR-[A-Z]')
            self.textEditProv.setTabChangesFocus(True)
            self.horizontalLayoutProvincia.addWidget(self.textEditProv)

            # SEGUNDO ARMAMOS EL HORIZONTAL LAYOUT CON EL INGRESO DE DEPARTAMENTO #

            self.horizontalLayoutDepartamento = QtWidgets.QHBoxLayout()
            self.horizontalLayoutDepartamento.setObjectName("horizontalLayoutDepartamento")

            labelDepto = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelDepto.setObjectName("labelDepto")
            labelDepto.setText("Ingrese un departamento:")
            self.horizontalLayoutDepartamento.addWidget(labelDepto)

            self.textEditDepto = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditDepto.setObjectName("textEditDepto")
            self.textEditDepto.setPlaceholderText('0000')
            self.textEditDepto.setTabChangesFocus(True)
            self.horizontalLayoutDepartamento.addWidget(self.textEditDepto)

            # TERCERO ARMAMOS EL HORIZONTAL LAYOUT CON EL INGRESO DE MUNICIPIO #

            self.horizontalLayoutMunicipio = QtWidgets.QHBoxLayout()
            self.horizontalLayoutMunicipio.setObjectName("horizontalLayoutMunicipio")

            labelMuni = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelMuni.setObjectName("label")
            labelMuni.setText("Ingrese un municipio:")
            self.horizontalLayoutMunicipio.addWidget(labelMuni)

            self.textEditMuni = QtWidgets.QTextEdit(self.verticalLayoutWidget)
            self.textEditMuni.setObjectName("textEdit")
            self.textEditMuni.setPlaceholderText('ABC123-01')
            self.textEditMuni.setTabChangesFocus(True)
            self.horizontalLayoutMunicipio.addWidget(self.textEditMuni)

            # AGREGAMOS LOS HORIZONTAL LAYOUTS AL VERTICAL LAYOUT #
            self.verticalLayout.addLayout(self.horizontalLayoutProvincia)
            self.verticalLayout.addLayout(self.horizontalLayoutDepartamento)
            self.verticalLayout.addLayout(self.horizontalLayoutMunicipio)

            ### FUERA DEL LAYOUT ###

            self.pushButtonMunicipio = QtWidgets.QPushButton(self.centralwidget)
            self.pushButtonMunicipio.setObjectName("pushButton")
            self.pushButtonMunicipio.setGeometry(128, 170, 361, 30)
            self.pushButtonMunicipio.setText("Seleccionar")

            self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.textEditOutput.setObjectName("textEditOutput")
            self.textEditOutput.setGeometry(128, 210, 361, 150)
            self.textEditOutput.setTabChangesFocus(True)
            self.textEditOutput.setPlaceholderText('Output textbox')

            self.backButtonMunicipio = QPushButton(self.centralwidget)
            self.backButtonMunicipio.setObjectName("backButtonMunicipio")
            self.backButtonMunicipio.setGeometry(128, 370, 361, 30)
            self.backButtonMunicipio.setText("Volver")

            Form.setCentralWidget(self.centralwidget)

            ## CONNECTS ##
            self.textEditProv.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoProv(self.pushButtonMunicipio))
            self.textEditDepto.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoDpto(self.pushButtonMunicipio))
            self.textEditMuni.textChanged.connect(lambda: self.botonSeleccionar_enableConTextoMuni(self.pushButtonMunicipio))

            QtCore.QMetaObject.connectSlotsByName(Form)
            self.valueChanged.connect(self.on_value_changed)
            self.pushButtonMunicipio.clicked.connect(self.on_clicked)

            # self.textEditProv.installEventFilter(self)
            # self.textEditDepto.installEventFilter(self)
            # self.textEditMuni.installEventFilter(self)

            self.backButtonMunicipio.clicked.connect(lambda: self.secondWidgetWindow.close())

    # def eventFilter(self, obj, event):
    #     if event.type() == QtCore.QEvent.KeyPress and obj is self.textEditMuni:
    #         if event.key() == QtCore.Qt.Key_Return and self.textEditMuni.hasFocus():
    #             print('Enter pressed')
    #             self.mostrarConexionesPorMunicipio()
    #     return super().eventFilter(obj, event)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia(), daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento(), daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio(), daemon=True).start()

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
        cantProv=0
        for router in Router.diccionarioRouter:
            if idProvinciaIngresada == Router.diccionarioRouter[router].provinciaID:
                for (_, conexion) in Router.diccionarioRouter[router].conexiones.items():
                    cantProv+=1
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))
        msg = QMessageBox()
        msg.setInformativeText("Cantidad total de conexiones de provincia {}: {}".format(idProvinciaIngresada,cantProv))
        msg.exec_()

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

        cantDpto = 0
        for routerId in Router.diccionarioRouter:
            router = Router.diccionarioRouter[routerId]
            if idDepartamentoIngresado == router.departamentoID and idProvIngresada == router.provinciaID:
                for (_, conexion) in router.conexiones.items():
                    cantDpto+=1
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))
        msg = QMessageBox()
        msg.setInformativeText("Cantidad total de conexiones de departamento {} de provincia {}: {}".format(idDepartamentoIngresado,idProvIngresada,cantDpto))
        msg.exec_()
                    

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
        
        cantMuni = 0
        for routerId in Router.diccionarioRouter.keys():
            router = Router.diccionarioRouter[routerId]
            if idMunicipioIngresado == router.municipioID and idDepartamentoIngresado == router.departamentoID and idProvIngresada == router.provinciaID:
                for (_, conexion) in router.conexiones.items():
                    cantMuni+=1
                    self.valueChanged.emit("MAC: {}, IP: {}".format(conexion.direccionMAC, conexion.direccionIP))
        msg = QMessageBox()
        msg.setInformativeText("Cantidad total de conexiones de municipio {}, departamento {}, provincia {}: {}".format(idMunicipioIngresado,idDepartamentoIngresado, idProvIngresada,cantMuni))
        msg.exec_()

    # Para que validar que no pueda apretar el boton seleccionar con un numero (prov, depto, muni)
    def botonSeleccionar_enableConTextoProv(self,boton):  
        text = self.textEditProv.toPlainText().strip()
        if len(text) != 0:
            try:
                if text in Provincia.diccionarioProv:
                    boton.setEnabled(True)
                else:
                    boton.setEnabled(False)
            except:
                boton.setEnabled(False)
        else:
            boton.setEnabled(False)

    def botonSeleccionar_enableConTextoDpto(self,boton):  
        idProv = self.textEditProv.toPlainText().strip()
        try:
            if idProv in Provincia.diccionarioProv:
                prov = Provincia.diccionarioProv[idProv]
                idDepto = self.textEditDepto.toPlainText().strip()
                if idDepto in prov.diccionarioDptos:
                    boton.setEnabled(True)
                    return
            
            boton.setEnabled(False)
        except:
            boton.setEnabled(False)

    def botonSeleccionar_enableConTextoMuni(self,boton):  
        idProv = self.textEditProv.toPlainText().strip()
        try:
            if idProv in Provincia.diccionarioProv:
                prov = Provincia.diccionarioProv[idProv]
                idDepto = self.textEditDepto.toPlainText().strip()
                if idDepto in prov.diccionarioDptos:
                    depto = prov.diccionarioDptos[idDepto]
                    idMuni = self.textEditMuni.toPlainText().strip()
                    if idMuni in depto.diccionarioMunicipios:
                        boton.setEnabled(True)
                        return
            
            boton.setEnabled(False)
        except:
            boton.setEnabled(False)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import re
import threading
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from routers import Router

# Esta clase es para ejecutar la opcion 7
class Ui_FormAgregarRouter(QMainWindow):
    valueChanged = QtCore.pyqtSignal(str)
    diccionarioObjetos = dict()
    
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, MainWindow,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Opcion ingresada: Agregar Router")
        MainWindow.resize(628, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 40, 391, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Ingreso de ID
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.labelIngresoID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoID.setObjectName("labelIngresoID")
        self.horizontalLayout_9.addWidget(self.labelIngresoID)

        self.textEditID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditID.setObjectName("textEditID")
        self.textEditID.setPlaceholderText('000/0000')
        self.textEditID.setTabChangesFocus(True)
        self.horizontalLayout_9.addWidget(self.textEditID)

        self.verticalLayout.addLayout(self.horizontalLayout_9)
        ###

        #Ingreso de identificador
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.labelIdentificador = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIdentificador.setObjectName("labelIdentificador")
        self.horizontalLayout.addWidget(self.labelIdentificador)

        self.textEditIdentificador = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditIdentificador.setObjectName("textEdit")
        self.textEditIdentificador.setPlaceholderText('ABC123-01')
        self.textEditIdentificador.setTabChangesFocus(True)
        self.horizontalLayout.addWidget(self.textEditIdentificador)

        self.verticalLayout.addLayout(self.horizontalLayout)
        ###

        #Ingreso de ubicacion
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.labelIngresoUbicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoUbicacion.setObjectName("labelIngresoUbicacion")
        self.horizontalLayout_8.addWidget(self.labelIngresoUbicacion)

        self.textEditUbicacion = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditUbicacion.setObjectName("textEditUbicacion")
        self.textEditUbicacion.setPlaceholderText('XXXXX')
        self.textEditUbicacion.setTabChangesFocus(True)
        self.horizontalLayout_8.addWidget(self.textEditUbicacion)

        self.verticalLayout.addLayout(self.horizontalLayout_8)
        ###

        #Ingreso de latitud
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.labelIngresoLatitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoLatitud.setObjectName("labelIngresoLatitud")
        self.horizontalLayout_10.addWidget(self.labelIngresoLatitud)

        self.textEditLatitud = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditLatitud.setObjectName("textEditLatitud")
        self.textEditLatitud.setPlaceholderText('(-)XX.XXXXXX')
        self.textEditLatitud.setTabChangesFocus(True)
        self.horizontalLayout_10.addWidget(self.textEditLatitud)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        ###

        #Ingreso de longitud
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.labelIngresoLongitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoLongitud.setObjectName("labelIngresoLongitud")
        self.horizontalLayout_11.addWidget(self.labelIngresoLongitud)

        self.textEditLongitud = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditLongitud.setObjectName("textEditLongitud")
        self.textEditLongitud.setPlaceholderText('(-)XX.XXXXXX')
        self.textEditLongitud.setTabChangesFocus(True)
        self.horizontalLayout_11.addWidget(self.textEditLongitud)

        self.verticalLayout.addLayout(self.horizontalLayout_11)
        ###

        #Ingreso de municipio ID
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.labelIngresoMuniID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoMuniID.setObjectName("labelIngresoMuniID")
        self.horizontalLayout_12.addWidget(self.labelIngresoMuniID)

        self.textEditMuniID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditMuniID.setObjectName("textEditMuniID")
        self.textEditMuniID.setPlaceholderText('ABC123')
        self.textEditMuniID.setTabChangesFocus(True)
        self.horizontalLayout_12.addWidget(self.textEditMuniID)

        self.verticalLayout.addLayout(self.horizontalLayout_12)
        ###

        #Ingreso de provincia ID
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.labelIngresoProvID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoProvID.setObjectName("labelIngresoProvID")
        self.horizontalLayout_13.addWidget(self.labelIngresoProvID)

        self.textEditProvID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditProvID.setObjectName("textEditProvID")
        self.textEditProvID.setPlaceholderText('AR-[A-Z]')
        self.textEditProvID.setTabChangesFocus(True)
        self.horizontalLayout_13.addWidget(self.textEditProvID)

        self.verticalLayout.addLayout(self.horizontalLayout_13)
        ###
        
        #Ingreso de departamento ID
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.labelIngresoDeptoID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoDeptoID.setObjectName("labelIngresoDeptoID")
        self.horizontalLayout_14.addWidget(self.labelIngresoDeptoID)

        self.textEditDeptoID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditDeptoID.setObjectName("textEditDeptoID")
        self.textEditDeptoID.setPlaceholderText('0000')
        self.textEditDeptoID.setTabChangesFocus(True)
        self.horizontalLayout_14.addWidget(self.textEditDeptoID)
    
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        ###

        # Push button de ingreso de datos
        self.botonIngresoDatos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonIngresoDatos.setObjectName("botonIngresoDatos")
        self.verticalLayout.addWidget(self.botonIngresoDatos)
        ###

        # Back button para volver al menu principal
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("pushButton")
        self.backButton.setText("Volver")
        self.backButton.setGeometry(100, 570, 400, 25)
        ###

        #Text box para mostrar el output de la funcion
        self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOutput.setObjectName("textEditOutput")
        self.textEditOutput.setGeometry(100, 450, 400, 110)
        self.textEditOutput.setPlaceholderText('Output textbox')
        self.textEditOutput.setTabChangesFocus(True)
        #self.verticalLayout.addWidget(self.textEditOutput)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Valido que el ID sea un valor numerico
        self.textEditID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([0-9]{3,4})',self.textEditID) if self.textEditID.toPlainText().isnumeric() == True else self.botonIngresoDatos.setEnabled(False))

        #Valido que el identificador tenga un patron tipo ABC123-01
        self.textEditIdentificador.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{3})([0-9]{3})-([0-9]{2})',self.textEditIdentificador))
        
        #Valido que la ubicacion sea un texto
        self.textEditUbicacion.textChanged.connect(lambda: self.botonIngresoDatos.setEnabled(True) if self.textEditUbicacion.toPlainText().isnumeric() == False else self.botonIngresoDatos.setEnabled(False))
        
        #Valido que la latitud sea un float
        if self.textEditLatitud.toPlainText().isnumeric() == True:
            self.textEditLatitud.textChanged.connect(lambda: self.botonIngresoDatos.setEnabled(True) if isinstance(self.textEditLatitud,float) == False else self.botonIngresoDatos.setEnabled(False))
        
        #Valido que la longitud sea un float
        if self.textEditLongitud.toPlainText().isnumeric() == True:
            self.textEditLongitud.textChanged.connect(lambda: self.botonIngresoDatos.setEnabled(True) if isinstance(self.textEditLongitud,float) == False else self.botonIngresoDatos.setEnabled(False))
        
        #Valido que municipio ID tenga un patron tipo ABC123
        self.textEditMuniID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{3})([0-9]{3})', self.textEditMuniID))
        
        #Valido que provinciaID tenga un patron AR-X
        self.textEditProvID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{2})-([A-Z])', self.textEditProvID))
        
        #Valido que dptoId tenga un patron de 4 numeros
        self.textEditDeptoID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([0-9]{4})', self.textEditDeptoID))
        
        self.valueChanged.connect(self.on_value_changed)
        self.botonIngresoDatos.clicked.connect(self.on_clicked)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.labelIngresoMuniID.setText(_translate("MainWindow", "Ingresar municipio ID:"))
        self.labelIngresoLongitud.setText(_translate("MainWindow", "Ingresar longitud:"))
        self.botonIngresoDatos.setText(_translate("MainWindow", "Ingresar datos del router nuevo"))
        self.labelIngresoDeptoID.setText(_translate("MainWindow", "Ingresar departamento ID:"))
        self.labelIngresoProvID.setText(_translate("MainWindow", "Ingresar provincia ID:"))
        self.labelIdentificador.setText(_translate("MainWindow", "Ingresar identificador:"))
        self.labelIngresoID.setText(_translate("MainWindow", "Ingresar ID:"))
        self.labelIngresoUbicacion.setText(_translate("MainWindow", "Ingresar ubicacion:"))
        self.labelIngresoLatitud.setText(_translate("MainWindow", "Ingresar latitud:"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        threading.Thread(target=self.funcionAgregarRouter(), daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEditOutput.append(value)

    def funcionAgregarRouter(self):
        try:
            id=int(self.textEditID.toPlainText())
            identificador=self.textEditIdentificador.toPlainText()
            ubicacion=self.textEditUbicacion.toPlainText()
            latitud=float(self.textEditLatitud.toPlainText())
            longitud=float(self.textEditLongitud.toPlainText())
            municipioID=self.textEditMuniID.toPlainText()
            provinciaID=self.textEditProvID.toPlainText()
            departamentoID=self.textEditDeptoID.toPlainText()
            router = Router(id,identificador,ubicacion,latitud,longitud,municipioID,provinciaID,departamentoID)
            self.valueChanged.emit(str(router))
            msg = QMessageBox()
            msg.setInformativeText("Router agregado correctamente")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setInformativeText("Error al agregar el router")
            msg.exec_()

    #Regex para activar o desactivar un boton cuando se intenta ingresar un router ID o direccion IP
    def botonSeleccionar_enableConAlfanumerico(self, pattern, textEdit):
        text = textEdit.toPlainText()
        if len(text) != 0:
            try:
                if re.fullmatch(pattern,text):
                    self.botonIngresoDatos.setEnabled(True)
                else:
                    self.botonIngresoDatos.setEnabled(False)
            except:
                self.botonIngresoDatos.setEnabled(False)
        else:
            self.botonIngresoDatos.setEnabled(False)
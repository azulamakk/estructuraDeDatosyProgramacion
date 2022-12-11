from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import re

# Esta clase es para ejecutar la opcion 7
class Ui_FormAgregarRouter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Opcion ingresada: Añadir router")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
 
        self.diccionarioObjetos = dict()

        #Ingresar id
        self.HlayoutID = QtWidgets.QHBoxLayout()

        self.labelID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelID.setObjectName('labelIngresoID')
        self.labelID.setText('Ingresar id: ')
        self.HlayoutID.addWidget(self.labelID)

        self.textEditID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditID.setObjectName("textEditIngresoID")
        self.HlayoutID.addWidget(self.textEditID)        

        self.verticalLayout.addLayout(self.HlayoutID)

        #Ingresar identificador
        self.HlayoutIdentificador = QtWidgets.QHBoxLayout()

        self.labelIdentificador = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIdentificador.setObjectName('labelIngresoIdentificador')
        self.labelIdentificador.setText('Ingresar identificador: ')
        self.HlayoutIdentificador.addWidget(self.labelIdentificador)

        self.textEditIdentificador = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditIdentificador.setObjectName("textEditIngresoIdentificador")
        self.HlayoutIdentificador.addWidget(self.textEditIdentificador)        

        self.verticalLayout.addLayout(self.HlayoutIdentificador)

        #Ingresar ubicacion
        self.HlayoutUbicacion = QtWidgets.QHBoxLayout()

        self.labelUbicacion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelUbicacion.setObjectName('labelIngresoUbicacion')
        self.labelUbicacion.setText('Ingresar ubicacion: ')
        self.HlayoutUbicacion.addWidget(self.labelUbicacion)

        self.textEditUbicacion = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditUbicacion.setObjectName("textEditIngresoUbicacion")
        self.HlayoutUbicacion.addWidget(self.textEditUbicacion)        

        self.verticalLayout.addLayout(self.HlayoutUbicacion)

        #Ingresar latitud
        self.HlayoutLatitud = QtWidgets.QHBoxLayout()

        self.labelLatitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelLatitud.setObjectName('labelIngresoLatitud')
        self.labelLatitud.setText('Ingresar latitud: ')
        self.HlayoutLatitud.addWidget(self.labelLatitud)

        self.textEditLatitud = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditLatitud.setObjectName("textEditIngresoLatitud")
        self.HlayoutLatitud.addWidget(self.textEditLatitud)        

        self.verticalLayout.addLayout(self.HlayoutLatitud)

        #Ingresar longitud
        self.HlayoutLongitud = QtWidgets.QHBoxLayout()

        self.labelLongitud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelLongitud.setObjectName('labelIngresoLongitud')
        self.labelLongitud.setText('Ingresar longitud: ')
        self.HlayoutLongitud.addWidget(self.labelLongitud)

        self.textEditLongitud = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditLongitud.setObjectName("textEditIngresoLongitud")
        self.HlayoutLongitud.addWidget(self.textEditLongitud)        

        #Ingresar municipio ID
        self.HlayoutMuniID = QtWidgets.QHBoxLayout()

        self.labelMuniID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelMuniID.setObjectName('labelIngresoMuniID')
        self.labelMuniID.setText('Ingresar municipio ID: ')
        self.HlayoutMuniID.addWidget(self.labelMuniID)

        self.textEditMuniID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditMuniID.setObjectName("textEditIngresoMuniID")
        self.HlayoutMuniID.addWidget(self.textEditMuniID)        

        self.verticalLayout.addLayout(self.HlayoutMuniID)

        #Ingresar provincia ID
        self.HlayoutProvID = QtWidgets.QHBoxLayout()

        self.labelProvID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelProvID.setObjectName('labelIngresoProvID')
        self.labelProvID.setText('Ingresar provincia ID: ')
        self.HlayoutProvID.addWidget(self.labelProvID)

        self.textEditProvID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditProvID.setObjectName("textEditIngresoProvinciaID")
        self.HlayoutProvID.addWidget(self.textEditProvID)        

        self.verticalLayout.addLayout(self.HlayoutProvID)

        #Ingresar departamento ID
        self.HlayoutDptoID = QtWidgets.QHBoxLayout()

        self.labelDptoID = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDptoID.setObjectName('labelIngresoDptoID')
        self.labelDptoID.setText('Ingresar departamento ID: ')
        self.HlayoutDptoID.addWidget(self.labelDptoID)

        self.textEditDptoID = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditDptoID.setObjectName("textEditIngresoDptoID")
        self.HlayoutDptoID.addWidget(self.textEditDptoID)        

        self.verticalLayout.addLayout(self.HlayoutDptoID)

        # Push button para seleccionar el ID escrito
        # Aca validar si no existe ya el router, blockear el boton de seleccionar o enviar un mensaje en rojo "eliga nu router no repetido"
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Agregar router")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Valido que el ID sea un valor numerico
        self.textEditID.textChanged.connect(lambda: self.pushButton.setEnabled(True) if self.textEditID.toPlainText().isnumeric() == True else self.pushButton.setEnabled(False))
        
        #Valido que el identificador tenga un patron tipo ABC123-01
        self.textEditIdentificador.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{3})([0-9]{3})-([0-9]{2})',self.textEditIdentificador))
        
        #Valido que la ubicacion sea un texto
        self.textEditUbicacion.textChanged.connect(lambda: self.pushButton.setEnabled(True) if self.textEditUbicacion.toPlainText().isnumeric() == False else self.pushButton.setEnabled(False))
        
        #Valido que la latitud sea un float
        if self.textEditLatitud.toPlainText().isnumeric() == True:
            self.textEditLatitud.textChanged.connect(lambda: self.pushButton.setEnabled(True) if isinstance(self.textEditLatitud,float) == False else self.pushButton.setEnabled(False))
        
        #Valido que la longitud sea un float
        if self.textEditLongitud.toPlainText().isnumeric() == True:
            self.textEditLongitud.textChanged.connect(lambda: self.pushButton.setEnabled(True) if isinstance(self.textEditLongitud,float) == False else self.pushButton.setEnabled(False))
        
        #Valido que municipio ID tenga un patron tipo ABC123
        self.textEditMuniID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{3})([0-9]{3})',self.textEditMuniID))
        
        #Valido que provinciaID tenga un patron AR-X
        self.textEditProvID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{2})-([A-Z])',self.textEditProvID))
        
        #Valido que dptoId tenga un patron de 4 numeros
        self.textEditDptoID.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([0-9]{4})',self.textEditDptoID))

        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter())


    def funcionAgregarRouter(self):       
        
        self.diccionarioObjetos['Id: '] = self.textEditID.toPlainText()
        self.diccionarioObjetos['Identificador: '] = self.textEditIdentificador.toPlainText()
        self.diccionarioObjetos['Ubicacion: '] = self.textEditUbicacion.toPlainText()
        self.diccionarioObjetos['Latitud: '] = self.textEditLatitud.toPlainText()
        self.diccionarioObjetos['Longitud: '] = self.textEditLongitud.toPlainText()
        self.diccionarioObjetos['Municipio ID: '] = self.textEditMuniID.toPlainText()
        self.diccionarioObjetos['Provincia ID: '] = self.textEditProvID.toPlainText()
        self.diccionarioObjetos['Departamento ID: '] = self.textEditDptoID.toPlainText()

        for k,v in self.diccionarioObjetos.items():
            print('{}{}'.format(k,v))

        msg = QMessageBox()
        msg.setInformativeText("Router agregado correctamente")
        msg.exec_()

    #Regex para activar o desactivar un boton cuando se intenta ingresar un router ID o direccion IP
    def botonSeleccionar_enableConAlfanumerico(self, pattern, textEdit):
        text = textEdit.toPlainText()
        if len(text) != 0:
            try:
                if re.fullmatch(pattern,text):
                    self.pushButton.setEnabled(True)
                else:
                    self.pushButton.setEnabled(False)
            except:
                self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(False)
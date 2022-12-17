from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

import sys
# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from conexiones import Conexion
from routers import Router

# Esta clase es para ejecutar la opcion 9
class Ui_FormAgregarConexion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Opcion ingresada: Agregar conexion")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 421, 280))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.diccionarioObjetos = dict()

        self.agregarObjetos('Direccion IP')
        self.agregarObjetos('MAC Address')
        self.agregarObjetos('Fecha')
        self.agregarObjetos('Horario')
        self.agregarObjetos('Activa')
        self.agregarObjetos('Router ID')


        # Push button para seleccionar el ID escrito
        # Aca validar si no existe ya el router, blockear el boton de seleccionar o enviar un mensaje en rojo "eliga nu router no repetido"
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Agregar conexion")
        self.verticalLayout.addWidget(self.pushButton)

        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("pushButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionAgregarConexion())

        # Text box y su label para ingresar por teclado el router ID
    def agregarObjetos(self, campo):
        Hlayout = QtWidgets.QHBoxLayout()
        Hlayout.setObjectName("Hlayout{}".format(campo))

        label = QtWidgets.QLabel(self.verticalLayoutWidget)
        label.setObjectName(campo)
        label.setText("{}:".format(campo))
        Hlayout.addWidget(label)

        textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        textEdit.setObjectName("textEdit{}".format(campo))
        textEdit.setTabChangesFocus(True)

        if campo == 'Direccion IP':
            textEdit.setPlaceholderText('ABC123-01')
        elif campo == 'MAC Address':
            textEdit.setPlaceholderText('0000000')
        elif campo == 'Fecha':
            textEdit.setPlaceholderText('dd/mm/aaaa')
        elif campo == 'Horario':
            textEdit.setPlaceholderText('hh:mm:ss')
        elif campo == 'Activa':
            textEdit.setPlaceholderText('0 o 1')
        else: #Router ID
            textEdit.setPlaceholderText('ABC123-01')

        Hlayout.addWidget(textEdit)        

        self.diccionarioObjetos[label.objectName()] = ''
        self.verticalLayout.addLayout(Hlayout)

        textEdit.textChanged.connect(lambda: self.funcionGuardarDatos(textEdit, label))
    
    def funcionGuardarDatos(self,textEdit,label):
        self.diccionarioObjetos[label.objectName()] = textEdit.toPlainText()

    def funcionAgregarConexion(self):            
        for k,v in self.diccionarioObjetos.items():
            print('{}: {}'.format(k,v))
        
        ip = self.diccionarioObjetos['Direccion IP']
        mac = self.diccionarioObjetos['MAC Address']
        fecha = self.diccionarioObjetos['Fecha']
        horario = self.diccionarioObjetos['Horario']
        activa = self.diccionarioObjetos['Activa']
        routerID = self.diccionarioObjetos['Router ID']
        try:
            if routerID not in Router.diccionarioRouter:
                raise Exception("el router no existe")
            conexion = Conexion(ip,mac,fecha,horario,activa,routerID)
            router = Router.diccionarioRouter[routerID]
            router.agregarConexion(conexion)
            print(conexion)
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setInformativeText("Error al agregar la conexion " + str(e))
            msg.exec_()
            return

        msg = QMessageBox()
        msg.setInformativeText("Conexion agregada correctamente")
        msg.exec_()
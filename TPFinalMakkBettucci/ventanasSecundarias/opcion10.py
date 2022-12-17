from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import re
import sys
# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from routers import Router
from conexiones import Conexion

# Esta clase es para ejecutar la opcion 10
class Ui_FormEliminarConexion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Opcion ingresada: Eliminar conexion")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 435, 150))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        # Text box y su label para ingresar por teclado el router ID (en el horizontal layout Router)
        self.horizontalLayoutRouter = QtWidgets.QHBoxLayout()

        labelRouter = QtWidgets.QLabel(self.verticalLayoutWidget)
        labelRouter.setObjectName('labelIngresoRouterID')
        labelRouter.setText('Ingresar ID router: ')
        self.horizontalLayoutRouter.addWidget(labelRouter)

        self.textEditRouter = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditRouter.setObjectName("textEditRouter")
        self.textEditRouter.setPlaceholderText('ABC123-01')
        self.textEditRouter.setTabChangesFocus(True)
        self.horizontalLayoutRouter.addWidget(self.textEditRouter)     

        self.verticalLayout.addLayout(self.horizontalLayoutRouter)

        # Text box y su label para ingresar por teclado el MAC Address (en el horizontal layout MAC)
        self.horizontalLayoutMAC = QtWidgets.QHBoxLayout()

        labelMAC = QtWidgets.QLabel(self.verticalLayoutWidget)
        labelMAC.setObjectName('labelIngresoMAC')
        labelMAC.setText('Ingresar MAC: ')
        self.horizontalLayoutMAC.addWidget(labelMAC)

        self.textEditMAC = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditMAC.setObjectName("textEditMAC")
        self.textEditMAC.setPlaceholderText('0000000')
        self.textEditMAC.setTabChangesFocus(True)
        self.horizontalLayoutMAC.addWidget(self.textEditMAC)      

        self.verticalLayout.addLayout(self.horizontalLayoutMAC)

        ### BOTONES EN EL VERTICAL LAYOUT ###

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar conexion")
        self.verticalLayout.addWidget(self.pushButton)

        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("pushButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.setEnabled(False)
        
        self.textEditRouter.textChanged.connect(lambda: self.botonSeleccionar_enable('^([A-Z]{3})([0-9]{3})-([0-9]{2})',self.textEditRouter,'^([0-9]{7})',self.textEditMAC))
        self.textEditMAC.textChanged.connect(lambda: self.botonSeleccionar_enable('^([A-Z]{3})([0-9]{3})-([0-9]{2})',self.textEditRouter,'^([0-9]{7})',self.textEditMAC))

        self.pushButton.clicked.connect(lambda: self.funcionEliminarConexion())

    def botonSeleccionar_enable(self, patternRouter, textEditRouter, patternMAC, textEditMAC):
        textRouter = textEditRouter.toPlainText()
        textMAC = str(textEditMAC.toPlainText())

        if len(textRouter) != 0 and len(textMAC) != 0:
            try:
                if re.fullmatch(patternRouter, textRouter) and re.fullmatch(patternMAC, textMAC) and textRouter in Router.diccionarioRouter and textMAC in Router.diccionarioRouter[textRouter].conexiones:
                    self.pushButton.setEnabled(True)
                else:
                    self.pushButton.setEnabled(False)
            except:
                self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(False)

    def funcionEliminarConexion(self):            
        routerID = self.textEditRouter.toPlainText()
        mac = self.textEditMAC.toPlainText()
        if routerID not in Router.diccionarioRouter:
            msg = QMessageBox()
            msg.setInformativeText("El router ingresado no existe")
            msg.exec_()
            return
        
        router = Router.diccionarioRouter[routerID]
        if mac not in router.conexiones:
            msg = QMessageBox()
            msg.setInformativeText("La MAC ingresada no existe")
            msg.exec_()
            return
        
        router.quitarConexion(mac)
        
        msg = QMessageBox()
        msg.setInformativeText("Conexion eliminada correctamente")
        msg.exec_()
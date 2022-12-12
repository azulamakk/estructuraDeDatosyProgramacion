from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

import sys
# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from routers import Router

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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # Text box y su label para ingresar por teclado el router ID
        self.Hlayout = QtWidgets.QHBoxLayout()

        label = QtWidgets.QLabel(self.verticalLayoutWidget)
        label.setObjectName('labelIngresoRouterID')
        label.setText('Ingresar ID router: ')
        self.Hlayout.addWidget(label)

        self.textEditRouter = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditRouter.setObjectName("textEditRouter")
        self.Hlayout.addWidget(self.textEditRouter)     

        label = QtWidgets.QLabel(self.verticalLayoutWidget)
        label.setObjectName('labelIngresoMAC')
        label.setText('Ingresar MAC: ')
        self.Hlayout.addWidget(label)

        self.textEditMAC = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEditMAC.setObjectName("textEditMAC")
        self.Hlayout.addWidget(self.textEditMAC)      

        self.verticalLayout.addLayout(self.Hlayout)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar conexion")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionEliminarConexion())

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
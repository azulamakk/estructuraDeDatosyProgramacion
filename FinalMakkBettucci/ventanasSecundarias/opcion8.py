from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QCalendarWidget, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
from PyQt5.QtCore import Qt,QUrl,QRect,QDateTime

import sys
# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from routers import Router

# Esta clase es para ejecutar la opcion 8
class Ui_FormEliminarRouter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Opcion ingresada: Eliminar router")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # Text box y su label para ingresar por teclado el router ID
        self.Hlayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName('labelIngresoDireccionIP')
        self.label.setText('Ingresar router ID: ')
        self.Hlayout.addWidget(self.label)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.Hlayout.addWidget(self.textEdit)        

        self.verticalLayout.addLayout(self.Hlayout)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar router")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionEliminarRouter())

    def funcionEliminarRouter(self):            
        print(self.textEdit.toPlainText())
        routerID = self.textEdit.toPlainText()
        if routerID not in Router.diccionarioRouter:
            msg = QMessageBox()
            msg.setInformativeText("El router no existe")
            msg.exec_()
            return

        del Router.diccionarioRouter[routerID]
        msg = QMessageBox()
        msg.setInformativeText("Router eliminado correctamente")
        msg.exec_()

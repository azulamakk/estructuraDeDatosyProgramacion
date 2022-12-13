from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QCalendarWidget, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
from PyQt5.QtCore import Qt,QUrl,QRect,QDateTime
import re
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 435, 130))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # Text box y su label para ingresar por teclado el router ID (en el horizontal layout)
        self.Hlayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName('labelIngresoDireccionIP')
        self.label.setText('Ingresar router ID: ')
        self.Hlayout.addWidget(self.label)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText('ABC123-01')
        self.textEdit.setTabChangesFocus(True)
        self.Hlayout.addWidget(self.textEdit)        

        self.verticalLayout.addLayout(self.Hlayout)

        ### BOTON ELIMINAR Y VOLVER EN EL VERTICAL LAYOUT ###

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar router")
        self.verticalLayout.addWidget(self.pushButton)

        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("pushButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.setEnabled(False)
        self.textEdit.textChanged.connect(lambda: self.botonSeleccionar_enableConAlfanumerico('^([A-Z]{3})([0-9]{3})-([0-9]{2})', self.textEdit))
        self.pushButton.clicked.connect(lambda: self.funcionEliminarRouter())

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

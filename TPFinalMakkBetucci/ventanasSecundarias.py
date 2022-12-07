from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
import sys,os
from PyQt5.QtCore import Qt,QUrl,QRect
from PyQt5.QtGui import QFont

#importo la funcion leerCSVMunicipios del modulo lecturaArchivos porque no quiero que se lea siempre, sino cuando llame a la funcion nada mas
from lecturaArchivos import leerArchivoMunicipio

#aca importar las funciones del menu que vamos a ejecutar

class Ui_FormRouters(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 426)
        self.labelCargarArchivoMuni = QtWidgets.QLabel(Form)
        self.labelCargarArchivoMuni.setGeometry(QtCore.QRect(100, 140, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelCargarArchivoMuni.setFont(font)
        self.labelCargarArchivoMuni.setObjectName("labelCargarArchivorRouters")
        self.botonCargarArchivoMuni = QtWidgets.QPushButton(Form)
        self.botonCargarArchivoMuni.setGeometry(QtCore.QRect(410, 140, 111, 23))
        self.botonCargarArchivoMuni.setObjectName("botonCargarArchivoRouter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cargar archivo router"))
        self.labelCargarArchivoMuni.setText(_translate("Form", "Arrastre o adjunte archivo router:"))
        self.botonCargarArchivoMuni.setText(_translate("Form", "Cargar archivo"))

class ListboxWidget(QListWidget):  
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setGeometry(200,200,100,100)   
    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self,event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
    def dropEvent(self,event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            #print(event.mimeData().urls())

            for url in event.mimeData().urls():
                #Veo si le paso un archivo local
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                #Si no es un archivo local no hago nada
            self.addItems(links)
        else: #si falla
            event.ignore()

class Ui_FormMunis(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cargar archivo municipios")

        self.resize(700,500)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)

        self.layoutPrincipal = QHBoxLayout() 


        self.labelCargarArchivoMuni = QLabel("Arrastre o adjunte archivo municipios:")
        self.labelCargarArchivoMuni.setGeometry(250,300,200,100)
        self.labelCargarArchivoMuni.setFont(font)
        self.labelCargarArchivoMuni.setObjectName("labelCargarArchivoMuni")

        self.layoutPrincipal.addWidget(self.labelCargarArchivoMuni)

        self.lstbox_ = ListboxWidget(self)

        self.layoutPrincipal.addWidget(self.lstbox_)
        
        self.botonCargarArchivoMuni = QPushButton()
        self.botonCargarArchivoMuni.setObjectName("botonCargarArchivoMuni")
        self.botonCargarArchivoMuni.setText("Cargar archivo")
        self.botonCargarArchivoMuni.setGeometry(350, 200, 200, 150)
        self.botonCargarArchivoMuni.clicked.connect(lambda: print(self.getSelectedItem()))

        self.layoutPrincipal.addWidget(self.botonCargarArchivoMuni)

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

    def getSelectedItem(self):
        #selecciono el archivo csv de municipios que quiero leer mediante la ejecucion de la funcion "leerArchivoMunicipio", para ello le paso el path que tengo en la listbox
        item = QListWidgetItem(self.lstbox_.currentItem())
        pathMunicipio = item.text()
        leerArchivoMunicipio(pathMunicipio)

class Ui_FormRouter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cargar archivo routers")

        self.resize(700,500)

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)

        self.layoutPrincipal = QHBoxLayout() 


        self.labelCargarArchivoMuni = QLabel("Arrastre o adjunte archivo routers:")
        self.labelCargarArchivoMuni.setGeometry(250,300,200,100)
        self.labelCargarArchivoMuni.setFont(font)
        self.labelCargarArchivoMuni.setObjectName("labelCargarArchivoRouter")

        self.layoutPrincipal.addWidget(self.labelCargarArchivoMuni)

        self.lstbox_ = ListboxWidget(self)

        self.layoutPrincipal.addWidget(self.lstbox_)
        
        self.botonCargarArchivoMuni = QPushButton()
        self.botonCargarArchivoMuni.setObjectName("botonCargarArchivoRouter")
        self.botonCargarArchivoMuni.setText("Cargar archivo")
        self.botonCargarArchivoMuni.setGeometry(350, 200, 200, 150)
        self.botonCargarArchivoMuni.clicked.connect(lambda: print(self.getSelectedItem()))

        self.layoutPrincipal.addWidget(self.botonCargarArchivoMuni)

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

    def getSelectedItem(self):
        item = QListWidgetItem(self.lstbox_.currentItem())
        return item.text()

class Ui_FormVerConexProv(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 160, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.mostrarConexionesPorProvincia)

    #Aca ejecutar la funcion importada que muestra las conexiones por provincia
    #Pensar como "importar" los resultados de esa funcion a una ventana nueva
    def mostrarConexionesPorProvincia(self):
        print("Aca se ejecuta la funcion que muestra las conexiones en la provincia dada")
        return

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        self.label.setText(_translate("Form", "Ingrese una provincia:"))


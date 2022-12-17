from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget, QListWidget,QListWidgetItem, QVBoxLayout, QHBoxLayout, QMainWindow,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from lecturaArchivos import cargarProvinciasyDptos

# Clase auxiliar
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

# Esta clase es para ejecutar la opcion 1
class VentanaCargarMunicipio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None    
    
    def setupUi(self, MainWindow,secondWidgetWindow):

        self.secondWidgetWindow = secondWidgetWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Opcion ingresada: Agregar Municipio")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## DEFINO EL VERTICAL LAYOUT ##
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 40, 500, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        ## DEFINO EL HORIZONTAL LAYOUT QUE VA A CONTENER EL LABEL Y EL BOTON CARGAR ##

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # CREO Y AGREGO EL LABEL AL HORIZONTAL LAYOUT #
        self.labelCargarArchivoMuni = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCargarArchivoMuni = QLabel("Arrastre o adjunte archivo municipios: ")
        self.labelCargarArchivoMuni = QLabel('''
        Las columnas de dicho archivo deben ser llamadas:
        id_provincia, id_departamento
        id_municipio, municipio, departamento, provincia''')
        font = QFont("Calibri", pointSize=14, weight=QFont.Medium, italic=False)
        self.labelCargarArchivoMuni.setFont(font)
        self.labelCargarArchivoMuni.setObjectName("labelCargarArchivoMuni")
        self.horizontalLayout.addWidget(self.labelCargarArchivoMuni)
        
        # CREO Y AGREGO EL BOTON DE CARGAR AL HORIZONTAL LAYOUT #
        self.botonCargarArchivoMuni = QPushButton(self.verticalLayoutWidget)
        self.botonCargarArchivoMuni.setObjectName("botonCargarArchivoMuni")
        self.botonCargarArchivoMuni.setText("Cargar archivo")
        self.horizontalLayout.addWidget(self.botonCargarArchivoMuni)

        # CARGO EL HORIZONTAL LAYOUT AL VERTICAL LAYOUT #
        self.verticalLayout.addLayout(self.horizontalLayout)

        # CREO Y AGREGO EL LISTBOX AL VERTICAL LAYOUT #
        self.lstbox_ = ListboxWidget(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.lstbox_)
        
        # CREO Y AGREGO EL BACK BUTTON AL VERTICAL LAYOUT #
        self.backButton = QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)

        MainWindow.setCentralWidget(self.centralwidget)

        # CONNECTS #
        self.botonCargarArchivoMuni.clicked.connect(lambda: self.getSelectedItem())
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    def getSelectedItem(self):
        if len(self.lstbox_) == 0:
            print('Por favor arrastre un archivo')
            msg = QMessageBox()
            msg.setText("Error")
            msg.setInformativeText("Por favor arrastre un archivo")
            msg.exec_()
        else:
            item = QListWidgetItem(self.lstbox_.currentItem())
            pathMuni = item.text()
            cargarProvinciasyDptos(pathMuni)
            msg = QMessageBox()
            msg.setInformativeText("Archivo cargado correctamente")
            msg.exec_()
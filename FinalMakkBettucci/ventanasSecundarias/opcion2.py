from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from ventanasSecundarias.opcion1 import ListboxWidget
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')
 
# importing
from lecturaArchivos import leerArchivoConexiones, leerArchivoRouter

class Ui_FormRouter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
    
    def setupUi(self, MainWindow,secondWidgetWindow):

        self.secondWidgetWindow = secondWidgetWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Opcion ingresada: Agregar Router")
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
        self.labelCargarArchivoRouter = QLabel(self.verticalLayoutWidget)
        self.labelCargarArchivoRouter = QLabel("Arrastre o adjunte archivo routers: ")
        self.labelCargarArchivoRouter = QLabel('''
        Las columnas de dicho archivo deben ser llamadas:
        id, identificador, ubicacion, latitud, longitud,
        municipio_id, provincia_id, departamento_id''')
        font = QFont("Calibri", pointSize=14, weight=QFont.Medium, italic=False)
        self.labelCargarArchivoRouter.setFont(font)
        self.labelCargarArchivoRouter.setObjectName("labelCargarArchivoRouter")
        self.horizontalLayout.addWidget(self.labelCargarArchivoRouter)
        
        self.botonCargarArchivoRouter = QPushButton(self.verticalLayoutWidget)
        self.botonCargarArchivoRouter.setObjectName("botonCargarArchivoRouter")
        self.botonCargarArchivoRouter.setText("Cargar archivo")
        self.horizontalLayout.addWidget(self.botonCargarArchivoRouter)

        # CARGO EL HORIZONTAL LAYOUT AL VERTICAL LAYOUT #
        self.verticalLayout.addLayout(self.horizontalLayout)

        # CREO Y AGREGO EL LISTBOX AL VERTICAL LAYOUT #
        self.lstbox_ = ListboxWidget(self)
        self.verticalLayout.addWidget(self.lstbox_)

        # CREO Y AGREGO EL BACK BUTTON AL VERTICAL LAYOUT #
        self.backButton = QPushButton()
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)

        MainWindow.setCentralWidget(self.centralwidget)

        # CONNECTS #
        self.botonCargarArchivoRouter.clicked.connect(lambda: self.getSelectedItem())
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    def getSelectedItem(self):
        if len(self.lstbox_) == 0:
            msg = QMessageBox()
            msg.setText("Error")
            msg.setInformativeText("Por favor arrastre un archivo")
            msg.exec_()
        else:
            item = QListWidgetItem(self.lstbox_.currentItem())
            pathRouter = item.text()
            leerArchivoRouter(pathRouter)
            msg = QMessageBox()
            msg.setInformativeText("Archivo cargado correctamente")
            msg.exec_()

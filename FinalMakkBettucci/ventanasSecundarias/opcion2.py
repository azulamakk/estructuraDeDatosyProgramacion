from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton
from PyQt5 import QtCore
from ventanasSecundarias.opcion1 import ListboxWidget
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')
 
# importing
from lecturaArchivos import leerArchivoConexiones, leerArchivoRouter

class Ui_FormRouter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opcion seleccionada: Cargar archivo routers")
        self.resize(700,500)

        self.layoutPrincipal = QHBoxLayout() 

        self.labelCargarArchivoRouter = QLabel("Arrastre o adjunte archivo routers:")
        self.labelCargarArchivoRouter.setGeometry(250,300,200,100)
        self.labelCargarArchivoRouter.setObjectName("labelCargarArchivoRouter")

        self.layoutPrincipal.addWidget(self.labelCargarArchivoRouter)

        self.lstbox_ = ListboxWidget(self)

        self.layoutPrincipal.addWidget(self.lstbox_)
        
        self.botonCargarArchivoRouter = QPushButton()
        self.botonCargarArchivoRouter.setObjectName("botonCargarArchivoRouter")
        self.botonCargarArchivoRouter.setText("Cargar archivo")
        self.botonCargarArchivoRouter.setGeometry(350, 200, 200, 150)
        self.botonCargarArchivoRouter.clicked.connect(lambda: self.getSelectedItem())
        self.layoutPrincipal.addWidget(self.botonCargarArchivoRouter)

        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.layoutPrincipal.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.exit())

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

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
            leerArchivoConexiones('conexiones.csv')
            msg = QMessageBox()
            msg.setInformativeText("Archivo cargado correctamente")
            msg.exec_()

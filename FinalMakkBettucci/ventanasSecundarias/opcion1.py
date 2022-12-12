from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton
from PyQt5.QtCore import Qt
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
        self.setWindowTitle("Opcion ingresada: Cargar archivo municipios")
        self.resize(700,500)

        self.layoutPrincipal = QHBoxLayout() 

        self.labelCargarArchivoMuni = QLabel("Arrastre o adjunte archivo municipios: ")
        self.labelCargarArchivoMuni = QLabel('''
        Las columnas de dicho archivo deben ser llamadas:
        id_procincia, id_departamento, id_municipio, municipio, departamento, provincia''')
        self.labelCargarArchivoMuni.setGeometry(250,300,200,100)
        self.labelCargarArchivoMuni.setObjectName("labelCargarArchivoMuni")

        self.layoutPrincipal.addWidget(self.labelCargarArchivoMuni)

        self.lstbox_ = ListboxWidget(self)

        self.layoutPrincipal.addWidget(self.lstbox_)
        
        self.botonCargarArchivoMuni = QPushButton()
        self.botonCargarArchivoMuni.setObjectName("botonCargarArchivoMuni")
        self.botonCargarArchivoMuni.setText("Cargar archivo")
        self.botonCargarArchivoMuni.setGeometry(350, 200, 200, 150)
        self.botonCargarArchivoMuni.clicked.connect(lambda: self.getSelectedItem())
        self.layoutPrincipal.addWidget(self.botonCargarArchivoMuni)

        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.layoutPrincipal.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

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
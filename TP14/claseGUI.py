from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QHBoxLayout, QLabel, QTextEdit, QPushButton, QWidget, QApplication
import sys

# Defino mi ventana
class MiVentanaPrincipal(QMainWindow):
    def botonCambiarTitulo_click(self):
        nuevoTitulo = self.campoTextoNombreVentana.toPlainText()
        self.setWindowTitle(nuevoTitulo)
        self.campoTextoNombreVentana.clear()

    def botonMostrarError_click(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Error')
        msg.setInformativeText('More Information')
        msg.setWindowTitle('Error')
        msg.exec()

    def campoTextoNombreVentana_textChanged(self):
        texto = self.campoTextoNombreVentana.toPlainText()
        if len(texto) == 0:
            self.botonCambiarTitulo.setEnabled(False)
        else:
            self.botonCambiarTitulo.setEnabled(True)
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Mi primer programa con UI')
        
        # Establezco posicion y tamaño inicial de la ventana
        self.setGeometry(500,500, 1000, 700)

        layoutPrincipal = QHBoxLayout() # Python ubica los elementos verticalmente

        # Creo un label y lo agrego al layout
        labelSaludo = QLabel('Bienvenidos al programa')
        layoutPrincipal.addWidget(labelSaludo)

        layoutCambioDeNombre = QHBoxLayout()
        layoutCambioDeNombre.addWidget(QLabel('Ingrese nuevo nombre de la ventana'))
        self.campoTextoNombreVentana=QTextEdit() # Por default ocupa la mayor cantidad de espacio posible
        self.campoTextoNombreVentana.textChanged.connect(self.campoTextoNombreVentana_textChanged)
        layoutCambioDeNombre.addWidget(self.campoTextoNombreVentana)
        # self.campoTextoNombreVentana.textChanged()

        layoutPrincipal.addLayout(layoutCambioDeNombre)

        self.botonCambiarTitulo = QPushButton()
        self.botonCambiarTitulo.setText('Mostrar creditos')
        self.botonCambiarTitulo.clicked.connect(self.botonCambiarTitulo_click)
        layoutPrincipal.addWidget(self.botonCambiarTitulo)

        self.botonMostrarError = QPushButton()
        self.botonMostrarError.setText('Mostrar error general')
        self.botonMostrarError.clicked.connect(self.botonMostrarError_click)
        layoutPrincipal.addWidget(self.botonMostrarError)
        # Establezco que mi widget que contiene al layout es el widget principal de la ventana, para que se muestre
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)
        
# Creo mi app y la muestro
app = QApplication(sys.argv) # Siempre ponemos esta linea
window = MiVentanaPrincipal()
window.show()

app.exec() # El control del programa lo tiene PyQt, por lo que no se cierra excepto que aprete X
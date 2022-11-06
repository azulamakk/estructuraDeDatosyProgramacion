from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys

# Defino mi ventana
class MiVentanaPrincipal(QMainWindow):
    def botonCambiarTIitulo_click(self):
        nuevoTitulo = self.campoTextoNombreVentana.toPlainText()
        self.setWindowTitle(nuevoTitulo)
        self.campoTextoNombreVentana.clear()

    def botonMostrarCreditos_click(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Error')
        msg.setInformativeText('More Information')
        msg.setWindowTitle('Error')
        msg.exec()

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
        layoutCambioDeNombre.addWidget(Qlabel('Ingrese nuevo nombre de la ventana'))
        self.campoTextoNombreVentana=QTextEdit() # Por default ocupa la mayor cantidad de espacio posible
        layoutCambioDeNombre.addWidget(campoTextoNombreVentana)

        layoutPrincipal.addLayout(layoutCambioDeNombre)

        botonCambiarTitulo = QPushButton()
        botonCambiarTitulo.setText('Cambiar titulo a ventana')
        botonCambiarTitulo.clicked.connect(self.botonCambiarTIitulo_click)
        layoutPrincipal.addWidget(botonCambiarTitulo)

        botonCambiarTitulo = QPushButton()
        botonCambiarTitulo.setText('Mostrar creditos')
        botonCambiarTitulo.clicked.connect(self.botonMostrarCreditos_click)
        layoutPrincipal.addWidget(botonMostrarCreditos)

        # Establezco que mi widget que contiene al layout es el widget principal de la ventana, para que se muestre
        widgetLayout = QWidget()
        widgetLayout.setLayout(layoutPrincipal)
        self.setCentralWidget(widgetLayout)

# Creo mi app y la muestro
app = QApplication(sys.argv) # Siempre ponemos esta linea
window = MiVentanaPrincipal()
window.show()

app.exec() # El control del programa lo tiene PyQt, por lo que no se cierra excepto que aprete X
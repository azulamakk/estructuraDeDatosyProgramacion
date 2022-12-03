from curses.ascii import isdigit
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout, QApplication
from PyQt5.QtGui import QFont
import sys
from funciones import*

class miVentana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Proyecto Final - Estructura de datos y programación") # titulo de ventana
        self.setGeometry(600,600,600,600) # posición y tamaño
        self.setWindowIconText("M y P")
        self.setStyleSheet("background-color: pink;")


        # layout --> contenedor de widgets
        self.layoutPrincipal = QVBoxLayout() 

        # título LABEL
        self.labelSaludo = QLabel("Menú Principal")
        self.labelSaludo.setFont(QFont('Times', 30))
        self.labelSaludo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layoutPrincipal.addWidget(self.labelSaludo)

        # Opciones del manú LABEL
        self.labelOpciones = QLabel("1.   Grabar en un archivo txt la cantidad de bandas en un barrio; y el nombre de su solista\n\n2.   Grabar en un archivo txt el promedio de bandas inscritas por barrio hasta una fecha \n\n3.   Personalidad de cada barrio según el género musical más tocado\n\n4.   Visualizar la información de una banda\n\n5.   Visualizar los barrios ordenados en forma decreciente por cantidad de bandas\n\n6.   Visualizar la cantidad de Bandas por Barrio, ordenados alfabéticamente\n\n7.   Mostrar la cantidad de bandas, discos y la cantidad de integrantes por género musical\n\n8.   Grabar en un archivo txt el Promedio de integrantes por Género musical\n\n9.   Ver gráfico de las 10 primeras bandas con más presencia en las redes sociales\n\n10.   Grabar en un archivo txt el género de música que las bandas tocan más por cada barrio\n\n11.   Mostrar gráfico de la cantidad de bandas inscritas por mes y el género predominante en un año\n\n12.   Género musical más común de las bandas inscritas en un periodo de tiempo\n\n13.   Visualizar para cada género musical sus diferentes estilos y cual es el que más tiene\n\n14.   Grabar en un archivo txt las bandas que hayan grabado discos hasta una determinada fecha\n\n15.   Salir")
        self.labelOpciones.setFont(QFont('Times', 15))
        self.layoutPrincipal.addWidget(self.labelOpciones)

        # Rta LAYOUT SECUNDARIO
        self.layoutRta = QHBoxLayout()

        # texto LABEL
        self.labelTexto = QLabel("Ingrese una opción del 1 al 15:")
        self.labelTexto.setAlignment(Qt.AlignmentFlag.AlignLeft)
        fuente = QFont('Times', 20)
        fuente.setBold(True)
        self.labelTexto.setFont(fuente)
        self.layoutRta.addWidget(self.labelTexto)

        # campo de texto TEXTO
        self.campoTextoRta = QTextEdit() # va a querer ocupar todo el espacio que tenga
        self.campoTextoRta.setFixedSize(150,25)
        self.campoTextoRta.textChanged.connect(self.botonSeleccionar_enable)
        self.layoutRta.addWidget(self.campoTextoRta)

        # boton seleccionar BOTÓN 
        self.botonSeleccionar = QPushButton() # espacio mínimo
        self.botonSeleccionar.setText("Seleccionar")
        self.botonSeleccionar.setEnabled(False)
        self.botonSeleccionar.clicked.connect(self.recibirRta_click)
        self.layoutRta.addWidget(self.botonSeleccionar)

    
        self.layoutPrincipal.addLayout(self.layoutRta)
    
        #Establecer Layout Principal
        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout) # el widget principal es mi layout que creo
    
    def botonSeleccionar_enable(self):
        texto = self.campoTextoRta.toPlainText()
        if len(texto) != 0:
            try:
                rta = int(texto)
                if rta in range(1,16):
                    self.botonSeleccionar.setEnabled(True)
                else:
                    self.botonSeleccionar.setEnabled(False)
            except:
                self.botonSeleccionar.setEnabled(False)
        else:
            self.botonSeleccionar.setEnabled(False)


    def recibirRta_click(self):
        rta = self.campoTextoRta.toPlainText()
        self.campoTextoRta.clear()
        rta = int(rta)
        if rta == 1:
            opcion1()
        elif rta == 2:
            opcion2()
        elif rta == 3:
            opcion3()
        elif rta == 4:
            opcion4()
        elif rta == 5:
            opcion5()
        elif rta == 6:
            opcion6()
        elif rta == 7:
            opcion7()
        elif rta == 8:
            opcion8()
        elif rta == 9:
            opcion9()
        elif rta == 10:
            opcion10()
        elif rta == 11:
            opcion11()
        elif rta == 12:
            opcion12()
        elif rta == 13:
            opcion13()
        elif rta == 14:
            opcion14()
        elif rta == 15:
            self.close()
            print('\n---PROGRAMA TERMINADO---\n')
        return
if __name__ == '__main__':
    cargar_datos()
    app = QApplication(sys.argv) 
    window = miVentana()
    window.show() 
    sys.exit(app.exec_())


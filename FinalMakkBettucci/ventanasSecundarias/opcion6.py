from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget, QMainWindow,QPushButton
import threading
from PyQt5.QtCore import QDateTime
import sys

# setting path
sys.path.append('TPFinalMakkBettucci')

# importing
from routers import *


# Esta clase es para ejecutar la opcion 6
class Ui_FormVerConexEntreFechas(QMainWindow):
    valueChanged = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None

    def setupUi(self,MainWindow,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(30, 30, 690, 400)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, -300)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -300, -100)
        self.horizontalLayout.setObjectName("horizontalLayout")       

        # Label de seleccionar fecha inicio
        self.labelIngresoFechaInicio = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelIngresoFechaInicio.setObjectName("label")
        self.labelIngresoFechaInicio.setText("Ingrese fecha de inicio:")
        self.horizontalLayout.addWidget(self.labelIngresoFechaInicio)

        # Objeto calendario para seleccionar la fecha inicio
        self.calendarInicio = QCalendarWidget(self.verticalLayoutWidget)
        self.horizontalLayout.addWidget(self.calendarInicio)
        self.calendarInicio.setGridVisible(True)

        # Boton para seleccionar la fecha inicio
        self.botonSeleccionarFechaInicio = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonSeleccionarFechaInicio.setObjectName("botonSeleccionarFechaInicio")
        self.botonSeleccionarFechaInicio.setText("Seleccionar")
        self.horizontalLayout.addWidget(self.botonSeleccionarFechaInicio)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -300, -100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Label de seleccionar fecha fin
        self.labelFechaFin = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelFechaFin.setObjectName("label")
        self.labelFechaFin.setText("Ingrese fecha de fin:")
        self.horizontalLayout_2.addWidget(self.labelFechaFin)

        # Objeto calendario para seleccionar fecha fin
        self.calendarFechaFin = QCalendarWidget(self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.calendarFechaFin)
        self.calendarFechaFin.setGridVisible(True)

        # Boton para seleccionar la fecha fin
        self.botonSeleccionarFechaFin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonSeleccionarFechaFin.setObjectName("botonSeleccionarFechaFin")
        self.botonSeleccionarFechaFin.setText("Seleccionar")
        self.horizontalLayout_2.addWidget(self.botonSeleccionarFechaFin)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
    
        ## Boton de ingreso de rango de fechas
        self.botonIngresoRangoFechas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonIngresoRangoFechas.setObjectName("botonIngresoRangoFechas")
        self.botonIngresoRangoFechas.setText("Ingresar rango de fechas")
        self.verticalLayout.addWidget(self.botonIngresoRangoFechas)

        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.exit())

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setGeometry(QtCore.QRect(380, 130, 100, 100))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        #### Acciones ####  PD: abria que validar que "fecha fin > fecha inicio" 
        self.valueChanged.connect(self.on_value_changed)

        self.botonSeleccionarFechaInicio.clicked.connect(lambda: self.asignarFechaInicio())
        self.botonSeleccionarFechaFin.clicked.connect(lambda: self.asignarFechaFin())
        # Se ejecuta la funcion que muestra las conexiones entre las dos fechas seleccionadas
        # deberia poder verificar que se hayan apretado ambos botones para poder ingresar el rango de fecha, ya que se compone de dos fechas
        self.botonIngresoRangoFechas.clicked.connect(self.on_clicked)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        #self.textEdit.clear()
        threading.Thread(target=self.mostrarConexionesEntreFechas, daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEdit.append("Conexion: {}".format(value))

    def asignarFechaInicio(self):
        self.fechaInicio = QDateTime(self.calendarInicio.selectedDate()).toPyDateTime()

    def asignarFechaFin(self):
        self.fechaFin = QDateTime(self.calendarFechaFin.selectedDate()).toPyDateTime()

    #Funcion que muestra las conexiones totales en el pais entre dos fechas
    def mostrarConexionesEntreFechas(self):
        for router in Router.diccionarioRouter.items():
            for conexion in router[1].conexiones.items():
                if conexion[1].fechaYHora > self.fechaInicio and conexion[1].fechaYHora < self.fechaFin:
                    self.valueChanged.emit(str(conexion[0]))
                    #time.sleep(0.1)
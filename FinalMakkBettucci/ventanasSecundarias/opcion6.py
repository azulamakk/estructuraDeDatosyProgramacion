from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QCalendarWidget, QMainWindow,QPushButton, QMessageBox
import threading
from PyQt5.QtCore import QDateTime
import sys
from datetime import datetime
from conexiones import *

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
        MainWindow.setWindowTitle("Opcion ingresada: Conexion en intervalo temporal")
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

        #Objeto time picker fecha inicio
        self.timeEditInicio = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEditInicio.setGeometry(QtCore.QRect(80, 100, 118, 22))
        self.timeEditInicio.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEditInicio)

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

        #Objeto time picker fecha fin
        self.timeEditFin = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEditFin.setGeometry(QtCore.QRect(80, 100, 118, 22))
        self.timeEditFin.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEditFin)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
    
        ## Boton de ingreso de rango de fechas
        self.botonIngresoRangoFechas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonIngresoRangoFechas.setObjectName("botonIngresoRangoFechas")
        self.botonIngresoRangoFechas.setText("Ingresar rango de fechas")
        self.verticalLayout.addWidget(self.botonIngresoRangoFechas)

        #Text box para mostrar el output de la funcion
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setGeometry(QtCore.QRect(380, 130, 100, 100))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText('Output textbox')
        self.textEdit.setTabChangesFocus(True)
        self.verticalLayout.addWidget(self.textEdit)

        #Boton para volver al menu principal
        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

        #### Acciones ####  PD: abria que validar que "fecha fin > fecha inicio" 
        self.valueChanged.connect(self.on_value_changed)

        # Se ejecuta la funcion que muestra las conexiones entre las dos fechas seleccionadas
        # deberia poder verificar que se hayan apretado ambos botones para poder ingresar el rango de fecha, ya que se compone de dos fechas
        self.botonIngresoRangoFechas.clicked.connect(self.on_clicked)

    def parseDate(self, date, time):
        datePart = datetime.strftime(date,"%d-%m-%Y")
        timePart1 = datetime.combine(datetime.today(),time)
        timePart2 = datetime.strftime(timePart1,"%H:%M:%S")

        dateParts = datePart.split("-")
        if len(dateParts) < 3:
            return None
        [year, month, day] = dateParts
        
        timeParts = timePart2.split(":")
        if len(timeParts) < 3:
            return None
        [hour, minute, seconds] = timeParts

        return datetime(int(day), int(month), int(year), int(hour), int(minute), int(seconds))

    @QtCore.pyqtSlot()
    def on_clicked(self):
        #self.textEdit.clear()
        self.fechaYhoraInicio = self.asignarFechaInicio()
        self.fechaYhoraFin = self.asignarFechaFin()

        if self.fechaYhoraInicio > self.fechaYhoraFin:
            msg = QMessageBox()
            msg.setInformativeText("La fecha de finalizacion no puede ser anterior a la fecha de inicio")
            msg.setText('Por favor vuelva a elegir las fechas')
            msg.exec_()
        else:
            threading.Thread(target=self.mostrarConexionesEntreFechas(self.fechaYhoraInicio,self.fechaYhoraFin), daemon=True).start()

    @QtCore.pyqtSlot(str)
    def on_value_changed(self,value):
        self.textEdit.append(value)

    def asignarFechaInicio(self):
        self.fechaInicio = QDateTime(self.calendarInicio.selectedDate()).toPyDateTime()
        self.horaInicio = self.timeEditInicio.time().toPyTime()
        self.fechaYhoraInicio = self.parseDate(self.fechaInicio,self.horaInicio)
        return self.fechaYhoraInicio

    def asignarFechaFin(self):
        self.fechaFin = QDateTime(self.calendarFechaFin.selectedDate()).toPyDateTime()
        self.horaFin = self.timeEditFin.time().toPyTime()
        self.fechaYhoraFin = self.parseDate(self.fechaFin,self.horaFin)
        return self.fechaYhoraFin

    #Funcion que muestra las conexiones totales en el pais entre dos fechas
    def mostrarConexionesEntreFechas(self, fechaHoraInicio, fechaHoraFin):
        print('Inicio: ',fechaHoraInicio)
        print('Fin: ',fechaHoraFin)

        self.textEdit.clear()
        nodoActual = Conexion.conexionesHistoricas.head
        
        while nodoActual != None:
            if nodoActual.valor.fechaYHora < fechaHoraInicio:
                nodoActual = nodoActual.prox
                continue
            if nodoActual.valor.fechaYHora > fechaHoraFin:
                break
              
            self.valueChanged.emit(str(nodoActual.valor))
            nodoActual = nodoActual.prox

    
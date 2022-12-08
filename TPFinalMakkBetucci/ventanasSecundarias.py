from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
import sys,os
from PyQt5.QtCore import Qt,QUrl,QRect,QDateTime
from PyQt5.QtGui import QFont
import datetime
import calendar

from lecturaArchivos import leerArchivoMunicipio
#aca importar las funciones del menu que vamos a ejecutar

# Clase auxiliar
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
        item = QListWidgetItem(self.lstbox_.currentItem())
        pathMuni = item.text()
        leerArchivoMunicipio(pathMuni)

# Esta clase es para ejecutar la opcion 2
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

# Esta clase es para ejecutar la opcion 6
class Ui_FormVerConexEntreFechas(object):

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
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
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.labelIngresoFechaInicio.setFont(font)
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
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.labelFechaFin.setFont(font)
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

        #### Acciones ####

        # PD: abria que validar que "fecha fin > fecha inicio" 
        
        # Console log de las fechas elegidas
        
        self.botonSeleccionarFechaInicio.clicked.connect(lambda: self.asignarFechaInicio())
        self.botonSeleccionarFechaFin.clicked.connect(lambda: self.asignarFechaFin())


        # Se ejecuta la funcion que muestra las conexiones entre las dos fechas seleccionadas
        self.botonIngresoRangoFechas.clicked.connect(lambda: self.mostrarConexionesEntreFechas(self.fechaInicio,self.fechaFin))

    def asignarFechaInicio(self):
        self.fechaInicio = QDateTime(self.calendarInicio.selectedDate()).toPyDateTime()

    def asignarFechaFin(self):
        self.fechaFin = QDateTime(self.calendarFechaFin.selectedDate()).toPyDateTime()

    def mostrarConexionesEntreFechas(self,fechaInicio,fechaFin):
        print('Fecha desde: ',fechaInicio)
        print('Fecha hasta: ',fechaFin)
        print('\n')
        print("Aca se ejecuta la funcion que muestra las conexiones entre las dos fechas")
        return

# Esta clase es para ejecutar la opcion 3,4 y 5
class Ui_FormVerConexPorUbicacion(object):
    def setupUi(self, Form, ubicacion):
        Form.setObjectName("Form")
        Form.resize(559, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.textEdit.setObjectName("textEdit")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        QtCore.QMetaObject.connectSlotsByName(Form)

        if ubicacion == 'provincia':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(40, 160, 151, 16))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese una provincia:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorProvincia)
        elif ubicacion == 'departamento':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un departamento:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)
        elif ubicacion == 'municipio':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un municipio:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)

    #Aca ejecutar la funcion importada que muestra las conexiones por provincia
    #Pensar como "importar" los resultados de esa funcion a una ventana nueva
    def mostrarConexionesPorProvincia(self):
        print("Aca se ejecuta la funcion que muestra las conexiones en la provincia dada")
        return

    def mostrarConexionesPorDepartamento(self):
        print("Aca se ejecuta la funcion que muestra las conexiones en el departamento dado")
        return

# Esta clase es para ejecutar la opcion 7
class Ui_FormAgregarRouter(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(240, 150, 120, 31))
        self.textEdit.setObjectName("textEdit")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 160, 250, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(_translate("Form", "Ingrese router ID a agregar:"))
        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter(self.textEdit.toPlainText()))

    def funcionAgregarRouter(self,texto):
        print(texto)



# def IngresoFechayHora():
#     diaFecha= obtenerInt('Ingrese un dia: ', 0, 31)

#     mesFecha= obtenerInt('Ingrese un mes: ', 0, 12)

#     anioFecha= obtenerInt('Ingrese un año: ', 2019, 2022)

#     horaFecha= obtenerInt('Ingrese una hora: ', 0, 23)

#     minutosFecha= obtenerInt('Ingrese un minuto: ', 0, 59)

#     fecha = datetime.datetime(anioFecha, mesFecha, diaFecha, horaFecha, minutosFecha)
#     print(fecha)
#     return fecha

# def IngresoSoloFecha():
#     diaFecha= obtenerInt('Ingrese un dia: ', 0, 31)

#     mesFecha= obtenerInt('Ingrese un mes: ', 0, 12)

#     anioFecha= obtenerInt('Ingrese un año: ', 2019, 2022) #revisar que año de inicio dejamos
#     fecha = datetime.date(anioFecha, mesFecha, diaFecha)
#     return fecha

# def IngresoSoloHora():
#     horaFecha= obtenerInt('Ingrese una hora: ', 0, 23)

#     minutosFecha= obtenerInt('Ingrese un minuto: ', 0, 59)

#     hora = datetime.time(horaFecha, minutosFecha)
    
#     return hora

# def obtenerInt(mensaje, minimo, maximo):
#     try:    
#         numero = int(input(mensaje))

#         if numero < minimo or numero > maximo:
#             print('Numero de fecha incorrecto. Intente de nuevo')
#             return obtenerInt(mensaje, minimo, maximo)
#         else:
#             return numero

#     except ValueError or TypeError:
#         print('Dato de tipo erroneo')
#         return obtenerInt(mensaje, minimo, maximo)

# def parseDate(date, time):
#     try:    
#         dateParts = date.split("/")
#         if len(dateParts) < 3:
#             return None

#         [month, day, year] = dateParts
#         timeParts = time.split(":")
#         if len(timeParts) < 2:
#             return None

#         [hour, minute] = timeParts

#         return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
#     except:
#         return None

from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QCalendarWidget, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
import sys,os
import time
import threading
from PyQt5.QtCore import Qt,QUrl,QRect,QDateTime
from PyQt5.QtGui import QFont
import datetime
import re
import calendar
import string
import lecturaArchivos, municipios,routers
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
        self.botonCargarArchivoMuni.clicked.connect(lambda: self.getSelectedItem())

        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.layoutPrincipal.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.close())

        self.layoutPrincipal.addWidget(self.botonCargarArchivoMuni)

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

    def getSelectedItem(self):
        item = QListWidgetItem(self.lstbox_.currentItem())
        pathMuni = item.text()
        lecturaArchivos.cargarProvinciasyDptos(pathMuni)

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

        self.labelCargarArchivoRouter = QLabel("Arrastre o adjunte archivo routers:")
        self.labelCargarArchivoRouter.setGeometry(250,300,200,100)
        self.labelCargarArchivoRouter.setFont(font)
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
        self.backButton.clicked.connect(lambda: self.close())

        widgetLayout = QWidget()
        widgetLayout.setLayout(self.layoutPrincipal)
        self.setCentralWidget(widgetLayout)

    def getSelectedItem(self):
        item = QListWidgetItem(self.lstbox_.currentItem())
        pathRouter = item.text()
        lecturaArchivos.leerArchivoRouter(pathRouter)

# Esta clase es para ejecutar la opcion 3,4 y 5
class Ui_FormVerConexPorUbicacion(QtWidgets.QMainWindow):   
    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        self.ubicacion = None

    def setupUi(self, Form, ubicacion,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        
        self.ubicacion = ubicacion

        Form.setObjectName("Form")
        Form.resize(559, 323)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.backButton = QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConTexto(self))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        self.backButton.setText(_translate("Form", "Volver"))

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
            self.pushButton.clicked.connect(self.mostrarConexionesPorMunicipio)

            self.valueChanged.connect(self.on_value_changed)
            self.pushButton.clicked.connect(self.on_clicked)

        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.textEdit.clear()
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 140, 100))

        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia, daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento, daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio, daemon=True).start()

    @QtCore.pyqtSlot(int)
    def on_value_changed(self,value):
        self.textEdit.append("Conexion: {}".format(value))

    #Funcion que muestra las conexiones por provincia dada
    def mostrarConexionesPorProvincia(self):
        #Extraigo el texto del text box, le saco los espacios, las tildes y pongo en mayuscula la primera letra de cada palabra para filtrar por provincia        
        text = self.textEdit.toPlainText().strip()
        texto = quitarTildes(text)
        textoFinal = string.capwords(texto)

        # Me fijo en el diccionario de provincias donde coincide el nombre escrito en el text box con el atributo Provincia (nombre de la provincia) de algun objeto provincia
        # Una vez que tengo la provincia ID, me fijo en el diccionario de routers para cada router si coincide la provincia ID (resultado del text box)
        # con el atributo provinciaID del router. Si coinciden entonces imprimo las conexiones que tiene ese router ID (imprimo las direcciones IP)
        
        for provincia in municipios.Provincia.diccionarioProv.items():
            if provincia.provinciaID == textoFinal:
                for router in routers.Router.diccionarioRouter.keys():
                    if provincia.provinciaID == routers.Router.diccionarioRouter[router].provinciaID:
                        for conexion in routers.Router.diccionarioRouter[router].conexiones.items():
                            #Esto hace un print del resultado de la funcion en un text box y lo imprime con un delay de 0.1 segundos
                            self.valueChanged.emit(conexion)
                            time.sleep(0.1)

    def mostrarConexionesPorDepartamento(self):
        text = self.textEdit.toPlainText().strip()
        texto = quitarTildes(text)
        textoFinal = string.capwords(texto)
        # agarro el deptoID que corresponde a la depto seleccionado
        for departamento in municipios.Provincia.diccionarioDptos.items():
            if departamento.departamentoID == textoFinal:
                #me fijo para cada router donde coincide el deptoID con el filtrado
                for router in routers.Router.diccionarioRouter.keys():
                    if departamento.departamentoID == routers.Router.diccionarioRouter[router].departamentoID:
                        for conexion in routers.Router.diccionarioRouter[router].conexiones.items():
                            self.valueChanged.emit(conexion)
                            time.sleep(0.1)
   
    def mostrarConexionesPorMunicipio(self):
        text = self.textEdit.toPlainText().strip()
        texto = quitarTildes(text)
        textoFinal = string.capwords(texto)
        # agarro el muniID que corresponde al muni seleccionado
        for municipio in municipios.Departamento.diccionarioMunicipios.items():
            if municipio.municipioID == textoFinal:
                #me fijo para cada router donde coincide el muniID con el filtrado
                for router in routers.Router.diccionarioRouter.keys():
                    if municipio.municipioID == routers.Router.diccionarioRouter[router].municipioID:
                        for conexion in routers.Router.diccionarioRouter[router].conexiones.items():
                            self.valueChanged.emit(conexion)
                            time.sleep(0.1)


# Esta clase es para ejecutar la opcion 6
class Ui_FormVerConexEntreFechas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None

    def setupUi(self,MainWindow,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow

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

        self.backButton = QPushButton()
        self.backButton.setGeometry(QtCore.QRect(380, 100, 71, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Volver")
        self.verticalLayout.addWidget(self.backButton)


        #### Acciones ####

        # PD: abria que validar que "fecha fin > fecha inicio" 
        
        # Console log de las fechas elegidas
        
        self.botonSeleccionarFechaInicio.clicked.connect(lambda: self.asignarFechaInicio())
        self.botonSeleccionarFechaFin.clicked.connect(lambda: self.asignarFechaFin())


        # Se ejecuta la funcion que muestra las conexiones entre las dos fechas seleccionadas
        self.botonIngresoRangoFechas.clicked.connect(lambda: self.mostrarConexionesEntreFechas(self.fechaInicio,self.fechaFin))
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    def asignarFechaInicio(self):
        self.fechaInicio = QDateTime(self.calendarInicio.selectedDate()).toPyDateTime()

    def asignarFechaFin(self):
        self.fechaFin = QDateTime(self.calendarFechaFin.selectedDate()).toPyDateTime()

    def mostrarConexionesEntreFechas(self,fechaInicio,fechaFin):
        print('Fecha desde: ',fechaInicio)
        print('Fecha hasta: ',fechaFin)
        print('\n')
        print("Aca se ejecuta la funcion que muestra las conexiones entre las dos fechas")
        
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
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConAlfanumerico(self))

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
        print('ID del router a agregar: ',texto)

# Esta clase es para ejecutar la opcion 8
class Ui_FormEliminarRouter(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(240, 150, 120, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConAlfanumerico(self))

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
        self.label.setText(_translate("Form", "Ingrese router ID a eliminar:"))
        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter(self.textEdit.toPlainText()))

    def funcionAgregarRouter(self,texto):
        print('ID del router a eliminar: ',texto)

# Esta clase es para ejecutar la opcion 9
class Ui_FormAgregarConexion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(400, 150, 120, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConAlfanumerico(self))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 160, 350, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(_translate("Form", "Ingrese direccion ID de la conexion a agregar:"))
        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter(self.textEdit.toPlainText()))

    def funcionAgregarRouter(self,texto):
        print('Direccion IP de la conexion a agregar: ',texto)

# Esta clase es para ejecutar la opcion 10
class Ui_FormEliminarConexion(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 323)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 150, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(400, 150, 120, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(lambda: botonSeleccionar_enableConAlfanumerico(self))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Seleccionar"))
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 160, 350, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(_translate("Form", "Ingrese direccion IP de la conexion a eliminar:"))

        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter(self.textEdit.toPlainText()))

    def funcionAgregarRouter(self,texto):
        print('Direccion IP a eliminar: ',texto)

# Para validar que se ingrese un alfanumerico con regex: AAA000-00
def botonSeleccionar_enableConAlfanumerico(self):
    pattern = '^([A-Z]{3})([0-9]{3})-([0-9]{2})'
    text = self.textEdit.toPlainText()
    if len(text) != 0:
        try:
            if re.fullmatch(pattern,text):
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
    else:
        self.pushButton.setEnabled(False)

# Para que validar que no pueda apretar el boton seleccionar con un numero (prov, depto, muni)
def botonSeleccionar_enableConTexto(self):
    
    #en realidad esta lista de provincias debeseria ser extraida de la base de datos nuestra, o sea de las prov que existen en nuestro sistema por el momento
    tuplaProvincias = ('Buenos Aires','Catamarca','Chaco','Chubut','Cordoba','Corrientes','Entre Rios','Formosa','Jujuy','La Pampa','La Rioja','Mendoza','Misiones','Neuquen','Rio Negro','Salta','San Juan','San Luis','Santa Cruz','Santa Fe','Santiago Del Estero','Tierra Del Fuego','Tucuman',)
    
    text = self.textEdit.toPlainText().strip()
    texto = quitarTildes(text)
    textoFinal = string.capwords(texto)
    #quitar tildes, hacer capitalize
    if len(textoFinal) != 0:
        try:
            if textoFinal.isnumeric() == False and textoFinal in tuplaProvincias:
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
    else:
        self.pushButton.setEnabled(False)

def quitarTildes(texto):
        replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
        for a, b in replacements:
            texto = texto.replace(a, b).replace(a.upper(), b.upper())
        return texto

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

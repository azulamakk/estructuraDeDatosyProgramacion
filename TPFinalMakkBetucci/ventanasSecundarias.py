from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QCalendarWidget, QLabel, QWidget, QListWidget,QListWidgetItem, QHBoxLayout, QMainWindow,QPushButton,QApplication
import sys,os
import time
import threading
from PyQt5.QtCore import Qt,QUrl,QRect,QDateTime
from datetime import datetime
import re
import calendar
import string
import lecturaArchivos, municipios, routers, conexiones
#aca importar las funciones del menu que vamos a ejecutar

# Clase auxiliar
class Ui_FormRouters(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 426)
        self.labelCargarArchivoMuni = QtWidgets.QLabel(Form)
        self.labelCargarArchivoMuni.setGeometry(QtCore.QRect(100, 140, 221, 16))

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

        self.layoutPrincipal = QHBoxLayout() 

        self.labelCargarArchivoMuni = QLabel("Arrastre o adjunte archivo municipios:")
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
        self.backButton.clicked.connect(lambda: self.close())

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
            lecturaArchivos.cargarProvinciasyDptos(pathMuni)
            msg = QMessageBox()
            msg.setInformativeText("Archivo cargado correctamente")
            msg.exec_()
        
# Esta clase es para ejecutar la opcion 2
class Ui_FormRouter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cargar archivo routers")
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
        self.backButton.clicked.connect(lambda: self.close())

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
            lecturaArchivos.leerArchivoRouter(pathRouter)
            lecturaArchivos.leerArchivoConexiones('conexiones.csv')
            msg = QMessageBox()
            msg.setInformativeText("Archivo cargado correctamente")
            msg.exec_()

# Esta clase es para ejecutar la opcion 3,4 y 5
class Ui_FormVerConexPorUbicacion(QtWidgets.QMainWindow):   
    valueChanged = QtCore.pyqtSignal(str)
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
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese una provincia:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorProvincia)

        elif ubicacion == 'departamento':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un departamento:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorDepartamento)

        elif ubicacion == 'municipio':
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(20, 160, 180, 16))
            self.label.setObjectName("label")
            self.label.setText(_translate("Form", "Ingrese un municipio:"))
            self.pushButton.clicked.connect(self.mostrarConexionesPorMunicipio)

        self.valueChanged.connect(self.on_value_changed)
        self.pushButton.clicked.connect(self.on_clicked)

        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

    @QtCore.pyqtSlot()
    def on_clicked(self):
        #self.textEdit.clear()
        self.textEdit.setGeometry(QtCore.QRect(210, 150, 140, 100))

        if self.ubicacion == 'provincia':
            threading.Thread(target=self.mostrarConexionesPorProvincia, daemon=True).start()
        if self.ubicacion == 'departamento':
            threading.Thread(target=self.mostrarConexionesPorDepartamento, daemon=True).start()
        if self.ubicacion == 'municipio':
            threading.Thread(target=self.mostrarConexionesPorMunicipio, daemon=True).start()

    @QtCore.pyqtSlot(str)
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
            if provincia[1].provincia == textoFinal:
                for router in routers.Router.diccionarioRouter.keys():
                    if provincia[1].provinciaID == routers.Router.diccionarioRouter[router].provinciaID:
                        for conexion in routers.Router.diccionarioRouter[router].conexiones.items():
                            #Esto hace un print del resultado de la funcion en un text box y lo imprime con un delay de 0.1 segundos
                            self.valueChanged.emit(str(conexion[0])) #imprime la direccion IP de la conexion (es la key de la tupla item)
                            time.sleep(0.1)

    #Funcion que muestra las conexiones por departamento dado             
    def mostrarConexionesPorDepartamento(self):
        text = self.textEdit.toPlainText().strip()
        texto = quitarTildes(text)
        textoFinal = string.capwords(texto)
        for provincia in municipios.Provincia.diccionarioProv.items():
            for departamento in provincia[1].diccionarioDptos.items():
                if departamento[1].departamento == textoFinal:
                    for router in routers.Router.diccionarioRouter.keys():
                        if departamento[0] == routers.Router.diccionarioRouter[router].departamentoID:
                            for conexion in routers.Router.diccionarioRouter[router].conexiones.items():
                                self.valueChanged.emit(str(conexion[0]))
                                time.sleep(0.1)
   
    #Funcion que muestra las conexiones por municipio dado
    def mostrarConexionesPorMunicipio(self):
        text = self.textEdit.toPlainText().strip()
        texto = quitarTildes(text)
        textoFinal = string.capwords(texto)
        for provincia in municipios.Provincia.diccionarioProv.items():
            for departamento in provincia[1].diccionarioDptos.items():
                for municipio in departamento[1].diccionarioMunicipios.items():
                    if municipio[1].municipio == textoFinal:
                        for router in routers.Router.diccionarioRouter.items():
                            if municipio[1].departamentoID == router[1].departamentoID:
                                for conexion in router[1].conexiones.items():
                                    self.valueChanged.emit(str(conexion[0]))
                                    time.sleep(0.1)

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
        self.backButton.clicked.connect(lambda: self.secondWidgetWindow.close())

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
        for router in routers.Router.diccionarioRouter.items():
            for conexion in router[1].conexiones.items():
                if conexion[1].fechaYHora > self.fechaInicio and conexion[1].fechaYHora < self.fechaFin:
                    self.valueChanged.emit(str(conexion[0]))
                    #time.sleep(0.1)
        
# Esta clase es para ejecutar la opcion 7
class Ui_FormAgregarRouter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Form")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.diccionarioObjetos = dict()

        i = 0
        cantidadDeCamposRouter = 8
        while i < cantidadDeCamposRouter:
            if i == 1:
                self.agregarObjetos(i,'Ingresar identificador: ')
            elif i == 2:
                self.agregarObjetos(i,'Ingresar identificador: ')
            elif i == 3:
                self.agregarObjetos(i,'Ingresar ubicacion: ')
            elif i == 4:
                self.agregarObjetos(i,'Ingresar latitud: ')
            elif i == 5:
                self.agregarObjetos(i,'Ingresar longitud: ')
            elif i == 6:
                self.agregarObjetos(i,'Ingresar municipio_id: ')
            elif i == 7:
                self.agregarObjetos(i,'Ingresar provincia_id: ')
            elif i == 8:
                self.agregarObjetos(i,'Ingresar id_departamento: ')
            i += 1    

        # Push button para seleccionar el ID escrito
        # Aca validar si no existe ya el router, blockear el boton de seleccionar o enviar un mensaje en rojo "eliga nu router no repetido"
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Agregar router")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionAgregarRouter())

        # Text box y su label para ingresar por teclado el router ID
    def agregarObjetos(self,i,campo):
        Hlayout = "horizontalLayout" + str(i)
        self.Hlayout = QtWidgets.QHBoxLayout()

        label = "label" + str(i)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(campo)
        self.label.setText(campo)
        self.Hlayout.addWidget(self.label)

        textEdit = "textEdit" + str(i)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit"+str(i))
        self.Hlayout.addWidget(self.textEdit)        

        self.diccionarioObjetos[self.label.objectName()] = ''
        self.verticalLayout.addLayout(self.Hlayout)

    def funcionAgregarRouter(self):            
        for k,v in self.diccionarioObjetos.items():
            print('{}{}'.format(k,v))

        msg = QMessageBox()
        msg.setInformativeText("Router agregado correctamente")
        msg.exec_()

# Esta clase es para ejecutar la opcion 8
class Ui_FormEliminarRouter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Form")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # Text box y su label para ingresar por teclado el router ID
        self.Hlayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName('labelIngresoDireccionIP')
        self.label.setText('Ingresar router ID: ')
        self.Hlayout.addWidget(self.label)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.Hlayout.addWidget(self.textEdit)        

        self.verticalLayout.addLayout(self.Hlayout)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar router")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionEliminarRouter())

    def funcionEliminarRouter(self):            
        print(self.textEdit.toPlainText())
        msg = QMessageBox()
        msg.setInformativeText("Router eliminado correctamente")
        msg.exec_()

# Esta clase es para ejecutar la opcion 9
class Ui_FormAgregarConexion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Form")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.diccionarioObjetos = dict()

        i = 0
        cantidadDeCamposRouter = 6
        while i < cantidadDeCamposRouter:
            if i == 1:
                self.agregarObjetos(i,'Ingresar direccion IP: ')
            elif i == 2:
                self.agregarObjetos(i,'Ingresar MAC Address: ')
            elif i == 3:
                self.agregarObjetos(i,'Fecha: ')
            elif i == 4:
                self.agregarObjetos(i,'Horario: ')
            #quizas no hace falta esto, total toda conexion que agregas deberia estar activa, salvo que ya este completo el cupo de 20 conexiones por router
            elif i == 5:
                self.agregarObjetos(i,'Activa: ')
            i += 1    

        # Push button para seleccionar el ID escrito
        # Aca validar si no existe ya el router, blockear el boton de seleccionar o enviar un mensaje en rojo "eliga nu router no repetido"
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Agregar conexion")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionAgregarConexion())

        # Text box y su label para ingresar por teclado el router ID
    def agregarObjetos(self,i,campo):
        Hlayout = "horizontalLayout" + str(i)
        self.Hlayout = QtWidgets.QHBoxLayout()

        label = "label" + str(i)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(campo)
        self.label.setText(campo)
        self.Hlayout.addWidget(self.label)

        textEdit = "textEdit" + str(i)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit"+str(i))
        self.Hlayout.addWidget(self.textEdit)        

        self.diccionarioObjetos[self.label.objectName()] = ''
        self.verticalLayout.addLayout(self.Hlayout)

    def funcionAgregarConexion(self):            
        for k,v in self.diccionarioObjetos.items():
            print('{}{}'.format(k,v))

        msg = QMessageBox()
        msg.setInformativeText("Conexion agregada correctamente")
        msg.exec_()

# Esta clase es para ejecutar la opcion 10
class Ui_FormEliminarConexion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Form")
        self.centralwidget = QtWidgets.QWidget(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 421, 233))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        # Text box y su label para ingresar por teclado el router ID
        self.Hlayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName('labelIngresoDireccionIP')
        self.label.setText('Ingresar direccion IP: ')
        self.Hlayout.addWidget(self.label)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.Hlayout.addWidget(self.textEdit)        

        self.verticalLayout.addLayout(self.Hlayout)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Eliminar conexion")
        self.verticalLayout.addWidget(self.pushButton)

        Form.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda: self.funcionEliminarConexion())

    def funcionEliminarConexion(self):            
        print(self.textEdit.toPlainText())
        msg = QMessageBox()
        msg.setInformativeText("Conexion eliminada correctamente")
        msg.exec_()

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
    text = self.textEdit.toPlainText().strip()
    texto = quitarTildes(text)
    textoFinal = string.capwords(texto)
    #quitar tildes, hacer capitalize
    if len(textoFinal) != 0:
        try:
            #El setProvincias/setDeptos/setMunicipios es extraido de la base de datos nuestra, o sea de las prov que existen en nuestro sistema por el momento
            if textoFinal.isnumeric() == False and (textoFinal in municipios.Provincia.setProvincias or textoFinal in municipios.Departamento.setDepartamentos or textoFinal in municipios.Municipio.setMunicipios):
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
        except:
            self.pushButton.setEnabled(False)
    else:
        self.pushButton.setEnabled(False)

# Funcion para quitar tildes
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

# Funcion para convertir el formato de fecha
def parseDate(fechahora):
    fecha = fechahora.split(" ")[0]
    hora = fechahora.split(" ")[1]

    dateParts = fecha.split("-")
    if len(dateParts) < 3:
        return None
    [year, month, day] = dateParts

    timeParts = hora.split(":")
    if len(timeParts) < 2:
        return None
    [hour, minute, seconds] = timeParts

    return datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds))
 


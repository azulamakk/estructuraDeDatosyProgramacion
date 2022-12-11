from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from ventanasSecundarias.opcion1 import VentanaCargarMunicipio
from ventanasSecundarias.opcion2 import Ui_FormRouter
from ventanasSecundarias.opcion345 import Ui_FormVerConexPorUbicacion
from ventanasSecundarias.opcion6 import Ui_FormVerConexEntreFechas
from ventanasSecundarias.opcion7 import Ui_FormAgregarRouter
from ventanasSecundarias.opcion8 import Ui_FormEliminarRouter
from ventanasSecundarias.opcion9 import Ui_FormAgregarConexion
from ventanasSecundarias.opcion10 import Ui_FormEliminarConexion

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        # cssFile="TPFinalMakkBetucci/styles.css"

        # with open(cssFile,"r") as css:
        #     self.setStyleSheet(css.read())
        MainWindow.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        MainWindow.resize(621, 457)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.botonSeleccionarOpcion = QtWidgets.QPushButton(self.centralwidget)
        self.botonSeleccionarOpcion.setGeometry(QtCore.QRect(430, 290, 121, 31))
        self.botonSeleccionarOpcion.setObjectName("botonSeleccionarOpcion")
        self.ingreseOpcionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ingreseOpcionLabel.setGeometry(QtCore.QRect(110, 280, 131, 41))

        self.ingreseOpcionLabel.setObjectName("ingreseOpcionLabel")
        self.textEditIngresoOpcion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditIngresoOpcion.setGeometry(QtCore.QRect(250, 290, 171, 31))
        self.textEditIngresoOpcion.setObjectName("textEditIngresoOpcion")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 461, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelSaludo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelSaludo.setObjectName("labelSaludo")
        self.verticalLayout.addWidget(self.labelSaludo)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botonSeleccionarOpcion.setEnabled(False)
        self.textEditIngresoOpcion.textChanged.connect(self.capturarOpcion)

    def capturarOpcion(self):

        texto = self.textEditIngresoOpcion.toPlainText()
        if len(texto) != 0:
            if texto.isnumeric() == False:
                try:
                    opcionIndicada = int(texto)
                    if opcionIndicada in range(1,12):
                        self.botonSeleccionarOpcion.setEnabled(True)
                    else:
                        self.botonSeleccionarOpcion.setEnabled(False)
                except:
                    self.botonSeleccionarOpcion.setEnabled(False)
        else:
            self.botonSeleccionarOpcion.setEnabled(False)
        
        if texto.isnumeric() == True:
            opcionIndicada = int(texto)
            if opcionIndicada == 1:
                self.botonSeleccionarOpcion.clicked.connect(self.ventanaLeerArchivoMuni)
            elif opcionIndicada == 2:
                self.botonSeleccionarOpcion.clicked.connect(self.ventanaLeerArchivoRouters)
            elif opcionIndicada == 3:
                self.botonSeleccionarOpcion.clicked.connect(self.verConexionesPorProvincia)
            elif opcionIndicada == 4:
                self.botonSeleccionarOpcion.clicked.connect(self.verConexionesPorDepartamento)
            elif opcionIndicada == 5:
                self.botonSeleccionarOpcion.clicked.connect(self.verConexionesPorMunicipio)
            elif opcionIndicada == 6:
                self.botonSeleccionarOpcion.clicked.connect(self.verConexionesEntreFechas)
            elif opcionIndicada == 7:
                self.botonSeleccionarOpcion.clicked.connect(self.agregarRouter)
            elif opcionIndicada == 8:
                self.botonSeleccionarOpcion.clicked.connect(self.eliminarRouter)
            elif opcionIndicada == 9:
                self.botonSeleccionarOpcion.clicked.connect(self.agregarConexion)
            elif opcionIndicada == 10:
                self.botonSeleccionarOpcion.clicked.connect(self.eliminarConexion)
            elif opcionIndicada == 11:
                self.botonSeleccionarOpcion.clicked.connect(lambda: QApplication.quit()) 
                print('\n---PROGRAMA FINALIZADO---\n')

    #Cargar archivo municipios
    def ventanaLeerArchivoMuni(self):
        demo = VentanaCargarMunicipio()
        demo.show()

    #Cargar archivo routers
    def ventanaLeerArchivoRouters(self):
        demo = Ui_FormRouter()
        demo.show()
    
    #Ver N° de conexiones por provincia dada 
    def verConexionesPorProvincia(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_FormVerConexPorUbicacion()
        self.ui.setupUi(self.Form,'provincia',self.Form)
        self.Form.show()
        
    #Ver N° de conexiones por departamento dado 
    def verConexionesPorDepartamento(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_FormVerConexPorUbicacion()
        self.ui.setupUi(self.Form,'departamento',self.Form)
        self.Form.show()
    
    #Ver N° de conexiones por municipio dado 
    def verConexionesPorMunicipio(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_FormVerConexPorUbicacion()
        self.ui.setupUi(self.Form,'municipio',self.Form)
        self.Form.show()
    
    #Filtrar y mostrar la # de conexiones entre dos fechas dadas
    def verConexionesEntreFechas(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_FormVerConexEntreFechas()
        self.ui.setupUi(self.Form,self.Form)
        self.Form.show()
        return

    #Agregar un router (validar los datos)
    def agregarRouter(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_FormAgregarRouter()
        self.ui.setupUi(self.Form,self.Form)
        self.Form.show()
    
    #Eliminar un router
    def eliminarRouter(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_FormEliminarRouter()
        self.ui.setupUi(self.Form,self.Form)
        self.Form.show()

    #Agregar una conexion (validar los datos)
    def agregarConexion(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_FormAgregarConexion()
        self.ui.setupUi(self.Form,self.Form)
        self.Form.show()

    #Eliminar una conexion
    def eliminarConexion(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_FormEliminarConexion()
        self.ui.setupUi(self.Form,self.Form)
        self.Form.show()

    #Funcion que le cambia el text a algunos objetos
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.botonSeleccionarOpcion.setText(_translate("MainWindow", "Seleccionar"))
        self.ingreseOpcionLabel.setText(_translate("MainWindow", "Ingrese una opción:"))
        self.labelSaludo.setText(_translate("MainWindow", "Bienvenidos al Sistema de Información de País Digital"))
        self.label.setText(_translate("MainWindow", '''
        1. Cargar nuevo archivo de municipios
        2. Cargar nuevo archivo de puntos de acceso
        3. Ver N° de conexiones por provincia dada
        4. Ver N° de conexiones por departamento dado
        5. Ver N° de conexiones por municipio dado
        6. Ver N° de conexiones totales en el pais entre 2 fechas y horas dadas
        7. Agregar un router
        8. Dar de baja un router
        9. Agregar conexiones
        10. Quitar conexiones
        11. Salir'''))

    #Main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
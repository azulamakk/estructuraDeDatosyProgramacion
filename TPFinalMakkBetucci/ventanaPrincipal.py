from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from ventanasSecundarias import Ui_FormMunis, Ui_FormRouter, Ui_FormVerConexProv, ListboxWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botonSeleccionarOpcion = QtWidgets.QPushButton(self.centralwidget)
        self.botonSeleccionarOpcion.setGeometry(QtCore.QRect(430, 290, 121, 31))
        self.botonSeleccionarOpcion.setObjectName("botonSeleccionarOpcion")
        self.ingreseOpcionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ingreseOpcionLabel.setGeometry(QtCore.QRect(110, 280, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ingreseOpcionLabel.setFont(font)
        self.ingreseOpcionLabel.setObjectName("ingreseOpcionLabel")
        self.textEditIngresoOpcion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditIngresoOpcion.textChanged.connect(self.botonSeleccionar_enable)
        self.textEditIngresoOpcion.setGeometry(QtCore.QRect(250, 290, 171, 31))
        self.textEditIngresoOpcion.setObjectName("textEditIngresoOpcion")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 10, 461, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSaludo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.labelSaludo.setFont(font)
        self.labelSaludo.setObjectName("labelSaludo")
        self.verticalLayout.addWidget(self.labelSaludo)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textEditIngresoOpcion.textChanged.connect(self.capturarOpcion)

    def capturarOpcion(self):
        
        opcionIndicada = self.textEditIngresoOpcion.toPlainText()
        #self.textEditIngresoOpcion.clear()
        opcionIndicada = int(opcionIndicada)

        if opcionIndicada == 1:
            self.botonSeleccionarOpcion.clicked.connect(self.ventanaLeerArchivoMuni)
            return
        elif opcionIndicada == 2:
            self.botonSeleccionarOpcion.clicked.connect(self.ventanaLeerArchivoRouters)
            return
        elif opcionIndicada == 3:
            self.botonSeleccionarOpcion.clicked.connect(self.verConexionesPorProvincia)
            return
        
    #Cargar archivo municipios
    def ventanaLeerArchivoMuni(self):
        demo = Ui_FormMunis()
        demo.show()

    #Cargar archivo routers
    def ventanaLeerArchivoRouters(self):
        demo = Ui_FormRouter()
        demo.show()

    #Ver N° de conexiones por provincia dada 
    def verConexionesPorProvincia(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_FormVerConexProv()
        self.ui.setupUi(self.Form)
        self.Form.show()

    #Funcion para cancelar la opcion de apretar el boton en caso de que no se escriba nada o no se ingrese una opcion numerica entre 1 y 11 (inclusive)
    def botonSeleccionar_enable(self):
        texto = self.textEditIngresoOpcion.toPlainText()
        if len(texto) != 0:
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

    #Funcion falopa que le cambia el text a algunos objetos
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonSeleccionarOpcion.setText(_translate("MainWindow", "Seleccionar"))
        self.ingreseOpcionLabel.setText(_translate("MainWindow", "Ingrese una opción:"))
        self.labelSaludo.setText(_translate("MainWindow", "Bienvenidos al Sistema de Información de País Digital"))
        self.label.setText(_translate("MainWindow", "1. Leer archivo de municipios\n2. Leer archivo de puntos de acceso\n3. Ver N° de conexiones por provincia dada\n4. Ver N° de conexiones por departamento dado\n5. Ver N° de conexiones por municipio dado\n6. Ver N° de conexiones totales en el pais entre 2 fechas\n7. Agregar un router\n8. Dar de baja un router\n9. Agregar conexiones\n10. Quitar conexiones\n11. Salir"))

    #Main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

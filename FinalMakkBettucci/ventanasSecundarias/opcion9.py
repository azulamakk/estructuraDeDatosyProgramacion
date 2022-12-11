from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

# Esta clase es para ejecutar la opcion 9
class Ui_FormAgregarConexion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWidgetWindow = None
        
    def setupUi(self, Form,secondWidgetWindow):
        self.secondWidgetWindow = secondWidgetWindow
        Form.setObjectName("Form")
        Form.resize(532, 421)
        Form.setWindowTitle("Opcion ingresada: Agregar conexion")
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
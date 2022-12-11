from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow

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

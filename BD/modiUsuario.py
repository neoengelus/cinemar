import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
import sqlite3

class PantallaModi(QWidget):
    def __init__(self):
        super(PantallaModi, self).__init__()
        loadUi(".\Vistas\modiUsuario.ui",self)
        self.box_dni.setStyleSheet("QTextEdit { padding-left:0; padding-top:0; padding-bottom:0; padding-right:0}");
        self.btnBuscar.clicked.connect(self.llenarboxes)
        self.btnConfirmar.clicked.connect(self.revisarCampos)
        
        
    def llenarboxes(self):
        dniUsuario = self.box_dni.toPlainText()
        #clave = self.passwordfield.text()
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        query =f"SELECT * FROM usuario WHERE dni ='{dniUsuario}'"
        cur.execute(query)
        usuario = cur.fetchone()
        self.boxNombre.setText (usuario[1])
        self.boxApellido.setText (usuario[3])
        self.boxEmail.setText (usuario[2])
        self.boxEdad.setText (str(usuario[4]))
        self.boxPass.setText (usuario[5])
        self.boxTipo.setText (str(usuario[6])) 
        
    def revisarCampos(self):
        dni = self.box_dni.toPlainText()
        nom=self.boxNombre.toPlainText ()
        ape=self.box_dni.toPlainText()
        email=self.boxEmail.toPlainText()
        edad=self.boxEdad.toPlainText()
        tipo=self.boxTipo.toPlainText()
        if dni=="" or nom=="" or ape==""or email=="" or edad=="" or tipo=="":
            QMessageBox.critical(self, "Error","No pueden haber campos vacios")
# main
BD = "./Cinemar.db"
app = QApplication(sys.argv)
pantModi1 = PantallaModi()
widget = QtWidgets.QStackedWidget()
widget.addWidget(pantModi1)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
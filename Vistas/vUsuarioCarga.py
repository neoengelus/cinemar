'''
Created on 12 dic. 2022

@author: engelus
'''


from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QLineEdit, qApp
from PyQt5.Qt import QMainWindow, QWidget
from BD import bdUsuario
from Clases.Usuario import Usuario

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaUsuarioCarga(QWidget):
  def __init__(self):
    super(ventanaUsuarioCarga, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    try :
      loadUi(".\Vistas\modiUsuario.ui",self)
      self.setWindowTitle("Cinemar - Registro de Usuario")
      self.setWindowIcon(QtGui.QIcon(ICON))
      self.btnBuscar.hide()
      self.btnConfirmar.setText("Registrarse")
      self.box_dni.setText("")
      self.boxTipo.hide()
      self.label_7.hide()
      self.tableListUsu.hide()
      self.show()
    except Exception as e:
      print(str(e))
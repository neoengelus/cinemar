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
      self.btnConfirmar.clicked.connect(lambda: self.registro())
      self.box_dni.setText("")
      self.boxTipo.hide()
      self.label_7.hide()
      self.tableListUsu.hide()
      self.show()
    except Exception as e:
      print(str(e))
      
  def registro(self):
    try :
      dni = self.box_dni.toPlainText()
      edad = self.boxEdad.toPlainText()
      nombre = self.boxNombre.toPlainText()
      apellido = self.boxApellido.toPlainText()
      mail = self.boxEmail.toPlainText()
      passw = self.boxPass.toPlainText()
      if self.esNumero(dni) :
        if edad.isdigit() :
          resultado = bdUsuario.buscarUsuario(BD, dni)
          if resultado == None :
            nuevoUsuario = Usuario(nombre, apellido, edad, dni, mail)
            bdUsuario.altaUsuario(BD, nuevoUsuario, passw)
            self.exito(f"Se creó correctamente el usuario {dni}")
          else :
            self.error(f"El usuario {dni} ya existe")
        else :
          self.error("La edad debe ser un número")
      else :
        self.error("El DNI debe ser un número y no debe tener puntos")
    except Exception as e:
      print(str(e))
    
  def error(self,mensaje):
    QMessageBox.critical(self, "Error", mensaje)
  
  def confirmar(self,mensaje):
    if QMessageBox.question(self, "Eliminación", mensaje) == QMessageBox.Yes:
      return True
    else :
      return False
    
  def exito(self,mensaje):
    QMessageBox.information(self, "Éxito", mensaje)
  
  def info(self):
    QMessageBox.about(self, "Sistema de Gestión Cinemar", "Desarrollado por CodeWarriors \nUsando Python 3 y Qt 5 \nBajo Licencia GPL")
    
  def esNumero(self, num):
    try:
        float(num)
        return True
    except ValueError:
      return False
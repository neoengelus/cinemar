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
from Vistas import vUsuarioCarga

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaLogin(QWidget):
  def __init__(self):
    super(ventanaLogin, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\login.ui",self)
    self.setWindowTitle("Cinemar - Inicio de Sesión")
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.btn_login.clicked.connect(lambda: self.entrar())
    self.btn_registrar.clicked.connect(lambda: self.registro())
    self.box_clave.setEchoMode(QLineEdit.Password)
    
    self.show()
    
  def entrar(self):
    dni = self.box_email.text()
    passw = self.box_clave.text()
    try :
      if dni == "" or  passw == "" :
        self.error("Los Campos DNI o Clave no deben estar vacíos")
      elif self.esNumero(dni):
        resultado = bdUsuario.buscarUsuario(BD, dni)
        if resultado != None :
          if resultado[5] == passw :
            pass
            #mostrar la pantalla de acuerdo al tipo de usuario 
          else :
            self.error("Contraseña incorrecta")
        else :
          self.error(f"No se econtró el usuario {dni}")
      else:
        self.error("El campo DNI debe ser numérico")
    except Exception as e :
      print(str(e))
  
  def registro(self):
    self.carga = vUsuarioCarga.ventanaUsuarioCarga()
  
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
  
  def closeEvent(self, event):
    #Cierra todas las ventanas abiertas
    try:
        self.carga.close() 
    except:
        pass
'''
Created on 5 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView
from PyQt5.Qt import QMainWindow, QWidget
from BD import bdSala


BD = "./Cinemar.db"

class ventanaSalaCarga(QWidget):
  def __init__(self):
    super(ventanaSalaCarga, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\salaCarga.ui",self)
    self.setWindowIcon(QtGui.QIcon("./Assets/cine.png"))
    self.btnCargarSala.clicked.connect(lambda: self.cargarSala())
    self.show()  
  
  def cargarSala(self):
    capacidad = self.txtCapacidad.text()
    costo = self.txtCosto.text()
    peli = self.txtIdPeli.text()
    ocupada = self.txtOcupada.text()
    
    if capacidad == "" or costo == "" or peli == "" :
      self.error("Los valores de Capacidad, Costo e Id Película son obligatorios")
      if self.esNumero(costo) and self.esNumero(capacidad) and self.esNumero(ocupada) :
        pass
      else :
        self.error("Los Valores de Costo, Capacidad y Butacas Ocupadas deben ser numéricos")
      
    
  def error(self,mensaje):
    QMessageBox.critical(self, "Error", mensaje)
  
  def confirmar(self,mensaje):
    if QMessageBox.question(self, "Eliminación", mensaje) == QMessageBox.Yes:
      return True
    else :
      return False
  
  def esNumero(self, num):
    try:
        float(num)
        return True
    except ValueError:
      return False
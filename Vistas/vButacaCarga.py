'''
Created on 7 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import QWidget
from BD import bdSala, bdButaca
from Clases.Butaca import Butaca
import string

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaButacaCarga(QWidget):
  def __init__(self):
    super(ventanaButacaCarga, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Cargabutaca.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.btnCargar.clicked.connect(lambda: self.cargar())
    self.show()
    
  def cargar(self):
    sala = self.txtNroSala.text()
    fila = self.txtFila.text().upper()
    asiento = self.txtAsiento.text()
    if not self.esNumero(sala) or sala == "" :
      self.error("El Valor de la Sala debe ser numérico")
    elif not self.esLetra(fila) or fila == "" :
      self.error("El Valor de la Fila debe ser una letra")
    elif not self.esNumero(asiento) or asiento == "" :
      self.error("El Valor del Asiento debe ser numérico")
    else :
      butaca = Butaca(fila, asiento, sala)
      resultados = bdButaca.buscarButaca(BD, butaca)
      capacidad = bdSala.capacidadSala(BD, sala)
      if resultados != [] :
        self.error("La butaca ya se encuntra agregada")
      elif capacidad[0] == capacidad[1] :
        self.error("La Sala se encuentra llena")
      else:
          existe_sala = bdSala.buscarSala(BD, sala)
          if existe_sala != [] :
            bdButaca.cargarButaca(BD, butaca)
            bdSala.actualizarCapacidad(BD, sala, int(capacidad[1]) + 1)
            self.exito(f"Se agregó correctamente la butaca\n{butaca}")
          else :
            self.error(f"No existe la Sala Nº {sala}")
    
  def esNumero(self, num):
    try:
        float(num)
        return True
    except ValueError:
      return False
  
  def esLetra(self, letra):
    abc = string.ascii_uppercase
    if abc.find(letra) != -1 :
      return True
    else :
      return False
  
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
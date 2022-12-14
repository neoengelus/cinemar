'''
Created on 14 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala, bdFuncion, bdReserva
from datetime import datetime
import time

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaReserva(QMainWindow):
  def __init__(self):
    super(ventanaReserva, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Reserva.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.cargarTabla()
    self.tabla.clicked.connect(lambda : self.cargarCombo())
    self.show()
    
  def cargarTabla(self):
    try :
      self.resultados = bdFuncion.mostrarFuncion(BD)
      self.tabla.setRowCount(len(self.resultados))
      print(self.resultados)
      tablerow = 0
      for resultado in self.resultados:
        self.tabla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(resultado[4])))
        self.tabla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.determinarTipoSala(resultado[8])))
        self.tabla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(resultado[9])))
        self.tabla.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(resultado[2])))
        self.tabla.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(resultado[1])))
        self.tabla.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(resultado[5])))
        tablerow+=1
    except Exception as e:
      print(str(e))
  
  def cargarCombo(self):
    try :
      lista = self.tabla.currentRow()
      id_sala = self.tabla.item(lista, 0).text()
      capacidad_sala = bdSala.capacidadSala(BD, id_sala)
      fila_sala = capacidad_sala[0] // 10
      for letra in range(65, 65 + fila_sala):
        for i in range(1, fila_sala +1):
          print(chr(letra),i)
    except Exception as e :
      print(str(e))
  
  def determinarTipoSala(self, tipo):
    if tipo : 
      return "3D"
    else :
      return "2D" 
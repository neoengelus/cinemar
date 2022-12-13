'''
Created on 13 dic. 2022

@author: engelus
'''
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala, bdFuncion

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaFuncion(QMainWindow):
  def __init__(self):
    super(ventanaFuncion, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Cargafuncion.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    #self.tabla.setSelectionBehavior(QTableView.selectRows)
    self.btnCargar.clicked.connect(lambda: self.cargar())
    self.cargarTabla()
    self.show()
    
  def cargarTabla(self):
    resultados = bdSala.mostarSalas(BD, 2)
    self.tabla.setRowCount(len(resultados))
    tablerow = 0
    for resultado in resultados:
      pelicula = bdSala.buscarPelicula(BD, int(resultado[5]))
      self.tabla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(resultado[0])))
      self.tabla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.determinarTipoSala(resultado[1])))
      self.tabla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(resultado[2])))
      self.tabla.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(resultado[3])))
      self.tabla.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(resultado[4])))
      self.tabla.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(pelicula[3])))
      tablerow+=1
  
  def cargar(self):
    pass
  
  def determinarTipoSala(self, tipo):
    if tipo : 
      return "3D"
    else :
      return "2D" 
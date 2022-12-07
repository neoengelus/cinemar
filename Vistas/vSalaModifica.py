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
ICON = "./Assets/cine.png"

class ventanaSalaModifica(QWidget):
  def __init__(self, lista):
    super(ventanaSalaModifica, self).__init__()
    self.infoSala = lista
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\salaModifica.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.txtSala.setText(self.infoSala[0])
    self.cmbTipoSala.setCurrentIndex(self.determinarTipoSala(self.infoSala[1]))
    self.txtCapacidad.setText(self.infoSala[2])
    self.txtOcupada.setText(self.infoSala[3])
    self.txtCosto.setText(self.infoSala[4])
    self.txtIdPeli.setText(self.infoSala[5])
    self.btnActulizarSala.clicked.connect(lambda: self.actualizarSala())
    self.btnMostrarPeli.clicked.connect(lambda: self.mostrarPeli())
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.tabla.clicked.connect(lambda : self.celdaClick())
    self.tabla.setVisible(False)
    self.show()  
      
  def error(self,mensaje):
    QMessageBox.critical(self, "Error", mensaje)
  
  def confirmar(self,mensaje):
    if QMessageBox.question(self, "Eliminación", mensaje) == QMessageBox.Yes:
      return True
    else :
      return False
  
  def exito(self,mensaje):
    QMessageBox.information(self, "Éxito", mensaje)
  
  def esNumero(self, num):
    try:
        float(num)
        return True
    except ValueError:
      return False
  
  def determinarTipoSala(self, tipo):
    if tipo == "2D" :
      return 0
    else :
      return 1
  
  def actualizarSala(self):
    try:
      lista = list()
      lista.append(self.infoSala[0])
      lista.append(self.cmbTipoSala.currentIndex())
      lista.append(self.txtCapacidad.text())
      lista.append(self.txtOcupada.text())
      lista.append(self.txtCosto.text())
      lista.append(self.id_pelicula)
      print(lista)
      bdSala.actualizaSala(BD,lista)
      self.exito(f"Se realizó con éxito la actualización de la Sala Nº {self.infoSala[0]}")
    except Exception as e:
      print(str(e))
  
  def mostrarPeli(self):
    self.tabla.setVisible(True)
    resultados = bdSala.cargarPeliculas(BD)
    tablerow = 0
    self.tabla.setRowCount(len(resultados))
    for resultado in resultados:
      self.tabla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(resultado[0])))
      self.tabla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(resultado[1])))
      self.tabla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(resultado[2])))
      self.tabla.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(resultado[3])))
      self.tabla.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(resultado[4])))
      tablerow+=1
  
  def celdaClick(self):
    lista = self.tabla.currentRow()
    id = self.tabla.item(lista, 0).text()
    self.txtIdPeli.setText(self.tabla.item(lista, 3).text())
    self.id_pelicula = id
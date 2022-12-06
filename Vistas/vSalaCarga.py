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

class ventanaSalaCarga(QWidget):
  def __init__(self):
    super(ventanaSalaCarga, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\salaCarga.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.btnCargarSala.clicked.connect(lambda: self.cargarSala())
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.tabla.clicked.connect(lambda : self.cargarIdPeli())
    self.cargarTabla()
    self.show()  
  
  def cargarSala(self):
    capacidad = self.txtCapacidad.text()
    costo = self.txtCosto.text()
    peli = self.txtIdPeli.text()
    ocupada = self.txtOcupada.text()
    tipo = self.cmbTipoSala.currentIndex()
    
    if capacidad == "" or costo == "" or peli == "" :
      self.error("Los valores de Capacidad, Costo e Id Película son obligatorios")
    elif (self.esNumero(costo) and self.esNumero(capacidad) and self.esNumero(ocupada)) or ocupada == "" :
      if ocupada == "" :
        ocupada = 0 #si no hago esto crashea
      capacidad = int(capacidad)
      costo = float(costo)
      peli = int(peli)
      ocupada = int(ocupada)
      tipo = bool(tipo)
      print(capacidad,costo,peli,ocupada,tipo)
      bdSala.cargarSalaValores(BD,tipo,capacidad,ocupada,costo,peli)
      self.exito("La operación se realizó con éxito")
    else :
      self.error("Los Valores de Costo, Capacidad y Butacas Ocupadas deben ser numéricos")
    
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
    
  def cargarTabla(self):
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
  
  def cargarIdPeli(self):
    lista = self.tabla.currentRow()
    id = self.tabla.item(lista, 0).text()
    self.txtIdPeli.setText(id)
    

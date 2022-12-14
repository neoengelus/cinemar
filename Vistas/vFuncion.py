'''
Created on 13 dic. 2022

@author: engelus
'''
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala, bdFuncion
from datetime import datetime
import time

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaFuncion(QMainWindow):
  def __init__(self):
    super(ventanaFuncion, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Cargafuncion.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.btnCargar.clicked.connect(lambda: self.cargar())
    self.tabla.clicked.connect(lambda : self.celdaClick())
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
    fecha = self.txtFecha.text()
    hora = self.txtHorario.text()
    if self.validadFecha(fecha) :
      if self.validarHora(hora) :
        try :
          resultado = bdSala.buscarPeliculaNombre(BD, self.nombre)
          bdFuncion.cargarFuncion(BD, resultado[0], hora, fecha, self.id_sala)
          self.exito("Se agregó correctamente la Función")
        except Exception as e:
          self.error("Debe seleccionar una Sala primero")
      else:
        self.error("La Hora ingresada no es válida, deber ser en formato H:M")
    else:
      self.error("La Fecha ingresada no es válida, debe ser en formato DD/MM/AAAA")
  
  def celdaClick(self):
    lista = self.tabla.currentRow()
    self.id_sala = self.tabla.item(lista, 0).text()
    self.nombre = self.tabla.item(lista, 5).text()
    
  def validadFecha(self,fecha):
    try:
      datetime.strptime(fecha, '%d/%m/%Y')
      return True
    except ValueError:
      return False
  
  def validarHora(self, hora):
    try:
      time.strptime(hora, "%H:%M")
      return True
    except ValueError:
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
  
  def determinarTipoSala(self, tipo):
    if tipo : 
      return "3D"
    else :
      return "2D" 
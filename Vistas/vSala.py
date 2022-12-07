'''
Created on 2 dic. 2022

@author: surate
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala
from Vistas import vSalaCarga, vSalaModifica

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaSala(QMainWindow):
  def __init__(self):
    super(ventanaSala, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\sala.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.btnBuscar.clicked.connect(lambda: self.buscar())
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.tabla.clicked.connect(lambda : self.celdaClick())
    self.btnEliminar.clicked.connect(lambda: self.borrar())
    self.btnCargar.clicked.connect(lambda: self.cargar())
    self.btnModificar.clicked.connect(lambda: self.modificar())
    self.actionSalir.triggered.connect(qApp.quit)
    self.actionAcerca_de.triggered.connect(lambda: self.info())
    self.show()  
  
  def determinarTipoSala(self, tipo):
    if tipo : 
      return "3D"
    else :
      return "2D" 
  
  def esNumero(self, num):
    try:
        float(num)
        return True
    except ValueError:
      return False
    
  def cargarTabla(self, resultados):
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
  
  def buscar(self):
    texto = self.txtNroSala.text()
    indice =  self.cmbTipoSala.currentIndex()
    if texto == "" and indice == 0 :
      resultados = bdSala.mostarSalas(BD, 2)
      self.tabla.setRowCount(len(resultados))
      self.cargarTabla(resultados)
    elif texto == "" and indice != 0 :
      resultados = bdSala.mostarSalas(BD, indice - 1)
      self.tabla.setRowCount(len(resultados))  
      self.cargarTabla(resultados)
    else :
      if self.esNumero(texto) :
        resultados = bdSala.buscarSala(BD,texto)
        self.tabla.setRowCount(len(resultados))
        self.cargarTabla(resultados)
        if resultados == [] :
          self.error("No se encontró la Sala buscada")
      else :
        self.error("El valor ingresado debe ser numérico")
  
  def celdaClick(self):
    lista = self.tabla.currentRow()
    id = self.tabla.item(lista, 0).text()
    return id
  
  def listaInfoSala(self):
    lista = self.tabla.currentRow()
    info = list()
    for i in range(0,6) :
      info.append(self.tabla.item(lista, i).text())
    return info

  def borrar(self):
    try:
      id_sala = self.celdaClick()
    except:
      self.error("Debe seleccionar un valor primero")
    else :
      respuesta = self.confirmar("Está seguro que desea eliminar la sala seleccionada?")
      if respuesta :
        bdSala.borrarSala(BD, id_sala)
        resultados = bdSala.mostarSalas(BD, 2)
        self.tabla.setRowCount(len(resultados))
        self.cargarTabla(resultados)
      else :
        self.error("Cancelado por el Usuario")
  
  def cargar(self):
    self.carga = vSalaCarga.ventanaSalaCarga()
  
  def modificar(self):
    try:
      id_sala = self.celdaClick()
    except:
      self.error("Debe seleccionar un valor primero")
    else :
      self.modifica = vSalaModifica.ventanaSalaModifica(self.listaInfoSala())
    
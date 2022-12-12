'''
Created on 7 dic. 2022

@author: surate
'''
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdButaca
from Vistas import  vButacaCarga
from Clases.Butaca import Butaca

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class ventanaButaca(QMainWindow):
  def __init__(self):
    super(ventanaButaca, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\sala.ui",self)
    self.setWindowTitle("Cinemar - Butacas")
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.cmbTipoSala.hide()
    self.lblTipoSala.hide()
    self.tabla.setColumnCount(3)
    self.tabla.setHorizontalHeaderLabels(["Sala Número","Fila","Asiento"])
    self.actionSalir.triggered.connect(qApp.quit)
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.btnBuscar.clicked.connect(lambda: self.buscar())
    self.tabla.clicked.connect(lambda : self.celdaClick())
    self.btnEliminar.clicked.connect(lambda: self.borrar())
    self.btnCargar.clicked.connect(lambda: self.cargar())
    self.btnModificar.clicked.connect(lambda: self.modificar())
    self.actionAcerca_de.triggered.connect(lambda: self.info())
    self.btnModificar.hide()
    self.show()
  
  def cargarTabla(self, resultados):
    tablerow = 0
    for resultado in resultados:
      self.tabla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(resultado[2])))
      self.tabla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(resultado[0])))
      self.tabla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(resultado[1])))
      tablerow+=1
  
  def cargar(self):
    self.carga = vButacaCarga.ventanaButacaCarga()
  
  def celdaClick(self):
    try :
      lista = self.tabla.currentRow()
      sala = self.tabla.item(lista, 0).text()
      fila = self.tabla.item(lista, 1).text()
      asiento = self.tabla.item(lista, 2).text()
      self.butaca = Butaca(fila, asiento, sala)
    except Exception as e :
      print(str(e))
  
  def buscar(self):
    id_sala = self.txtNroSala.text()
    if  id_sala == "" or not self.esNumero(id_sala):
      self.error("El valor introduciodo debe ser numérico")
    else :
      resultados = bdButaca.mostrarButacas(BD, id_sala)
      if resultados == [] :
        self.error(f"La sala {id_sala} no posee butacas cargadas")
      else :
        self.tabla.setRowCount(len(resultados))
        self.cargarTabla(resultados)
  
  def modificar(self):
    pass
  
  def borrar(self):
    try:
      datos_butaca = self.celdaClick()
    except:
      self.error("Debe seleccionar un valor primero")
    else :
      respuesta = self.confirmar("Está seguro que desea eliminar la sala seleccionada?")
      if respuesta :
        try :
          bdButaca.borrarButaca(BD, self.butaca)
          id_sala = self.butaca.sala
          resultados = bdButaca.mostrarButacas(BD, id_sala)
          self.exito("El registro se eliminó correctamente")
          self.tabla.setRowCount(len(resultados))
          self.cargarTabla(resultados)
        except Exception as e:
          print(str(e))
      else :
        self.error("Cancelado por el Usuario")
  
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
'''
Created on 14 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala, bdFuncion, bdReserva, bdButaca
from datetime import datetime
import time
from Clases.Butaca import Butaca

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"
CANT_ASIENTO = 10

class ventanaReserva(QMainWindow):
  def __init__(self):
    super(ventanaReserva, self).__init__()
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Reserva.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.cargarTabla()
    self.tabla.clicked.connect(lambda : self.cargarLista())
    self.btnReserva.clicked.connect(lambda : self.reservar())
    self.show()
    
  def cargarTabla(self):
    try :
      self.resultados = bdFuncion.mostrarFuncion(BD)
      self.tabla.setRowCount(len(self.resultados))
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
  
  def cargarLista(self):
    try :
      self.lstButaca.clear()
      lista = self.tabla.currentRow()
      id_sala = self.tabla.item(lista, 0).text()
      capacidad_sala = bdSala.capacidadSala(BD, id_sala)
      fila_sala = capacidad_sala[0] // CANT_ASIENTO
      butaca = list()
      for letra in range(65, 65 + fila_sala):
        for i in range(1, CANT_ASIENTO +1):
          butaca.append(chr(letra) + " " +str(i)) #Carga las butacas en una lista
      butaca_sala = bdButaca.mostrarButacas(BD, id_sala) #Busca las butacas ocupadas
      if len(butaca_sala) == 0 : 
        self.lstButaca.addItems(butaca) #Carga todas las butacas en caso de este vacía la sala
      elif len(butaca_sala) == capacidad_sala[0] :
        self.lstButaca.addItem("Sala Llena")
      else :
        butacas_sala = list()
        for elemento in butaca_sala :
          butacas_sala.append(str(elemento[0]) + " " +str(elemento[1])) #arma la lista con las butacas ocupadas según la consulta sql
        for elemento in butacas_sala :
          if elemento in butaca :
            butaca.remove(elemento)
        self.lstButaca.addItems(butaca) #Carga todas las butacas libres
    except Exception as e :
      print(str(e))
  
  def reservar(self):
    try: 
      butaca_inidice = self.lstButaca.selectedItems()
      if len(butaca_inidice) == 0 :
        self.error("Primero debe seleccionar una Sala y una Butaca")
      else:
        butacas = list()
        lista = self.tabla.currentRow()
        id_sala = self.tabla.item(lista, 0).text()
        for x in range(len(butaca_inidice)):
            butacas.append(butaca_inidice[x].text()) #crea una lista con las butacas seleccionadas
        for x in range(len(butacas)):
          butaca_aux = butacas[x].split() #separa la fila del nro de asiento
          butaca = Butaca(butaca_aux[0],butaca_aux[1],id_sala)
          bdButaca.cargarButaca(BD, butaca) #registra la butaca ocupada en la BD
          
        print(self.resultados)
    except Exception as e:
      print(str(e))
  
  def cargarButaca(self, lista):
    lista.append(self.cmbButaca.currentText())
    return lista
    
  def determinarTipoSala(self, tipo):
    if tipo : 
      return "3D"
    else :
      return "2D" 
    
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
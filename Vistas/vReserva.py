'''
Created on 14 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from BD import bdSala, bdFuncion, bdReserva, bdButaca, bdDescuento
from datetime import datetime
import time
from Clases.Butaca import Butaca

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"
CANT_ASIENTO = 10

class ventanaReserva(QMainWindow):
  def __init__(self, datos_usuario):
    super(ventanaReserva, self).__init__()
    self.datos_usuario = datos_usuario
    self.viendoReserva = 0
    self.cargarUi()
  
  def cargarUi(self):
    loadUi(".\Vistas\Reserva.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.tabla.setSelectionBehavior(QTableView.SelectRows)
    self.cargarTabla()
    self.tabla.clicked.connect(lambda : self.cargarLista())
    self.btnReserva.clicked.connect(lambda : self.reservar())
    self.btnCancelar.clicked.connect(lambda : self.cancelar())
    self.btnVer.clicked.connect(lambda : self.verReserva())
    self.btnHistorico.clicked.connect(lambda : self.historicoReserva())
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
  
  def cargarTablaReserva(self,resultado):
    tablerow = 0
    for resultado in self.resultadosReserva:
      self.tabla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(resultado[0])))
      self.tabla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(resultado[1])))
      self.tabla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(resultado[3])))
      self.tabla.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(resultado[8])))
      self.tabla.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(resultado[6])))
      self.tabla.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(resultado[7])))
      tablerow+=1
          
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
      if self.viendoReserva == 1:
        self.lblButaca.show()
        self.lstButaca.show()
        self.tabla.setRowCount(len(self.resultadosReserva))
        self.cargarTabla()
        self.viendoReserva = 0
      else :
        butaca_inidice = self.lstButaca.selectedItems()
        if len(butaca_inidice) == 0 :
          self.error("Primero debe seleccionar una Sala y una Butaca")
        elif "Sala Llena" in butaca_inidice[0].text() :
          self.error("La Sala está llena, por favor elige otra")
        else:
          butacas = list()
          lista = self.tabla.currentRow()
          id_sala = self.tabla.item(lista, 0).text()
          butacas_reserva = ""
          for x in range(len(butaca_inidice)):
              butacas.append(butaca_inidice[x].text()) #crea una lista con las butacas seleccionadas
          for x in range(len(butacas)):
            butaca_aux = butacas[x].split() #separa la fila del nro de asiento para poder ser registrado en la BD
            butaca = Butaca(butaca_aux[0],butaca_aux[1],id_sala)
            butacas_reserva += str(butacas[x]) +" "#Lo convierte a string para poder ser alamcenado en la BD
            bdButaca.cargarButaca(BD, butaca) #registra la butaca ocupada en la BD
          datos_reserva = self.resultados[lista] #trae los datos de la función en base a la columna seleccionada
          id_funcion = self.resultados[lista][0]
          dni = self.datos_usuario[0]
          fecha_reserva = self.resultados[lista][2]
          cant_asiento = len(butacas)
          costo = cant_asiento * float (self.resultados[lista][9])
          semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
          dia = semana[datetime.today().weekday()] #Determinamos el día para calcular el descuento
          dias = bdDescuento.buscarDescuento(BD, dia) #traemos el porcentaje del descuento a aplicar 
          precio = costo - (float(dias[0])*costo/100)
          hora = self.resultados[lista][1]
          capacidad_sala = bdSala.capacidadSala(BD, id_sala) #Traemos la capacidad de la sala
          ocupada = int(capacidad_sala[1]) + cant_asiento #calculamos la nueva capacidad de la sala
          bdSala.actualizarCapacidad(BD, id_sala, ocupada) #Registramos en la BD la nueva cantidad de butacas ocupadas
          bdReserva.cargarReserva(BD, id_funcion, dni, fecha_reserva, cant_asiento, precio, dia, butacas_reserva, hora)
          self.exito(f"Se realizó su reserva: \nFunción Número: {id_funcion}\nFecha: {fecha_reserva}\nHora: {hora}\nAsientos: {butacas_reserva}\nCosto: ${precio} ")
    except Exception as e:
      print(str(e))
  
  def cancelar(self):
    try:
      if self.viendoReserva == 0 :
        self.error("Primero Debe seleccionar una reserva haciendo click en el botón de Ver Reservas")
      elif self.resultadosReserva == None or self.resultadosReserva == [] :
          self.error("No tiene reservas para cancelar\nSolo se puede cancelar una reserva con 1(una) hora de anticipación")
      else :
        lista = self.tabla.currentRow()
        id_reserva = self.tabla.item(lista, 0).text()
        dni = self.datos_usuario[0]
        fecha_hora = datetime.now()
        fecha = fecha_hora.strftime("%d/%m/%Y")
        hora = fecha_hora.strftime("%H:%M")
        respuesta = self.confirmar("Esta seguro que desea cancelar la reserva?")
        print(respuesta)
        if respuesta :
          bdReserva.cancelarReserva(BD, id_reserva)
          self.resultadosReserva = bdReserva.horarioReserva(BD, hora, fecha, dni)
          self.cargarTablaReserva(self.resultadosReserva)
          self.exito("Se Canceló con éxito su reserva")
        else :
          self.error("Cancelado por el Usuario")
    except Exception as e:
      print(str(e))
  
  def verReserva(self):
    try:
      self.lblButaca.hide()
      self.lstButaca.hide()
      self.viendoReserva = 1
      dni = self.datos_usuario[0]
      fecha_hora = datetime.now()
      fecha = fecha_hora.strftime("%d/%m/%Y")
      hora = fecha_hora.strftime("%H:%M")
      self.resultadosReserva = bdReserva.horarioReserva(BD, hora, fecha, dni)
      self.tabla.setRowCount(len(self.resultadosReserva))
      header = ["Número Reserva", "Número Función", "Fecha Reserva","Hora", "Día", "Butaca"]
      self.tabla.setColumnCount(len(header))
      columna = 0
      for elemento in header:
        item = QtWidgets.QTableWidgetItem(elemento)
        QtWidgets.QTableWidget.setHorizontalHeaderItem(self.tabla,columna, item)
        columna += 1
      if self.resultadosReserva == None or self.resultadosReserva == [] :
          self.error("No tiene reservas para actuales para mostrar, puede ver reservas pasadas haciendo click en el botón Histórico")
      else :
        self.cargarTablaReserva(self.resultadosReserva)
    except Exception as e:
      print(str(e))
   
  def historicoReserva(self):
    try:
      self.lblButaca.hide()
      self.lstButaca.hide()
      self.viendoReserva = 1
      dni = self.datos_usuario[0]
      self.resultadosReserva = bdReserva.verReservaxCliente(BD, dni)
      header = ["Número Reserva", "Número Función", "Fecha Reserva","Hora", "Día", "Butaca"]
      self.tabla.setColumnCount(len(header))
      columna = 0
      for elemento in header:
        item = QtWidgets.QTableWidgetItem(elemento)
        QtWidgets.QTableWidget.setHorizontalHeaderItem(self.tabla,columna, item)
        columna += 1
      self.tabla.setRowCount(len(self.resultadosReserva))
      self.cargarTablaReserva(self.resultadosReserva)
    except Exception as e :
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
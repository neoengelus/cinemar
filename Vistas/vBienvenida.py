'''
Created on 15 dic. 2022

@author: engelus
'''

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableView, qApp
from PyQt5.Qt import QMainWindow
from  Vistas import vReserva, vUsuarioCarga, vSala, vButaca

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"


class ventanaBienvenida(QMainWindow):
  def __init__(self,datosUsuario):
    super(ventanaBienvenida, self).__init__()
    self.datosUsuario = datosUsuario
    self.cargarUi()
    
  def cargarUi(self):
    loadUi(".\Vistas\Bienvenida.ui",self)
    self.setWindowIcon(QtGui.QIcon(ICON))
    self.lblBienvenida.setText(f"Bienvenido {self.datosUsuario[1]}")
    self.btnReserva.clicked.connect(lambda: self.reserva())
    self.btnModificar.clicked.connect(lambda: self.modifica() )
    self.btnSala.clicked.connect(lambda: self.sala()) 
    self.btnPelicula.clicked.connect(lambda: self.pelicula())
    self.btnButaca.clicked.connect(lambda: self.butaca())
    self.btnLogout.clicked.connect(lambda: self.logout()) 
    if self.datosUsuario[6] == 1 :
      self.btnSala.hide()
      self.btnPelicula.hide()
      self.btnButaca.hide()
    self.show()
  
  def reserva(self):
    self.vReserva = vReserva.ventanaReserva()
  
  def modifica(self):
    self.vModifica = vUsuarioCarga.ventanaUsuarioCarga()
  
  def sala(self):
    self.vSala = vSala.ventanaSala()
  
  def pelicula(self):
    pass 
  
  def butaca(self):
    self.vButaca = vButaca.ventanaButaca()
  
  def logout(self):
    self.close()
  
'''
Created on 2 nov. 2022

@author: engelus
'''
class Butaca():
  def __init__(self,fila="A",asiento="1",sala="1"):
    self.__fila = fila
    self.__asiento = asiento
    self.__sala = sala
    
  @property
  def fila(self):
    return self.__fila
  @fila.setter
  def fila(self,fila):
    self.__fila = fila
  @property
  def asiento(self):
    return self.__asiento
  @asiento.setter
  def asiento(self,asiento):
    self.__asiento = asiento
  @property
  def sala(self):
    return self.__sala
  @sala.setter
  def sala(self,nroSala):
    self.__sala = nroSala
    
  def __str__(self):
    return f"Sala: {self.__sala}\nFila: {self.__fila}\nAsiento: {self.__asiento}"
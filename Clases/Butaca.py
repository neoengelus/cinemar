'''
Created on 2 nov. 2022

@author: engelus
'''
class Butaca():
  def __init__(self,fila="A",asiento="1",ocupada=False):
    self.__ocupada = ocupada
    self.__fila = fila
    self.__asiento = asiento
    
  @property
  def ocupada(self):
    return self.__ocupada
  @ocupada.setter
  def ocupada(self,ocupada):
    self.__ocupada = ocupada
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
  def estaOcupada(self):
    if self.__ocupada:
      return "Ocupada"
    else:
      return "Libre"
  def __str__(self):
    return f"Fila: {self.__fila}\nAsiento: {self.__asiento}\nEstado: {self.estaOcupada()}"
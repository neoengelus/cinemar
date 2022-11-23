'''
Created on 2 nov. 2022

@author: engelus
'''
class Sala:
  def __init__(self, pelicula, butaca, costo = 0, butaca_max = 0, butaca_ocupada = 0, tipo_sala = False):
    self.__pelicula = pelicula
    self.__costo = costo
    self.__butacaMax = butaca_max
    self.__butacaOcupada = butaca_ocupada
    self.__butaca = butaca
    self.__tipoSala = tipo_sala 
    
  @property
  def pelicula(self):
    return self.__pelicula
  @property
  def costo(self):
    return self.__costo
  @property
  def butacaMax(self):
    return self.__butacaMax
  @property
  def butacaOcupada(self):
    return self.__butacaOcupada
  @property
  def butaca(self):
    return self.__butaca
  @property
  def tipoSala(self):
    return self.__tipoSala
  @pelicula.setter
  def pelicula(self,pelicula):
    self.__pelicula = pelicula
  @costo.setter
  def costo(self,costo):
    self.__costo = costo
  @butacaMax.setter
  def butacaMax(self,cant):
    self.bu__tacaMax = cant
  @butacaOcupada.setter
  def butacaOcupada(self,cant):
    self.__butacaOcupada = cant
  @butaca.setter
  def butaca(self,butaca):
    self.__butaca = butaca
  @tipoSala.setter
  def tipoSala(self,tipo):
    self.__tipo = tipo
  
  def determinarTipoSala(self):
    if self.__tipoSala : 
      return "3D"
    else :
      return "2D"  
  
  def __str__(self):
    cadena = f"Película: {self.__pelicula.nombre}\nDuración: {self.__pelicula.duracion}"
    cadena += f"\nTipo Sala: {self.determinarTipoSala()}\nCantidad de Butacas: {self.__butacaMax}"
    cadena += f"\nCantidad de Butacas Ocupadas: {self.__butacaOcupada}\nCosto: $ {self.__costo}"
    return cadena
'''
Created on 18 oct. 2022

@author: engelus
'''
class Pelicula:
  ### Setters y Getters ###
  @property
  def nombre(self):
    return self.__nombre
  @property
  def director(self):
    return self.__director
  @property
  def categoria(self):
    return self.__categoria
  @property
  def duracion(self):
    return self.__duracion
  @property
  def fechaEstreno(self):
    return self.__fechaEstreno
  @property
  def clasificacion(self):
    return self.__clasificacion
  @nombre.setter
  def nombre(self,nombre):
    self.__nombre = nombre
  @director.setter
  def director(self,director):
    self.__director = director
  @categoria.setter
  def categoria(self,categooria):
    self.__categoria = categooria
  @duracion.setter
  def duracion(self,duracion):
    self.__duracion = duracion
  @fechaEstreno.setter
  def fechaEstreno(self,fecha):
    self.__fechaEstreno = fecha
  @clasificacion.setter
  def clasificacion(self,clasificacion):
    self.__clasificacion = clasificacion
  ### Metodos propios ###
  def __init__(self, nombre, director, duracion, fechaEstreno, clasificacion, categoria="Sin Asignar"):
    self.__nombre = nombre
    self.__director = director
    self.__categoria = categoria
    self.__duracion = duracion
    self.__fechaEstreno = fechaEstreno
    self.__clasificacion = clasificacion
  
  def cargarCategoria(self):
    categorias = ("Accion", "Comedia", "Drama", "Suspenso")
    for i in range(len(categorias)):
      print(f"\n{i + 1} - {categorias[i]}")
    pos = int(input("Elija categoria: "))
    self.categoria = categorias[pos - i]

  def calcularValoracion(self):
    if (self.clasificacion >= 0 and self.clasificacion <= 2):
      return "Muy mala"
    elif (self.clasificacion <= 5):
      return "Mala"
    elif (self.clasificacion <= 7):
      return "Regular"
    elif (self.clasificacion <= 8):
      return "Buena"
    elif (self.clasificacion <= 10):
      return "Excelente"
    else:
      return "Error. La pelicula tiene una clasificacion invalida"
  
  def esSimilar(self,peli):
    return (self.__categoria == peli.__categoria) and (self.__clasificacion == peli.__clasificacion)

  def esEpica(self):
    return (self.__duracion >= 180) and (self.__clasificacion == 10)
  
  def __str__(self):
    cadena = "Nombre: " + self.__nombre + "\nDirector: " + self.__director +"\nDuración: " +str(self.__duracion)
    cadena += "\nFecha de Estreno: " +self.__fechaEstreno + "\nClasificación: " +self.calcularValoracion() 
    cadena += "\nCategoría: " +self.__categoria
    return cadena
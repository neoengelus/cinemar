class Pelicula:
#CONSTRUCTOR
  def __init__(self, nombre, director, duracion, categoria):
    self.__nombre = nombre
    self.__director = director
    self.__duracion = duracion
    self.__categoria = categoria

  #GETTERS AND SETTERS
  @property
  def nombre(self):
    return self.__nombre

  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre

  @property
  def director(self):
    return self.__director

  @director.setter
  def director(self, director):
    self.__director = director

  @property
  def duracion(self):
    return self.__duracion

  @duracion.setter
  def duracion(self, duracion):
    self.__duracion = duracion
  
  @property
  def categoria(self):
    return self.__categoria

  @categoria.setter
  def categoria(self, categoria):
    self.__categoria = categoria
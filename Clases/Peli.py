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

 #PROGRAMA PRINCIPAL
  pelicula1 = Pelicula("Avatar"," James Cameron","165 Minutos”,"Ciencia Ficción")
  pelicula2 = Pelicula("Harry Potter y la cámara secreta", "Chris Columbus", "157 Minutos”,"Aventura")
  pelicula3 = Pelicula("Pantera Negra: Wakanda por siempre", "Ryan Coogle", " 161 Minutos","Acción") 
  pelicula4 = Pelicula("Star Wars: El Ascenso de Skywalker", "Jeffrey Jacob Abrams", "155 Minutos","Acción, Aventura, Fantasía")
  pelicula5 = Pelicula("El Señor de los anillos: El retorno del rey", "Peter Jackson", "201 Minutos","Acción, Aventura,Fantasía")

   print(pelicula1)
   print(pelicula2)
   print(pelicula3)
   print(pelicula4)
   print(pelicula5)
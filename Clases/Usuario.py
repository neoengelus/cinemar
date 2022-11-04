'''
Created on 20 oct. 2022

@author: engelus
'''
class Usuario:
  def __init__(self, nombre="", apellido="", edad=0, dni=0, email="", tipo=1):
    '''Email (usuario de login)
    Tipo (0 admin, 1 registrado, 2 visitante) '''
    self.__nombre = nombre
    self.__apellido = apellido
    self.__edad = edad
    self.__dni = dni
    self.__email = email
    self.__tipo = tipo
  
  @property
  def nombre(self):
    return self.__nombre
  @property
  def apellido(self):
    return self.__apellido
  @property
  def edad(self):
    return self.__edad
  @property
  def dni(self):
    return self.__dni
  @property
  def email(self):
    return self.__email
  @property
  def tipo(self):
    return self.__tipo
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre
  @apellido.setter
  def apellido(self, apellido):
    self.__apellido = apellido
  @edad.setter
  def edad(self, edad):
    self.__edad = edad
  @dni.setter
  def dni(self, dni):
    self.__dni = dni
  @email.setter
  def email(self,mail):
    self.__email = mail
  @tipo.setter
  def tipo(self, tipo):
    self.__tipo = tipo
  def tipoUsuario(self):
    if self.__tipo == 0:
      return "Administrador"
    elif self.__tipo == 1:
      return "Registrado"
    else:
      return "Visitante"
  def __str__(self):
    cadena = "Nombre: " + self.__nombre
    cadena += "\nApellido: " + self.__apellido
    cadena += "\nEdad: " + str(self.__edad)
    cadena += "\nDNI: " + str(self.__dni)
    cadena += "\nemail " + self.__email
    cadena += "\nTipo: " + self.tipoUsuario()
    return cadena
  
  def mayorEdad(self):
    return self.__edad >= 18

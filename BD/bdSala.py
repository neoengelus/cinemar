'''
Created on 24 nov. 2022

@author: engelus
'''
from Clases.Conexion import Conexion_BD

def mostarSalas(BD,tipo):
  conexion = Conexion_BD(BD)
  if tipo == 2 :
    consulta = "SELECT * FROM sala"
  else :
    consulta = consulta = f"SELECT * FROM sala WHERE tipo_sala = {tipo}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado 

def buscarSala(BD,id_sala):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM sala WHERE id_sala = {id_sala}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def cargarSala(BD,sala):
  conexion = Conexion_BD(BD)
  consulta = f"""INSERT INTO sala VALUES 
            (null,{sala.tipoSala},{sala.butacaMax},{sala.butacaOcupada},{sala.costo},null)"""
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def borrarSala(BD,id_sala):
  conexion = Conexion_BD(BD)
  consulta = f"DELETE FROM sala WHERE id_Sala = {id_sala}"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()

def actualizarSala(BD,id_sala):
  sala = buscarSala(BD, id_sala)
  if sala != [] :
    print("+------------------------------------------------------------------+")
    print("|                     Modificación de Sala                         |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Cambiar Tipo de Sala                                         |")
    print("| (2) Cambiar Cantidad Máximna de Butacas                          |")
    print("| (3) Cambiar Cantidad de Butacas Ocupadas                         |")
    print("| (4) Cambiar el Costo de la Entrada                               |")
    print("| (5) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    opcion = int(input(("| Ingrese su opción: ") ))
    if opcion == 1 :
      print("+------------------------------------------------------------------+")
      print("|                     Modificación Tipo de Sala                    |")
      print("+------------------------------------------------------------------+")
      print("|                                                                  |")
      print("| (0) Sala 2D                                                      |")
      print("| (1) Sala 3D                                                      |")
      print("| (2) Salir                                                        |")
      print("+------------------------------------------------------------------+")
      dato = int(input(("| Ingrese su opción: ") ))
      if (dato == 0) or (dato == 1) :
        conexion = Conexion_BD(BD)
        consulta = f"UPDATE sala SET tipo_sala = {dato} WHERE id_Sala = {id_sala}"
        conexion.consulta(consulta)
        conexion.commit()
        conexion.cerrar()
    elif opcion == 2 :
      cantidad = int(input("Ingrese la nueva cantidad máxima de butacas: "))
      conexion = Conexion_BD(BD)
      consulta = f"UPDATE sala SET butaca_max = {cantidad} WHERE id_Sala = {id_sala}"
      conexion.consulta(consulta)
      conexion.commit()
      conexion.cerrar()
    elif opcion == 3 :
      cantidad = int(input("Ingrese la nueva cantidad de butacas ocupadas: "))
      conexion = Conexion_BD(BD)
      consulta = f"UPDATE sala SET butaca_ocupada = {cantidad} WHERE id_Sala = {id_sala}"
      conexion.consulta(consulta)
      conexion.commit()
      conexion.cerrar()
    elif opcion == 4 :
      valor = float(input("Ingrese el nuevo valor de la entrada: "))
      conexion = Conexion_BD(BD)
      consulta = f"UPDATE sala SET costo = {valor} WHERE id_Sala = {id_sala}"
      conexion.consulta(consulta)
      conexion.commit()
      conexion.cerrar()
    elif opcion == 5 :
      pass
    else :
      print("Opción incorrecta")
  else :
    print("Error Sala no encontrada")


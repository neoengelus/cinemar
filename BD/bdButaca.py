'''
Created on 24 nov. 2022

@author: engelus
'''

from Clases.Conexion import Conexion_BD

def mostrarButaca(BD,id_reserva):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_reserva = {id_reserva}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def buscarButaca(BD,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE butaca = '{butaca}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def cargarButaca(BD,id_reserva,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"INSERT INTO butaca VALUES('{butaca.fila}{butaca.asiento}',{id_reserva})"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def borrarButaca(BD, id_reserva, butaca):
  conexion = Conexion_BD(BD)
  consulta = f"DELETE FROM butaca WHERE id_reserva = {id_reserva} AND butaca = '{butaca.fila}{butaca.asiento}'"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def actualizarButaca(BD,butaca):
  existe = buscarButaca(BD, butaca)
  if existe != [] :
    print("+------------------------------------------------------------------+")
    print("|                     Modificación de Butaca                       |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Cambiar Butaca                                               |")
    print("| (2) Cambiar Reservación                                          |")
    print("| (3) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    opcion = int(input(("| Ingrese su opción: ") ))
    if opcion == 1 : 
      op = input("Ingrese la nueva butaca por ej H17: ")
      conexion = Conexion_BD(BD)
      consulta = f"UPDATE butaca SET butaca = {op} WHERE id_reserva = {existe[0][1]}"
      conexion.consulta(consulta)
      conexion.commit()
      conexion.cerrar()
    elif opcion == 2 :
      op = int(input("Ingrese el identificador de la función: "))
      conexion = Conexion_BD(BD)
      consulta = f"UPDATE butaca SET id_reserva = {op} WHERE butaca = {existe[0][0]}"
      conexion.consulta(consulta)
      conexion.commit()
      conexion.cerrar()
    elif opcion == 3 :
      pass
    else :
      print("Opción incorrecta")
  else :
    print("Error no existe la butaca ",butaca)
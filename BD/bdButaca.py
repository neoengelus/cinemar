'''
Created on 24 nov. 2022

@author: engelus
'''

from Clases.Conexion import Conexion_BD

def mostrarButaca(BD,id_butaca):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_butaca = {id_butaca}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def buscarButaca(BD,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_butaca = '{butaca}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def cargarButaca(BD,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"INSERT INTO butaca VALUES('{butaca.sala}{butaca.fila}{butaca.asiento},null')"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def borrarButaca(BD, butaca):
  conexion = Conexion_BD(BD)
  consulta = f"DELETE FROM butaca WHERE id_butaca = {butaca}"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def actualizarButaca(BD,butaca):
  existe = buscarButaca(BD, butaca)
  if existe != [] :
    op = input("Ingrese la nueva butaca por ej 1H17: ")
    conexion = Conexion_BD(BD)
    consulta = f"UPDATE butaca SET id_butaca = {op} WHERE id_butaca = {existe[0][0]}"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()
  else :
    print("Error no existe la butaca ",butaca)
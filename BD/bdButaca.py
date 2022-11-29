'''
Created on 24 nov. 2022

@author: engelus
'''

from Clases.Conexion import Conexion_BD

def mostrarButacas(BD,id_sala):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_sala = {id_sala}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def mostrarButaca(BD,fila,asiento,id_sala):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_sala = {id_sala} AND fila = '{fila}' AND asiento = {asiento} "
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def mostrarButacaFila(BD,fila,id_sala):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_sala = {id_sala} AND fila = '{fila}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def buscarButaca(BD,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM butaca WHERE id_sala = {butaca.sala} AND fila = '{butaca.fila}' AND asiento = '{butaca.asiento}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def cargarButaca(BD,butaca):
  conexion = Conexion_BD(BD)
  consulta = f"INSERT INTO butaca VALUES('{butaca.fila}','{butaca.asiento}',{butaca.sala})"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def borrarButaca(BD, butaca):
  conexion = Conexion_BD(BD)
  consulta = f"DELETE FROM butaca WHERE id_sala = {butaca.sala} AND fila = '{butaca.fila}' AND asiento = '{butaca.asiento}'"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def actualizarButaca(BD,butaca):
  existe = buscarButaca(BD, butaca)
  if existe != [] :
    fila = input("Ingrese la nueva fila: ")
    asiento = input("Ingrese el nuevo asiento: ")
    conexion = Conexion_BD(BD)
    consulta = f"UPDATE butaca SET fila = '{fila}' AND asiento = '{asiento}' WHERE id_sala = {existe[0][2]}"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()
  else :
    print("Error no existe la butaca ",butaca)
'''
Created on 16 dic. 2022

@author: engelus
'''

from Clases.Conexion import Conexion_BD

def buscarDescuento(BD,dia):
  conexion= Conexion_BD(BD)
  consulta = f"SELECT porcentaje FROM descuento WHERE dias = '{dia}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return  resultado
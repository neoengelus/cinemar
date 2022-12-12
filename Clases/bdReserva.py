'''
Created on 24 nov. 2022

@author: engelus
'''
from CLASSES.Conexion import Conexion_BD

def verReservaxCliente (BD,dni):
    conexion= Conexion_BD(BD)
    consulta=f"select * from reservas where dni={dni}"
    resultado=conexion.consulta(consulta)
    conexion.cerrar
    return resultado   
       
def verReservas (BD):
    conexion= Conexion_BD(BD)
    consulta="select * from reservas"
    resultado=conexion.consulta(consulta)
    conexion.cerrar
    return resultado 
  

    
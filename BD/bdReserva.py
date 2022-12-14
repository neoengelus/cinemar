'''
Created on 24 nov. 2022

@author: engelus
'''
from Clases.Conexion import Conexion_BD

def verReservaxCliente (BD,dni):
    conexion= Conexion_BD(BD)
    consulta=f"select * from reserva where dni={dni}"
    resultado=conexion.consulta(consulta)
    conexion.cerrar
    return resultado   
       
def verReservas (BD):
    conexion= Conexion_BD(BD)
    consulta="select * from reserva"
    resultado=conexion.consulta(consulta)
    conexion.cerrar
    return resultado 
  
def cargarReserva(BD, id_funcion, dni, fecha_reserva, cant_asiento, costo, dias, id_butaca):
  conexion= Conexion_BD(BD)
  consulta = f"""INSTERT INTO reserva VALUES  
                 ({id_funcion}, {dni}, '{fecha_reserva}', {cant_asiento}, {costo}, {dias}, {id_butaca})
            """
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def cancelarReserva(BD,id_reserva):
  conexion= Conexion_BD(BD)
  consulta = f"DELETE FROM reserva WHERE id_reserva = {id_reserva}"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
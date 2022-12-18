'''
Created on 24 nov. 2022

@author: engelus
'''
from Clases.Conexion import Conexion_BD

def verReservaxCliente (BD,dni):
    conexion= Conexion_BD(BD)
    consulta=f"select * from reserva where dni={dni}"
    conexion.consulta(consulta)
    resultado = conexion.fetchall()
    conexion.cerrar()
    return resultado   
       
def verReservas (BD):
    conexion= Conexion_BD(BD)
    consulta="select * from reserva"
    conexion.consulta(consulta)
    resultado = conexion.fetchall()
    conexion.cerrar
    return resultado 
  
def cargarReserva(BD, id_funcion, dni, fecha_reserva, cant_asiento, costo, dias, id_butaca, hora):
  conexion= Conexion_BD(BD)
  consulta = f"""INSERT INTO reserva VALUES   
                 (null, {id_funcion}, {dni}, '{fecha_reserva}', 
                 {cant_asiento}, {costo}, '{dias}', '{id_butaca}', 
                 '{hora}')
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
  
def verReservaFecha(BD, fecha, dni):
    conexion= Conexion_BD(BD)
    consulta=f"SELECT * FROM reserva WHERE fecha_reserva >= '{fecha}' AND dni = {dni}"
    conexion.consulta(consulta)
    resultado = conexion.fetchall()
    conexion.cerrar()
    return resultado 
  
def horarioReserva(BD, hora, fecha, dni):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM reserva WHERE hora >= '{hora}' AND fecha_reserva >= '{fecha}' AND dni = {dni}"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado 
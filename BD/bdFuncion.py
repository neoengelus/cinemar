'''
Created on 13 dic. 2022

@author: engelus
'''

from Clases.Conexion import Conexion_BD

def buscarFuncion(BD, id_funcion):
  conexion = Conexion_BD(BD)
  consulta = f"""SELECT 
                      funcion.id_funcion, pelicula.titulo, funcion.horario, 
                      funcion.dia_funcion, funcion.id_sala, sala.tipo_sala,
                      sala.butaca_max, sala.butaca_ocupada, sala.costo
                FROM funcion
                JOIN sala on funcion.id_pelicula = sala.id_pelicula 
                JOIN pelicula on funcion.id_pelicula = pelicula.id_pelicula
                WHERE funcion.id_funcion = {id_funcion}
              """
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return resultado

def borrarFuncion(BD,id_funcion):
  conexion = Conexion_BD(BD)
  consulta = f"DELETE FROM funcion WHERE id_funcion = {id_funcion}"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def actualizarFuncion(BD,id_funcion, hora, fecha, sala):
  conexion = Conexion_BD(BD)
  consulta = f"""UPDATE funcion SET 
                            horario = {hora},
                            dia_funcion = {fecha},
                            id_sala = {sala} 
                WHERE id_funcion = {id_funcion}
              """
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def cargarFuncion(BD, pelicula, hora, fecha, sala):
  conexion = Conexion_BD(BD)
  consulta = f"""INSERT INTO funcion VALUES 
                        (null, {pelicula}, '{hora}', '{fecha}', {sala}) 
              """
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
  
def mostrarFuncion(BD):
  conexion = Conexion_BD(BD)
  consulta= f"""SELECT 
                funcion.id_funcion, funcion.horario, funcion.dia_funcion,
                funcion.id_pelicula, funcion.id_sala, 
                pelicula.titulo, pelicula.duracion, pelicula.clasificacion,
                sala.tipo_sala, sala.costo, sala.butaca_ocupada, sala.butaca_max
            FROM funcion
            JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula
            JOIN sala on sala.id_pelicula = funcion.id_pelicula
            """
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def mostrarFuncionFecha(BD, fecha):
  conexion = Conexion_BD(BD)
  consulta= f"""SELECT 
                funcion.id_funcion, funcion.horario, funcion.dia_funcion,
                funcion.id_pelicula, funcion.id_sala, 
                pelicula.titulo, pelicula.duracion, pelicula.clasificacion,
                sala.tipo_sala, sala.costo, sala.butaca_ocupada, sala.butaca_max
            FROM funcion
            JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula
            JOIN sala on sala.id_pelicula = funcion.id_pelicula
            WHERE funcion.dia_funcion = '{fecha}'
            """
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado


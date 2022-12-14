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

def cargarSalaValores(BD,tipoSala,butacaMax,butacaOcupada,costo,id_pelicula):
  conexion = Conexion_BD(BD)
  consulta = f"""INSERT INTO sala VALUES 
            (null,{tipoSala},{butacaMax},{butacaOcupada},{costo},{id_pelicula})"""
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

def actualizaSala(BD,lista):
  conexion = Conexion_BD(BD)
  consulta = f"""UPDATE sala SET 
                tipo_sala = {lista[1]},
                butaca_max = {lista[2]},
                butaca_ocupada = {lista[3]},
                costo = {lista[4]},
                id_pelicula = {lista[5]}
                WHERE id_sala = {lista[0]};
            """
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()

def mostrarSalaPelicula(BD,id_sala):
  sala = buscarSala(BD, id_sala)
  conexion = Conexion_BD(BD)
  consulta = f"""SELECT sala.id_sala, sala.tipo_sala, sala.butaca_max, sala.butaca_ocupada, 
            sala.costo, pelicula.titulo 
            FROM sala 
            JOIN pelicula on sala.id_pelicula = pelicula.id_pelicula 
            WHERE sala.id_pelicula = {sala[0][5]}
            """
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def cargarPeliculas(BD):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM Pelicula"
  conexion.consulta(consulta)
  resultado = conexion.fetchall()
  conexion.cerrar()
  return resultado

def buscarPelicula(BD, id):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM Pelicula WHERE id_pelicula = {id}"
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return resultado

def buscarPeliculaNombre(BD, nombre):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT * FROM Pelicula WHERE titulo = '{nombre}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return resultado

def capacidadSala(BD,id):
  conexion = Conexion_BD(BD)
  consulta = f"SELECT butaca_max, butaca_ocupada FROM sala WHERE id_sala = {id}"
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return resultado

def actualizarCapacidad(BD, id, ocupada):
  conexion = Conexion_BD(BD)
  consulta = f"UPDATE sala SET butaca_ocupada = {ocupada} WHERE id_sala = {id}"
  conexion.consulta(consulta)
  conexion.commit()
  conexion.cerrar()
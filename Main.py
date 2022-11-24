'''
Created on 1 nov. 2022

@author: engelus
'''
from Clases.Pelicula import Pelicula
from Clases.Butaca import Butaca
from Clases.Usuario import Usuario
from Clases.Conexion import Conexion_BD
from Clases.Sala import Sala


conexion = Conexion_BD("./Cinemar.db")

with open("./Recursos/Cinemar.sql","r") as archivo :
  script = archivo.read()
  
conexion.script(script)

consulta = "SELECT * FROM sala WHERE tipo_sala = 0"
conexion.consulta(consulta)
resultados = conexion.fetchall()
conexion.cerrar()

peli = Pelicula("El Señor de los Anillos Ed. Extendida","Peter Jackson",201,"16/12/2003",10,"Acción")
print(peli)
humano = Usuario("Juan","Perez",30,123456,"123@gmail.com",1)
print(humano)
asiento = Butaca("H","15",True)
print(asiento)
print(resultados)
#humano.cargarUsuario(0)
for resultado in resultados:
  room = Sala(peli,asiento,resultado[4],resultado[2],resultado[3],resultado[1])
  print(f"Sala Número : {resultado[0]}")
  print(room)
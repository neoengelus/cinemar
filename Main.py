'''
Created on 1 nov. 2022

@author: engelus
'''
from Clases.Pelicula import Pelicula
from Clases.Butaca import Butaca
from Clases.Usuario import Usuario
from Clases.Sala import Sala
from BD import bdSala, bdButaca

BD = "./Cinemar.db"


'''with open("./Assets/Cinemar.sql","r") as archivo :
  script = archivo.read()
  
conexion.script(script)'''


peli = Pelicula("El Señor de los Anillos Ed. Extendida","Peter Jackson",201,"16/12/2003",10,"Acción")
#print(peli)
humano = Usuario("Juan","Perez",30,123456,"123@gmail.com",1)
#print(humano)
asiento = Butaca("H","18")
#print(asiento)
resultados = bdSala.mostarSalas(BD,2)
#print(resultados)
#humano.cargarUsuario(0)
'''for resultado in resultados:
  room = Sala(peli,asiento,resultado[4],resultado[2],resultado[3],resultado[1])
  print(f"Sala Número : {resultado[0]}")
  print(room)'''
nuevaSala = Sala(peli,asiento,600,20,1,True)
#bdSala.cargarSala(BD, nuevaSala)
hola = bdButaca.buscarButaca(BD, "H17")
print(hola[0][0])
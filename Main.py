'''
Created on 1 nov. 2022

@author: engelus
'''
from Clases.Pelicula import Pelicula
from Clases.Butaca import Butaca
from Clases.Usuario import Usuario


peli = Pelicula("El Señor de los Anillos Ed. Extendida","Peter Jackson",201,"16/12/2003",10,"Acción")
print(peli)
humano = Usuario("Juan","Perez",30,123456,"123@gmail.com",1)
print(humano)
asiento = Butaca("H","15",True)
print(asiento)

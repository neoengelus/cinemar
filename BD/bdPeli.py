from Clases.Conexion import Conexion_BD

def buscarPelicula(BD):
  conexion=Conexion_BD (BD)
  cursor=conexion.cursor()
  cursor.execute("SELECT * FROM peliculas")
  peliculas=cursor.fetchall()
  conexion.close()
  return peliculas

def modificarPelicula(BD,nombre,id_pelicula):
  conexion  =  Conexion_BD (BD)
  cursor=conexion.cursor()
  cursor.execute("UPDATE peliculas SET titulo={nombre} WHERE id_pelicula={id_pelicula}")
  conexion.commit()
  conexion.close()

def eliminarPelicula (BD,id_pelicula): 
  conexion  =  Conexion_BD (BD)
  cursor=conexion.cursor()
  cursor.execute("DELETE FROM peliculas WHERE id_pelicula={id_pelicula} ")
  conexion.commit()
  conexion.close()

def nuevaPelicula (BD,id_pelicula): 
  conexion  =  Conexion_BD (BD)
  cursor=conexion.cursor()
  cursor.execute("INSERT INTO pelicula VALUES (nombre, director, duracion, categoria)") 
  nuevapeli=cursor.fetchall()
  conexion.commit()
  conexion.close()
  return nuevapeli
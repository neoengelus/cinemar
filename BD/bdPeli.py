import pelis_DB
conexion=pelis_DB.connect ('peliculas_DB')
cursor=conexion.cursor()
cursor.execute("SELECT * FROM peliculas")
peliculas=cursor.fetchall()
conexion.close()

import pelis_DB
conexión  =  pelis_DB.connect ('peliculas_DB')
  cursor=conexion.cursor()
  cursor.execute("UPDATE peliculas SET NombrePelicula='?',Director='?' ,Duracion='?',  Categoria='?' \ WHERE NombrePelicula='?' ,Director='?' ,Duracion='?',  Categoria='?' "
  conexion.commit()
  conexión.close()

import pelis_DB eliminarPeliculas 
  conexión  =  pelis_DB.connect ('peliculas_DB')
  cursor=conexion.cursor()
  cursor.execute("DELETE FROM peliculas WHERE NombrePelicula='?' ,Director='?' ,Duracion='?',  Categoria='?' "
  conexion.commit()
  conexión.close()
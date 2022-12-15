import pelis_DB
conexion=pelis_DB.connect ('peliculas_DB')
cursor=conexion.cursor()
cursor.execute("SELECT * FROM peliculas")
peliculas=cursor.fetchall()
conexion.close()

print("Lista de Peliculas")
print("NombrePelicula \tID \t Director \t Duracion \t Categoria")
i=1
for pelicula in peliculas:
    print (f"{i} \t {pelicula[0]} \t {pelicula[1]} \t {pelicula[2]} \t {pelicula[3]}")
i=i+1
    print(peliculas)

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
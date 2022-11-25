'''
Created on 2 nov. 2022

@author: engelus
'''

version = "Cinemar 1.0"

def menuPrincipal() :
  print("+------------------------------------------------------------------+")
  print(f"|                     {version}                                  |")
  print("+------------------------------------------------------------------+")
  print("|                                                                  |")
  print("| (1) Ingresar al sistema con su usuario                           |")
  print("| (2) Ingresar al sistema como invitado                            |")
  print("| (3) Crear nuevo usuario                                          |")
  print("| (4) Salir                                                        |")
  print("|                                                                  |")
  print("+------------------------------------------------------------------+")
  opcion = int(input(("| Ingrese su opción: ") ))
  return opcion
    
def menuOpciones(opcion):
  if opcion == 1:
    print("+------------------------------------------------------------------+")
    print("|                          LOGIN                                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("|                                                                  |")
    user = input("     USUARIO: ")
    passw = input("     CONTRASEÑA: ")
    if True : #Esto luego hay que cambiarlo para que coteje contra una BD la contraseña (passw) y el usuario (user)
      print("+------------------------------------------------------------------+")
      print("|                       Login exitoso                              |")
      print("+------------------------------------------------------------------+")
      print("|                  Bienvenido/a nuevamente                         |")
      print("+------------------------------------------------------------------+")
      #time.sleep(1500)
      menuUsuario(0) #Esto luego hay que cambiarlo para que traiga desde la BD el usuario (user) y su tipo
    else:
      print("+------------------------------------------------------------------+")
      print("|          ERROR! Usuario o Contraseña incorrectos                 |")
      print("+------------------------------------------------------------------+")
      print("|        Desea intentarlo nuevamente...?                           |")
      print("| (1) SI                                                           |")
      print("| (2) NO (volver al menu anterior)                                 |")
      op = int(input("|  Ingrese su opción: "))
      if op == 1 :
        menuOpciones(op);
      else: 
        menuOpciones(menuPrincipal())
  elif opcion == 2:
    print("Mostrar el listado de películas")
    menuOpciones(menuPrincipal())
  elif opcion == 3:
    print("+------------------------------------------------------------------+")
    print("|                         NUEVO USUARIO                            |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("|                                                                  |")
    mail = input(("   Ingrese su email este será su nombre de Usuario: "))
    passw = input(("   Ingrese contraseña: "))
    nombre = input(("   Ingrese su Nombre: "))
    apellido = input(("   Ingrese su Apellido: "))
    dni = input(("   Ingrese su DNI: "))
    edad = input(("   Ingrese su  edad: "))
    tipo = 2
    # Consultar en la BD si el usuario existe y cambiar el if de abajo
    if True :
      #Creamos el usuario en la BD con los datos de arriba
      print("+------------------------------------------------------------------+")
      print(f"                  Bienvenido/a {nombre} {apellido}")
      print("+------------------------------------------------------------------+")
      menuUsuario(2)
    else :
      print("+------------------------------------------------------------------+")
      print("|          ERROR! El nombre de usuario ya existe                   |")
      print("+------------------------------------------------------------------+")
      print("|        Desea intentarlo nuevamente...?                           |")
      print("| (1) SI                                                           |")
      print("| (2) NO (volver al menu anterior)                                 |")
      op = int(input("|  Ingrese su opción: "))
      if  op == 1 :
        menuOpciones(3)
      else :
        menuOpciones(menuPrincipal())
  elif opcion == 4 :
    print("+------------------------------------------------------------------+")
    print("|                         HASTA LUEGO!!                            |")
    print("+------------------------------------------------------------------+")
  else :
    print("+------------------------------------------------------------------+")
    print("|          OPCION NO DISPONIBLE, INTENTE NUEVAMENTE                |")
    print("+------------------------------------------------------------------+")
    menuOpciones(menuPrincipal());

def menuUsuario(tipoUsuario):
  if tipoUsuario == 0 :
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear, Ver, Actualizar o Borrar un usuario administrador     |")
    print("| (2) Ver, Actualizar o Dar de Baja un Socio                       |")
    print("| (3) Ver Reservas                                                 |")
    print("| (4) Crear, Ver, Actualizar o Borrar Salas de Cine                |")
    print("| (5) Crear, Ver, Actualizar o Borrar Películas                    |")
    print("| (6) Crear, Ver, Actualizar o Borrar Descuentos                   |")
    print("| (7) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    opcion = int(input("| Ingrese su opción: "))
    if opcion == 7 :
      menuOpciones(menuPrincipal())
    else:
      accionesAdmin(opcion)
  elif tipoUsuario == 1 :
    print("+------------------------------------------------------------------+")
    print(f"|                  Usuarios - {version}                          |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Ver Funciones Disponibles                                    |")
    print("| (2) Buscar una Pelicula                                          |")
    print("| (3) Crear, Ver o Actualizar una Reserva                          |")
    print("| (4) Ver historico de Entradas                                    |")
    print("| (5) Darse de baja                                                |")
    print("| (6) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    opcion = int(input("| Ingrese su opción: "))
    if opcion == 6 :
      menuOpciones(menuPrincipal())
    else :
      accionesUser(opcion)
  else :
    print("+------------------------------------------------------------------+")
    print("|         ERROR!! Regresando al menú anterior...                   |")
    print("+------------------------------------------------------------------+")
    menuOpciones(menuPrincipal())
    
def accionesAdmin(opcion):
  if opcion == 1 :
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear un nuevo usuario administrador                         |")
    print("| (2) Ver datos de un Administrador                                |")
    print("| (3) Actualizar datos de un Administrador                         |")
    print("| (4) Borrar un usuario Administrador                              |")
    print("| (5) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    op = int(input("| Ingrese su opción: "))
    if op == 5: 
      menuOpciones(1)
    else:
      crudUsuario(op, 1);
  elif opcion == 2:
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                    |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Ver datos de un Socio                                        |")
    print("| (2) Actualizar datos de un Socio                                 |")
    print("| (3) Dar de baja un Socio                                         |")
    print("| (4) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    op = int(input("| Ingrese su opción: "))
    if op == 4:
      menuUsuario(0)
    else:
      crudUsuario(op, 2)
  elif opcion == 3:
    print("Reservas") #Hay que traer las reservas desde la BD
  elif opcion == 4:
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear una Sala de Cine nueva                                 |")
    print("| (2) Actualizar datos de una Sala de Cine                         |")
    print("| (3) Borrar una Sala de Cine                                      |")
    print("| (4) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    op = int(input("| Ingrese su opción: "))
    if op == 4 :
      menuUsuario(0)
    else :
      crearSala(op)
  elif opcion == 5:
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear una Película nueva                                     |")
    print("| (2) Actualizar datos de una Película                             |")
    print("| (3) Borrar una Película                                          |")
    print("| (4) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    op = int(input("| Ingrese su opción: "))
    if op == 4 :
      menuUsuario(0)
    else :
      crudPelicula(op)
  elif opcion == 6:
    print("+------------------------------------------------------------------+")
    print(f"|                  Administradores - {version}                   |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear un Nuevo Descuento                                     |")
    print("| (2) Actualizar datos de un Desciento                             |")
    print("| (3) Borrar un Descuento                                          |")
    print("| (4) Salir                                                        |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+")
    op = int(input("| Ingrese su opción: "))
    if op == 4:
      menuUsuario(0)
    else:
      crearDescuento(op)
  elif opcion == 7:
    menuUsuario(0)
  else:
    print("+------------------------------------------------------------------+")
    print("|         Regresando al menú anterior...                           |")
    print("+------------------------------------------------------------------+")
    menuUsuario(0)
    
def accionesUser(opcion):
  if opcion == 1:
    #Traer desde la BD las funciones disponibles
    print("Funciones")
    print("+------------------------------------------------------------------+")
    print("|        Desea realizar otra consulta...?                          |")
    print("+------------------------------------------------------------------+")
    print("| (1) SI                                                           |")
    print("| (2) NO (sale del sistema)                                        |")
    print("+------------------------------------------------------------------+")
    op = int(input("|  Ingrese su opción: "))
    if op == 1 :
      menuUsuario(1)
    else:
      menuPrincipal()
  elif opcion == 2:
    print("+------------------------------------------------------------------+")
    print("|                   Búsqueda de Películas                          |")
    print("+------------------------------------------------------------------+")
    print("| (1) Buscar por nombre de Película                                |")
    print("| (2) Buscar por ID de Película                                    |")
    print("| (3) Volver al menú anterior                                      |")
    print("+------------------------------------------------------------------+")
    op = int(input("|  Ingrese su opción: "))
    if op == 1 :
      nombre = input("|  Ingrese el nombre de la Película: ")
      #Buscar la película en la BD y mostrar los datos
      print("Datos de Película")
    elif op == 2 :
      id = int(input("|  Ingrese el ID del libro: "))
      #Buscar la película en la BD y mostrar los datos
      print("Datos de Película")
    else :
        accionesUser(2)
  elif opcion == 3:
    print("+------------------------------------------------------------------+")
    print("|                  Reserva de Películas                            |")
    print("+------------------------------------------------------------------+")
    print("|                                                                  |")
    print("| (1) Crear una Reserva                                            |")
    print("| (2) Actualizar una Reserva                                       |")
    print("| (3) Dar de baja una Reserva                                      |")
    print("| (4) Ver una Reserva                                              |")
    print("| (5) Volver al menú anterior                                      |")
    print("|                                                                  |")
    print("+------------------------------------------------------------------+") 
    op = int(input("|   Ingrese su opción: "))
    if op == 1:
      fecha = input("Ingrese la Fecha de la Reserva")
      pelicula = input("Ingrese el nombre de la Película")
      #En la BD se verifica que los datos ingresados se correspondan y en caso de ser así se graba
    elif op == 2 :
      fecha = input("Ingrese la Fecha de la Reserva")
      pelicula = input("Ingrese el nombre de la Película")
      #En la BD se verifica que los datos ingresados se correspondan y en caso de ser así se graba
    elif op == 3 :
      fecha = input("Ingrese la Fecha de la Reserva")
      pelicula = input("Ingrese el nombre de la Película")
      #En la BD se verifica que los datos ingresados se correspondan y en caso de ser así se graba y que sea por lo menos 1 hs antes
    elif op == 4 :
      #Traer las reservas del usuario de la BD
      print("Reservas")
    else:
      accionesUser(2)
  elif opcion == 4:
    print("+------------------------------------------------------------------+")
    print("|                   Historial de Entradas                          |")
    print("+------------------------------------------------------------------+")
    #Traer de la BD el historial de las entradas
    print("+------------------------------------------------------------------+")
    print("|        Desea realizar otra consulta...?                          |")
    print("+------------------------------------------------------------------+")
    print("| (1) SI                                                           |")
    print("| (2) NO (sale del sistema)                                        |")
    print("+------------------------------------------------------------------+")
    op = int(input("|  Ingrese su opción: "))
    if op == 1 :
      menuUsuario(1)
    else :
      menuPrincipal()
  elif opcion == 5 :
    print("+------------------------------------------------------------------+")
    print("|                Baja de Usuario                                   |")
    print("+------------------------------------------------------------------+")
    #Traer los datos del usuario para la Baja y realizar la baja en caso de existir
    print("+------------------------------------------------------------------+")
    print("|        Desea realizar otra consulta...?                          |")
    print("+------------------------------------------------------------------+")
    print("| (1) SI                                                           |")
    print("| (2) NO (sale del sistema)                                        |")
    print("+------------------------------------------------------------------+")
    op = int(input("|  Ingrese su opción: "))
    if op == 1 :
      menuUsuario(1)
    else :
      menuPrincipal()
  else :
    print("+------------------------------------------------------------------+")
    print("|         Regresando al menú anterior...                           |")
    print("+------------------------------------------------------------------+")
    menuUsuario(1)
    
def crudUsuario(opcion,idUsuario):
  pass
def crudPelicula(opcion,idPelicula):
  pass
def crudReserva(opcion,idUsuario):
  pass
def crearSala(opcion,idSala):
  pass
def crearDescuento(opcion):
  pass
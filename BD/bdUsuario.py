from Clases.Conexion import Conexion_BD

def altaUsuario (BD,persona,password):
    conexion= Conexion_BD(BD)
    consulta = f"INSERT INTO usuario VALUES('{persona.dni}','{persona.nombre}','{persona.email}','{persona.apellido}','{persona.edad}','{password}','{persona.tipo}')"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()
    
def bajaUsuario (BD,dni):
    conexion= Conexion_BD(BD)
    consulta = f"delete from usuario where dni='{dni}'"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar() 
    
def buscarUsuario(BD,dni):
  conexion= Conexion_BD(BD)
  consulta = f"SELECT * From Usuario WHERE dni='{dni}'"
  conexion.consulta(consulta)
  resultado = conexion.fetchone()
  conexion.cerrar()
  return  resultado 

def actualizarUsuario (BD,persona,passw):
    conexion= Conexion_BD(BD)
    consulta = f"""UPDATE usuario SET nombre = {persona.nombre}
                                      mail = {persona.email}
                                      apellido = {persona.apellido}
                                      edad = {persona.edad}
                                      passw = {passw}
                                      tipo = {persona.tipo}')
                  WHERE dni = {persona.dni}
                  """
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()
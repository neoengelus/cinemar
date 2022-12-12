from Clases.Conexion import Conexion_BD

def altaUsuario (BD,persona,password):
    conexion= Conexion_BD(BD)
    consulta = f"INSERT INTO usuario VALUES('{persona.dni}','{persona.nombre}','{persona.mail}','{persona.apellido}','{persona.edad}','{password}','{persona.tipo}')"
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
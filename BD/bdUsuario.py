from CLASSES.Conexion import Conexion_BD
def altaUsuario (BD,persona):
    conexion= Conexion_BD(BD)
    consulta = f"INSERT INTO usuario VALUES('{persona.dni}','{persona.nom}','{persona.mail}','{persona.ape}','{persona.edad}','{persona.password}','{persona.tipo}')"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()
def bajaUsuario (BD,dni):
    conexion= Conexion_BD(BD)
    consulta = f"delete from usuario where dni='{dni}'"
    conexion.consulta(consulta)
    conexion.commit()
    conexion.cerrar()  
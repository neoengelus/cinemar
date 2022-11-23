'''
Created on 17 nov. 2022

@author: engelus
'''
import sqlite3 as sql

class Conexion_BD():

  def __init__(self,bd):#bd es el nombre de la base de datos
    self.conexion = sql.connect(bd)
    self.cursor = self.conexion.cursor()

  def consulta(self, consulta):
    self.cursor.execute(consulta)
    
  def many(self,consulta):
    self.cursor.executemany(consulta)
  
  def script(self,script):
    self.cursor.executescript(script)

  def commit(self):
    self.conexion.commit()

  def cerrar(self):
    self.conexion.close()
  
  def fetchone(self):
    return self.cursor.fetchone()
  
  def fetchall(self):
    return self.cursor.fetchall()
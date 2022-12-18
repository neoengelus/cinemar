import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox,QTableView
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QPixmap
import sqlite3

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

class PantallaModi(QWidget):
    usuarioActivo=False
    def __init__(self):
        super(PantallaModi, self).__init__()
        loadUi(".\Vistas\modiSuperUsu.ui",self)
        self.btnBuscar.clicked.connect(self.llenarboxes)
        self.btnConfirmar.clicked.connect(self.revisarCampos)
        self.btnEli.clicked.connect(self.eliminar)
        self.setWindowIcon(QtGui.QIcon(ICON))
        self.setWindowTitle("Cinemar - Gestión Datos de Usuario")
        self.setFixedSize(966,723)
        self.show()
        
    def eliminar(self):
        dniUsuario = self.box_dni.text()
        resp = QMessageBox.question(self, 'Advertencia', "Desea borrar el Usuario?", QMessageBox.Yes | QMessageBox.Cancel)
        if resp == QMessageBox.Cancel:
            
            QMessageBox.critical(self, "Cancelado","Se cancela la Operacion")
            return
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        if dniUsuario=="" :
            return
        query =f"delete FROM usuario WHERE dni ='{dniUsuario}'"
        cur.execute(query)
        conn.commit()
        QMessageBox.critical(self, "Confirmacion Borrado","Se ha borrado el Usuario")
        query =f"SELECT * FROM usuario"
        cur.execute(query)  
        setUsuarios=cur.fetchall()
        self.tableListUsu.setRowCount(len(setUsuarios))
        conn.commit()
        conn.close()
        
        tablerow=0
        for fila in setUsuarios:
            self.tableListUsu.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.tableListUsu.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(fila[1]))
            self.tableListUsu.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(fila[3]))
            self.tableListUsu.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(fila[2]))
            self.tableListUsu.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(fila[4])))
            if str(fila[6])=="1":
                tipou="1 - Admin"
            else:
                tipou="0 - Usuario"    
            self.tableListUsu.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(tipou))
            tablerow+=1
        conn.close()
        
    def llenarboxes(self):
        dniUsuario = self.box_dni.text()
        #clave = self.passwordfield.text()
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        query =f"SELECT * FROM usuario WHERE dni ='{dniUsuario}'"
        cur.execute(query)
        usuario = cur.fetchone()
        conn.commit()
        #conn.close()
        
        if usuario :
            self.boxNombre.setText (usuario[1])
            self.boxApellido.setText (usuario[3])
            self.boxEmail.setText (usuario[2])
            self.boxEdad.setText (str(usuario[4]))
            self.boxTipo.setText (str(usuario[6]))
            usuarioActivo=True 
        else:
            QMessageBox.critical(self, "Error","No hay Coincidencias")
            usuarioActivo=False 
        query =f"SELECT * FROM usuario"
        cur.execute(query)  
        setUsuarios=cur.fetchall()
        self.tableListUsu.setRowCount(len(setUsuarios))
        conn.commit()
        #conn.close()
        tablerow=0
        for fila in setUsuarios:
            
            self.tableListUsu.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.tableListUsu.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(fila[1]))
            self.tableListUsu.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(fila[3]))
            self.tableListUsu.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(fila[2]))
            self.tableListUsu.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(fila[4])))
            if str(fila[6])=="1":
                tipou="1 - Admin"
            else:
                tipou="0 - Usuario"    
            self.tableListUsu.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(tipou))
            tablerow+=1
        
    def revisarCampos(self):
        dni=self.box_dni.text ()
        nom=self.boxNombre.text ()
        ape=self.boxApellido.text()
        email=self.boxEmail.text()
        edad=self.boxEdad.text()
        tipo=self.boxTipo.text()
       
        
        if edad.isdigit()==False:
            QMessageBox.critical(self, "Error","Ingrese un Numero en Edad")
            return
        if int(edad)<12:
            QMessageBox.critical(self, "Error","No se Admite Edad Menor a 12 años")
            return
        if tipo.isdigit()==False:
            QMessageBox.critical(self, "Error","Ingrese un Numero en Tipo")
            return
        if int(tipo)!=1 and int(tipo)!=0:
            QMessageBox.critical(self, "Error","Valor Invalido en Tipo")
            return               
        if dni=="" or nom=="" or ape==""or email=="" or edad=="" or tipo=="":
            QMessageBox.critical(self, "Error","No pueden haber campos vacios")
        
        else:
            
            conn = sqlite3.connect(BD)
            cur = conn.cursor()
            query =f"UPDATE usuario SET nombre = '{nom}', apellido = '{ape}',mail='{email}', edad='{edad}', tipo='{tipo}' WHERE dni ='{dni}'"
            
            cur.execute(query)
            conn.commit()
            conn.close()
            self.llenarboxes()
            QMessageBox.critical(self, "Exito","Se han modificado los Datos Exitosamente")
            
            
                

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox,QTableView
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QPixmap
import sqlite3

class PantallaModi(QWidget):
    usuarioActivo=False
    def __init__(self):
        super(PantallaModi, self).__init__()
        loadUi(".\Vistas\CRUDPeli.ui",self)
        self.cargaTablaPeli()
        self.btnConfirmar.clicked.connect(self.revisarCampos)
        self.btnEli.clicked.connect(self.eliminarPeli)
        self.btnNuevo.clicked.connect(self.nuevaPeli)
        list_clasi = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        self.comboClasi.addItems(list_clasi)
        self.tableListUsu.setColumnWidth(1, 400)
    
    def nuevaPeli(self):
        titulo=self.boxTitulo.text ()
        duracion=self.boxDuracion.text ()
        clasi=self.comboClasi.currentText()
        director=self.boxDirector.text ()
        if titulo=="" or duracion=="" or director=="" :
            QMessageBox.critical(self, "Error","No pueden haber campos vacios")
            return
        else:
            conn = sqlite3.connect(BD)
            cur = conn.cursor()
            query =f"insert into pelicula (titulo, duracion,clasificacion, director) values ('{titulo}','{duracion}','{clasi}', '{director}')"
            cur.execute(query)
            conn.commit()
            QMessageBox.critical(self, "Exito","Se ha creado la pelicula Exitosamente")
            self.cargaTablaPeli()
            
    def eliminarPeli(self):
        codPeli = self.boxIdpeli.text()
        resp = QMessageBox.question(self, 'Advertencia', "Desea borrar el Usuario?", QMessageBox.Yes | QMessageBox.Cancel)
        if resp == QMessageBox.Cancel:
            
            QMessageBox.critical(self, "Cancelado","Se cancela la Operacion")
            return
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        if codPeli=="" :
            return
        query =f"delete FROM pelicula WHERE id_pelicula ='{codPeli}'"
        cur.execute(query)
        conn.commit()
        QMessageBox.critical(self, "Confirmacion Borrado","Se ha borrado la Pelicula")
        self.cargaTablaPeli()       
        
    def llenarboxes(self):
        dniUsuario = self.box_dni.text()
        #clave = self.passwordfield.text()
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        query =f"SELECT * FROM usuario WHERE dni ='{dniUsuario}'"
        cur.execute(query)
        usuario = cur.fetchone()
        conn.commit()
        conn.close()
        
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
        if int(tipo)!=1 and tipo!=0:
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
            
    def cargaTablaPeli(self):
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        query =f"SELECT * FROM pelicula"
        cur.execute(query)
        setPelis = cur.fetchall()
        self.tableListUsu.setRowCount(len(setPelis))
        conn.commit()
        #conn.close
        tablerow = 0
        for fila in setPelis:
            print (fila)
            self.tableListUsu.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(fila[1])))
            self.tableListUsu.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(fila[2]))
            self.tableListUsu.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(fila[4]))           
            self.tableListUsu.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(fila[3]))           
            tablerow+=1    
        conn.close        
# main
BD = "./Cinemar.db"
app = QApplication(sys.argv)
pantModi1 = PantallaModi()
widget = QtWidgets.QStackedWidget()
widget.addWidget(pantModi1)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
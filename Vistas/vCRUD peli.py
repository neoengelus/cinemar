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
        self.id=0
        self.cargaTablaPeli()
        
        self.btnEli.clicked.connect(self.eliminarPeli)
        self.btnNuevo.clicked.connect(self.limpiaCampos)
        self.btnGrabaNueva.clicked.connect(self.grabaPeli)
        self.btnConfirmar.clicked.connect(self.modiPeli)
        self.tableListUsu.clicked.connect(lambda : self.celdaClick())
        self.btnSalir.clicked.connect(self.salepantalla)
        #print (self.id)
        list_clasi = ["PM13", "PM16", "PM18","ATP"]
        self.comboClasi.addItems(list_clasi)
        self.tableListUsu.setColumnWidth(1, 300)
        self.tableListUsu.setSelectionBehavior(QTableView.SelectRows)
        self.btnGrabaNueva.setVisible(False)
        
    def salepantalla(self):
        try:
            widget.close()
        except:
            print("Exiting")
        
    def celdaClick(self):
        lista = self.tableListUsu.currentRow()
        self.id = self.tableListUsu.item(lista, 0).text()
        self.boxIdpeli.setText (self.tableListUsu.item(lista, 0).text())
        self.boxTitulo.setText (self.tableListUsu.item(lista, 1).text())
        self.boxDuracion.setText (self.tableListUsu.item(lista, 3).text())
        self.boxDirector.setText (self.tableListUsu.item(lista, 2).text())
        if self.tableListUsu.item(lista, 4).text()=="PM13":
            self.comboClasi.setCurrentIndex(0)
        elif self.tableListUsu.item(lista, 4).text()=="PM16":
            self.comboClasi.setCurrentIndex(1)
        elif self.tableListUsu.item(lista, 4).text()=="PM18":
            self.comboClasi.setCurrentIndex(2)
        elif self.tableListUsu.item(lista, 4).text()=="ATP":
            self.comboClasi.setCurrentIndex(3)
        else:
            self.comboClasi.setCurrentIndex(3)           
        return 
    def limpiaCampos(self):
        self.btnGrabaNueva.setVisible(True)
        self.boxIdpeli.setText("")
        self.boxTitulo.setText("")
        self.boxDuracion.setText("")
        self.boxDirector.setText("")
    def grabaPeli(self):
        titulo=self.boxTitulo.text ()
        duracion=self.boxDuracion.text ()
        clasi=self.comboClasi.currentText()
        director=self.boxDirector.text ()
        if duracion.isdigit()!=True:
            QMessageBox.critical(self, "Error","Duracion debe ser un Numero")
            return
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
            self.btnGrabaNueva.setVisible(False)
            
            self.cargaTablaPeli()
    def modiPeli(self):
        idpeli=self.id
        titulo=self.boxTitulo.text ()
        duracion=self.boxDuracion.text ()
        clasi=self.comboClasi.currentText()
        director=self.boxDirector.text ()
        if duracion.isdigit()!=True:
            QMessageBox.critical(self, "Error","Duracion debe ser un Numero")
            return
        if titulo=="" or duracion=="" or director=="" :
            QMessageBox.critical(self, "Error","No pueden haber campos vacios")
            return
        else:
            conn = sqlite3.connect(BD)
            cur = conn.cursor()
            query =f"update pelicula set titulo='{titulo}', duracion='{duracion}',clasificacion='{clasi}', director='{director}' where id_pelicula='{idpeli}'"
            cur.execute(query)
            conn.commit()
            QMessageBox.critical(self, "Exito","Se ha modificado la pelicula Exitosamente")
            self.cargaTablaPeli()  
                  
    def eliminarPeli(self):
        Idpeli = self.boxIdpeli.text()
        resp = QMessageBox.question(self, 'Advertencia', "Desea borrar la Pelicula?", QMessageBox.Yes | QMessageBox.Cancel)
        if resp == QMessageBox.Cancel:
            
            QMessageBox.critical(self, "Cancelado","Se cancela la Operacion")
            return
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        if Idpeli=="" :
            return
        query =f"delete FROM pelicula WHERE id_pelicula ='{Idpeli}'"
        cur.execute(query)
        conn.commit()
        QMessageBox.critical(self, "Confirmacion Borrado","Se ha borrado la Pelicula")
        self.cargaTablaPeli()       
        
    
        
            
    def cargaTablaPeli(self):
        conn = sqlite3.connect(BD)
        cur = conn.cursor()
        query =f"SELECT * FROM pelicula"
        cur.execute(query)
        setPelis = cur.fetchall()
        self.tableListUsu.setRowCount(len(setPelis))
        conn.commit()
        conn.close
        tablerow = 0
        for fila in setPelis:
            self.tableListUsu.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.tableListUsu.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(fila[3]))
            self.tableListUsu.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(fila[2]))           
            self.tableListUsu.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(fila[1]))
            self.tableListUsu.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(fila[4]))            
            tablerow+=1    
        #conn.close        
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
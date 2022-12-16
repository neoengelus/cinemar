'''
Created on 1 nov. 2022

@author: engelus
'''

import sys
from Vistas.vFuncion import ventanaFuncion
from PyQt5.QtWidgets import  QApplication
from Vistas.vLogin import ventanaLogin

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

app = QApplication(sys.argv)
mainwindow = ventanaLogin()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
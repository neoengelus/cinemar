'''
Created on 1 nov. 2022

@author: engelus
'''

import sys
from Vistas.vLogin import ventanaLogin
from PyQt5.QtWidgets import  QApplication

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

app = QApplication(sys.argv)
mainwindow = ventanaLogin()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
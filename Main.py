'''
Created on 1 nov. 2022

@author: engelus
'''

import sys
from Vistas.vFuncion import ventanaFuncion
from PyQt5.QtWidgets import  QApplication
from Vistas.vReserva import ventanaReserva

BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

app = QApplication(sys.argv)
mainwindow = ventanaReserva()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
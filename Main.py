
'''
Created on 1 nov. 2022

@author: engelus
'''

import sys
from Vistas.vSala import ventanaSala
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


BD = "./Cinemar.db"

app = QApplication(sys.argv)
mainwindow = ventanaSala()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
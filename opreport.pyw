import sys


from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QDialog
import ctypes  # An included library with Python install.




class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        #self.resize(800,500) #tamaño inicial de la ventana 800 x 500
        self.showFullScreen()
        #Create the status bar
        self.statusBar().showMessage("Wlecome to the Operations Report Sofware")
        #Object MenuBar
        menu = self.menuBar()
        
        #Menu Father
        menu_start = menu.addMenu("&Start")
        
        # Add a Sub Menu to the menu Start
        menu_start_mbusasales_ny = menu_start.addMenu("&MBUSA Sales")
        
        
        #Add an action elemento to the menu start
        menu_start_mbusasales_ny_add = QAction(QIcon(), "&MBUSA Sales New Year Data",self)
        menu_start_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_mbusasales_ny_add.setStatusTip("Start input data to MBUSA Sales")#Message in status bar
        menu_start_mbusasales_ny_add.triggered.connect(self.menu_start_mbusasales_new_year)#Launcher
        menu_start_mbusasales_ny.addAction(menu_start_mbusasales_ny_add)
     
        
        #Menu Padre 
        menu_salir = menu.addMenu("&Exit")
        

        #Agregar un elemento accion al menu Salir_Salir
        menu_Salir_Salir = QAction(QIcon(), "&Salir del Programa", self)
        menu_Salir_Salir.setStatusTip("Salir del Programa") #Mensaje en la barra de estado
        menu_Salir_Salir.triggered.connect(self.menu_exit) # Lanzado
        menu_salir.addAction(menu_Salir_Salir)
        
    
    def menu_start_mbusasales_new_year(self):
        QMessageBox.information(self,"MBUSA Sales","You will start capturing MBUSA Sales", QMessageBox.Discard)       
        import mbusasales_ny
        #from PyQt5 import QtCore, QtGui, uic, QtWidgets
        #import sys
  
        Dialog =  mbusasales_ny.MyWindowClass()
        Dialog.exec_()
       

    
    def menu_exit(self):
        import salir_programa
        salir = salir_programa.salir()
        salir

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Principal()
    ventana.show()
    app.exec_()
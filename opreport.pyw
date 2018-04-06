#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
In thismodule it is input the data of MB USA sales
"""
__author__ = "Alejandro Othoniel Gomez Chavez"
__copyright__ = "Copyright 2017 AOGCH"
__credits__ = "Mar Bran S.A. de C.V."

__licence__= "Open Code"
__version__ = "0.1"
__maintainer__ = "Alejandro Othoniel Gomez Chavez"
__email__ = "agomez@marbran.com.mx"
__status__ = "Developer"

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
        menu_sales = menu_start.addMenu("&Sales")
        menu_start_sales_mbusasales = menu_sales.addMenu('&MBUSA Sales')

        #Add an action elemento to the menu start
        menu_start_sales_mbusasales_ny_add = QAction(QIcon(), "&MBUSA Sales New Year Data",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_sales_mbusasales_ny_add.setStatusTip("Start input data to MBUSA Sales")#Message in status bar
        menu_start_sales_mbusasales_ny_add.triggered.connect(self.menu_start_mbusasales_new_year)#Launcher
        menu_start_sales_mbusasales.addAction(menu_start_sales_mbusasales_ny_add)

        #Add an action elemento to the menu start
        menu_start_sales_mbusasales_ny_table_data = QAction(QIcon(), "&MBUSA Sales Open data table",self)
        #menu_start_sales_mbusasales_ny_table_data.setShortcut("Ctrl+V") # keyboard Shortcut
        menu_start_sales_mbusasales_ny_table_data.setStatusTip("Open and edit saved data")#Message in status bar
        menu_start_sales_mbusasales_ny_table_data.triggered.connect(self.menu_start_mbusasales_data_table)#Launcher
        menu_start_sales_mbusasales.addAction(menu_start_sales_mbusasales_ny_table_data)

        #Add an action elemento to the menu start
        menu_start_sales_mbusasales_xls_report = QAction(QIcon(), "&MBUSA Sales Generate Excel file ",self)
        #menu_start_sales_mbusasales_csv_report.setShortcut("Ctrl+C") # keyboard Shortcut
        menu_start_sales_mbusasales_xls_report.setStatusTip("Open and save data with calculations")#Message in status bar
        menu_start_sales_mbusasales_xls_report.triggered.connect(self.menu_start_mbusasales_Csv)#Launcher
        menu_start_sales_mbusasales.addAction(menu_start_sales_mbusasales_xls_report)
     
        menu_start_sales_Domesticsales = menu_sales.addMenu('&Domestic Sales')
        #Add an action elemento to the menu start
        menu_start_sales_Domesticsales_ny_add = QAction(QIcon(), "&Domestic Sales New Year Data",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_sales_Domesticsales_ny_add.setStatusTip("Start input data to Domestic Sales")#Message in status bar
        menu_start_sales_Domesticsales_ny_add.triggered.connect(self.menu_start_domesticsales_new_year)#Launcher
        menu_start_sales_Domesticsales.addAction(menu_start_sales_Domesticsales_ny_add)

        #Add an action elemento to the menu start
        menu_start_sales_Domesticsales_ny_table_data = QAction(QIcon(), "&Domestic Sales Open data table",self)
        #menu_start_sales_mbusasales_ny_table_data.setShortcut("Ctrl+V") # keyboard Shortcut
        menu_start_sales_Domesticsales_ny_table_data.setStatusTip("Open and edit saved data")#Message in status bar
        menu_start_sales_Domesticsales_ny_table_data.triggered.connect(self.menu_start_domesticsales_data_table)#Launcher
        menu_start_sales_Domesticsales.addAction(menu_start_sales_Domesticsales_ny_table_data)

        #Add an action elemento to the menu start
        menu_start_sales_Domesticsales_xls_report = QAction(QIcon(), "&Domestic Sales Generate Excel file ",self)
        #menu_start_sales_mbusasales_csv_report.setShortcut("Ctrl+C") # keyboard Shortcut
        menu_start_sales_Domesticsales_xls_report.setStatusTip("Open and save data with calculations")#Message in status bar
        menu_start_sales_Domesticsales_xls_report.triggered.connect(self.menu_start_domesticsales_xls)#Launcher
        menu_start_sales_Domesticsales.addAction(menu_start_sales_Domesticsales_xls_report)

        menu_sales_Esa = menu_sales.addMenu('&Sales to ESA')
        menu_sales_Others = menu_sales.addMenu('&Sales to Others')
        
        # Add a Sub Menu to the menu Start
        menu_Purchases = menu_start.addMenu("&Purchases")
        menu_start_Purchases_Domestic = menu_Purchases.addMenu('&Domestic Purchases')
        #Add an action elemento to the menu start
        menu_start_Purchases_Domestic_ny_add = QAction(QIcon(), "&Domestic Purchases New Year Data",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Domestic_ny_add.setStatusTip("Start input data to Domestic Sales")#Message in status bar
        menu_start_Purchases_Domestic_ny_add.triggered.connect(self.menu_Start_Purchases_Domestic_ny)#Launcher
        menu_start_Purchases_Domestic.addAction(menu_start_Purchases_Domestic_ny_add)

        #Add an action elemento to the menu start
        menu_start_Purchases_Domestic_table_edit = QAction(QIcon(), "&Domestic Purchases Edit",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Domestic_table_edit.setStatusTip("Start input data to Domestic Sales")#Message in status bar
        menu_start_Purchases_Domestic_table_edit.triggered.connect(self.menu_start_Purchases_Domestic_data_table)#Launcher
        menu_start_Purchases_Domestic.addAction(menu_start_Purchases_Domestic_table_edit)

        #Add an action elemento to the menu start
        menu_start_Purchases_Domestic_xls_report = QAction(QIcon(), "&Domestic Purchases Generate Xls Report",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Domestic_xls_report.setStatusTip("Generate report Xls")#Message in status bar
        menu_start_Purchases_Domestic_xls_report.triggered.connect(self.menu_start_domesticpurchases_xls)#Launcher
        menu_start_Purchases_Domestic.addAction(menu_start_Purchases_Domestic_xls_report)

        """
        Import Purchases Option Menu
        """
        menu_Start_Purchases_Import = menu_Purchases.addMenu('&Import Purchases')
        #Add an action elemento to the menu start
        menu_start_Purchases_Import_ny_add = QAction(QIcon(), "&Import Purchases New Year Data",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Import_ny_add.setStatusTip("Start input data to Import Purchases")#Message in status bar
        menu_start_Purchases_Import_ny_add.triggered.connect(self.menu_Start_Purchases_Import_ny)#Launcher
        menu_Start_Purchases_Import.addAction(menu_start_Purchases_Import_ny_add)

        #Add an action elemento to the menu start
        menu_start_Purchases_Import_table_edit = QAction(QIcon(), "&Import Purchases Edit",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Import_table_edit.setStatusTip("Edit data of Import Purchases")#Message in status bar
        menu_start_Purchases_Import_table_edit.triggered.connect(self.menu_start_Purchases_Import_data_table)#Launcher
        menu_Start_Purchases_Import.addAction(menu_start_Purchases_Import_table_edit)

        #Add an action elemento to the menu start
        menu_start_Purchases_Import_xls_report = QAction(QIcon(), "&Import Purchases Generate Xls Report",self)
        #menu_start_sales_mbusasales_ny_add.setShortcut("Ctrl+U") # keyboard Shortcut
        menu_start_Purchases_Import_xls_report.setStatusTip("Generate report Xls")#Message in status bar
        menu_start_Purchases_Import_xls_report.triggered.connect(self.menu_start_Importpurchases_xls)#Launcher
        menu_Start_Purchases_Import.addAction(menu_start_Purchases_Import_xls_report)

        # Add a Sub Menu to the menu Start
        menu_Inventories = menu_start.addMenu("&Inventories")
        menu_Inventories_Broccoli = menu_Inventories.addMenu('&Inventories Broccoli')
        menu_Inventories_Broccoli_Finished = menu_Inventories_Broccoli.addMenu('&Inventories Broccoli Finished')
        menu_Inventories_Broccoli_Process = menu_Inventories_Broccoli.addMenu('&Inventories Broccoli Process')

        
        menu_Inventories_Cauliflower = menu_Inventories.addMenu('&Inventories Cauliflower')
        
        menu_Inventories_Carrots = menu_Inventories.addMenu('&Inventories Carrots')
        
        menu_Inventories_Ingredients = menu_Inventories.addMenu('& Inventories Ingredients')
        
        menu_Inventories_Mbusa = menu_Inventories.addMenu('&Inventories MB USA')
        #Add an action elemento to the menu start
        menu_Inventories_Mbusa_ny_add = QAction(QIcon(), "&Inventories MB USA new year",self)
        menu_Inventories_Mbusa_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Inventories_Mbusa_ny_add.triggered.connect(self.menu_Inventories_MBusa_ny)#Launcher
        menu_Inventories_Mbusa.addAction(menu_Inventories_Mbusa_ny_add)

         #Add an action elemento to the menu start
        menu_Inventories_Mbusa_table_edit = QAction(QIcon(), "&Edit data of MBUSA Inventories",self)
        menu_Inventories_Mbusa_table_edit.setStatusTip("Edit data of MBUSA Inventories")#Message in status bar
        menu_Inventories_Mbusa_table_edit.triggered.connect(self.menu_Inventories_Mbusa_Edit)#Launcher
        menu_Inventories_Mbusa.addAction(menu_Inventories_Mbusa_table_edit)

        #Add an action elemento to the menu start
        menu_Inventories_Mbusa_xls_report = QAction(QIcon(), "&MBUSA Inventories Generate XLS Report",self)
        menu_Inventories_Mbusa_xls_report.setStatusTip("Generate a Excel file of MBUSA Inventories")#Message in status bar
        menu_Inventories_Mbusa_xls_report.triggered.connect(self.menu_Inventories_Mbusa_xls)#Launcher
        menu_Inventories_Mbusa.addAction(menu_Inventories_Mbusa_xls_report)

                
        

        

        # Menu Father
        menu_exit = menu.addMenu("&Exit")
        #Agregar un elemento accion al menu Salir_Salir
        menu_Exit_Exit = QAction(QIcon(), "&Exit the Program", self)
        menu_Exit_Exit.setStatusTip("Leave the program") #Mensaje en la barra de estado
        menu_Exit_Exit.triggered.connect(self.menu_exit) # Lanzado
        menu_exit.addAction(menu_Exit_Exit)
            
    """
    Functions to call the Objects for the MB USA Sales
    """

    def menu_start_mbusasales_data_table(self):
        QMessageBox.information(self,"MBUSA Sales","You will open the saved data of MB USA Sales", QMessageBox.Discard)       
        import mbusasales_table_edit2
        Dialog =  mbusasales_table_edit2.Dialogo()
        Dialog.exec_()

    def menu_start_mbusasales_new_year(self):
        QMessageBox.information(self,"MBUSA Sales","You will start capturing MBUSA Sales", QMessageBox.Discard)       
        import mbusasales_ny2
        Dialog =  mbusasales_ny2.MyWindowClass()
        Dialog.exec_()

    def menu_start_mbusasales_Csv(self):
        QMessageBox.information(self,"MBUSA Sales","You will generate a XLS file", QMessageBox.Discard)       
        import mbusasales_csv_report
        Dialog =  mbusasales_csv_report.MyWindowClass()
        Dialog.exec_()

    """
    Functions to call the Objects for the Domestic Sales
    """
    def menu_start_domesticsales_data_table(self):
        QMessageBox.information(self,"Domestic Sales","You will open the saved data of MB USA Sales", QMessageBox.Discard)       
        import domestic_sales_table_edit
        Dialog =  domestic_sales_table_edit.Dialogo()
        Dialog.exec_()

    def menu_start_domesticsales_new_year(self):
        QMessageBox.information(self,"Domestic Sales","You will start capturing MBUSA Sales", QMessageBox.Discard)       
        import domestic_sales_ny
        Dialog =  domestic_sales_ny.MyWindowClass()
        Dialog.exec_()

    def menu_start_domesticsales_xls(self):
        QMessageBox.information(self,"Domestic Sales","You will generate a XLS file", QMessageBox.Discard)       
        import domesticsales_xls_report
        Dialog =  domesticsales_xls_report.MyWindowClass()
        Dialog.exec_()

    """
    Functions to call the Objects for the Domestic Purchases
    """
    def menu_Start_Purchases_Domestic_ny(self):
        QMessageBox.information(self,"Domestic Purchases","You will generate a new year file", QMessageBox.Discard)       
        import domestic_purchases_ny
        Dialog =  domestic_purchases_ny.MyWindowClass()
        Dialog.exec_()

    def menu_start_Purchases_Domestic_data_table(self):
        QMessageBox.information(self,"Domestic Purchases","You will edit the saved data of Domestic Purchases", QMessageBox.Discard)       
        import domestic_purchases_table_edit
        Dialog =  domestic_purchases_table_edit.Dialogo()
        Dialog.exec_()

    def menu_start_domesticpurchases_xls(self):
        QMessageBox.information(self,"Domestic Purchases","You will generate a XLS file", QMessageBox.Discard)       
        import domesticpurchases_xls_report
        Dialog =  domesticpurchases_xls_report.MyWindowClass()
        Dialog.exec_()

    """
    Functions to call the Objects for the Import Purchases
    """
    def menu_Start_Purchases_Import_ny(self):
        QMessageBox.information(self,"Domestic Purchases","You will generate a new year file", QMessageBox.Discard)       
        import Import_purchases_ny
        Dialog =  Import_purchases_ny.MyWindowClass()
        Dialog.exec_()

    def menu_start_Purchases_Import_data_table(self):
        QMessageBox.information(self,"Domestic Purchases","You will edit the saved data of Domestic Purchases", QMessageBox.Discard)       
        import import_purchases_table_edit
        Dialog =  import_purchases_table_edit.Dialogo()
        Dialog.exec_()

    def menu_start_Importpurchases_xls(self):
        QMessageBox.information(self,"Domestic Purchases","You will generate a XLS file", QMessageBox.Discard)       
        import importpurchases_xls_report
        Dialog =  importpurchases_xls_report.MyWindowClass()
        Dialog.exec_()
    
    def menu_Inventories_MBusa_ny(self):
        QMessageBox.information(self,"Inventories MB USA","You will start a New year data", QMessageBox.Discard)       
        import inventories_mbusa_ny
        Dialog =  inventories_mbusa_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Mbusa_Edit (self):
        QMessageBox.information(self,"Inventories MB USA","You will edit the saved data of MB USA Inventories", QMessageBox.Discard)       
        pass

    def menu_Inventories_Mbusa_xls (self):
        QMessageBox.information(self,"Inventories MB USA","You will generate a XLS file of MBUSA Inventories", QMessageBox.Discard)       
        pass

    """
    Function to call the Objects to Exit the program
    """
    def menu_exit(self):
        import salir_programa
        salir = salir_programa.salir()
        salir

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Principal()
    ventana.show()
    app.exec_()
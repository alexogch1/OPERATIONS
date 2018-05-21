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
        #Add an action elemento to the menu start
        menu_start_sales_Esa_ny_add = QAction(QIcon(), "&Sales ESA New Year Data",self)
        menu_start_sales_Esa_ny_add.setStatusTip("Start input data to ESA Sales")#Message in status bar
        menu_start_sales_Esa_ny_add.triggered.connect(self.menu_Sales_Esa_ny)#Launcher
        menu_sales_Esa.addAction(menu_start_sales_Esa_ny_add)

        #Add an action elemento to the menu start
        menu_start_sales_esa_table_edit = QAction(QIcon(), "&Sales ESA Edit data table",self)
        menu_start_sales_esa_table_edit.setStatusTip("Edit data of ESA Sales")#Message in status bar
        menu_start_sales_esa_table_edit.triggered.connect(self.menu_Sales_Esa_Table_Edit)#Launcher
        menu_sales_Esa.addAction(menu_start_sales_esa_table_edit)

        #Add an action elemento to the menu start
        menu_start_sales_esa_xls_report = QAction(QIcon(), "&Sales ESA Generate Excel file ",self)
        menu_start_sales_esa_xls_report.setStatusTip("Open and save data with calculations")#Message in status bar
        menu_start_sales_esa_xls_report.triggered.connect(self.menu_Sales_Esa_xls)#Launcher
        menu_sales_Esa.addAction(menu_start_sales_esa_xls_report)





        menu_sales_Others = menu_sales.addMenu('&Sales to Others')
        #Add an action elemento to the menu start
        menu_start_sales_Others_ny_add = QAction(QIcon(), "&Sales Others New Year Data",self)
        menu_start_sales_Others_ny_add.setStatusTip("Start input data to Sales Others")#Message in status bar
        menu_start_sales_Others_ny_add.triggered.connect(self.menu_Sales_Others_ny)#Launcher
        menu_sales_Others.addAction(menu_start_sales_Others_ny_add)



         #Add an action elemento to the menu start
        menu_start_sales_Others_Table_Edit = QAction(QIcon(), "&Sales Others Edit data table",self)
        menu_start_sales_Others_Table_Edit.setStatusTip("Edit data of Others Sales")#Message in status bar
        menu_start_sales_Others_Table_Edit.triggered.connect(self.menu_Sales_Others_Table_Edit)#Launcher
        menu_sales_Others.addAction(menu_start_sales_Others_Table_Edit)


        #Add an action elemento to the menu start
        menu_start_sales_Others_Xls_Report = QAction(QIcon(), "&Sales Others Generate Excel file ",self)
        menu_start_sales_Others_Xls_Report.setStatusTip("Open and save data with calculations")#Message in status bar
        menu_start_sales_Others_Xls_Report.triggered.connect(self.menu_Sales_Others_xls)#Launcher
        menu_sales_Others.addAction(menu_start_sales_Others_Xls_Report)




        
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
        menu_Inventories_Broccoli_Finissh_Process= menu_Inventories_Broccoli.addMenu('&Inventories Broccoli Finished and In Process')

        #Add an action elemento to the menu Inventories Broccoli 
        menu_Inventories_Broccoli_ny_add = QAction(QIcon(), "&Inventories Broccoli new year",self)
        menu_Inventories_Broccoli_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Inventories_Broccoli_ny_add.triggered.connect(self.menu_Inventories_Broccoli_ny)#Launcher
        menu_Inventories_Broccoli_Finissh_Process.addAction(menu_Inventories_Broccoli_ny_add)

        
        #Add an action elemento to the menu start
        menu_Inventories_Broccoli_table_edit = QAction(QIcon(), "&Edit data of Broccoli Inventories",self)
        menu_Inventories_Broccoli_table_edit.setStatusTip("Edit data of Broccoli Inventories")#Message in status bar
        menu_Inventories_Broccoli_table_edit.triggered.connect(self.menu_Inventories_Broccoli_Edit)#Launcher
        menu_Inventories_Broccoli_Finissh_Process.addAction(menu_Inventories_Broccoli_table_edit)

        
        #Add an action elemento to the menu start
        menu_Inventories_broccoli_xls_report = QAction(QIcon(), "&Broccoli Inventories Generate XLS Report",self)
        menu_Inventories_broccoli_xls_report.setStatusTip("Generate a Excel file of Broccoli Inventories")#Message in status bar
        menu_Inventories_broccoli_xls_report.triggered.connect(self.menu_Inventories_broccoli_xls)#Launcher
        menu_Inventories_Broccoli_Finissh_Process.addAction(menu_Inventories_broccoli_xls_report)
        
        

        
        menu_Inventories_Cauliflower = menu_Inventories.addMenu('&Inventories Cauliflower')
        menu_Inventories_Cauliflower_Finissh_Process= menu_Inventories_Cauliflower.addMenu('&Inventories Cauliflower Finished and In Process')

        #Add an action elemento to the menu Inventories Cauliflower 
        menu_Inventories_Cauliflower_ny_add = QAction(QIcon(), "&Inventories Cauliflower new year",self)
        menu_Inventories_Cauliflower_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Inventories_Cauliflower_ny_add.triggered.connect(self.menu_Inventories_cauliflower_ny)#Launcher
        menu_Inventories_Cauliflower_Finissh_Process.addAction(menu_Inventories_Cauliflower_ny_add)

        
        #Add an action elemento to the menu start
        menu_Inventories_Cauliflower_table_edit = QAction(QIcon(), "&Edit data of Cauliflower Inventories",self)
        menu_Inventories_Cauliflower_table_edit.setStatusTip("Edit data of Cauliflower Inventories")#Message in status bar
        menu_Inventories_Cauliflower_table_edit.triggered.connect(self.menu_Inventories_Cauliflower_Edit)#Launcher
        menu_Inventories_Cauliflower_Finissh_Process.addAction(menu_Inventories_Cauliflower_table_edit)

        
        #Add an action elemento to the menu start
        menu_Inventories_Cauliflower_xls_report = QAction(QIcon(), "&Cauliflower Inventories Generate XLS Report",self)
        menu_Inventories_Cauliflower_xls_report.setStatusTip("Generate a Excel file of Cauliflower Inventories")#Message in status bar
        menu_Inventories_Cauliflower_xls_report.triggered.connect(self.menu_Inventories_Cauliflower_xls)#Launcher
        menu_Inventories_Cauliflower_Finissh_Process.addAction(menu_Inventories_Cauliflower_xls_report)
        
        
        menu_Inventories_Carrots = menu_Inventories.addMenu('&Inventories Carrots')

        menu_Inventories_Carrots_Finissh_Process= menu_Inventories_Carrots.addMenu('&Inventories Carrots Finished and In Process')

        #Add an action elemento to the menu Inventories Carrots 
        menu_Inventories_Carrots_ny_add = QAction(QIcon(), "&Inventories Carrots new year",self)
        menu_Inventories_Carrots_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Inventories_Carrots_ny_add.triggered.connect(self.menu_Inventories_carrots_ny)#Launcher
        menu_Inventories_Carrots_Finissh_Process.addAction(menu_Inventories_Carrots_ny_add)

        
        #Add an action elemento to the menu start
        menu_Inventories_Carrots_table_edit = QAction(QIcon(), "&Edit data of Carrots Inventories",self)
        menu_Inventories_Carrots_table_edit.setStatusTip("Edit data of Carrots Inventories")#Message in status bar
        menu_Inventories_Carrots_table_edit.triggered.connect(self.menu_Inventories_Carrots_Edit)#Launcher
        menu_Inventories_Carrots_Finissh_Process.addAction(menu_Inventories_Carrots_table_edit)

        
        #Add an action elemento to the menu start
        menu_Inventories_Carrots_xls_report = QAction(QIcon(), "&Carrots Inventories Generate XLS Report",self)
        menu_Inventories_Carrots_xls_report.setStatusTip("Generate a Excel file of Carrots Inventories")#Message in status bar
        menu_Inventories_Carrots_xls_report.triggered.connect(self.menu_Inventories_Carrots_xls)#Launcher
        menu_Inventories_Carrots_Finissh_Process.addAction(menu_Inventories_Carrots_xls_report)        

        menu_Inventories_Ingredients = menu_Inventories.addMenu('& Inventories Ingredients')


        #Add an action elemento to the menu Inventories Ingredients
        menu_Inventories_Ingredients_ny_add = QAction(QIcon(), "&Inventories Ingredients new year",self)
        menu_Inventories_Ingredients_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Inventories_Ingredients_ny_add.triggered.connect(self.menu_Inventories_Ingredients_ny)#Launcher
        menu_Inventories_Ingredients.addAction(menu_Inventories_Ingredients_ny_add)

        
        #Add an action elemento to the menu start
        menu_Inventories_Ingredients_table_edit = QAction(QIcon(), "&Edit data of Ingredients Inventories",self)
        menu_Inventories_Ingredients_table_edit.setStatusTip("Edit data of Ingredients Inventories")#Message in status bar
        menu_Inventories_Ingredients_table_edit.triggered.connect(self.menu_Inventories_Ingredients_Edit)#Launcher
        menu_Inventories_Ingredients.addAction(menu_Inventories_Ingredients_table_edit)

        
        #Add an action elemento to the menu start
        menu_Inventories_Ingredients_xls_report = QAction(QIcon(), "&Ingredients Inventories Generate XLS Report",self)
        menu_Inventories_Ingredients_xls_report.setStatusTip("Generate a Excel file of Ingredients Inventories")#Message in status bar
        menu_Inventories_Ingredients_xls_report.triggered.connect(self.menu_Inventories_Ingredients_xls)#Launcher
        menu_Inventories_Ingredients.addAction(menu_Inventories_Ingredients_xls_report)        
        
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

        menu_production = menu_start.addMenu("&Production")
        
        #Add an action elemento to the menu start
        menu_Production_ny_add = QAction(QIcon(), "&Production new year",self)
        menu_Production_ny_add.setStatusTip("Start input data of a new year")#Message in status bar
        menu_Production_ny_add.triggered.connect(self.menu_Production_ny)#Launcher
        menu_production.addAction(menu_Production_ny_add)

        #Add an action elemento to the menu start
        menu_Production_table_edit = QAction(QIcon(), "&Edit data of Production",self)
        menu_Production_table_edit.setStatusTip("Edit data of Production")#Message in status bar
        menu_Production_table_edit.triggered.connect(self.menu_Production_Table_Edit)#Launcher
        menu_production.addAction(menu_Production_table_edit)

        #Add an action elemento to the menu start
        menu_Production_xls_report = QAction(QIcon(), "&Production Generate XLS Report",self)
        menu_Production_xls_report.setStatusTip("Generate a Excel file of Productions")#Message in status bar
        menu_Production_xls_report.triggered.connect(self.menu_Production_xls)#Launcher
        menu_production.addAction(menu_Production_xls_report)



        

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
        import inventories_mbusa_table_edit
        Dialog =  inventories_mbusa_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Inventories_Mbusa_xls (self):
        QMessageBox.information(self,"Inventories MB USA","You will generate a XLS file of MBUSA Inventories", QMessageBox.Discard)       
        import inventories_mbusa_xls_report
        Dialog =  inventories_mbusa_xls_report.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Broccoli_ny(self):
        QMessageBox.information(self,"Inventories Broccoli","You will start a New year data", QMessageBox.Discard)       
        import inventories_broccoli_ny
        Dialog =  inventories_broccoli_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Broccoli_Edit (self):
        QMessageBox.information(self,"Inventories Broccoli","You will edit the saved data of Broccoli Inventories", QMessageBox.Discard)       
        import inventories_broccoli_table_edit
        Dialog =  inventories_broccoli_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Inventories_broccoli_xls (self):
        QMessageBox.information(self,"Inventories Broccoli","You will generate a XLS file of Broccoli Inventories", QMessageBox.Discard)       
        import inventories_broccoli_xls_report
        Dialog =  inventories_broccoli_xls_report.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_cauliflower_ny(self):
        QMessageBox.information(self,"Inventories Cauliflower","You will start a New year data", QMessageBox.Discard)       
        import inventories_cauliflower_ny
        Dialog =  inventories_cauliflower_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Cauliflower_Edit (self):
        QMessageBox.information(self,"Inventories Cauliflower","You will edit the saved data of Cauliflower Inventories", QMessageBox.Discard)       
        import inventories_cauliflower_table_edit
        Dialog =  inventories_cauliflower_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Inventories_Cauliflower_xls (self):
        QMessageBox.information(self,"Inventories Cauliflower","You will generate a XLS file of Cauliflower Inventories", QMessageBox.Discard)       
        import inventories_cauliflower_xls_report
        Dialog =  inventories_cauliflower_xls_report.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_carrots_ny(self):
        QMessageBox.information(self,"Inventories Carrots","You will start a New year data", QMessageBox.Discard)       
        import inventories_carrots_ny
        Dialog =  inventories_carrots_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Carrots_Edit (self):
        QMessageBox.information(self,"Inventories Carrots","You will edit the saved data of Carrots Inventories", QMessageBox.Discard)       
        import inventories_carrots_table_edit
        Dialog =  inventories_carrots_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Inventories_Carrots_xls (self):
        QMessageBox.information(self,"Inventories Carrots","You will generate a XLS file of Carrots Inventories", QMessageBox.Discard)       
        import inventories_carrots_xls_report
        Dialog =  inventories_carrots_xls_report.MyWindowClass()
        Dialog.exec_()        

    def menu_Inventories_Ingredients_ny(self):
        QMessageBox.information(self,"Inventories Carrots","You will start a New year data", QMessageBox.Discard)       
        import inventories_Ingredients_ny
        Dialog =  inventories_Ingredients_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Inventories_Ingredients_Edit (self):
        QMessageBox.information(self,"Inventories Carrots","You will edit the saved data of Carrots Inventories", QMessageBox.Discard)       
        import inventories_ingredients_table_edit
        Dialog =  inventories_ingredients_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Inventories_Ingredients_xls (self):
        QMessageBox.information(self,"Inventories Carrots","You will generate a XLS file of Carrots Inventories", QMessageBox.Discard)       
        import inventories_ingredients_xls_report
        Dialog =  inventories_ingredients_xls_report.MyWindowClass()
        Dialog.exec_()        
            

    def menu_Sales_Esa_ny(self):
        QMessageBox.information(self,"Sales ESA","You will start a New year data", QMessageBox.Discard)       
        import sales_esa_ny
        Dialog =  sales_esa_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Sales_Esa_Table_Edit (self):
        QMessageBox.information(self,"Sales ESA","You will edit the saved data of MB USA Inventories", QMessageBox.Discard)       
        import sales_esa_table_edit
        Dialog =  sales_esa_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Sales_Esa_xls (self):
        QMessageBox.information(self,"Sales ESA","You will generate a XLS file of MBUSA Inventories", QMessageBox.Discard)       
        import sales_esa_xls_report
        Dialog =  sales_esa_xls_report.MyWindowClass()
        Dialog.exec_()

    def menu_Sales_Others_ny(self):
        QMessageBox.information(self,"Sales Others","You will start a New year data", QMessageBox.Discard)       
        import sales_others_ny
        Dialog =  sales_others_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Sales_Others_Table_Edit (self):
        QMessageBox.information(self,"Sales Others","You will edit the saved data of Others Sales", QMessageBox.Discard)       
        import sales_others_table_edit
        Dialog =  sales_others_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Sales_Others_xls (self):
        QMessageBox.information(self,"Sales Others","You will generate a XLS file of Others Sales", QMessageBox.Discard)       
        import sales_others_xls_report
        Dialog =  sales_others_xls_report.MyWindowClass()
        Dialog.exec_()

    def menu_Production_ny(self):
        QMessageBox.information(self,"Production","You will start a New year data", QMessageBox.Discard)       
        import production_ny
        Dialog =  production_ny.MyWindowClass()
        Dialog.exec_()

    def menu_Production_Table_Edit (self):
        QMessageBox.information(self,"Production","You will edit the saved data of Production", QMessageBox.Discard)       
        import production_table_edit
        Dialog =  production_table_edit.Dialogo()
        Dialog.exec_()

    def menu_Production_xls (self):
        QMessageBox.information(self,"Production","You will generate a XLS file of Production Data", QMessageBox.Discard)       
        import production_xls_report
        Dialog =  production_xls_report.MyWindowClass()
        Dialog.exec_()

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
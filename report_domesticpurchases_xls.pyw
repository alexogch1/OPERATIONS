#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this module is generated the report of Domestic Sales
"""
__author__ = "Alejandro Othoniel Gomez Chavez"
__copyright__ = "Copyright 2018 AOGCH"
__credits__ = "Mar Bran S.A. de C.V."

__licence__= "Open Code"
__version__ = "0.1"
__maintainer__ = "Alejandro Othoniel Gomez Chavez"
__email__ = "agomez@marbran.com.mx"
__status__ = "Developer"

import xlwt
from tempfile import TemporaryFile


from datetime import datetime 
from datetime import  timedelta
import numpy as np
import pandas as pd
import caja_mensaje as mensaje


title = ""
title2 = ""

from PyQt5 import QtCore, QtWidgets
import datetime
import pandas as pd

class main():
    def __init__(self,datos):
        print('aqui se estan generando el archivo en excel')
        print(datos)
        print
        xls = XLS(datos)
        xls.genera_reporte(datos)
        

class XLS():
    
    def caja_mensaje (self, text, title, style):
        import caja_mensaje as mensaje
        mensaje.Caja_mensaje.mbox(text, title, style)
        
    def __init__(self,datos):
        self.datos = datos

    def genera_reporte(self,datos):

  

        list_row = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Total']

        self.book = xlwt.Workbook()
        self.sheet1 = self.book.add_sheet('DOMESTIC PURCHASES')          # Crea las columnas con los datos correspondientes
        
        encabezado = self.header(self.sheet1, list_row)
        encabezado

        principa =self.main_body_sht(self.sheet1)
        principa

        
        guardar = self.save_sheet()
        guardar

   


    def header(self, hoja, rows): # Coloca los titulos principales en la hoja de calculo)
        import caja_mensaje as mensaje
        title = 'Mar Bran S.A. de C.V.'
        title2 = 'Innovación, Mejora Continua y Six Sigma'
        title3 = 'DOMESTIC PURCHASES'
        rows = rows
        hoja = hoja
        hoja.write(0,0,title)  
        hoja.write(1,0,title2 )
        hoja.write(2,0,title3 )
        for i, valor in  enumerate(rows):
            print( i, valor)
            hoja.write(6+i, 0,valor)
        

    def main_body_sht(self,hoja):
        hoja = hoja
        
        prod = {}
        prod = self.datos[0]
        values = list(prod.values())
        product = list(prod.keys())
        columna = 1
        np_prod = np.array(values)
        print(np_prod)
        acum = np_prod.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        

        prod2 = {}
        prod2 = self.datos[1]
        values = list(prod2.values())
        product = list(prod2.keys())
        columna = 2
        np_prod2 = np.array(values)
        print(np_prod2)
        acum = np_prod2.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod3 = {}
        prod3 = self.datos[2]
        values = list(prod3.values())
        product = list(prod3.keys())
        columna = 3
        np_prod3 = np.array(values)
        print(np_prod3)
        acum = np_prod3.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod4 = {}
        prod4 = self.datos[3]
        values = list(prod4.values())
        product = list(prod4.keys())
        columna = 4
        np_prod4 = np.array(values)
        print(np_prod4)
        acum = np_prod4.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        total_Domestic_Purchases = np_prod + np_prod2 + np_prod3 + np_prod4
        print(total_Domestic_Purchases)
        total_Domestic_Purchases = total_Domestic_Purchases.tolist()
        print('Total Purchases ', total_Domestic_Purchases[0])
        dict_total_Domestic_Purchases = {}
        dict_total_Domestic_Purchases['total Domestic Purchases'] = total_Domestic_Purchases[0]
        print(dict_total_Domestic_Purchases)
        values = list(dict_total_Domestic_Purchases.values())
        producto = list(dict_total_Domestic_Purchases.keys())
        np_Total_Domestic_Purchases = np.array(values)
        acum = np_Total_Domestic_Purchases.sum()
        columna = 6
        self.ingresa_datos(hoja,columna,producto,values,acum)

        
        

    def ingresa_datos(self,hoja, columna,producto,values, acum):
        total = acum
        hoja = hoja
        lista_titulos2 = ['lbs']
        columna = columna
        prod1 = producto
        values = values
        hoja.write(4, columna,producto[0])
        hoja.write(5, columna,lista_titulos2[0])

        for i, valor in  enumerate(values[0]):
            print( i, valor)
            hoja.write(6+i, columna,valor)
        hoja.write(18, columna,total)
     

   
    def save_sheet(self):
        name = "domestic purchases.xls"
        try:
            self.book.save(name)
            self.book.save(TemporaryFile())
            mensaje = "Archivo Garudado como: "+ name +  ' \nDatos guardados con Exito!!!'
            self.caja_mensaje('Guadar Datos;',mensaje  ,0)
            #DialogProduccion.show()
        except Exception as ex:
            ex = 'El archivo '+ name +" esta abierto: " +  str(ex) 
            #print(ex)
            self.caja_mensaje('Error al momento de guardar ', ex,0)
  
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this module is generated the report of import Sales
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

  

        list_row = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

        self.book = xlwt.Workbook()
        self.sheet1 = self.book.add_sheet('MB USA INVENTORIES')          # Crea las columnas con los datos correspondientes
        
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
        title3 = 'MBUSA INVENTORIES'
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
        columna = 38
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

        prod5 = {}
        prod5 = self.datos[4]
        values = list(prod5.values())
        product = list(prod5.keys())
        columna = 5
        np_prod5 = np.array(values)
        print(np_prod5)
        acum = np_prod5.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod6 = {}
        prod6 = self.datos[5]
        values = list(prod6.values())
        product = list(prod6.keys())
        columna = 6
        np_prod6 = np.array(values)
        print(np_prod6)
        acum = np_prod6.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod7 = {}
        prod7 = self.datos[6]
        values = list(prod7.values())
        product = list(prod7.keys())
        columna = 7
        np_prod7 = np.array(values)
        print(np_prod7)
        acum = np_prod7.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod8 = {}
        prod8 = self.datos[7]
        values = list(prod8.values())
        product = list(prod8.keys())
        columna = 8
        np_prod8 = np.array(values)
        print(np_prod8)
        acum = np_prod8.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod9 = {}
        prod9 = self.datos[8]
        values = list(prod9.values())
        product = list(prod9.keys())
        columna = 9
        np_prod9 = np.array(values)
        print(np_prod9)
        acum = np_prod9.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod10 = {}
        prod10 = self.datos[9]
        values = list(prod10.values())
        product = list(prod10.keys())
        columna = 10
        np_prod10 = np.array(values)
        print(np_prod10)
        acum = np_prod10.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod11 = {}
        prod11 = self.datos[10]
        values = list(prod11.values())
        product = list(prod11.keys())
        print(product)
        columna = 11
        np_prod11 = np.array(values)
        print(np_prod11)
        acum = np_prod11.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod12 = {}
        prod12 = self.datos[11]
        values = list(prod12.values())
        product = list(prod12.keys())
        columna = 12
        np_prod12 = np.array(values)
        print(np_prod12)
        acum = np_prod12.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod13 = {}
        prod13 = self.datos[12]
        values = list(prod13.values())
        product = list(prod13.keys())
        columna = 13
        np_prod13 = np.array(values)
        print(np_prod13)
        acum = np_prod13.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod14 = {}
        prod14 = self.datos[13]
        values = list(prod14.values())
        product = list(prod14.keys())
        columna = 14
        np_prod14 = np.array(values)
        print(np_prod14)
        acum = np_prod14.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        """
        prod15 = {}
        prod15 = self.datos[14]
        values = list(prod15.values())
        product = list(prod15.keys())
        columna = 15
        np_prod15 = np.array(values)
        print(np_prod15)
        acum = np_prod15.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod16 = {}
        prod16 = self.datos[15]
        values = list(prod16.values())
        product = list(prod16.keys())
        columna = 16
        np_prod16 = np.array(values)
        print(np_prod16)
        acum = np_prod16.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod17 = {}
        prod17 = self.datos[16]
        values = list(prod17.values())
        product = list(prod17.keys())
        columna = 17
        np_prod17 = np.array(values)
        print(np_prod17)
        acum = np_prod17.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod18 = {}
        prod18 = self.datos[17]
        values = list(prod18.values())
        product = list(prod18.keys())
        columna = 18
        np_prod18 = np.array(values)
        print(np_prod18)
        acum = np_prod18.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod19 = {}
        prod19 = self.datos[18]
        values = list(prod19.values())
        product = list(prod19.keys())
        columna = 19
        np_prod19 = np.array(values)
        print(np_prod19)
        acum = np_prod19.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod20 = {}
        prod20 = self.datos[19]
        values = list(prod20.values())
        product = list(prod20.keys())
        columna = 20
        np_prod20 = np.array(values)
        print(np_prod20)
        acum = np_prod20.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod21 = {}
        prod21 = self.datos[20]
        values = list(prod21.values())
        product = list(prod21.keys())
        columna = 21
        np_prod21 = np.array(values)
        print(np_prod21)
        acum = np_prod21.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod22 = {}
        prod22 = self.datos[21]
        values = list(prod22.values())
        product = list(prod22.keys())
        columna = 22
        np_prod22 = np.array(values)
        print(np_prod22)
        acum = np_prod22.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod23 = {}
        prod23 = self.datos[22]
        values = list(prod23.values())
        product = list(prod23.keys())
        columna = 23
        np_prod23 = np.array(values)
        print(np_prod23)
        acum = np_prod23.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod24 = {}
        prod24 = self.datos[23]
        values = list(prod24.values())
        product = list(prod24.keys())
        columna = 24
        np_prod24 = np.array(values)
        print(np_prod24)
        acum = np_prod24.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod25 = {}
        prod25 = self.datos[24]
        values = list(prod25.values())
        product = list(prod25.keys())
        columna = 25
        np_prod25 = np.array(values)
        print(np_prod25)
        acum = np_prod25.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod26 = {}
        prod26 = self.datos[25]
        values = list(prod26.values())
        product = list(prod26.keys())
        columna = 26
        np_prod26 = np.array(values)
        print(np_prod26)
        acum = np_prod26.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod27 = {}
        prod27 = self.datos[26]
        values = list(prod27.values())
        product = list(prod27.keys())
        columna = 27
        np_prod27 = np.array(values)
        print(np_prod27)
        acum = np_prod27.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod28 = {}
        prod28 = self.datos[27]
        values = list(prod28.values())
        product = list(prod28.keys())
        columna = 28
        np_prod28 = np.array(values)
        print(np_prod28)
        acum = np_prod28.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod29 = {}
        prod29 = self.datos[28]
        values = list(prod29.values())
        product = list(prod29.keys())
        columna = 29
        np_prod29 = np.array(values)
        print(np_prod29)
        acum = np_prod29.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod30 = {}
        prod30 = self.datos[29]
        values = list(prod30.values())
        product = list(prod30.keys())
        columna = 30
        np_prod30 = np.array(values)
        print(np_prod30)
        acum = np_prod30.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod31 = {}
        prod31 = self.datos[30]
        values = list(prod31.values())
        product = list(prod31.keys())
        columna = 31
        np_prod31 = np.array(values)
        print(np_prod31)
        acum = np_prod31.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod32 = {}
        prod32 = self.datos[31]
        values = list(prod32.values())
        product = list(prod32.keys())
        columna = 32
        np_prod32 = np.array(values)
        print(np_prod32)
        acum = np_prod32.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod33 = {}
        prod33 = self.datos[32]
        values = list(prod33.values())
        product = list(prod33.keys())
        columna = 33
        np_prod33 = np.array(values)
        print(np_prod33)
        acum = np_prod33.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )

        prod34 = {}
        prod34 = self.datos[33]
        values = list(prod34.values())
        product = list(prod34.keys())
        columna = 34
        np_prod34 = np.array(values)
        print(np_prod34)
        acum = np_prod34.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,product,values, acum )
        """

        np_group1 = np_prod + np_prod2 + np_prod3 + np_prod4 + np_prod5 
        np_group2 = np_prod6+ np_prod7 + np_prod8 + np_prod9 +np_prod10 
        np_group3 = np_prod11 + np_prod12 + np_prod13 + np_prod14 
        
        np_Total_Mbusa_Inventories = np_group1 + np_group2 + np_group3 
        print(np_Total_Mbusa_Inventories)
        Total_Mbusa_Inventories = np_Total_Mbusa_Inventories.tolist()
        print('Total MBUSA INVENTORIES ', Total_Mbusa_Inventories[0])
        dict_total_Mbusa_Inventories = {}
        dict_total_Mbusa_Inventories['Total MBUSA INVENTORIESs'] = Total_Mbusa_Inventories[0]
        print(dict_total_Mbusa_Inventories)
        values = list(dict_total_Mbusa_Inventories.values())
        producto = list(dict_total_Mbusa_Inventories.keys())
        np_Total_Inventories = np.array(values)
        acum = np_Total_Inventories.sum()
        columna = 16
        self.ingresa_datos(hoja,columna,producto,values,acum)


        
        

        np_conventional = np_prod + np_prod3 +  np_prod5 + np_prod7 + np_prod8 + np_prod9 + np_prod10 + np_prod11 + np_prod12 + np_prod13 + np_prod14
        total_Conventional  = np_conventional.tolist()
        print('Total Inventories Conventional ', total_Conventional[0])
        dict_total_Conventional = {}
        dict_total_Conventional['total Conventional'] = total_Conventional[0]
        print(dict_total_Conventional)
        values = list(dict_total_Conventional.values())
        producto = list(dict_total_Conventional.keys())
        np_Total_Conv = np.array(values)
        acum = np_Total_Conv.sum()
        columna = 18
        self.ingresa_datos(hoja,columna,producto,values,acum)      


        np_Organic = np_prod2 + np_prod4 + np_prod6
        total_Organic = np_Organic.tolist()
        print('Total Inventories Organic  ', total_Organic[0])
        dict_total_Organic = {}
        dict_total_Organic['Total Inventories Organic'] = total_Organic[0]
        print(dict_total_Organic)
        values = list(dict_total_Organic.values())
        producto = list(dict_total_Organic.keys())
        np_Total_Org = np.array(values)
        acum = np_Total_Org.sum()
        columna = 19
        self.ingresa_datos(hoja,columna,producto,values,acum)      

    

    def ingresa_datos(self,hoja, columna,producto,values, acum):
        total = acum
        hoja = hoja
        lista_titulos2 = ['lbs']
        columna = columna
        prod1 = producto
        values = values
        hoja.write(4, columna,prod1[0])
        hoja.write(5, columna,lista_titulos2[0])

        for i, valor in  enumerate(values[0]):
            print( i, valor)
            hoja.write(6+i, columna,valor)
        #hoja.write(18, columna,total)
     

   
    def save_sheet(self):
        name = "mbusa Inventories.xls"
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
  
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In thismodule it is input the data of MB USA sales
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
        self.sheet1 = self.book.add_sheet('MBUSA SALES')          # Crea las columnas con los datos correspondientes
        
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
        title3 = 'MB USA SALES'
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
        Total_brocc = {}
        Total_brocc = self.datos[0]
                
        values = list(Total_brocc.values())
        prod1 = list(Total_brocc.keys())
        columna = 1
        np_Brocc_Total = np.array(values)
        print(np_Brocc_Total)
        acum = np_Brocc_Total.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )
        

        Total_colif = {}
        Total_colif = self.datos[1]
        values = list(Total_colif.values())
        prod1 = list(Total_colif.keys())
        columna = 2
        np_Caulif_Total = np.array(values)
        print(np_Caulif_Total)
        acum = np_Caulif_Total.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum)



        Total_BrSpr = {}
        Total_BrSpr = self.datos[2]
        values = list(Total_BrSpr.values())
        prod1 = list(Total_BrSpr.keys())
        columna = 3
        np_BrSp_Total = np.array(values)
        acum = np_BrSp_Total.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum)
        

        Total_Ssp = {}
        Total_Ssp = self.datos[3]
        values = list(Total_Ssp.values())
        prod1 = list(Total_Ssp.keys())
        columna = 4
        np_Ssp = np.array(values)
        acum = np_Ssp.sum()
        self.ingresa_datos(hoja,columna,prod1, values, acum)

        Total_Y_Sq = {}
        Total_Y_Sq = self.datos[4]
        values = list(Total_Y_Sq.values())
        prod1 = list(Total_Y_Sq.keys())
        columna = 5
        np_Y_Sq = np.array(values)
        acum = np_Y_Sq.sum()
        self.ingresa_datos(hoja,columna,prod1,values, acum)


        Total_G_Zucc = {}
        Total_G_Zucc = self.datos[5]
        values = list(Total_G_Zucc.values())
        prod1 = list(Total_G_Zucc.keys())
        columna = 6
        np_G_Succ = np.array(values)
        acum = np_G_Succ.sum()
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        Total_Other = {}
        Total_Other = self.datos[6]
        values = list(Total_Other.values())
        prod1 = list(Total_Other.keys())
        columna = 7
        np_Others = np.array(values)
        acum = np_Others.sum()
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        Total_Sales= {}
        Total_Sales = self.datos[14]
        values = list(Total_Sales.values())
        prod1 = list(Total_Sales.keys())
        columna = 8
        np_total_Sales = np.array(values)
        acum = np_total_Sales.sum()
        print('arra de Ventas Totales',np_total_Sales )
        self.ingresa_datos(hoja,columna,prod1,values, acum)

        Brocc_Org= {}
        Brocc_Org = self.datos[7]
        values = list(Brocc_Org.values())
        prod1 = list(Brocc_Org.keys())
        columna = 10
        np_Brocc_Org = np.array(values)
        acum = np_Brocc_Org.sum()
        print('array de broccoli org',np_Brocc_Org )
        self.ingresa_datos(hoja,columna,prod1,values, acum)

        caulif_Org= {}
        caulif_Org = self.datos[8]
        values = list(caulif_Org.values())
        prod1 = list(caulif_Org.keys())
        columna = 11
        np_Caulif_Org = np.array(values)
        acum = np_Caulif_Org.sum()
        print('array de broccoli org',np_Caulif_Org )
        self.ingresa_datos(hoja,columna,prod1,values, acum)


        carrots_Org= {}
        carrots_Org = self.datos[9]
        values = list(carrots_Org.values())
        prod1 = list(carrots_Org.keys())
        np_Carrot_Org = np.array(values)
        acum = np_Carrot_Org.sum()
        columna = 12
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        corn_Org= {}
        corn_Org = self.datos[10]
        values = list(corn_Org.values())
        prod1 = list(corn_Org.keys())
        columna = 13
        np_Corn_Org = np.array(values)
        acum = np_Corn_Org.sum()
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        edamame_Org= {}
        edamame_Org = self.datos[11]
        values = list(edamame_Org.values())
        prod1 = list(edamame_Org.keys())
        np_Edamame_Org = np.array(values)
        acum = np_Edamame_Org.sum()
        columna = 14
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        total_Org= {}
        total_Org = self.datos[12]
        values = list(total_Org.values())
        prod1 = list(total_Org.keys())
        columna = 15
        np_total_Org = np.array(values)
        acum = np_total_Org.sum()
        print('array de Total org',np_total_Org )
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        Brocc_Conv = np_Brocc_Total- np_Brocc_Org
        Brocc_Conv=Brocc_Conv.tolist()
        print('broccoli convencional ', Brocc_Conv[0])
        dict_Brocc_Conv = {}
        dict_Brocc_Conv['Brocc Conv'] = Brocc_Conv[0]
        print(dict_Brocc_Conv)
        values = list(dict_Brocc_Conv.values())
        prod1 = list(dict_Brocc_Conv.keys())
        columna = 16
        np_Brocc_Conv = np.array(values)
        acum = np_Brocc_Conv.sum()
        self.ingresa_datos(hoja,columna,prod1,values,acum)


        Caulif_Conv = np_Caulif_Total- np_Caulif_Org
        Caulif_Conv=Caulif_Conv.tolist()
        print('Coliflor convencional ', Caulif_Conv[0])
        dict_Caulif_Conv = {}
        dict_Caulif_Conv['Caulif Conv'] = Caulif_Conv[0]
        print(dict_Caulif_Conv)
        values = list(dict_Caulif_Conv.values())
        prod1 = list(dict_Caulif_Conv.keys())
        np_Caulif_Conv = np.array(values)
        acum = np_Caulif_Conv.sum()
        columna = 17
        self.ingresa_datos(hoja,columna,prod1,values,acum)


        total_Conv = np_total_Sales- np_total_Org
        total_Conv=total_Conv.tolist()
        print('Total convencional ', total_Conv[0])
        dict_total_Conv = {}
        dict_total_Conv['Total Conv'] = total_Conv[0]
        print(dict_total_Conv)
        values = list(dict_total_Conv.values())
        prod1 = list(dict_total_Conv.keys())
        np_Total_Conv = np.array(values)
        acum = np_Total_Conv.sum()
        columna = 18
        self.ingresa_datos(hoja,columna,prod1,values,acum)

    def ingresa_datos(self,hoja, columna,prod,values, acum):
        total = acum
        hoja = hoja
        lista_titulos2 = ['lbs']
        columna = columna
        prod1 = prod
        values = values
        hoja.write(4, columna,prod1[0])
        hoja.write(5, columna,lista_titulos2[0])

        for i, valor in  enumerate(values[0]):
            print( i, valor)
            hoja.write(6+i, columna,valor/1000)
        hoja.write(18, columna,total/1000)
     

   
    def save_sheet(self):
        name = "mbusa sales.xls"
        try:
            self.book.save(name)
            self.book.save(TemporaryFile())
            mensaje = "Archivo Garudado como: "+ name+'.xls'   ' \nDatos guardados con Exito!!!'
            self.caja_mensaje('Guadar Datos;',mensaje  ,0)
            #DialogProduccion.show()
        except Exception as ex:
            ex = 'El archivo '+ name +" esta abierto: " +  str(ex) 
            #print(ex)
            self.caja_mensaje('Error al momento de guardar ', ex,0)
  
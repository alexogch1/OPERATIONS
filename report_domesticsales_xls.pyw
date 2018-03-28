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
        self.sheet1 = self.book.add_sheet('DOMESTIC SALES')          # Crea las columnas con los datos correspondientes
        
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
        title3 = 'DOMESTIC SALES'
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
        
        conv_Brocc = {}
        conv_Brocc = self.datos[0]
        values = list(conv_Brocc.values())
        prod1 = list(conv_Brocc.keys())
        columna = 1
        np_Conv_Brocc = np.array(values)
        print(np_Conv_Brocc)
        acum = np_Conv_Brocc.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        org_Brocc = {}
        org_Brocc = self.datos[1]
        values = list(org_Brocc.values())
        prod1 = list(org_Brocc.keys())
        columna = 2
        np_Org_Brocc = np.array(values)
        print(np_Org_Brocc)
        acum = np_Org_Brocc.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        conv_Caulif = {}
        conv_Caulif = self.datos[2]
        values = list(conv_Caulif.values())
        prod1 = list(conv_Caulif.keys())
        columna = 3
        np_Conv_Caulif = np.array(values)
        print(np_Conv_Caulif)
        acum = np_Conv_Caulif.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        org_Caulif = {}
        org_Caulif = self.datos[3]
        values = list(org_Caulif.values())
        prod1 = list(org_Caulif.keys())
        columna = 4
        np_Org_Caulif = np.array(values)
        print(np_Org_Caulif)
        acum = np_Org_Caulif.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        conv_Crkle_Carrots = {}
        conv_Crkle_Carrots = self.datos[4]
        values = list(conv_Crkle_Carrots.values())
        prod1 = list(conv_Crkle_Carrots.keys())
        columna = 5
        np_conv_Crkle_Carrots = np.array(values)
        print(np_conv_Crkle_Carrots)
        acum = np_conv_Crkle_Carrots.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        conv_Ddc_Carrots = {}
        conv_Ddc_Carrots = self.datos[5]
        values = list(conv_Ddc_Carrots.values())
        prod1 = list(conv_Ddc_Carrots.keys())
        columna = 6
        np_Conv_Dcd_Carrots = np.array(values)
        print(np_Conv_Dcd_Carrots)
        acum = np_Conv_Dcd_Carrots.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        org_Carrots = {}
        org_Carrots = self.datos[7]
        values = list(org_Carrots.values())
        prod1 = list(org_Carrots.keys())
        columna = 8
        np_Org_Carrots = np.array(values)
        print(np_Org_Carrots)
        acum = np_Org_Carrots.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        total_Conv_Carrots = np_conv_Crkle_Carrots + np_Conv_Dcd_Carrots
        total_Conv_Carrots = total_Conv_Carrots.tolist()
        print('Total convencional Carrots ', total_Conv_Carrots[0])
        dict_total_Conv_Carrots = {}
        dict_total_Conv_Carrots['total Conv Carrots'] = total_Conv_Carrots[0]
        print(dict_total_Conv_Carrots)
        values = list(dict_total_Conv_Carrots.values())
        prod1 = list(dict_total_Conv_Carrots.keys())
        np_Total_Conv_Carrots = np.array(values)
        acum = np_Total_Conv_Carrots.sum()
        columna = 7
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        green_Zucc = {}
        green_Zucc = self.datos[8]
        values = list(green_Zucc.values())
        prod1 = list(green_Zucc.keys())
        columna = 9
        np_green_Zucc = np.array(values)
        print(np_green_Zucc)
        acum = np_green_Zucc.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        peas = {}
        peas = self.datos[9]
        values = list(peas.values())
        prod1 = list(peas.keys())
        columna = 10
        np_Peas = np.array(values)
        print(np_Peas)
        acum = np_Peas.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )


        poblano = {}
        poblano = self.datos[10]
        values = list(poblano.values())
        prod1 = list(poblano.keys())
        columna = 11
        np_Poblano = np.array(values)
        print(np_Poblano)
        acum = np_Poblano.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        whole_Corn = {}
        whole_Corn = self.datos[11]
        values = list(whole_Corn.values())
        prod1 = list(whole_Corn.keys())
        columna = 12
        np_Whole_Corn = np.array(values)
        print(np_Whole_Corn)
        acum = np_Whole_Corn.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        total_Corn = {}
        total_Corn = self.datos[12]
        values = list(total_Corn.values())
        prod1 = list(total_Corn.keys())
        columna = 14
        np_Total_Corn = np.array(values)
        print(np_Total_Corn)
        acum = np_Total_Corn.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )


        sweet_Corn  = np_Total_Corn - np_Whole_Corn
        sweet_Corn = sweet_Corn.tolist()
        print('Sweet Corn ', sweet_Corn[0])
        dict_Sweet_Corn = {}
        dict_Sweet_Corn['Sweet Corn'] = sweet_Corn[0]
        print(dict_Sweet_Corn)
        values = list(dict_Sweet_Corn.values())
        prod1 = list(dict_Sweet_Corn.keys())
        np_Sweet_Corn = np.array(values)
        acum = np_Sweet_Corn.sum()
        columna = 13
        self.ingresa_datos(hoja,columna,prod1,values,acum)

        green_Beans = {}
        green_Beans = self.datos[14]
        values = list(green_Beans.values())
        prod1 = list(green_Beans.keys())
        columna = 15
        np_Green_Beans = np.array(values)
        print(np_Green_Beans)
        acum = np_Green_Beans.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        mushrooms = {}
        mushrooms = self.datos[15]
        values = list(mushrooms.values())
        prod1 = list(mushrooms.keys())
        columna = 16
        np_Mushrooms = np.array(values)
        print(np_Mushrooms)
        acum = np_Mushrooms.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )


        onion = {}
        onion = self.datos[16]
        values = list(onion.values())
        prod1 = list(onion.keys())
        columna = 17
        np_Onion = np.array(values)
        print(np_Onion)
        acum = np_Onion.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        potatoes = {}
        potatoes = self.datos[17]
        values = list(potatoes.values())
        prod1 = list(potatoes.keys())
        columna = 18
        np_Potatoes = np.array(values)
        print(np_Potatoes)
        acum = np_Potatoes.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        red_Pepper = {}
        red_Pepper = self.datos[18]
        values = list(red_Pepper.values())
        prod1 = list(red_Pepper.keys())
        columna = 19
        np_Red_Pepper = np.array(values)
        print(np_Red_Pepper)
        acum = np_Red_Pepper.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        snow_Peas = {}
        snow_Peas = self.datos[19]
        values = list(snow_Peas.values())
        prod1 = list(snow_Peas.keys())
        columna = 20
        np_Snow_Peas = np.array(values)
        print(np_Snow_Peas)
        acum = np_Snow_Peas.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        spinach = {}
        spinach = self.datos[20]
        values = list(spinach.values())
        prod1 = list(spinach.keys())
        columna = 21
        np_Spinach = np.array(values)
        print(np_Spinach)
        acum = np_Spinach.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        wchn = {}
        wchn = self.datos[21]
        values = list(wchn.values())
        prod1 = list(wchn.keys())
        columna = 22
        np_Wchn = np.array(values)
        print(np_Wchn)
        acum = np_Wchn.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        others = {}
        others = self.datos[22]
        values = list(others.values())
        prod1 = list(others.keys())
        columna = 23
        np_Others = np.array(values)
        print(np_Others)
        acum = np_Others.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        total_Org = {}
        total_Org = self.datos[23]
        values = list(total_Org.values())
        prod1 = list(total_Org.keys())
        columna = 25
        np_Total_Org = np.array(values)
        print(np_Total_Org)
        acum = np_Total_Org.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        total_Conv = {}
        total_Conv = self.datos[24]
        values = list(total_Conv.values())
        prod1 = list(total_Conv.keys())
        columna = 26
        np_Total_Conv = np.array(values)
        print(np_Total_Conv)
        acum = np_Total_Conv.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        total_Sales = {}
        total_Sales = self.datos[25]
        values = list(total_Sales.values())
        prod1 = list(total_Sales.keys())
        columna = 27
        np_Total_Sales = np.array(values)
        print(np_Total_Sales)
        acum = np_Total_Sales.sum()
        print(acum)
        self.ingresa_datos(hoja,columna,prod1,values, acum )

        

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
        name = "domestic sales.xls"
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
  
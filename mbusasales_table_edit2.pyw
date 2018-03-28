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

import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton,QMessageBox
from PyQt5 import uic

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setWindowTitle("MBUSA Sales") #Título
		self.resize(1400, 450) #Tamaño inicial
		self.layout = QGridLayout() #Crear un layout grid
		self.setLayout(self.layout) #Agregar el layout al cuadro de diálogo
		self.table = QTableWidget() #Crear la tabla
		self.btn_eliminar = QPushButton("Eliminar fila/s")
		self.layout.addWidget(self.btn_eliminar)
		self.layout.addWidget(self.table) #Agregar la tabla al layout
		
		self.Seleccionar()
		self.table.itemChanged.connect(self.Actualizar)
		self.btn_eliminar.clicked.connect(self.Eliminar)
		
	def Seleccionar(self):
		self.table.setColumnCount(16)
		self.table.setHorizontalHeaderLabels(['ID','INDEX', 'YEAR', 'MONTH',
			'TOTAL SALES','BROCC.', 'CAULIF.', 'BRUSSELS SPR', 'SUGAR SNAP PEAS',
			'YELLOW SQ', 'GREEN ZUCC', 'BROCC. ORG', 'CAULIF. ORG.' , 
			'CARROTS ORG.', 'CORN ORG.', 'EDAM. ORG.'])
		
		mbusasales = pd.read_csv('mbusasales.csv', index_col = 0, encoding = 'utf-8')
		mbusasales.apply(lambda x: pd.lib.infer_dtype(x.values))
		mbusasales.index = range(mbusasales.shape[0])
		num_datos = int(mbusasales['year'].count())
		print(type(num_datos))
		print(mbusasales.index)
		row = 0 
		print("se cumple condicion while", row <= num_datos, "renglon","numero de datos", num_datos, "renglon", row)
		while row < num_datos:
			self.table.insertRow(row)
			id1 = mbusasales.index[row]
			print(id1)
			id = QTableWidgetItem(str(id1))
			self.table.setItem(row, 0, id)
			indice1 = mbusasales['indice'][row]
			indice = QTableWidgetItem(str(indice1))
			self.table.setItem(row, 1, indice)
			year1 = mbusasales['year'][row]
			year = QTableWidgetItem(str(year1))
			self.table.setItem(row, 2, year)
			month1 = mbusasales['month'][row]
			month = QTableWidgetItem(str(month1))
			self.table.setItem(row, 3,month)
			prod01= mbusasales['totsales'][row]
			prod0 = QTableWidgetItem(str(prod01))
			self.table.setItem(row, 4,prod0)
			prod11 = mbusasales['broc'][row]
			prod1 = QTableWidgetItem(str(prod11))
			self.table.setItem(row, 5,prod1)
			prod21 = mbusasales['cauliflower'][row]
			prod2 = QTableWidgetItem(str(prod21))
			self.table.setItem(row, 6,prod2)
			prod31 = mbusasales['br spr'][row]
			prod3=QTableWidgetItem(str(prod31))
			self.table.setItem(row, 7,prod3)
			prod41 = mbusasales['Sugar Snap Peas'][row]
			prod4=QTableWidgetItem(str(prod41))
			self.table.setItem(row,8,prod4)
			prod51 = mbusasales['Yellow Sq'][row]
			prod5 = QTableWidgetItem(str(prod51))
			self.table.setItem(row,9,prod5)
			prod61 = mbusasales['Green Zucch'][row]
			prod6 = QTableWidgetItem(str(prod61))
			self.table.setItem(row,10,prod6)
			prod71= mbusasales['Brocc Org'][row]
			prod7 = QTableWidgetItem(str(prod71))
			self.table.setItem(row,11,prod7)
			prod81 = mbusasales['Caulif Org'][row]
			prod8 = QTableWidgetItem(str(prod81))
			self.table.setItem(row,12,prod8)
			prod91 = mbusasales['Carrots Org'][row]
			prod9 = QTableWidgetItem(str(prod91))
			self.table.setItem(row,13,prod9)
			prod101= mbusasales['Corn Org'][row]
			prod10 = QTableWidgetItem(str(prod101))
			self.table.setItem(row,14,prod10)
			prod111= mbusasales['Edamame Org'][row]
			prod11 = QTableWidgetItem(str(prod111))
			self.table.setItem(row,15,prod11)
			row = row + 1      
		
	def Actualizar(self):
					print("modulo actualizar")
					datos = pd.read_csv('mbusasales.csv', index_col = 0, encoding = 'utf-8')
					datos.apply(lambda x: pd.lib.infer_dtype(x.values))
					column = self.table.currentColumn()-1
					row = self.table.currentRow()
					id = self.table.item(row, 0).text()
					id =int(id)
					id_datos = self.table.item(row, 1).text()
					year = self.table.item(row,2).text()
					month = self.table.item(row,3).text()
					prod0 = self.table.item(row,4).text()
					prod1 = self.table.item(row,5).text()
					prod2 = self.table.item(row,6).text()
					prod3 = self.table.item(row,7).text()
					prod4 = self.table.item(row,8).text()
					prod5 = self.table.item(row,9).text()
					prod6 = self.table.item(row,10).text()
					prod7 = self.table.item(row,11).text()
					prod8 = self.table.item(row,12).text()
					prod9 = self.table.item(row,13).text()
					prod10 = self.table.item(row,14).text()
					prod11 = self.table.item(row,15).text()
					print("el id a actualizar es",id)
					print("la columna a actualizar es", column)
					nombre_columna = datos.columns.values[column]
					print(nombre_columna)
					value = self.table.currentItem().text()
					print("el valor nuevo a actualizar es", value)
					print()
					print("datos originales")
					print(datos)

					if nombre_columna == "indice":
						print("vamos a actualizar la tabla con el indice")
						id_datos = value
						print(id_datos)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')
					
					elif nombre_columna == "year" :
						print("vamos a actualizar la tabla con el año ")
						year = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')
					
					elif nombre_columna == "month" :
						print("vamos a actualizar la tabla con el mes ")
						month = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "totsales" :
						print("vamos a actualizar la tabla con las ventas totals ")
						prod0 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "broc" :
						print("vamos a actualizar la tabla con el broccoli conv ")
						prod1 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "cauliflower" :
						print("vamos a actualizar la tabla con el coliflor convencional ")
						prod2 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "br spr" :
						print("vamos a actualizar la tabla con Col de Bruselas ")
						prod3 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "Sugar Snap Peas" :
						print("vamos a actualizar la tabla con Sugar S P")
						prod4 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')

					elif nombre_columna == "Yellow Sq" :
						print("vamos a actualizar la tabla con Yellow Sq")
						prod5 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')					

					elif nombre_columna == "Green Zucch" :
						print("vamos a actualizar la tabla con Green Zucch")
						prod6 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')					

					elif nombre_columna == "Brocc Org" :
						print("vamos a actualizar la tabla con Green Brocc Org")
						prod7 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')					

					elif nombre_columna == "Caulif Org" :
						print("vamos a actualizar la tabla con Green Caulif Org")
						prod8 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')	

					elif nombre_columna == "Carrots Org" :
						print("vamos a actualizar la tabla con Green Carrots Org")
						prod9 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')										

					elif nombre_columna == "Corn Org" :
						print("vamos a actualizar la tabla con Green Corn Org")
						prod10 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')										

					elif nombre_columna == "Edamame Org" :
						print("vamos a actualizar la tabla con Edamame Org")
						prod11 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11]
						print()
						print("listado actualizado")
						print(datos)
						datos.index = range(datos.shape[0])
						datos.to_csv('mbusasales.csv', encoding = 'utf-8')										

					else :
						pass
				
	def Eliminar(self):
		datos = pd.read_csv('mbusasales.csv', index_col = 0)
		QMessageBox.information(self,"Mensaje","Se eliminará el renglón seleccionado", QMessageBox.Discard) 

		datos = pd.read_csv('mbusasales.csv', index_col = 0, encoding = 'utf-8')
		datos.apply(lambda x: pd.lib.infer_dtype(x.values))
		column = self.table.currentColumn()-1
		row = self.table.currentRow()
		id = self.table.item(row, 0).text()
		id =int(id)
		id_datos = self.table.item(row, 1).text()
		year = self.table.item(row,2).text()
		month = self.table.item(row,3).text()
		prod1 = self.table.item(row,4).text()
		prod2 = self.table.item(row,5).text()
		prod3 = self.table.item(row,6).text()
		prod4 = self.table.item(row,7).text()
		prod5 = self.table.item(row,8).text()
		prod6 = self.table.item(row,9).text()
		prod7 = self.table.item(row,10).text()
		prod8 = self.table.item(row,11).text()
		prod9 = self.table.item(row,12).text()
		prod10 = self.table.item(row,13).text()
		prod11 = self.table.item(row,14).text()
		print("el id a eliminar  es",id)
		datos = datos.drop(datos.index[[id]])
		datos.index = range(datos.shape[0])
		print(datos)
		datos.to_csv('mbusasales.csv', encoding = 'utf-8')
		self.close()
		return

if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialogo = Dialogo()
	dialogo.show()
	app.exec_()
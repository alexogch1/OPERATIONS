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
		self.setWindowTitle("Domestic Purchases") #Título
		self.resize(2000, 450) #Tamaño inicial
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
		self.table.setColumnCount(14)
		self.table.setHorizontalHeaderLabels(['ID', 'indice', 'year', 'month', 'Diced Red Pper',
											 'Strips Red Pper', 'Corn Kernels', 'Organic Broccoli Florets', 'none',
         										'none', 'none', 'none', 'none', 'none'])
		
		domesticPurchases = pd.read_csv('domesticPurchases.csv', index_col = 0, encoding = 'utf-8')
		domesticPurchases.apply(lambda x: pd.lib.infer_dtype(x.values))
		domesticPurchases.index = range(domesticPurchases.shape[0])
		num_datos = int(domesticPurchases['year'].count())
		print(type(num_datos))
		print(domesticPurchases.index)
		row = 0 
		print("se cumple condicion while", row <= num_datos, "renglon","numero de datos", num_datos, "renglon", row)
		while row < num_datos:
			self.table.insertRow(row)
			id1 = domesticPurchases.index[row]
			print(id1)
			id = QTableWidgetItem(str(id1))
			self.table.setItem(row, 0, id)
			indice1 = domesticPurchases['indice'][row]
			indice = QTableWidgetItem(str(indice1))
			self.table.setItem(row, 1, indice)
			year1 = domesticPurchases['year'][row]
			year = QTableWidgetItem(str(year1))
			self.table.setItem(row, 2, year)
			month1 = domesticPurchases['month'][row]
			month = QTableWidgetItem(str(month1))
			self.table.setItem(row, 3,month)
			prod01 = domesticPurchases['Diced Red Pper'][row]
			prod0 = QTableWidgetItem(str(prod01))
			self.table.setItem(row, 4,prod0)
			prod11 = domesticPurchases['Strips Red Pper'][row]
			prod1 = QTableWidgetItem(str(prod11))
			self.table.setItem(row, 5,prod1)
			prod21 = domesticPurchases['Corn Kernels'][row]
			prod2=QTableWidgetItem(str(prod21))
			self.table.setItem(row, 6,prod2)
			prod31 = domesticPurchases['Organic Broccoli Florets'][row]
			prod3=QTableWidgetItem(str(prod31))
			self.table.setItem(row,7,prod3)
			prod41 = domesticPurchases['prod5'][row]
			prod4 = QTableWidgetItem(str(prod41))
			self.table.setItem(row,8,prod4)
			prod51 = domesticPurchases['prod6'][row]
			prod5 = QTableWidgetItem(str(prod51))
			self.table.setItem(row,9,prod5)
			prod61= domesticPurchases['prod7'][row]
			prod6 = QTableWidgetItem(str(prod61))
			self.table.setItem(row,10,prod6)
			prod71 = domesticPurchases['prod8'][row]
			prod7 = QTableWidgetItem(str(prod71))
			self.table.setItem(row,11,prod7)
			prod81 = domesticPurchases['prod9'][row]
			prod8 = QTableWidgetItem(str(prod81))
			self.table.setItem(row,12,prod8)
			prod91= domesticPurchases['prod10'][row]
			prod9 = QTableWidgetItem(str(prod91))
			self.table.setItem(row,13,prod9)
			row +=1



	def Actualizar(self):
					print("modulo actualizar")
					datos = pd.read_csv('domesticPurchases.csv', index_col = 0, encoding = 'utf-8')
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
						prod7, prod8, prod9]
				
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
					
					elif nombre_columna == "year" :
						print("vamos a actualizar la tabla con el año ")
						year = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
						
					
					elif nombre_columna == "month" :
						print("vamos a actualizar la tabla con el mes ")
						month = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Diced Red Pper" :
						print("vamos a actualizar la tabla con Diced Red Pper")
						prod0 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Strips Red Pper" :
						print("vamos a actualizar la tabla con el bStrips Red Pper ")
						prod1 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Corn Kernels" :
						print("vamos a actualizar la tabla con el Corn Kernels")
						prod2 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "COrganic Broccoli Florets" :
						print("vamos a actualizar la tabla con COrganic Broccoli Florets ")
						prod3 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod5" :
						print("vamos a actualizar la tabla con prod5")
						prod4 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod6" :
						print("vamos a actualizar la tabla con prod6")
						prod5 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod7" :
						print("vamos a actualizar la tabla con prod7")
						prod6 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod8" :
						print("vamos a actualizar la tabla con prod8")
						prod7 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod8, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod9" :
						print("vamos a actualizar la tabla con prod9")
						prod8 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod8, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod10" :
						print("vamos a actualizar la tabla con prod10")
						prod9 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod8, 
						prod7, prod8, prod9]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					else :
						pass
	def caja_mensaje (self, text, title, style):
		import caja_mensaje as mensaje
		mensaje.Caja_mensaje.mbox(text, title, style) 
		return 

	def guarda_archivo(self,datos):
		datos.index = range(datos.shape[0])
		try: 
			datos.to_csv('domesticPurchases.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
				
	def Eliminar(self):
		datos = pd.read_csv('domesticPurchases.csv', index_col = 0)
		QMessageBox.information(self,"Mensaje","Se eliminará el renglón seleccionado", QMessageBox.Discard) 

		datos = pd.read_csv('domesticPurchases.csv', index_col = 0, encoding = 'utf-8')
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
		print("el id a eliminar  es",id)
		datos = datos.drop(datos.index[[id]])
		datos.index = range(datos.shape[0])
		print(datos)
		self.guarda_archivo(datos)
		self.close()
		return

if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialogo = Dialogo()
	dialogo.show()
	app.exec_()
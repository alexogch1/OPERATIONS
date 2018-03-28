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
		self.setWindowTitle("DOMESTIC Sales") #Título
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
		self.table.setColumnCount(25)
		self.table.setHorizontalHeaderLabels(['ID', 'indice', 'year', 'month', 'broc_Conv',
			'brocc_Org', 'cauliflower', 'Caulif_Org', 'Sugar Snap Peas', 'Carrot Diced', 'Carrot Crinkl', 'Green Z', 
			'Peas', 'Poblano', 'Whole Corn', 'Total Corn', 'Green Beans', 'Mushrooms', 'Onion',
			'Potatoes', 'Red Pepper', 'Snow Peas', 'Spinach', 'Water Chest N.', 'Others'])
		
		domesticsales = pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8')
		domesticsales.apply(lambda x: pd.lib.infer_dtype(x.values))
		domesticsales.index = range(domesticsales.shape[0])
		num_datos = int(domesticsales['year'].count())
		print(type(num_datos))
		print(domesticsales.index)
		row = 0 
		print("se cumple condicion while", row <= num_datos, "renglon","numero de datos", num_datos, "renglon", row)
		while row < num_datos:
			self.table.insertRow(row)
			id1 = domesticsales.index[row]
			print(id1)
			id = QTableWidgetItem(str(id1))
			self.table.setItem(row, 0, id)
			indice1 = domesticsales['indice'][row]
			indice = QTableWidgetItem(str(indice1))
			self.table.setItem(row, 1, indice)
			year1 = domesticsales['year'][row]
			year = QTableWidgetItem(str(year1))
			self.table.setItem(row, 2, year)
			month1 = domesticsales['month'][row]
			month = QTableWidgetItem(str(month1))
			self.table.setItem(row, 3,month)
		

			prod01 = domesticsales['broc_Conv'][row]
			prod0 = QTableWidgetItem(str(prod01))
			self.table.setItem(row, 4,prod0)
			prod11 = domesticsales['brocc_Org'][row]
			prod1 = QTableWidgetItem(str(prod11))
			self.table.setItem(row, 5,prod1)
			prod21 = domesticsales['cauliflower'][row]
			prod2=QTableWidgetItem(str(prod21))
			self.table.setItem(row, 6,prod2)
			prod31 = domesticsales['Caulif_Org'][row]
			prod3=QTableWidgetItem(str(prod31))
			self.table.setItem(row,7,prod3)
			prod41 = domesticsales['Crinkle_Carrot'][row]
			prod4 = QTableWidgetItem(str(prod41))
			self.table.setItem(row,8,prod4)
			prod51 = domesticsales['Dcd_Carrot'][row]
			prod5 = QTableWidgetItem(str(prod51))
			self.table.setItem(row,9,prod5)
			prod61= domesticsales['Org_Carrot'][row]
			prod6 = QTableWidgetItem(str(prod61))
			self.table.setItem(row,10,prod6)
			prod71 = domesticsales['GZucc'][row]
			prod7 = QTableWidgetItem(str(prod71))
			self.table.setItem(row,11,prod7)
			prod81 = domesticsales['Peas'][row]
			prod8 = QTableWidgetItem(str(prod81))
			self.table.setItem(row,12,prod8)
			prod91= domesticsales['Poblano'][row]
			prod9 = QTableWidgetItem(str(prod91))
			self.table.setItem(row,13,prod9)
			prod101= domesticsales['WCorn'][row]
			prod10 = QTableWidgetItem(str(prod101))
			self.table.setItem(row,14,prod10)
			prod111= domesticsales['Total_Corn'][row]
			prod11 = QTableWidgetItem(str(prod111))
			self.table.setItem(row,15,prod11)
			prod121= domesticsales['GreenBeans'][row]
			prod12 = QTableWidgetItem(str(prod121))
			self.table.setItem(row,16,prod12)
			prod131= domesticsales['Mushrooms'][row]
			prod13 = QTableWidgetItem(str(prod131))
			self.table.setItem(row,17,prod13)
			prod141= domesticsales['Onion'][row]
			prod14 = QTableWidgetItem(str(prod141))
			self.table.setItem(row,18,prod14)
			prod151= domesticsales['Potatoes'][row]
			prod15 = QTableWidgetItem(str(prod151))
			self.table.setItem(row,19,prod15)

			prod161= domesticsales['RedPepper'][row]
			prod16 = QTableWidgetItem(str(prod161))
			self.table.setItem(row,20,prod16)

			prod171= domesticsales['snowPeas'][row]
			prod17 = QTableWidgetItem(str(prod171))
			self.table.setItem(row,21,prod17)

			prod181= domesticsales['Spinach'][row]
			prod18 = QTableWidgetItem(str(prod181))
			self.table.setItem(row,22,prod18)

			prod191= domesticsales['WCN'][row]
			prod19 = QTableWidgetItem(str(prod191))
			self.table.setItem(row,23,prod19)

			prod201= domesticsales['Others'][row]
			prod20 = QTableWidgetItem(str(prod201))
			self.table.setItem(row,24,prod20)
			row +=1



	def Actualizar(self):
					print("modulo actualizar")
					datos = pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8')
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
					prod12 = self.table.item(row,16).text()
					prod13 = self.table.item(row,17).text()
					prod14 = self.table.item(row,18).text()
					prod15 = self.table.item(row,19).text()
					prod16 = self.table.item(row,20).text()
					prod17 = self.table.item(row,21).text()
					prod18 = self.table.item(row,22).text()
					prod19 = self.table.item(row,23).text()
					prod20 = self.table.item(row,24).text()

	
					
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
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
				
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
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						
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
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "broc_Conv" :
						print("vamos a actualizar la tabla con broc_Conv ")
						prod0 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "brocc_Org" :
						print("vamos a actualizar la tabla con el brocc_Org ")
						prod1 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "cauliflower" :
						print("vamos a actualizar la tabla con el cauliflower")
						prod2 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Caulif_Org" :
						print("vamos a actualizar la tabla con Caulif_Org ")
						prod3 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Crinkle_Carrot" :
						print("vamos a actualizar la tabla con Crinkle_Carrot")
						prod4 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Dcd_Carrot" :
						print("vamos a actualizar la tabla con Dcd_Carrot")
						prod5 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Org_Carrot" :
						print("vamos a actualizar la tabla con Org_Carrot")
						prod6 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "GZucc" :
						print("vamos a actualizar la tabla con Green GZucc")
						prod7 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Peas" :
						print("vamos a actualizar la tabla con Peas")
						prod8 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Poblano" :
						print("vamos a actualizar la tabla con Green Poblano")
						prod9 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "WCorn" :
						print("vamos a actualizar la tabla con Green WCorn")
						prod10 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Total_Corn" :
						print("vamos a actualizar la tabla con Total_Corn")
						prod11 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "GreenBeans" :
						print("vamos a actualizar la tabla con GreenBeans")
						prod12 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Mushrooms" :
						print("vamos a actualizar la tabla con Mushrooms")
						prod13 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Onion" :
						print("vamos a actualizar la tabla con Onion")
						prod14 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Potatoes" :
						print("vamos a actualizar la tabla con Potatoes")
						prod15 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "RedPepper" :
						print("vamos a actualizar la tabla con RedPepper")
						prod16 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "snowPeas" :
						print("vamos a actualizar la tabla con snowPeas")
						prod17 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Spinach" :
						print("vamos a actualizar la tabla con Spinach")
						prod18 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "WCN" :
						print("vamos a actualizar la tabla con WCN")
						prod19 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "Other" :
						print("vamos a actualizar la tabla con Others")
						prod20 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, prod5, prod6, 
						prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15, prod16,
						prod17, prod18, prod19, prod20]
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
			datos.to_csv('domesticsales.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
				
	def Eliminar(self):
		datos = pd.read_csv('domesticsales.csv', index_col = 0)
		QMessageBox.information(self,"Mensaje","Se eliminará el renglón seleccionado", QMessageBox.Discard) 

		datos = pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8')
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
		self.guarda_archivo(datos)
		self.close()
		return

if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialogo = Dialogo()
	dialogo.show()
	app.exec_()
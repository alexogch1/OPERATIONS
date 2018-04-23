#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In thismodule it is input the data of Broccoli Inventories
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
		self.setWindowTitle("Inventories Broccoli") #Título
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
		self.table.setColumnCount(38)
		self.table.setHorizontalHeaderLabels(['ID', 'indice', 'year', 'month', 
												'F Spears','F Flrts Conv', 'F Crowns' ,'F Flrts Org', 'F Stalks Conv', 
							'F Stalks Org', 'F Chopped', 'F Sori Pearls', 'F Cuts', 'F Cuts Org',
							'prod11', 'prod12', 'prod13', 'prod14','prod15', 
							 'prod16', 'prod17','prod18', 'P Spears', 'P Florets',
							 'P Crowns', 'P Flrts Org', 'P Stalks Conv', 'P Stalks Org', 'P Chopped',
							 'P Sori Pearls', 'P Cuts Conv', 'P Cuts Org', 'prod29', 'prod30',
							 'prod31', 'prod32', 'prod33', 'prod34'])
		
		datos = pd.read_csv('inventoriesbroccoli.csv', index_col = 0, encoding = 'utf-8')
		datos.apply(lambda x: pd.lib.infer_dtype(x.values))
		datos.index = range(datos.shape[0])
		num_datos = int(datos['year'].count())
		print(type(num_datos))
		print(datos.index)
		row = 0 
		print("se cumple condicion while", row <= num_datos, "renglon","numero de datos", num_datos, "renglon", row)
		while row < num_datos:
			self.table.insertRow(row)
			id1 = datos.index[row]
			print(id1)
			id = QTableWidgetItem(str(id1))
			self.table.setItem(row, 0, id)
			indice1 = datos['indice'][row]
			indice = QTableWidgetItem(str(indice1))
			self.table.setItem(row, 1, indice)
			year1 = datos['year'][row]
			year = QTableWidgetItem(str(year1))
			self.table.setItem(row, 2, year)
			month1 = datos['month'][row]
			month = QTableWidgetItem(str(month1))
			self.table.setItem(row, 3,month)
			prod01 = datos['F Spears'][row]
			prod0 = QTableWidgetItem(str(prod01))
			self.table.setItem(row, 4,prod0)
			prod11 = datos['F Flrts Conv'][row]
			prod1 = QTableWidgetItem(str(prod11))
			self.table.setItem(row, 5,prod1)
			prod21 = datos['F Crowns'][row]
			prod2=QTableWidgetItem(str(prod21))
			self.table.setItem(row, 6,prod2)
			prod31 = datos['F Flrts Org'][row]
			prod3=QTableWidgetItem(str(prod31))
			self.table.setItem(row,7,prod3)
			prod41 = datos['F Stalks Conv'][row]
			prod4 = QTableWidgetItem(str(prod41))
			self.table.setItem(row,8,prod4)
			prod51 = datos['F Stalks Org'][row]
			prod5 = QTableWidgetItem(str(prod51))
			self.table.setItem(row,9,prod5)
			prod61= datos['F Chopped'][row]
			prod6 = QTableWidgetItem(str(prod61))
			self.table.setItem(row,10,prod6)
			prod71 = datos['F Sori Pearls'][row]
			prod7 = QTableWidgetItem(str(prod71))
			self.table.setItem(row,11,prod7)
			prod81 = datos['F Cuts'][row]
			prod8 = QTableWidgetItem(str(prod81))
			self.table.setItem(row,12,prod8)
			prod91= datos['F Cuts Org'][row]
			prod9 = QTableWidgetItem(str(prod91))
			self.table.setItem(row,13,prod9)
			prod101 = datos['prod11'][row]
			prod10 = QTableWidgetItem(str(prod101))
			self.table.setItem(row, 14,prod10)
			prod111 = datos['prod12'][row]
			prod11 = QTableWidgetItem(str(prod111))
			self.table.setItem(row, 15,prod11)
			prod121 = datos['prod13'][row]
			prod12=QTableWidgetItem(str(prod121))
			self.table.setItem(row, 16,prod12)
			prod131 = datos['prod14'][row]
			prod13=QTableWidgetItem(str(prod131))
			self.table.setItem(row,17,prod13)
			
			prod141 = datos['prod15'][row]
			prod14 = QTableWidgetItem(str(prod141))
			self.table.setItem(row,18,prod14)
			prod151 = datos['prod16'][row]
			prod15 = QTableWidgetItem(str(prod151))
			self.table.setItem(row,19,prod15)
			prod161= datos['prod17'][row]
			prod16 = QTableWidgetItem(str(prod161))
			self.table.setItem(row,20,prod16)
			prod171 = datos['prod18'][row]
			prod17 = QTableWidgetItem(str(prod171))
			self.table.setItem(row,21,prod17)
			prod181 = datos['P Spears'][row]
			prod18 = QTableWidgetItem(str(prod181))
			self.table.setItem(row,22,prod18)
			prod191= datos['P Florets'][row]
			prod19 = QTableWidgetItem(str(prod191))
			self.table.setItem(row,23,prod19)
			prod201 = datos['P Crowns'][row]
			prod20 = QTableWidgetItem(str(prod201))
			self.table.setItem(row, 24,prod20)
			prod211 = datos['P Flrts Org'][row]
			prod21 = QTableWidgetItem(str(prod211))
			self.table.setItem(row, 25,prod21)
			prod221 = datos['P Stalks Conv'][row]
			prod22=QTableWidgetItem(str(prod221))
			self.table.setItem(row, 26,prod22)
			prod231 = datos['P Stalks Org'][row]
			prod23=QTableWidgetItem(str(prod231))
			self.table.setItem(row,27,prod23)
			prod241 = datos['P Chopped'][row]
			prod24 = QTableWidgetItem(str(prod241))
			self.table.setItem(row,28,prod24)
			prod251 = datos['P Sori Pearls'][row]
			prod25 = QTableWidgetItem(str(prod251))
			self.table.setItem(row,29,prod25)
			prod261= datos['P Cuts Conv'][row]
			prod26 = QTableWidgetItem(str(prod261))
			self.table.setItem(row,30,prod26)
			prod271 = datos['P Cuts Org'][row]
			prod27 = QTableWidgetItem(str(prod271))
			self.table.setItem(row,31,prod27)
			prod281 = datos['prod29'][row]
			prod28 = QTableWidgetItem(str(prod281))
			self.table.setItem(row,32,prod28)
			prod291= datos['prod30'][row]
			prod29 = QTableWidgetItem(str(prod291))
			self.table.setItem(row,33,prod29)
			prod301 = datos['prod31'][row]
			prod30 = QTableWidgetItem(str(prod301))
			self.table.setItem(row, 34,prod30)
			prod311 = datos['prod32'][row]
			prod31 = QTableWidgetItem(str(prod311))
			self.table.setItem(row, 35,prod31)
			prod321 = datos['prod33'][row]
			prod32=QTableWidgetItem(str(prod321))
			self.table.setItem(row, 36,prod32)
			prod331 = datos['prod34'][row]
			prod33=QTableWidgetItem(str(prod331))
			self.table.setItem(row,37,prod33)
			
			row +=1



	def Actualizar(self):
					print("modulo actualizar")
					datos = pd.read_csv('inventoriesbroccoli.csv', index_col = 0, encoding = 'utf-8')
					datos.apply(lambda x: pd.lib.infer_dtype(x.values))
					column = self.table.currentColumn()-1
					row = self.table.currentRow()
					id = self.table.item(row, 0).text()# id
					id =int(id)
					id_datos = self.table.item(row, 1).text() #indice
					year = self.table.item(row,2).text()#month
					month = self.table.item(row,3).text()#year
					prod0 = self.table.item(row,4).text()# producto 1
					prod1 = self.table.item(row,5).text()# producto 2
					prod2 = self.table.item(row,6).text()# producto 3
					prod3 = self.table.item(row,7).text()# producto 4
					prod4 = self.table.item(row,8).text()# producto 5
					prod5 = self.table.item(row,9).text()# producto 6
					prod6 = self.table.item(row,10).text()# producto 7
					prod7 = self.table.item(row,11).text()# producto 8
					prod8 = self.table.item(row,12).text()# producto 9
					prod9 = self.table.item(row,13).text()# producto 10
					prod10 = self.table.item(row,14).text()# producto 11
					prod11 = self.table.item(row,15).text()# producto 12
					prod12 = self.table.item(row,16).text()# producto 13
					prod13 = self.table.item(row,17).text()# producto 14
					
					prod14 = self.table.item(row,18).text()
					
					prod15 = self.table.item(row,19).text()
					prod16 = self.table.item(row,20).text()
					prod17 = self.table.item(row,21).text()
					prod18 = self.table.item(row,22).text()
					prod19 = self.table.item(row,23).text()
					prod20 = self.table.item(row,24).text()
					prod21 = self.table.item(row,25).text()
					prod22 = self.table.item(row,26).text()
					prod23 = self.table.item(row,27).text()
					prod24 = self.table.item(row,28).text()
					prod25 = self.table.item(row,29).text()
					prod26 = self.table.item(row,30).text()
					prod27 = self.table.item(row,31).text()
					prod28 = self.table.item(row,32).text()
					prod29 = self.table.item(row,33).text()
					prod30 = self.table.item(row,34).text()
					prod31 = self.table.item(row,35).text()
					prod32 = self.table.item(row,36).text()
					prod33 = self.table.item(row,37).text()
					
						
					
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
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
				
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
					
					elif nombre_columna == "year" :
						print("vamos a actualizar la tabla con el año ")
						year = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
						
					
					elif nombre_columna == "month" :
						print("vamos a actualizar la tabla con el mes ")
						month = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Spears" :
						print("vamos a actualizar la tabla con BRUSSEL SPR")
						prod0 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Flrts Conv" :
						print("vamos a actualizar la tabla con el CRKLE CARR CONV ")
						prod1 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Crowns" :
						print("vamos a actualizar la tabla con el BABY ORG CARR")
						prod2 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Flrts Org" :
						print("vamos a actualizar la tabla con COrganic YLLW ORG CARR ")
						prod3 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						self.guarda_archivo(datos)

					elif nombre_columna == "F Stalks Conv" :
						print("vamos a actualizar la tabla con YLLW BIAS CARR")
						prod4 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Stalks Org" :
						print("vamos a actualizar la tabla con GRN BEANS")
						prod5 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Chopped" :
						print("vamos a actualizar la tabla con SLAB GR BEANS")
						prod6 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Sori Pearls" :
						print("vamos a actualizar la tabla con SUGAR SNAP P")
						prod7 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Cuts" :
						print("vamos a actualizar la tabla con BROC FLTS")
						prod8 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "F Cuts Org" :
						print("vamos a actualizar la tabla con ORG JUL. CARR")
						prod9 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
						

					elif nombre_columna == "prod11" :
						print("vamos a actualizar la tabla con STRPS GR PEPPER")
						prod10 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod12" :
						print("vamos a actualizar la tabla con el CELERY ")
						prod11 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod13" :
						print("vamos a actualizar la tabla con el BABY ORG ONION")
						prod12 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod14" :
						print("vamos a actualizar la tabla con MUSHROOM ")
						prod13 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24,
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33]
						print(datos)
						self.guarda_archivo(datos)
					
					elif nombre_columna == "prod15" :
						print("vamos a actualizar la tabla con WATER CH NUTS")
						prod14 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod16" :
						print("vamos a actualizar la tabla con CORN WHOLE")
						prod15 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod17" :
						print("vamos a actualizar la tabla con CORN KERNELS")
						prod16 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod18" :
						print("vamos a actualizar la tabla con GARBANZO")
						prod17 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Spears" :
						print("vamos a actualizar la tabla con GREEN PEPPER")
						prod18 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Florets" :
						print("vamos a actualizar la tabla con KIDNEY BEANS")
						prod19 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
					elif nombre_columna == "P Crowns" :
						print("vamos a actualizar la tabla con NAVY BEANS")
						prod20 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Flrts Org" :
						print("vamos a actualizar la tabla con el RED PEPPER ")
						prod21 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Stalks Conv" :
						print("vamos a actualizar la tabla con el GREEN PEAS")
						prod22 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Stalks Org" :
						print("vamos a actualizar la tabla con COrganic ITALIAN GR BEANS ")
						prod23 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Chopped" :
						print("vamos a actualizar la tabla con DCED POTATOES")
						prod24 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Sori Pearls" :
						print("vamos a actualizar la tabla con LIMA BEANS")
						prod25 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Cuts Conv" :
						print("vamos a actualizar la tabla con CUT GR BEANS")
						prod26 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "P Cuts Org" :
						print("vamos a actualizar la tabla con BROC CUTS")
						prod27 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod29" :
						print("vamos a actualizar la tabla con SNOW PEAS")
						prod28 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod30" :
						print("vamos a actualizar la tabla con PARIS CARR")
						prod29 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)
						

					elif nombre_columna == "prod31" :
						print("vamos a actualizar la tabla con prod31")
						prod30 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod32" :
						print("vamos a actualizar la tabla con prod32")
						prod31 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod33" :
						print("vamos a actualizar la tabla con prod33")
						prod32 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
						print()
						print("listado actualizado")
						print(datos)
						self.guarda_archivo(datos)

					elif nombre_columna == "prod34" :
						print("vamos a actualizar la tabla con prod34")
						prod33 = value
						print(year)
						datos.loc[id] = [ id_datos, year,  month,
						prod0, prod1, prod2, prod3, prod4, 
						prod5, prod6, prod7, prod8, prod9, 
						prod10, prod11, prod12, prod13, prod14,
						prod15, prod16, prod17, prod18, prod19,
						prod20, prod21, prod22, prod23, prod24, 
						prod25, prod26, prod27, prod28, prod29,
						prod30, prod31, prod32, prod33 ]
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
			datos.to_csv('inventoriesbroccoli.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
				
	def Eliminar(self):
		datos = pd.read_csv('inventoriesbroccoli.csv', index_col = 0)
		QMessageBox.information(self,"Mensaje","Se eliminará el renglón seleccionado", QMessageBox.Discard) 

		datos = pd.read_csv('inventoriesbroccoli.csv', index_col = 0, encoding = 'utf-8')
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
		prod12 = self.table.item(row,15).text()
		prod13 = self.table.item(row,16).text()
		prod14 = self.table.item(row,17).text()
		prod15 = self.table.item(row,18).text()
		prod16 = self.table.item(row,19).text()
		prod26 = self.table.item(row,29).text()
		prod27 = self.table.item(row,30).text()
		prod28 = self.table.item(row,31).text()
		prod29 = self.table.item(row,32).text()
		prod30 = self.table.item(row,33).text()
		prod31 = self.table.item(row,34).text()
		prod32 = self.table.item(row,35).text()
		prod33 = self.table.item(row,36).text()
		prod34 = self.table.item(row,37).text()
		
		
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
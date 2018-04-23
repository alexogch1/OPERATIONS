#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In thismodule it is input the data of Sales ESA
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
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem
from PyQt5 import uic
import datetime
import pandas as pd
import numpy as np
import cajaMensajePregunta as cajaMensaje

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("general_format_several_products.ui")[0]

class MyWindowClass(QtWidgets.QDialog, form_class):
	def __init__(self, parent=None):
		
		QtWidgets.QDialog.__init__(self, parent)
		list_ingredients = ['Br. Flrts 1 - 2 1/8','Br Stalks','Br Pearls' ,'Col. Flrts 1 - 2 1/8', 'Col. Flrts 3/4 - 1 3/8', 
							'Col Nuggets', 'Yellow Squash', 'Green Zucchini', 'prod9', 'prod10',
							'prod11', 'prod12', 'prod13', 'prod14','prod15', 
							 'prod16', 'prod17','prod18', 'prod19', 'prod20',
							 'prod21', 'prod22', 'prod23', 'prod24', 'prod25',
							 'prod26', 'prod27', 'prod28', 'prod29', 'prod30',
							 'prod31', 'prod32', 'prod33', 'prod34']
		 
        #14 INGREDIENTS LISTED
        
		self.setupUi(self)
		self.pBtnSave.setEnabled(False)
		self.pBtnSave.setVisible(False)
		self.Title.setText(str('ESA Sales'))
		self.lblTotalAnual.setText(str('ESA SALES'))

		titles = self.set_titles(list_ingredients)
		self.pBtnSelectYear.setEnabled(True)
		self.pBtnUpdate.setEnabled(False)
		self.table = 'esasales'
		self.lock_fields()
		
		
		self.pBtnReport.clicked.connect(self.save_data)

		# Signal when the button SelectYear is Clicked				
		self.pBtnSelectYear.clicked.connect(self.widget_year)

		# Signal when the button Update is clicked
		self.pBtnUpdate.clicked.connect(self.update_totals)

		# Signal when the button close Window is clicked
		self.pbtnClose.clicked.connect(self.close_window)		
	
	
	def widget_year(self):
		"""
		In this function we open de Widget to capture the Year
		and prints the value in the corresponding label
		"""
		import wid_year
		self.selected_year = wid_year.App.getDate(self)
		self.lbl_year_selected.setText(str(self.selected_year))
		self.pBtnSelectYear.setEnabled(False)
		self.years(self.selected_year)
		
	def years(self, selected_year):
		"""
		This function is used to compare the 
		selected year Vs the current Year.
		if the selected year is > than the actual year, 
		displays a message error and
		close the window
		"""

		# Get the current year 
		self.current_year = self.actual_Year()
		
		""" 
		Call the function selected_year to get 
		the year from the field
		"""
		self.selected_year = selected_year
		

		if self.selected_year > self.current_year:
			message = ' Sorry, It is not possible to Work with future years, '+ str(self.selected_year)
			self.caja_mensaje('Message ', message,0)
		else :
			#self.search_In_File(self.selected_year)
			#self.inicializar_campós() # Set al fields as Zero
			self.read_data_from_file(self.selected_year)

	def read_data_from_file(self, year):	
			message = ' reading, Data from file '
			self.caja_mensaje('Message ', message,0)	
			self.list_keys = self.issue_keys()
			datos = pd.read_csv('esasales.csv', index_col = 0, encoding = 'utf-8' )
			datos.apply(lambda x: pd.lib.infer_dtype(x.values))
			print(year)
			print('los datos son: \n',datos)
			datos = datos.loc [datos['year'] == year]
			datos.index = range(datos.shape[0])
	
			dict_prod = {'Br. Flrts 1 - 2 1/8': list(datos['Br. Flrts 1 - 2 1/8'])}
			dict_prod2 = {'Br Stalks': list(datos['Br Stalks'])}
			dict_prod3 = {'Br Pearls': list(datos['Br Pearls'])}
			dict_prod4 = {'Col. Flrts 1 - 2 1/8': list(datos['Col. Flrts 1 - 2 1/8'])}
			dict_prod5 = {'Col. Flrts 3/4 - 1 3/8': list(datos['Col. Flrts 3/4 - 1 3/8'])}
			dict_prod6 = {'Col Nuggets': list(datos['Col Nuggets'])}
			dict_prod7 = {'Yellow Squash': list(datos['Yellow Squash'])}
			dict_prod8 = {'Green Zucchini': list(datos['Green Zucchini'])}
			dict_prod9 = {'prod9': list(datos['prod9'])}
			dict_prod10 = {'prod10': list(datos['prod10'])}
			dict_prod11 = {'prod11': list(datos['prod11'])}
			dict_prod12 = {'prod12': list(datos['prod12'])}
			dict_prod13 = {'prod13': list(datos['prod13'])}
			dict_prod14 = {'prod14': list(datos['prod14'])}
			dict_prod15 = {'prod15': list(datos['prod15'])}
			dict_prod16 = {'prod16': list(datos['prod16'])}
			dict_prod17 = {'prod17': list(datos['prod17'])}
			dict_prod18 = {'prod18': list(datos['prod18'])}
			dict_prod19 = {'prod19': list(datos['prod19'])}
			dict_prod20 = {'prod20': list(datos['prod20'])}
			dict_prod21 = {'prod21': list(datos['prod21'])}
			dict_prod22 = {'prod22': list(datos['prod22'])}
			dict_prod23 = {'prod23': list(datos['prod23'])}
			dict_prod24 = {'prod24': list(datos['prod24'])}
			dict_prod25 = {'prod25': list(datos['prod25'])}
			dict_prod26 = {'prod26': list(datos['prod26'])}
			dict_prod27 = {'prod27': list(datos['prod27'])}
			dict_prod28 = {'prod28': list(datos['prod28'])}
			dict_prod29 = {'prod29': list(datos['prod29'])}
			dict_prod30 = {'prod30': list(datos['prod30'])}
			dict_prod31 = {'prod31': list(datos['prod31'])}
			dict_prod32 = {'prod32': list(datos['prod32'])}
			dict_prod33 = {'prod33': list(datos['prod33'])}
			dict_prod34 = {'prod34': list(datos['prod34'])}
			

			Dict_Final = {}
			Dict_Final['Br. Flrts 1 - 2 1/8'] = list(datos['Br. Flrts 1 - 2 1/8'])
			Dict_Final['Br Stalks'] = list(datos['Br Stalks'])
			Dict_Final['Br Pearls'] = list(datos['Br Pearls'])
			Dict_Final['Col. Flrts 1 - 2 1/8'] = list(datos['Col. Flrts 1 - 2 1/8'])
			Dict_Final['Col. Flrts 3/4 - 1 3/8'] = list(datos['Col. Flrts 3/4 - 1 3/8'])
			Dict_Final['Col Nuggets'] = list(datos['Col Nuggets'])
			Dict_Final['Yellow Squash'] = list(datos['Yellow Squash'])
			Dict_Final['Green Zucchini'] = list(datos['Green Zucchini'])
			Dict_Final['prod9'] = list(datos['prod9'])
			Dict_Final['prod10'] = list(datos['prod10'])
			Dict_Final['prod11'] = list(datos['prod11'])
			Dict_Final['prod12'] = list(datos['prod12'])
			Dict_Final['prod13'] = list(datos['prod13'])
			Dict_Final['prod14'] = list(datos['prod14'])
			Dict_Final['prod15'] = list(datos['prod15'])
			Dict_Final['prod16'] = list(datos['prod16'])
			Dict_Final['prod17'] = list(datos['prod17'])
			Dict_Final['prod18'] = list(datos['prod18'])
			Dict_Final['prod19'] = list(datos['prod19'])
			Dict_Final['prod20'] = list(datos['prod20'])
			Dict_Final['prod21'] = list(datos['prod21'])
			Dict_Final['prod22'] = list(datos['prod22'])
			Dict_Final['prod23'] = list(datos['prod23'])
			Dict_Final['prod24'] = list(datos['prod24'])
			Dict_Final['prod25'] = list(datos['prod25'])
			Dict_Final['prod26'] = list(datos['prod26'])
			Dict_Final['prod27'] = list(datos['prod27'])
			Dict_Final['prod28'] = list(datos['prod28'])
			Dict_Final['prod29'] = list(datos['prod29'])
			Dict_Final['prod30'] = list(datos['prod30'])
			Dict_Final['prod31'] = list(datos['prod31'])
			Dict_Final['prod32'] = list(datos['prod32'])
			Dict_Final['prod33'] = list(datos['prod33'])
			Dict_Final['prod34'] = list(datos['prod34'])
			

			self.inicializar_campós(Dict_Final)
		

	def actual_Year(self):
		"""
		Function to get the current year from the system
		"""
		now = datetime.datetime.now()
		act_year = now.year
		return act_year 
	
	def search_In_File(self, year):
		self.list_keys = self.issue_keys()
		datos = pd.read_csv('esasales.csv', index_col = 0, encoding = 'utf-8' )
		datos.apply(lambda x: pd.lib.infer_dtype(x.values))
		num_datos = int(datos['indice'].count())
		nuevo_Valor = num_datos+1
		datos.index = range(datos.shape[0])
		indice_archivo = list(datos.indice)
		counter_flag=0
		for i, valor in enumerate(self.list_keys):
			if valor in indice_archivo:
				counter_flag = counter_flag + 1
			else:
				counter_flag = counter_flag
		if counter_flag >1:
			message = "THE DATA IS ALREADY IN THE DATABASE"
			self.caja_mensaje('Error;', message,0)
			self.close()
		else:
			pass
		return

	def save_data(self):
		self.genera_archivo_csv(self.list_keys,self.selected_year)
		self.close()


	def update_totals(self):
		self.list_keys = self.issue_keys()
		self.read_data_from_fields()
		

		dict_prod = {}
		dict_prod['Br. Flrts 1 - 2 1/8'] = list([
			self.Jan_Prod, self.Feb_Prod, self.Mar_Prod, 
			self.Apr_Prod, self.May_Prod, self.Jun_Prod, 
			self.Jul_Prod, self.Aug_Prod, self.Sep_Prod, 
			self.Oct_Prod, self.Nov_Prod, self.Dec_Prod])
		values_prod = list(dict_prod.values())
		key_prod = list(dict_prod.keys())
		np_prod = np.array(values_prod)
		print(np_prod)
		acum_prod = np_prod.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod)
		self.lblTotalAnualProd.setText(str(acum_prod))
		
		dict_prod2 = {}
		dict_prod2['Br Stalks'] = list([
			self.Jan_Prod_2, self.Feb_Prod_2, self.Mar_Prod_2, 
			self.Apr_Prod_2, self.May_Prod_2, self.Jun_Prod_2, 
			self.Jul_Prod_2, self.Aug_Prod_2, self.Sep_Prod_2, 
			self.Oct_Prod_2, self.Nov_Prod_2, self.Dec_Prod_2])
		values_prod_2 = list(dict_prod2.values())
		key_prod_2 = list(dict_prod2.keys())
		np_prod_2 = np.array(values_prod_2)
		print(np_prod_2)
		acum_prod_2 = np_prod_2.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_2)
		self.lblTotalAnualProd_2.setText(str(acum_prod_2))

		dict_prod3 = {}
		dict_prod3['Br Pearls'] = list([
			self.Jan_Prod_3, self.Feb_Prod_3, self.Mar_Prod_3, 
			self.Apr_Prod_3, self.May_Prod_3, self.Jun_Prod_3, 
			self.Jul_Prod_3, self.Aug_Prod_3, self.Sep_Prod_3, 
			self.Oct_Prod_3, self.Nov_Prod_3, self.Dec_Prod_3])
		values_prod_3 = list(dict_prod3.values())
		key_prod_3 = list(dict_prod3.keys())
		np_prod_3 = np.array(values_prod_3)
		print(np_prod_3)
		acum_prod_3 = np_prod_3.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_3)
		self.lblTotalAnualProd_3.setText(str(acum_prod_3))

		dict_prod4 = {}
		dict_prod4['Col. Flrts 1 - 2 1/8'] = list([
			self.Jan_Prod_4, self.Feb_Prod_4, self.Mar_Prod_4, 
			self.Apr_Prod_4, self.May_Prod_4, self.Jun_Prod_4, 
			self.Jul_Prod_4, self.Aug_Prod_4, self.Sep_Prod_4, 
			self.Oct_Prod_4, self.Nov_Prod_4, self.Dec_Prod_4])
		values_prod_4 = list(dict_prod4.values())
		key_prod_4 = list(dict_prod4.keys())
		np_prod_4 = np.array(values_prod_4)
		print(np_prod_4)
		acum_prod_4 = np_prod_4.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_4)
		self.lblTotalAnualProd_4.setText(str(acum_prod_4))

		dict_prod5 = {}
		dict_prod5['Col. Flrts 3/4 - 1 3/8'] = list([
			self.Jan_Prod_5, self.Feb_Prod_5, self.Mar_Prod_5, 
			self.Apr_Prod_5, self.May_Prod_5, self.Jun_Prod_5, 
			self.Jul_Prod_5, self.Aug_Prod_5, self.Sep_Prod_5, 
			self.Oct_Prod_5, self.Nov_Prod_5, self.Dec_Prod_5])
		values_prod_5 = list(dict_prod5.values())
		key_prod_5 = list(dict_prod5.keys())
		np_prod_5 = np.array(values_prod_5)
		print(np_prod_5)
		acum_prod_5 = np_prod_5.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_5)
		self.lblTotalAnualProd_5.setText(str(acum_prod_5))

		dict_prod6 = {}
		dict_prod6['Col Nuggets'] = list([
			self.Jan_Prod_6, self.Feb_Prod_6, self.Mar_Prod_6, 
			self.Apr_Prod_6, self.May_Prod_6, self.Jun_Prod_6, 
			self.Jul_Prod_6, self.Aug_Prod_6, self.Sep_Prod_6, 
			self.Oct_Prod_6, self.Nov_Prod_6, self.Dec_Prod_6])
		values_prod_6 = list(dict_prod6.values())
		key_prod_6 = list(dict_prod6.keys())
		np_prod_6 = np.array(values_prod_6)
		print(np_prod_6)
		acum_prod_6 = np_prod_6.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_6)
		self.lblTotalAnualProd_6.setText(str(acum_prod_6))

		dict_prod7 = {}
		dict_prod7['Yellow Squash'] = list([
			self.Jan_Prod_7, self.Feb_Prod_7, self.Mar_Prod_7, 
			self.Apr_Prod_7, self.May_Prod_7, self.Jun_Prod_7, 
			self.Jul_Prod_7, self.Aug_Prod_7, self.Sep_Prod_7, 
			self.Oct_Prod_7, self.Nov_Prod_7, self.Dec_Prod_7])
		values_prod_7 = list(dict_prod7.values())
		key_prod_7 = list(dict_prod7.keys())
		np_prod_7 = np.array(values_prod_7)
		print(np_prod_7)
		acum_prod_7 = np_prod_7.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_7)
		self.lblTotalAnualProd_7.setText(str(acum_prod_7))

		dict_prod8 = {}
		dict_prod8['Green Zucchini'] = list([
			self.Jan_Prod_8, self.Feb_Prod_8, self.Mar_Prod_8, 
			self.Apr_Prod_8, self.May_Prod_8, self.Jun_Prod_8, 
			self.Jul_Prod_8, self.Aug_Prod_8, self.Sep_Prod_8, 
			self.Oct_Prod_8, self.Nov_Prod_8, self.Dec_Prod_8])
		values_prod_8 = list(dict_prod8.values())
		key_prod_8 = list(dict_prod8.keys())
		np_prod_8 = np.array(values_prod_8)
		print(np_prod_8)
		acum_prod_8 = np_prod_8.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_8)
		self.lblTotalAnualProd_8.setText(str(acum_prod_8))

		dict_prod9 = {}
		dict_prod9['prod9'] = list([
			self.Jan_Prod_9, self.Feb_Prod_9, self.Mar_Prod_9, 
			self.Apr_Prod_9, self.May_Prod_9, self.Jun_Prod_9, 
			self.Jul_Prod_9, self.Aug_Prod_9, self.Sep_Prod_9, 
			self.Oct_Prod_9, self.Nov_Prod_9, self.Dec_Prod_9])
		values_prod_9 = list(dict_prod9.values())
		key_prod_9 = list(dict_prod9.keys())
		np_prod_9 = np.array(values_prod_9)
		print(np_prod_9)
		acum_prod_9 = np_prod_9.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_9)
		self.lblTotalAnualProd_9.setText(str(acum_prod_9))

		dict_prod10 = {}
		dict_prod10['prod10'] = list([
			self.Jan_Prod_10, self.Feb_Prod_10, self.Mar_Prod_10, 
			self.Apr_Prod_10, self.May_Prod_10, self.Jun_Prod_10, 
			self.Jul_Prod_10, self.Aug_Prod_10, self.Sep_Prod_10, 
			self.Oct_Prod_10, self.Nov_Prod_10, self.Dec_Prod_10])
		values_prod_10 = list(dict_prod10.values())
		key_prod_10 = list(dict_prod10.keys())
		np_prod_10 = np.array(values_prod_10)
		print(np_prod_10)
		acum_prod_10 = np_prod_10.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_10)
		self.lblTotalAnualProd_10.setText(str(acum_prod_10))

		dict_prod11 = {}
		dict_prod11['prod11'] = list([
			self.Jan_Prod_11, self.Feb_Prod_11, self.Mar_Prod_11, 
			self.Apr_Prod_11, self.May_Prod_11, self.Jun_Prod_11, 
			self.Jul_Prod_11, self.Aug_Prod_11, self.Sep_Prod_11, 
			self.Oct_Prod_11, self.Nov_Prod_11, self.Dec_Prod_11])
		values_prod_11 = list(dict_prod11.values())
		key_prod_11 = list(dict_prod11.keys())
		np_prod_11 = np.array(values_prod_11)
		print(np_prod_11)
		acum_prod_11 = np_prod_11.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_11)
		self.lblTotalAnualProd_11.setText(str(acum_prod_11))

		dict_prod12 = {}
		dict_prod12['prod12'] = list([
			self.Jan_Prod_12, self.Feb_Prod_12, self.Mar_Prod_12, 
			self.Apr_Prod_12, self.May_Prod_12, self.Jun_Prod_12, 
			self.Jul_Prod_12, self.Aug_Prod_12, self.Sep_Prod_12, 
			self.Oct_Prod_12, self.Nov_Prod_12, self.Dec_Prod_12])
		values_prod_12 = list(dict_prod12.values())
		key_prod_12 = list(dict_prod12.keys())
		np_prod_12 = np.array(values_prod_12)
		print(np_prod_12)
		acum_prod_12 = np_prod_12.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_12)
		self.lblTotalAnualProd_12.setText(str(acum_prod_12))

		dict_prod13 = {}
		dict_prod13['prod13'] = list([
			self.Jan_Prod_13, self.Feb_Prod_13, self.Mar_Prod_13, 
			self.Apr_Prod_13, self.May_Prod_13, self.Jun_Prod_13, 
			self.Jul_Prod_13, self.Aug_Prod_13, self.Sep_Prod_13, 
			self.Oct_Prod_13, self.Nov_Prod_13, self.Dec_Prod_13])
		values_prod_13 = list(dict_prod13.values())
		key_prod_13 = list(dict_prod13.keys())
		np_prod_13 = np.array(values_prod_13)
		print(np_prod_13)
		acum_prod_13 = np_prod_13.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_13)
		self.lblTotalAnualProd_13.setText(str(acum_prod_13))

		dict_prod14 = {}
		dict_prod14['prod14'] = list([
			self.Jan_Prod_14, self.Feb_Prod_14, self.Mar_Prod_14, 
			self.Apr_Prod_14, self.May_Prod_14, self.Jun_Prod_14, 
			self.Jul_Prod_14, self.Aug_Prod_14, self.Sep_Prod_14, 
			self.Oct_Prod_14, self.Nov_Prod_14, self.Dec_Prod_14])
		values_prod_14 = list(dict_prod14.values())
		key_prod_14 = list(dict_prod14.keys())
		np_prod_14 = np.array(values_prod_14)
		print(np_prod_14)
		acum_prod_14 = np_prod_14.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_14)
		self.lblTotalAnualProd_14.setText(str(acum_prod_14))

		dict_prod15 = {}
		dict_prod15['prod15'] = list([
			self.Jan_Prod_15, self.Feb_Prod_15, self.Mar_Prod_15, 
			self.Apr_Prod_15, self.May_Prod_15, self.Jun_Prod_15, 
			self.Jul_Prod_15, self.Aug_Prod_15, self.Sep_Prod_15, 
			self.Oct_Prod_15, self.Nov_Prod_15, self.Dec_Prod_15])
		values_prod_15 = list(dict_prod15.values())
		key_prod_15 = list(dict_prod15.keys())
		np_prod_15 = np.array(values_prod_15)
		print(np_prod_15)
		acum_prod_15 = np_prod_15.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_15)
		self.lblTotalAnualProd_15.setText(str(acum_prod_15))

		dict_prod16 = {}
		dict_prod16['prod16'] = list([
			self.Jan_Prod_16, self.Feb_Prod_16, self.Mar_Prod_16, 
			self.Apr_Prod_16, self.May_Prod_16, self.Jun_Prod_16, 
			self.Jul_Prod_16, self.Aug_Prod_16, self.Sep_Prod_16, 
			self.Oct_Prod_16, self.Nov_Prod_16, self.Dec_Prod_16])
		values_prod_16 = list(dict_prod16.values())
		key_prod_16 = list(dict_prod16.keys())
		np_prod_16 = np.array(values_prod_16)
		print(np_prod_16)
		acum_prod_16 = np_prod_16.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_16)
		self.lblTotalAnualProd_16.setText(str(acum_prod_16))

		dict_prod17 = {}
		dict_prod17['prod17'] = list([
			self.Jan_Prod_17, self.Feb_Prod_17, self.Mar_Prod_17, 
			self.Apr_Prod_17, self.May_Prod_17, self.Jun_Prod_17, 
			self.Jul_Prod_17, self.Aug_Prod_17, self.Sep_Prod_17, 
			self.Oct_Prod_17, self.Nov_Prod_17, self.Dec_Prod_17])
		values_prod_17 = list(dict_prod17.values())
		key_prod_17 = list(dict_prod17.keys())
		np_prod_17 = np.array(values_prod_17)
		print(np_prod_17)
		acum_prod_17 = np_prod_17.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_17)
		self.lblTotalAnualProd_17.setText(str(acum_prod_17))

		dict_prod18 = {}
		dict_prod18['prod18'] = list([
			self.Jan_Prod_18, self.Feb_Prod_18, self.Mar_Prod_18, 
			self.Apr_Prod_18, self.May_Prod_18, self.Jun_Prod_18, 
			self.Jul_Prod_18, self.Aug_Prod_18, self.Sep_Prod_18, 
			self.Oct_Prod_18, self.Nov_Prod_18, self.Dec_Prod_18])
		values_prod_18 = list(dict_prod18.values())
		key_prod_18 = list(dict_prod18.keys())
		np_prod_18 = np.array(values_prod_18)
		print(np_prod_18)
		acum_prod_18 = np_prod_18.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_18)
		self.lblTotalAnualProd_18.setText(str(acum_prod_18))

		dict_prod19 = {}
		dict_prod19['prod19'] = list([
			self.Jan_Prod_19, self.Feb_Prod_19, self.Mar_Prod_19, 
			self.Apr_Prod_19, self.May_Prod_19, self.Jun_Prod_19, 
			self.Jul_Prod_19, self.Aug_Prod_19, self.Sep_Prod_19, 
			self.Oct_Prod_19, self.Nov_Prod_19, self.Dec_Prod_19])
		values_prod_19 = list(dict_prod19.values())
		key_prod_19 = list(dict_prod19.keys())
		np_prod_19 = np.array(values_prod_19)
		print(np_prod_19)
		acum_prod_19 = np_prod_19.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_19)
		self.lblTotalAnualProd_19.setText(str(acum_prod_19))

		dict_prod20 = {}
		dict_prod20['prod20'] = list([
			self.Jan_Prod_20, self.Feb_Prod_20, self.Mar_Prod_20, 
			self.Apr_Prod_20, self.May_Prod_20, self.Jun_Prod_20, 
			self.Jul_Prod_20, self.Aug_Prod_20, self.Sep_Prod_20, 
			self.Oct_Prod_20, self.Nov_Prod_20, self.Dec_Prod_20])
		values_prod_20 = list(dict_prod20.values())
		key_prod_20 = list(dict_prod20.keys())
		np_prod_20 = np.array(values_prod_20)
		print(np_prod_20)
		acum_prod_20 = np_prod_20.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_20)
		self.lblTotalAnualProd_20.setText(str(acum_prod_20))

		dict_prod21 = {}
		dict_prod21['prod21'] = list([
			self.Jan_Prod_21, self.Feb_Prod_21, self.Mar_Prod_21, 
			self.Apr_Prod_21, self.May_Prod_21, self.Jun_Prod_21, 
			self.Jul_Prod_21, self.Aug_Prod_21, self.Sep_Prod_21, 
			self.Oct_Prod_21, self.Nov_Prod_21, self.Dec_Prod_21])
		values_prod_21 = list(dict_prod21.values())
		key_prod_21 = list(dict_prod21.keys())
		np_prod_21 = np.array(values_prod_21)
		print(np_prod_21)
		acum_prod_21 = np_prod_21.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_21)
		self.lblTotalAnualProd_21.setText(str(acum_prod_21))

		dict_prod22 = {}
		dict_prod22['prod22'] = list([
			self.Jan_Prod_22, self.Feb_Prod_22, self.Mar_Prod_22, 
			self.Apr_Prod_22, self.May_Prod_22, self.Jun_Prod_22, 
			self.Jul_Prod_22, self.Aug_Prod_22, self.Sep_Prod_22, 
			self.Oct_Prod_22, self.Nov_Prod_22, self.Dec_Prod_22])
		values_prod_22 = list(dict_prod22.values())
		key_prod_22 = list(dict_prod22.keys())
		np_prod_22 = np.array(values_prod_22)
		print(np_prod_22)
		acum_prod_22 = np_prod_22.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_22)
		self.lblTotalAnualProd_22.setText(str(acum_prod_22))

		dict_prod23 = {}
		dict_prod23['prod23'] = list([
			self.Jan_Prod_23, self.Feb_Prod_23, self.Mar_Prod_23, 
			self.Apr_Prod_23, self.May_Prod_23, self.Jun_Prod_23, 
			self.Jul_Prod_23, self.Aug_Prod_23, self.Sep_Prod_23, 
			self.Oct_Prod_23, self.Nov_Prod_23, self.Dec_Prod_23])
		values_prod_23 = list(dict_prod23.values())
		key_prod_23 = list(dict_prod23.keys())
		np_prod_23 = np.array(values_prod_23)
		print(np_prod_23)
		acum_prod_23 = np_prod_23.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_23)
		self.lblTotalAnualProd_23.setText(str(acum_prod_23))

		dict_prod24 = {}
		dict_prod24['prod24'] = list([
			self.Jan_Prod_24, self.Feb_Prod_24, self.Mar_Prod_24, 
			self.Apr_Prod_24, self.May_Prod_24, self.Jun_Prod_24, 
			self.Jul_Prod_24, self.Aug_Prod_24, self.Sep_Prod_24, 
			self.Oct_Prod_24, self.Nov_Prod_24, self.Dec_Prod_24])
		values_prod_24 = list(dict_prod24.values())
		key_prod_24 = list(dict_prod24.keys())
		np_prod_24 = np.array(values_prod_24)
		print(np_prod_24)
		acum_prod_24 = np_prod_24.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_24)
		self.lblTotalAnualProd_24.setText(str(acum_prod_24))

		dict_prod25 = {}
		dict_prod25['prod25'] = list([
			self.Jan_Prod_25, self.Feb_Prod_25, self.Mar_Prod_25, 
			self.Apr_Prod_25, self.May_Prod_25, self.Jun_Prod_25, 
			self.Jul_Prod_25, self.Aug_Prod_25, self.Sep_Prod_25, 
			self.Oct_Prod_25, self.Nov_Prod_25, self.Dec_Prod_25])
		values_prod_25 = list(dict_prod25.values())
		key_prod_25 = list(dict_prod25.keys())
		np_prod_25 = np.array(values_prod_25)
		print(np_prod_25)
		acum_prod_25 = np_prod_25.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_25)
		self.lblTotalAnualProd_25.setText(str(acum_prod_25))

		dict_prod26 = {}
		dict_prod26['prod26'] = list([
			self.Jan_Prod_26, self.Feb_Prod_26, self.Mar_Prod_26, 
			self.Apr_Prod_26, self.May_Prod_26, self.Jun_Prod_26, 
			self.Jul_Prod_26, self.Aug_Prod_26, self.Sep_Prod_26, 
			self.Oct_Prod_26, self.Nov_Prod_26, self.Dec_Prod_26])
		values_prod_26 = list(dict_prod26.values())
		key_prod_26 = list(dict_prod26.keys())
		np_prod_26 = np.array(values_prod_26)
		print(np_prod_26)
		acum_prod_26 = np_prod_26.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_26)
		self.lblTotalAnualProd_26.setText(str(acum_prod_26))

		dict_prod27 = {}
		dict_prod27['prod27'] = list([
			self.Jan_Prod_27, self.Feb_Prod_27, self.Mar_Prod_27, 
			self.Apr_Prod_27, self.May_Prod_27, self.Jun_Prod_27, 
			self.Jul_Prod_27, self.Aug_Prod_27, self.Sep_Prod_27, 
			self.Oct_Prod_27, self.Nov_Prod_27, self.Dec_Prod_27])
		values_prod_27 = list(dict_prod27.values())
		key_prod_27 = list(dict_prod27.keys())
		np_prod_27 = np.array(values_prod_27)
		print(np_prod_27)
		acum_prod_27 = np_prod_27.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_27)
		self.lblTotalAnualProd_27.setText(str(acum_prod_27))

		dict_prod28 = {}
		dict_prod28['prod28'] = list([
			self.Jan_Prod_28, self.Feb_Prod_28, self.Mar_Prod_28, 
			self.Apr_Prod_28, self.May_Prod_28, self.Jun_Prod_28, 
			self.Jul_Prod_28, self.Aug_Prod_28, self.Sep_Prod_28, 
			self.Oct_Prod_28, self.Nov_Prod_28, self.Dec_Prod_28])
		values_prod_28 = list(dict_prod28.values())
		key_prod_28 = list(dict_prod28.keys())
		np_prod_28 = np.array(values_prod_28)
		print(np_prod_28)
		acum_prod_28 = np_prod_28.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_28)
		self.lblTotalAnualProd_28.setText(str(acum_prod_28))

		dict_prod29 = {}
		dict_prod29['prod29'] = list([
			self.Jan_Prod_29, self.Feb_Prod_29, self.Mar_Prod_29, 
			self.Apr_Prod_29, self.May_Prod_29, self.Jun_Prod_29, 
			self.Jul_Prod_29, self.Aug_Prod_29, self.Sep_Prod_29, 
			self.Oct_Prod_29, self.Nov_Prod_29, self.Dec_Prod_29])
		values_prod_29 = list(dict_prod29.values())
		key_prod_29 = list(dict_prod29.keys())
		np_prod_29 = np.array(values_prod_29)
		print(np_prod_29)
		acum_prod_29 = np_prod_29.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_29)
		self.lblTotalAnualProd_29.setText(str(acum_prod_29))

		dict_prod30 = {}
		dict_prod30['prod30'] = list([
			self.Jan_Prod_30, self.Feb_Prod_30, self.Mar_Prod_30, 
			self.Apr_Prod_30, self.May_Prod_30, self.Jun_Prod_30, 
			self.Jul_Prod_30, self.Aug_Prod_30, self.Sep_Prod_30, 
			self.Oct_Prod_30, self.Nov_Prod_30, self.Dec_Prod_30])
		values_prod_30 = list(dict_prod30.values())
		key_prod_30 = list(dict_prod30.keys())
		np_prod_30 = np.array(values_prod_30)
		print(np_prod_30)
		acum_prod_30 = np_prod_30.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_30)
		self.lblTotalAnualProd_30.setText(str(acum_prod_30))

		dict_prod31 = {}
		dict_prod31['prod31'] = list([
			self.Jan_Prod_31, self.Feb_Prod_31, self.Mar_Prod_31, 
			self.Apr_Prod_31, self.May_Prod_31, self.Jun_Prod_31, 
			self.Jul_Prod_31, self.Aug_Prod_31, self.Sep_Prod_31, 
			self.Oct_Prod_31, self.Nov_Prod_31, self.Dec_Prod_31])
		values_prod_31 = list(dict_prod31.values())
		key_prod_31 = list(dict_prod31.keys())
		np_prod_31 = np.array(values_prod_31)
		print(np_prod_31)
		acum_prod_31 = np_prod_31.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_31)
		self.lblTotalAnualProd_31.setText(str(acum_prod_31))

		dict_prod32 = {}
		dict_prod32['prod32'] = list([
			self.Jan_Prod_32, self.Feb_Prod_32, self.Mar_Prod_32, 
			self.Apr_Prod_32, self.May_Prod_32, self.Jun_Prod_32, 
			self.Jul_Prod_32, self.Aug_Prod_32, self.Sep_Prod_32, 
			self.Oct_Prod_32, self.Nov_Prod_32, self.Dec_Prod_32])
		values_prod_32 = list(dict_prod32.values())
		key_prod_32 = list(dict_prod32.keys())
		np_prod_32 = np.array(values_prod_32)
		print(np_prod_32)
		acum_prod_32 = np_prod_32.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_32)
		self.lblTotalAnualProd_32.setText(str(acum_prod_32))

		dict_prod33 = {}
		dict_prod33['prod33'] = list([
			self.Jan_Prod_33, self.Feb_Prod_33, self.Mar_Prod_33, 
			self.Apr_Prod_33, self.May_Prod_33, self.Jun_Prod_33, 
			self.Jul_Prod_33, self.Aug_Prod_33, self.Sep_Prod_33, 
			self.Oct_Prod_33, self.Nov_Prod_33, self.Dec_Prod_33])
		values_prod_33 = list(dict_prod33.values())
		key_prod_33 = list(dict_prod33.keys())
		np_prod_33 = np.array(values_prod_33)
		print(np_prod_33)
		acum_prod_33 = np_prod_33.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_33)
		self.lblTotalAnualProd_33.setText(str(acum_prod_33))

		dict_prod34 = {}
		dict_prod34['prod34'] = list([
			self.Jan_Prod_34, self.Feb_Prod_34, self.Mar_Prod_34, 
			self.Apr_Prod_34, self.May_Prod_34, self.Jun_Prod_34, 
			self.Jul_Prod_34, self.Aug_Prod_34, self.Sep_Prod_34, 
			self.Oct_Prod_34, self.Nov_Prod_34, self.Dec_Prod_34])
		values_prod_34 = list(dict_prod34.values())
		key_prod_34 = list(dict_prod34.keys())
		np_prod_34 = np.array(values_prod_34)
		print(np_prod_34)
		acum_prod_34 = np_prod_34.sum()
		print('la suma del producto 1 es ', key_prod, acum_prod_34)
		self.lblTotalAnualProd_34.setText(str(acum_prod_34))

		np_group1 = np_prod + np_prod_2 + np_prod_3 + np_prod_4 + np_prod_5 
		np_group2 = np_prod_6 + np_prod_7 + np_prod_8 + np_prod_9 +np_prod_10 
		np_group3 = np_prod_11 + np_prod_12 + np_prod_13 + np_prod_14 + np_prod_15  
		np_group4 = np_prod_16 + np_prod_17 + np_prod_18 + np_prod_19 + np_prod_20  
		np_group5 = np_prod_21 + np_prod_22 + np_prod_23 + np_prod_24 + np_prod_25 
		np_group6 = np_prod_26 + np_prod_27 + np_prod_28 + np_prod_29 + np_prod_30  
		np_group7 = np_prod_31 + np_prod_32 + np_prod_33 + np_prod_34
		
		np_total = np_group1 + np_group2 + np_group3 + np_group4 + np_group5 + np_group6 + np_group7
		

		acum_total = np_total.sum()
		print('total',np_total)
		print('acumulado total', acum_total)

		np_total_Jan = np_total[0][0]
		np_total_Feb = np_total[0][1]
		np_total_Mar = np_total[0][2]
		np_total_Apr = np_total[0][3]
		np_total_May = np_total[0][4]
		np_total_Jun = np_total[0][5]
		np_total_Jul = np_total[0][6]
		np_total_Aug = np_total[0][7]
		np_total_Sep = np_total[0][8]
		np_total_Oct = np_total[0][9]
		np_total_Nov = np_total[0][10]
		np_total_Dec = np_total[0][11]
		print(np_total_Jan, np_total_Feb, np_total_Mar,
				np_total_Apr, np_total_May, np_total_Jun,
				np_total_Jul,  np_total_Aug, np_total_Sep,
				np_total_Oct, np_total_Nov, np_total_Dec)
		
		self.lblTotalJan.setText(str(np_total_Jan))
		self.lblTotalFeb.setText(str(np_total_Feb))
		self.lblTotalMar.setText(str(np_total_Mar))
		self.lblTotalApr.setText(str(np_total_Apr))
		self.lblTotalMay.setText(str(np_total_May))
		self.lblTotalJun.setText(str(np_total_Jun))
		self.lblTotalJul.setText(str(np_total_Jul))
		self.lblTotalAug.setText(str(np_total_Aug))
		self.lblTotalSep.setText(str(np_total_Sep))
		self.lblTotalOct.setText(str(np_total_Oct))
		self.lblTotalNov.setText(str(np_total_Nov))
		self.lblTotalDec.setText(str(np_total_Dec))


		dict_total_Esa_Sales = {}
		dict_total_Esa_Sales['total Sales'] = list([
			np_total_Jan, np_total_Feb, np_total_Mar, 
			np_total_Apr, np_total_May, np_total_Jun, 
			np_total_Jul, np_total_Aug, np_total_Sep, 
			np_total_Oct, np_total_Nov, np_total_Dec])
		print('diccionario de Esa Sales', dict_total_Esa_Sales)

		self.lblTotalAnual.setText(str(acum_total))

		self.data_complete = [
						dict_prod, dict_prod2, dict_prod3, dict_prod4, dict_prod5,
						dict_prod6, dict_prod7, dict_prod8, dict_prod9, dict_prod10,
						dict_prod11, dict_prod12, dict_prod13, dict_prod14, dict_prod15,
						dict_prod16, dict_prod17, dict_prod18, dict_prod19, dict_prod20,
						dict_prod21, dict_prod22, dict_prod23, dict_prod24, dict_prod25,
						dict_prod26, dict_prod27, dict_prod28, dict_prod29, dict_prod30,
						dict_prod31, dict_prod32, dict_prod33, dict_prod34]

		self.pBtnReport.setEnabled(True)
		generaExcel =self.genera_excel(self.data_complete)

	def inicializar_campós(self,datos):
		"""

		This function set all field values as the value in the file
		"""
		print(datos)
		prod = datos.get('Br. Flrts 1 - 2 1/8')
		self.lEditJanProd.insert(str(round(prod[0],2)))
		self.lEditFebProd.insert(str(prod[1]))
		self.lEditMarProd.insert(str(prod[2]))
		self.lEditAprProd.insert(str(prod[3]))
		self.lEditMayProd.insert(str(prod[4]))
		self.lEditJunProd.insert(str(prod[5]))
		self.lEditJulProd.insert(str(prod[6]))
		self.lEditAugProd.insert(str(prod[7]))
		self.lEditSepProd.insert(str(prod[8]))
		self.lEditOctProd.insert(str(prod[9]))
		self.lEditNovProd.insert(str(prod[10]))
		self.lEditDecProd.insert(str(prod[11]))

		prod2 = datos.get('Br Stalks')
		self.lEditJanProd_2.insert(str(prod2[0]))
		self.lEditFebProd_2.insert(str(prod2[1]))
		self.lEditMarProd_2.insert(str(prod2[2]))
		self.lEditAprProd_2.insert(str(prod2[3]))
		self.lEditMayProd_2.insert(str(prod2[4]))
		self.lEditJunProd_2.insert(str(prod2[5]))
		self.lEditJulProd_2.insert(str(prod2[6]))
		self.lEditAugProd_2.insert(str(prod2[7]))
		self.lEditSepProd_2.insert(str(prod2[8]))
		self.lEditOctProd_2.insert(str(prod2[9]))
		self.lEditNovProd_2.insert(str(prod2[10]))
		self.lEditDecProd_2.insert(str(prod2[11]))
						
		prod3 = datos.get('Br Pearls')
		self.lEditJanProd_3.insert(str(prod3[0]))
		self.lEditFebProd_3.insert(str(prod3[1]))
		self.lEditMarProd_3.insert(str(prod3[2]))
		self.lEditAprProd_3.insert(str(prod3[3]))
		self.lEditMayProd_3.insert(str(prod3[4]))
		self.lEditJunProd_3.insert(str(prod3[5]))
		self.lEditJulProd_3.insert(str(prod3[6]))
		self.lEditAugProd_3.insert(str(prod3[7]))
		self.lEditSepProd_3.insert(str(prod3[8]))
		self.lEditOctProd_3.insert(str(prod3[9]))
		self.lEditNovProd_3.insert(str(prod3[10]))
		self.lEditDecProd_3.insert(str(prod3[11]))
						
		prod4 = datos.get('Col. Flrts 1 - 2 1/8')
		self.lEditJanProd_4.insert(str(prod4[0]))
		self.lEditFebProd_4.insert(str(prod4[1]))
		self.lEditMarProd_4.insert(str(prod4[2]))
		self.lEditAprProd_4.insert(str(prod4[3]))
		self.lEditMayProd_4.insert(str(prod4[4]))
		self.lEditJunProd_4.insert(str(prod4[5]))
		self.lEditJulProd_4.insert(str(prod4[6]))
		self.lEditAugProd_4.insert(str(prod4[7]))
		self.lEditSepProd_4.insert(str(prod4[8]))
		self.lEditOctProd_4.insert(str(prod4[9]))
		self.lEditNovProd_4.insert(str(prod4[10]))
		self.lEditDecProd_4.insert(str(prod4[11]))

		prod5 = datos.get('Col. Flrts 3/4 - 1 3/8')
		self.lEditJanProd_5.insert(str(prod5[0]))
		self.lEditFebProd_5.insert(str(prod5[1]))
		self.lEditMarProd_5.insert(str(prod5[2]))
		self.lEditAprProd_5.insert(str(prod5[3]))
		self.lEditMayProd_5.insert(str(prod5[4]))
		self.lEditJunProd_5.insert(str(prod5[5]))
		self.lEditJulProd_5.insert(str(prod5[6]))
		self.lEditAugProd_5.insert(str(prod5[7]))
		self.lEditSepProd_5.insert(str(prod5[8]))
		self.lEditOctProd_5.insert(str(prod5[9]))
		self.lEditNovProd_5.insert(str(prod5[10]))
		self.lEditDecProd_5.insert(str(prod5[11]))
						
		prod6 = datos.get('Col Nuggets')
		self.lEditJanProd_6.insert(str(prod6[0]))
		self.lEditFebProd_6.insert(str(prod6[1]))
		self.lEditMarProd_6.insert(str(prod6[2]))
		self.lEditAprProd_6.insert(str(prod6[3]))
		self.lEditMayProd_6.insert(str(prod6[4]))
		self.lEditJunProd_6.insert(str(prod6[5]))
		self.lEditJulProd_6.insert(str(prod6[6]))
		self.lEditAugProd_6.insert(str(prod6[7]))
		self.lEditSepProd_6.insert(str(prod6[8]))
		self.lEditOctProd_6.insert(str(prod6[9]))
		self.lEditNovProd_6.insert(str(prod6[10]))
		self.lEditDecProd_6.insert(str(prod6[11]))
		
		prod7 = datos.get('Yellow Squash')
		self.lEditJanProd_7.insert(str(prod7[0]))
		self.lEditFebProd_7.insert(str(prod7[1]))
		self.lEditMarProd_7.insert(str(prod7[2]))
		self.lEditAprProd_7.insert(str(prod7[3]))
		self.lEditMayProd_7.insert(str(prod7[4]))
		self.lEditJunProd_7.insert(str(prod7[5]))
		self.lEditJulProd_7.insert(str(prod7[6]))
		self.lEditAugProd_7.insert(str(prod7[7]))
		self.lEditSepProd_7.insert(str(prod7[8]))
		self.lEditOctProd_7.insert(str(prod7[9]))
		self.lEditNovProd_7.insert(str(prod7[10]))
		self.lEditDecProd_7.insert(str(prod7[11]))

		prod8 = datos.get('Green Zucchini')
		self.lEditJanProd_8.insert(str(prod8[0]))
		self.lEditFebProd_8.insert(str(prod8[1]))
		self.lEditMarProd_8.insert(str(prod8[2]))
		self.lEditAprProd_8.insert(str(prod8[3]))
		self.lEditMayProd_8.insert(str(prod8[4]))
		self.lEditJunProd_8.insert(str(prod8[5]))
		self.lEditJulProd_8.insert(str(prod8[6]))
		self.lEditAugProd_8.insert(str(prod8[7]))
		self.lEditSepProd_8.insert(str(prod8[8]))
		self.lEditOctProd_8.insert(str(prod8[9]))
		self.lEditNovProd_8.insert(str(prod8[10]))
		self.lEditDecProd_8.insert(str(prod8[11]))
		
		prod9 = datos.get('prod9')
		self.lEditJanProd_9.insert(str(prod9[0]))
		self.lEditFebProd_9.insert(str(prod9[1]))
		self.lEditMarProd_9.insert(str(prod9[2]))
		self.lEditAprProd_9.insert(str(prod9[3]))
		self.lEditMayProd_9.insert(str(prod9[4]))
		self.lEditJunProd_9.insert(str(prod9[5]))
		self.lEditJulProd_9.insert(str(prod9[6]))
		self.lEditAugProd_9.insert(str(prod9[7]))
		self.lEditSepProd_9.insert(str(prod9[8]))
		self.lEditOctProd_9.insert(str(prod9[9]))
		self.lEditNovProd_9.insert(str(prod9[9]))
		self.lEditDecProd_9.insert(str(prod9[11]))
						
		
		prod10 = datos.get('prod10')
		self.lEditJanProd_10.insert(str(prod10[0]))
		self.lEditFebProd_10.insert(str(prod10[1]))
		self.lEditMarProd_10.insert(str(prod10[2]))
		self.lEditAprProd_10.insert(str(prod10[3]))
		self.lEditMayProd_10.insert(str(prod10[4]))
		self.lEditJunProd_10.insert(str(prod10[5]))
		self.lEditJulProd_10.insert(str(prod10[6]))
		self.lEditAugProd_10.insert(str(prod10[7]))
		self.lEditSepProd_10.insert(str(prod10[8]))
		self.lEditOctProd_10.insert(str(prod10[9]))
		self.lEditNovProd_10.insert(str(prod10[10]))
		self.lEditDecProd_10.insert(str(prod10[11]))

		
		prod11 = datos.get('prod11')
		self.lEditJanProd_11.insert(str(prod11[0]))
		self.lEditFebProd_11.insert(str(prod11[1]))
		self.lEditMarProd_11.insert(str(prod11[2]))
		self.lEditAprProd_11.insert(str(prod11[3]))
		self.lEditMayProd_11.insert(str(prod11[4]))
		self.lEditJunProd_11.insert(str(prod11[5]))
		self.lEditJulProd_11.insert(str(prod11[6]))
		self.lEditAugProd_11.insert(str(prod11[7]))
		self.lEditSepProd_11.insert(str(prod11[8]))
		self.lEditOctProd_11.insert(str(prod11[9]))
		self.lEditNovProd_11.insert(str(prod11[10]))
		self.lEditDecProd_11.insert(str(prod11[11]))

		prod12 = datos.get('prod12')
		self.lEditJanProd_12.insert(str(prod12[0]))
		self.lEditFebProd_12.insert(str(prod12[1]))
		self.lEditMarProd_12.insert(str(prod12[2]))
		self.lEditAprProd_12.insert(str(prod12[3]))
		self.lEditMayProd_12.insert(str(prod12[4]))
		self.lEditJunProd_12.insert(str(prod12[5]))
		self.lEditJulProd_12.insert(str(prod12[6]))
		self.lEditAugProd_12.insert(str(prod12[7]))
		self.lEditSepProd_12.insert(str(prod12[8]))
		self.lEditOctProd_12.insert(str(prod12[9]))
		self.lEditNovProd_12.insert(str(prod12[10]))
		self.lEditDecProd_12.insert(str(prod12[11]))

		prod13 = datos.get('prod13')
		self.lEditJanProd_13.insert(str(prod13[0]))
		self.lEditFebProd_13.insert(str(prod13[1]))
		self.lEditMarProd_13.insert(str(prod13[2]))
		self.lEditAprProd_13.insert(str(prod13[3]))
		self.lEditMayProd_13.insert(str(prod13[4]))
		self.lEditJunProd_13.insert(str(prod13[5]))
		self.lEditJulProd_13.insert(str(prod13[6]))
		self.lEditAugProd_13.insert(str(prod13[7]))
		self.lEditSepProd_13.insert(str(prod13[8]))
		self.lEditOctProd_13.insert(str(prod13[9]))
		self.lEditNovProd_13.insert(str(prod13[10]))
		self.lEditDecProd_13.insert(str(prod13[11]))

		prod14 = datos.get('prod14')
		self.lEditJanProd_14.insert(str(prod14[0]))
		self.lEditFebProd_14.insert(str(prod14[1]))
		self.lEditMarProd_14.insert(str(prod14[2]))
		self.lEditAprProd_14.insert(str(prod14[3]))
		self.lEditMayProd_14.insert(str(prod14[4]))
		self.lEditJunProd_14.insert(str(prod14[5]))
		self.lEditJulProd_14.insert(str(prod14[6]))
		self.lEditAugProd_14.insert(str(prod14[7]))
		self.lEditSepProd_14.insert(str(prod14[8]))
		self.lEditOctProd_14.insert(str(prod14[9]))
		self.lEditNovProd_14.insert(str(prod14[10]))
		self.lEditDecProd_14.insert(str(prod14[11]))

		prod15 = datos.get('prod15')
		self.lEditJanProd_15.insert(str(prod15[0]))
		self.lEditFebProd_15.insert(str(prod15[1]))
		self.lEditMarProd_15.insert(str(prod15[2]))
		self.lEditAprProd_15.insert(str(prod15[3]))
		self.lEditMayProd_15.insert(str(prod15[4]))
		self.lEditJunProd_15.insert(str(prod15[5]))
		self.lEditJulProd_15.insert(str(prod15[6]))
		self.lEditAugProd_15.insert(str(prod15[7]))
		self.lEditSepProd_15.insert(str(prod15[8]))
		self.lEditOctProd_15.insert(str(prod15[9]))
		self.lEditNovProd_15.insert(str(prod15[10]))
		self.lEditDecProd_15.insert(str(prod15[11]))

		prod16 = datos.get('prod16')
		self.lEditJanProd_16.insert(str(prod16[0]))
		self.lEditFebProd_16.insert(str(prod16[1]))
		self.lEditMarProd_16.insert(str(prod16[2]))
		self.lEditAprProd_16.insert(str(prod16[3]))
		self.lEditMayProd_16.insert(str(prod16[4]))
		self.lEditJunProd_16.insert(str(prod16[5]))
		self.lEditJulProd_16.insert(str(prod16[6]))
		self.lEditAugProd_16.insert(str(prod16[7]))
		self.lEditSepProd_16.insert(str(prod16[8]))
		self.lEditOctProd_16.insert(str(prod16[9]))
		self.lEditNovProd_16.insert(str(prod16[10]))
		self.lEditDecProd_16.insert(str(prod16[11]))

		prod17 = datos.get('prod17')
		self.lEditJanProd_17.insert(str(prod17[0]))
		self.lEditFebProd_17.insert(str(prod17[1]))
		self.lEditMarProd_17.insert(str(prod17[2]))
		self.lEditAprProd_17.insert(str(prod17[3]))
		self.lEditMayProd_17.insert(str(prod17[4]))
		self.lEditJunProd_17.insert(str(prod17[5]))
		self.lEditJulProd_17.insert(str(prod17[6]))
		self.lEditAugProd_17.insert(str(prod17[7]))
		self.lEditSepProd_17.insert(str(prod17[8]))
		self.lEditOctProd_17.insert(str(prod17[9]))
		self.lEditNovProd_17.insert(str(prod17[10]))
		self.lEditDecProd_17.insert(str(prod17[11]))

		prod18 = datos.get('prod18')
		self.lEditJanProd_18.insert(str(prod18[0]))
		self.lEditFebProd_18.insert(str(prod18[1]))
		self.lEditMarProd_18.insert(str(prod18[2]))
		self.lEditAprProd_18.insert(str(prod18[3]))
		self.lEditMayProd_18.insert(str(prod18[4]))
		self.lEditJunProd_18.insert(str(prod18[5]))
		self.lEditJulProd_18.insert(str(prod18[6]))
		self.lEditAugProd_18.insert(str(prod18[7]))
		self.lEditSepProd_18.insert(str(prod18[8]))
		self.lEditOctProd_18.insert(str(prod18[9]))
		self.lEditNovProd_18.insert(str(prod18[10]))
		self.lEditDecProd_18.insert(str(prod18[11]))

		prod19= datos.get('prod19')
		self.lEditJanProd_19.insert(str(prod19[0]))
		self.lEditFebProd_19.insert(str(prod19[1]))
		self.lEditMarProd_19.insert(str(prod19[2]))
		self.lEditAprProd_19.insert(str(prod19[3]))
		self.lEditMayProd_19.insert(str(prod19[4]))
		self.lEditJunProd_19.insert(str(prod19[5]))
		self.lEditJulProd_19.insert(str(prod19[6]))
		self.lEditAugProd_19.insert(str(prod19[7]))
		self.lEditSepProd_19.insert(str(prod19[8]))
		self.lEditOctProd_19.insert(str(prod19[9]))
		self.lEditNovProd_19.insert(str(prod19[10]))
		self.lEditDecProd_19.insert(str(prod19[11]))

		prod20 = datos.get('prod20')
		self.lEditJanProd_20.insert(str(prod20[0]))
		self.lEditFebProd_20.insert(str(prod20[1]))
		self.lEditMarProd_20.insert(str(prod20[2]))
		self.lEditAprProd_20.insert(str(prod20[3]))
		self.lEditMayProd_20.insert(str(prod20[4]))
		self.lEditJunProd_20.insert(str(prod20[5]))
		self.lEditJulProd_20.insert(str(prod20[6]))
		self.lEditAugProd_20.insert(str(prod20[7]))
		self.lEditSepProd_20.insert(str(prod20[8]))
		self.lEditOctProd_20.insert(str(prod20[9]))
		self.lEditNovProd_20.insert(str(prod20[10]))
		self.lEditDecProd_20.insert(str(prod20[11]))

		prod21 = datos.get('prod21')
		self.lEditJanProd_21.insert(str(prod21[0]))
		self.lEditFebProd_21.insert(str(prod21[1]))
		self.lEditMarProd_21.insert(str(prod21[2]))
		self.lEditAprProd_21.insert(str(prod21[3]))
		self.lEditMayProd_21.insert(str(prod21[4]))
		self.lEditJunProd_21.insert(str(prod21[5]))
		self.lEditJulProd_21.insert(str(prod21[6]))
		self.lEditAugProd_21.insert(str(prod21[7]))
		self.lEditSepProd_21.insert(str(prod21[8]))
		self.lEditOctProd_21.insert(str(prod21[9]))
		self.lEditNovProd_21.insert(str(prod21[10]))
		self.lEditDecProd_21.insert(str(prod21[11]))

		prod22 = datos.get('prod22')
		self.lEditJanProd_22.insert(str(prod22[0]))
		self.lEditFebProd_22.insert(str(prod22[1]))
		self.lEditMarProd_22.insert(str(prod22[2]))
		self.lEditAprProd_22.insert(str(prod22[3]))
		self.lEditMayProd_22.insert(str(prod22[4]))
		self.lEditJunProd_22.insert(str(prod22[5]))
		self.lEditJulProd_22.insert(str(prod22[6]))
		self.lEditAugProd_22.insert(str(prod22[7]))
		self.lEditSepProd_22.insert(str(prod22[8]))
		self.lEditOctProd_22.insert(str(prod22[9]))
		self.lEditNovProd_22.insert(str(prod22[10]))
		self.lEditDecProd_22.insert(str(prod22[11]))

		prod23 = datos.get('prod23')
		self.lEditJanProd_23.insert(str(prod23[0]))
		self.lEditFebProd_23.insert(str(prod23[1]))
		self.lEditMarProd_23.insert(str(prod23[2]))
		self.lEditAprProd_23.insert(str(prod23[3]))
		self.lEditMayProd_23.insert(str(prod23[4]))
		self.lEditJunProd_23.insert(str(prod23[5]))
		self.lEditJulProd_23.insert(str(prod23[6]))
		self.lEditAugProd_23.insert(str(prod23[7]))
		self.lEditSepProd_23.insert(str(prod23[8]))
		self.lEditOctProd_23.insert(str(prod23[9]))
		self.lEditNovProd_23.insert(str(prod23[10]))
		self.lEditDecProd_23.insert(str(prod23[11]))

		prod24 = datos.get('prod24')
		self.lEditJanProd_24.insert(str(prod24[0]))
		self.lEditFebProd_24.insert(str(prod24[1]))
		self.lEditMarProd_24.insert(str(prod24[2]))
		self.lEditAprProd_24.insert(str(prod24[3]))
		self.lEditMayProd_24.insert(str(prod24[4]))
		self.lEditJunProd_24.insert(str(prod24[5]))
		self.lEditJulProd_24.insert(str(prod24[6]))
		self.lEditAugProd_24.insert(str(prod24[7]))
		self.lEditSepProd_24.insert(str(prod24[8]))
		self.lEditOctProd_24.insert(str(prod24[9]))
		self.lEditNovProd_24.insert(str(prod24[10]))
		self.lEditDecProd_24.insert(str(prod24[11]))

		prod25 = datos.get('prod25')
		self.lEditJanProd_25.insert(str(prod25[0]))
		self.lEditFebProd_25.insert(str(prod25[1]))
		self.lEditMarProd_25.insert(str(prod25[2]))
		self.lEditAprProd_25.insert(str(prod25[3]))
		self.lEditMayProd_25.insert(str(prod25[4]))
		self.lEditJunProd_25.insert(str(prod25[5]))
		self.lEditJulProd_25.insert(str(prod25[6]))
		self.lEditAugProd_25.insert(str(prod25[7]))
		self.lEditSepProd_25.insert(str(prod25[8]))
		self.lEditOctProd_25.insert(str(prod25[9]))
		self.lEditNovProd_25.insert(str(prod25[10]))
		self.lEditDecProd_25.insert(str(prod25[11]))

		prod26 = datos.get('prod26')
		self.lEditJanProd_26.insert(str(prod26[0]))
		self.lEditFebProd_26.insert(str(prod26[1]))
		self.lEditMarProd_26.insert(str(prod26[2]))
		self.lEditAprProd_26.insert(str(prod26[3]))
		self.lEditMayProd_26.insert(str(prod26[4]))
		self.lEditJunProd_26.insert(str(prod26[5]))
		self.lEditJulProd_26.insert(str(prod26[6]))
		self.lEditAugProd_26.insert(str(prod26[7]))
		self.lEditSepProd_26.insert(str(prod26[8]))
		self.lEditOctProd_26.insert(str(prod26[9]))
		self.lEditNovProd_26.insert(str(prod26[10]))
		self.lEditDecProd_26.insert(str(prod26[11]))

		prod27 = datos.get('prod27')
		self.lEditJanProd_27.insert(str(prod27[0]))
		self.lEditFebProd_27.insert(str(prod27[1]))
		self.lEditMarProd_27.insert(str(prod27[2]))
		self.lEditAprProd_27.insert(str(prod27[3]))
		self.lEditMayProd_27.insert(str(prod27[4]))
		self.lEditJunProd_27.insert(str(prod27[5]))
		self.lEditJulProd_27.insert(str(prod27[6]))
		self.lEditAugProd_27.insert(str(prod27[7]))
		self.lEditSepProd_27.insert(str(prod27[8]))
		self.lEditOctProd_27.insert(str(prod27[9]))
		self.lEditNovProd_27.insert(str(prod27[10]))
		self.lEditDecProd_27.insert(str(prod27[11]))

		prod28 = datos.get('prod28')
		self.lEditJanProd_28.insert(str(prod28[0]))
		self.lEditFebProd_28.insert(str(prod28[1]))
		self.lEditMarProd_28.insert(str(prod28[2]))
		self.lEditAprProd_28.insert(str(prod28[3]))
		self.lEditMayProd_28.insert(str(prod28[4]))
		self.lEditJunProd_28.insert(str(prod28[5]))
		self.lEditJulProd_28.insert(str(prod28[6]))
		self.lEditAugProd_28.insert(str(prod28[7]))
		self.lEditSepProd_28.insert(str(prod28[8]))
		self.lEditOctProd_28.insert(str(prod28[9]))
		self.lEditNovProd_28.insert(str(prod28[10]))
		self.lEditDecProd_28.insert(str(prod28[11]))

		prod29 = datos.get('prod29')
		self.lEditJanProd_29.insert(str(prod29[0]))
		self.lEditFebProd_29.insert(str(prod29[1]))
		self.lEditMarProd_29.insert(str(prod29[2]))
		self.lEditAprProd_29.insert(str(prod29[3]))
		self.lEditMayProd_29.insert(str(prod29[4]))
		self.lEditJunProd_29.insert(str(prod29[5]))
		self.lEditJulProd_29.insert(str(prod29[6]))
		self.lEditAugProd_29.insert(str(prod29[7]))
		self.lEditSepProd_29.insert(str(prod29[8]))
		self.lEditOctProd_29.insert(str(prod29[9]))
		self.lEditNovProd_29.insert(str(prod29[10]))
		self.lEditDecProd_29.insert(str(prod29[11]))

		prod30 = datos.get('prod30')
		self.lEditJanProd_30.insert(str(prod30[0]))
		self.lEditFebProd_30.insert(str(prod30[1]))
		self.lEditMarProd_30.insert(str(prod30[2]))
		self.lEditAprProd_30.insert(str(prod30[3]))
		self.lEditMayProd_30.insert(str(prod30[4]))
		self.lEditJunProd_30.insert(str(prod30[5]))
		self.lEditJulProd_30.insert(str(prod30[6]))
		self.lEditAugProd_30.insert(str(prod30[7]))
		self.lEditSepProd_30.insert(str(prod30[8]))
		self.lEditOctProd_30.insert(str(prod30[9]))
		self.lEditNovProd_30.insert(str(prod30[10]))
		self.lEditDecProd_30.insert(str(prod30[11]))

		prod31 = datos.get('prod31')
		self.lEditJanProd_31.insert(str(prod31[0]))
		self.lEditFebProd_31.insert(str(prod31[1]))
		self.lEditMarProd_31.insert(str(prod31[2]))
		self.lEditAprProd_31.insert(str(prod31[3]))
		self.lEditMayProd_31.insert(str(prod31[4]))
		self.lEditJunProd_31.insert(str(prod31[5]))
		self.lEditJulProd_31.insert(str(prod31[6]))
		self.lEditAugProd_31.insert(str(prod31[7]))
		self.lEditSepProd_31.insert(str(prod31[8]))
		self.lEditOctProd_31.insert(str(prod31[9]))
		self.lEditNovProd_31.insert(str(prod31[10]))
		self.lEditDecProd_31.insert(str(prod31[11]))

		prod32 = datos.get('prod32')
		self.lEditJanProd_32.insert(str(prod32[0]))
		self.lEditFebProd_32.insert(str(prod32[1]))
		self.lEditMarProd_32.insert(str(prod32[2]))
		self.lEditAprProd_32.insert(str(prod32[3]))
		self.lEditMayProd_32.insert(str(prod32[4]))
		self.lEditJunProd_32.insert(str(prod32[5]))
		self.lEditJulProd_32.insert(str(prod32[6]))
		self.lEditAugProd_32.insert(str(prod32[7]))
		self.lEditSepProd_32.insert(str(prod32[8]))
		self.lEditOctProd_32.insert(str(prod32[9]))
		self.lEditNovProd_32.insert(str(prod32[10]))
		self.lEditDecProd_32.insert(str(prod32[11]))

		prod33 = datos.get('prod33')
		self.lEditJanProd_33.insert(str(prod33[0]))
		self.lEditFebProd_33.insert(str(prod33[1]))
		self.lEditMarProd_33.insert(str(prod33[2]))
		self.lEditAprProd_33.insert(str(prod33[3]))
		self.lEditMayProd_33.insert(str(prod33[4]))
		self.lEditJunProd_33.insert(str(prod33[5]))
		self.lEditJulProd_33.insert(str(prod33[6]))
		self.lEditAugProd_33.insert(str(prod33[7]))
		self.lEditSepProd_33.insert(str(prod33[8]))
		self.lEditOctProd_33.insert(str(prod33[9]))
		self.lEditNovProd_33.insert(str(prod33[10]))
		self.lEditDecProd_33.insert(str(prod33[11]))

		prod34 = datos.get('prod34')
		self.lEditJanProd_34.insert(str(prod34[0]))
		self.lEditFebProd_34.insert(str(prod34[1]))
		self.lEditMarProd_34.insert(str(prod34[2]))
		self.lEditAprProd_34.insert(str(prod34[3]))
		self.lEditMayProd_34.insert(str(prod34[4]))
		self.lEditJunProd_34.insert(str(prod34[5]))
		self.lEditJulProd_34.insert(str(prod34[6]))
		self.lEditAugProd_34.insert(str(prod34[7]))
		self.lEditSepProd_34.insert(str(prod34[8]))
		self.lEditOctProd_34.insert(str(prod34[9]))
		self.lEditNovProd_34.insert(str(prod34[10]))
		self.lEditDecProd_34.insert(str(prod34[11]))

		self.unlock_fields()

	def issue_keys(self):
		"""
		This function generate the keys for the dictionary
		"""
		self.KeyJan = str(self.selected_year) + str(self.table)+'jan'
		self.KeyFeb = str(self.selected_year) + str(self.table)+'feb'
		self.KeyMar = str(self.selected_year) + str(self.table)+'mar'
		self.KeyApr = str(self.selected_year) + str(self.table)+'apr'
		self.KeyMay = str(self.selected_year) + str(self.table)+'may'
		self.KeyJun = str(self.selected_year) + str(self.table)+'jun'
		self.KeyJul = str(self.selected_year) + str(self.table)+'jul'
		self.KeyAug = str(self.selected_year) + str(self.table)+'aug'
		self.KeySep = str(self.selected_year) + str(self.table)+'sep'
		self.KeyOct = str(self.selected_year) + str(self.table)+'oct'
		self.KeyNov = str(self.selected_year) + str(self.table)+'nov'
		self.KeyDec = str(self.selected_year) + str(self.table)+'dec'
		
		list_keys = [self.KeyJan, self.KeyFeb, self.KeyMar, self.KeyApr, 
			self.KeyMay, self.KeyJun, self.KeyJul, self.KeyAug, 
			self.KeySep, self.KeyOct, self.KeyNov, self.KeyDec]
		return list_keys
		
	def genera_archivo_csv(self, list_keys,year):
		"""
		this function generates the CSV file with the input data
		"""
		data = {}
		data_dict = {}
		for sequence, values in enumerate(list_keys):
			if values.find('jan')>0:
				indice = values
				month = 'January'
				prod = self.Jan_Prod
				prod_2 = self.Jan_Prod_2
				prod_3 = self.Jan_Prod_3
				prod_4 = self.Jan_Prod_4
				prod_5 = self.Jan_Prod_5
				prod_6 = self.Jan_Prod_6
				prod_7 = self.Jan_Prod_7
				prod_8 = self.Jan_Prod_8
				prod_9 = self.Jan_Prod_9
				prod_10 = self.Jan_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

				
			elif values.find('feb')>0: 
				indice = values
				month = 'February'
				prod = self.Feb_Prod
				prod_2 = self.Feb_Prod_2
				prod_3 = self.Feb_Prod_3
				prod_4 = self.Feb_Prod_4
				prod_5 = self.Feb_Prod_5
				prod_6 = self.Feb_Prod_6
				prod_7 = self.Feb_Prod_7
				prod_8 = self.Feb_Prod_8
				prod_9 = self.Feb_Prod_9
				prod_10 = self.Feb_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

			elif values.find('mar')>0: 
				indice = values
				month = 'March'
				prod = self.Mar_Prod
				prod_2 = self.Mar_Prod_2
				prod_3 = self.Mar_Prod_3
				prod_4 = self.Mar_Prod_4
				prod_5 = self.Mar_Prod_5
				prod_6 = self.Mar_Prod_6
				prod_7 = self.Mar_Prod_7
				prod_8 = self.Mar_Prod_8
				prod_9 = self.Mar_Prod_9
				prod_10 = self.Mar_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

			elif values.find('apr')>0: 
				indice = values
				month = 'April'
				prod = self.Apr_Prod
				prod_2 = self.Apr_Prod_2
				prod_3 = self.Apr_Prod_3
				prod_4 = self.Apr_Prod_4
				prod_5 = self.Apr_Prod_5
				prod_6 = self.Apr_Prod_6
				prod_7 = self.Apr_Prod_7
				prod_8 = self.Apr_Prod_8
				prod_9 = self.Apr_Prod_9
				prod_10 = self.Apr_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

			elif values.find('may')>0: 
				indice = values
				month = 'May'
				prod = self.May_Prod
				prod_2 = self.May_Prod_2
				prod_3 = self.May_Prod_3
				prod_4 = self.May_Prod_4
				prod_5 = self.May_Prod_5
				prod_6 = self.May_Prod_6
				prod_7 = self.May_Prod_7
				prod_8 = self.May_Prod_8
				prod_9 = self.May_Prod_9
				prod_10 = self.May_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
				
			elif values.find('jun')>0: 
				indice = values
				month = 'June'
				prod = self.Jun_Prod
				prod_2 = self.Jun_Prod_2
				prod_3 = self.Jun_Prod_3
				prod_4 = self.Jun_Prod_4
				prod_5 = self.Jun_Prod_5
				prod_6 = self.Jun_Prod_6
				prod_7 = self.Jun_Prod_7
				prod_8 = self.Jun_Prod_8
				prod_9 = self.Jun_Prod_9
				prod_10 = self.Jun_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

			elif values.find('jul')>0: 
				indice = values
				month = 'July'
				prod = self.Jul_Prod
				prod_2 = self.Jul_Prod_2
				prod_3 = self.Jul_Prod_3
				prod_4 = self.Jul_Prod_4
				prod_5 = self.Jul_Prod_5
				prod_6 = self.Jul_Prod_6
				prod_7 = self.Jul_Prod_7
				prod_8 = self.Jul_Prod_8
				prod_9 = self.Jul_Prod_9
				prod_10 = self.Jul_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
				
			elif values.find('aug')>0: 
				indice = values
				month = 'August'
				prod = self.Aug_Prod
				prod_2 = self.Aug_Prod_2
				prod_3 = self.Aug_Prod_3
				prod_4 = self.Aug_Prod_4
				prod_5 = self.Aug_Prod_5
				prod_6 = self.Aug_Prod_6
				prod_7 = self.Aug_Prod_7
				prod_8 = self.Aug_Prod_8
				prod_9 = self.Aug_Prod_9
				prod_10 = self.Aug_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
								
			elif values.find('sep')>0: 
				indice = values
				month = 'September'
				prod = self.Sep_Prod
				prod_2 = self.Sep_Prod_2
				prod_3 = self.Sep_Prod_3
				prod_4 = self.Sep_Prod_4
				prod_5 = self.Sep_Prod_5
				prod_6 = self.Sep_Prod_6
				prod_7 = self.Sep_Prod_7
				prod_8 = self.Sep_Prod_8
				prod_9 = self.Sep_Prod_9
				prod_10 = self.Sep_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
				
			elif values.find('oct')>0: 
				indice = values
				month = 'October'
				prod = self.Oct_Prod
				prod_2 = self.Oct_Prod_2
				prod_3 = self.Oct_Prod_3
				prod_4 = self.Oct_Prod_4
				prod_5 = self.Oct_Prod_5
				prod_6 = self.Oct_Prod_6
				prod_7 = self.Oct_Prod_7
				prod_8 = self.Oct_Prod_8
				prod_9 = self.Oct_Prod_9
				prod_10 = self.Oct_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34

			elif values.find('nov')>0: 
				indice = values
				month = 'November'
				prod = self.Nov_Prod
				prod_2 = self.Nov_Prod_2
				prod_3 = self.Nov_Prod_3
				prod_4 = self.Nov_Prod_4
				prod_5 = self.Nov_Prod_5
				prod_6 = self.Nov_Prod_6
				prod_7 = self.Nov_Prod_7
				prod_8 = self.Nov_Prod_8
				prod_9 = self.Nov_Prod_9
				prod_10 = self.Nov_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
				
			elif values.find('dec')>0: 
				indice = values
				month = 'December'
				prod = self.Dec_Prod
				prod_2 = self.Dec_Prod_2
				prod_3 = self.Dec_Prod_3
				prod_4 = self.Dec_Prod_4
				prod_5 = self.Dec_Prod_5
				prod_6 = self.Dec_Prod_6
				prod_7 = self.Dec_Prod_7
				prod_8 = self.Dec_Prod_8
				prod_9 = self.Dec_Prod_9
				prod_10 = self.Dec_Prod_10
				prod_11 = self.Jan_Prod_11
				prod_12 = self.Jan_Prod_12
				prod_13 = self.Jan_Prod_13
				prod_14 = self.Jan_Prod_14
				prod_15 = self.Jan_Prod_15
				prod_16 = self.Jan_Prod_16
				prod_17 = self.Jan_Prod_17
				prod_18 = self.Jan_Prod_18
				prod_19 = self.Jan_Prod_19
				prod_20 = self.Jan_Prod_20
				prod_21 = self.Jan_Prod_21
				prod_22 = self.Jan_Prod_22
				prod_23 = self.Jan_Prod_23
				prod_24 = self.Jan_Prod_24
				prod_25 = self.Jan_Prod_25
				prod_26 = self.Jan_Prod_26
				prod_27 = self.Jan_Prod_27
				prod_28 = self.Jan_Prod_28
				prod_29 = self.Jan_Prod_29
				prod_30 = self.Jan_Prod_30
				prod_31 = self.Jan_Prod_31
				prod_32 = self.Jan_Prod_32
				prod_33 = self.Jan_Prod_33
				prod_34 = self.Jan_Prod_34
				
		
				
				
			data = {values : [ sequence, indice, year, month, prod, prod_2, prod_3, prod_4,
					prod_5, prod_6, prod_7, prod_8, prod_9, prod_10,
					prod_11, prod_12, prod_13, prod_14, prod_15,
					prod_16, prod_17, prod_18, prod_19, prod_20,
					prod_21, prod_22, prod_23, prod_24, prod_25,
					prod_26, prod_27, prod_28, prod_29, prod_30,
					prod_31, prod_32, prod_33, prod_34]}
			data_dict.update(data)
			

		message = 'Now we are going to save the file'
		self.caja_mensaje('Save data;', message,0)
		datos =pd.read_csv('esasales.csv', index_col = 0, encoding = 'utf-8')
		datos.apply(lambda x: pd.lib.infer_dtype(x.values))
		num_datos = int(datos['indice'].count())
		datos.index = range(datos.shape[0])
		indice_archivo = list(datos.indice)
		llaves = data_dict.keys()
		nuevo_Valor = num_datos+1
		valores = list(data_dict.values())
		print(valores)
			
		for i, valor in enumerate(valores):
			nuevo_valor = int(nuevo_Valor)+i
			print(nuevo_valor, i, valor)
			datos.loc[int(nuevo_valor)]= [
				valor[1], valor[2], valor[3], valor[4], valor[5],
				valor[6], valor[7], valor[8], valor[9], valor[10],
				valor[11], valor[12], valor[13], valor[14], valor[15], 
				valor[16], valor[17], valor[18], valor[19], valor[20], 
				valor[21], valor[22], valor[23], valor[24], valor[25], 
				valor[26], valor[27], valor[28], valor[29], valor[30], 
				valor[31], valor[32], valor[33], valor[34], valor[35], 
				valor[36], valor[37]]
		try: 
			datos.to_csv('esasales.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
		
	

	def read_data_from_fields(self):

		self.Jan_Prod = float(self.lEditJanProd.text())
		self.Feb_Prod = float(self.lEditFebProd.text())
		self.Mar_Prod = float(self.lEditMarProd.text())
		self.Apr_Prod = float(self.lEditAprProd.text())
		self.May_Prod = float(self.lEditMayProd.text())
		self.Jun_Prod = float(self.lEditJunProd.text())
		self.Jul_Prod = float(self.lEditJulProd.text())
		self.Aug_Prod = float(self.lEditAugProd.text())
		self.Sep_Prod = float(self.lEditSepProd.text())
		self.Oct_Prod = float(self.lEditOctProd.text())
		self.Nov_Prod = float(self.lEditNovProd.text())
		self.Dec_Prod = float(self.lEditDecProd.text())

		self.Jan_Prod_2 = float(self.lEditJanProd_2.text())
		self.Feb_Prod_2 = float(self.lEditFebProd_2.text())
		self.Mar_Prod_2 = float(self.lEditMarProd_2.text())
		self.Apr_Prod_2 = float(self.lEditAprProd_2.text())
		self.May_Prod_2 = float(self.lEditMayProd_2.text())
		self.Jun_Prod_2 = float(self.lEditJunProd_2.text())
		self.Jul_Prod_2 = float(self.lEditJulProd_2.text())
		self.Aug_Prod_2 = float(self.lEditAugProd_2.text())
		self.Sep_Prod_2 = float(self.lEditSepProd_2.text())
		self.Oct_Prod_2 = float(self.lEditOctProd_2.text())
		self.Nov_Prod_2 = float(self.lEditNovProd_2.text())
		self.Dec_Prod_2 = float(self.lEditDecProd_2.text())

		self.Jan_Prod_3 = float(self.lEditJanProd_3.text())
		self.Feb_Prod_3 = float(self.lEditFebProd_3.text())
		self.Mar_Prod_3 = float(self.lEditMarProd_3.text())
		self.Apr_Prod_3 = float(self.lEditAprProd_3.text())
		self.May_Prod_3 = float(self.lEditMayProd_3.text())
		self.Jun_Prod_3 = float(self.lEditJunProd_3.text())
		self.Jul_Prod_3 = float(self.lEditJulProd_3.text())
		self.Aug_Prod_3 = float(self.lEditAugProd_3.text())
		self.Sep_Prod_3 = float(self.lEditSepProd_3.text())
		self.Oct_Prod_3 = float(self.lEditOctProd_3.text())
		self.Nov_Prod_3 = float(self.lEditNovProd_3.text())
		self.Dec_Prod_3 = float(self.lEditDecProd_3.text())

		self.Jan_Prod_4 = float(self.lEditJanProd_4.text())
		self.Feb_Prod_4 = float(self.lEditFebProd_4.text())
		self.Mar_Prod_4 = float(self.lEditMarProd_4.text())
		self.Apr_Prod_4 = float(self.lEditAprProd_4.text())
		self.May_Prod_4 = float(self.lEditMayProd_4.text())
		self.Jun_Prod_4 = float(self.lEditJunProd_4.text())
		self.Jul_Prod_4 = float(self.lEditJulProd_4.text())
		self.Aug_Prod_4 = float(self.lEditAugProd_4.text())
		self.Sep_Prod_4 = float(self.lEditSepProd_4.text())
		self.Oct_Prod_4 = float(self.lEditOctProd_4.text())
		self.Nov_Prod_4 = float(self.lEditNovProd_4.text())
		self.Dec_Prod_4 = float(self.lEditDecProd_4.text())

		self.Jan_Prod_5 = float(self.lEditJanProd_5.text())
		self.Feb_Prod_5 = float(self.lEditFebProd_5.text())
		self.Mar_Prod_5 = float(self.lEditMarProd_5.text())
		self.Apr_Prod_5 = float(self.lEditAprProd_5.text())
		self.May_Prod_5 = float(self.lEditMayProd_5.text())
		self.Jun_Prod_5 = float(self.lEditJunProd_5.text())
		self.Jul_Prod_5 = float(self.lEditJulProd_5.text())
		self.Aug_Prod_5 = float(self.lEditAugProd_5.text())
		self.Sep_Prod_5 = float(self.lEditSepProd_5.text())
		self.Oct_Prod_5 = float(self.lEditOctProd_5.text())
		self.Nov_Prod_5 = float(self.lEditNovProd_5.text())
		self.Dec_Prod_5 = float(self.lEditDecProd_5.text())

		self.Jan_Prod_6 = float(self.lEditJanProd_6.text())
		self.Feb_Prod_6 = float(self.lEditFebProd_6.text())
		self.Mar_Prod_6 = float(self.lEditMarProd_6.text())
		self.Apr_Prod_6 = float(self.lEditAprProd_6.text())
		self.May_Prod_6 = float(self.lEditMayProd_6.text())
		self.Jun_Prod_6 = float(self.lEditJunProd_6.text())
		self.Jul_Prod_6 = float(self.lEditJulProd_6.text())
		self.Aug_Prod_6 = float(self.lEditAugProd_6.text())
		self.Sep_Prod_6 = float(self.lEditSepProd_6.text())
		self.Oct_Prod_6 = float(self.lEditOctProd_6.text())
		self.Nov_Prod_6 = float(self.lEditNovProd_6.text())
		self.Dec_Prod_6 = float(self.lEditDecProd_6.text())

		self.Jan_Prod_7 = float(self.lEditJanProd_7.text())
		self.Feb_Prod_7 = float(self.lEditFebProd_7.text())
		self.Mar_Prod_7 = float(self.lEditMarProd_7.text())
		self.Apr_Prod_7 = float(self.lEditAprProd_7.text())
		self.May_Prod_7 = float(self.lEditMayProd_7.text())
		self.Jun_Prod_7 = float(self.lEditJunProd_7.text())
		self.Jul_Prod_7 = float(self.lEditJulProd_7.text())
		self.Aug_Prod_7 = float(self.lEditAugProd_7.text())
		self.Sep_Prod_7 = float(self.lEditSepProd_7.text())
		self.Oct_Prod_7 = float(self.lEditOctProd_7.text())
		self.Nov_Prod_7 = float(self.lEditNovProd_7.text())
		self.Dec_Prod_7 = float(self.lEditDecProd_7.text())

		self.Jan_Prod_8 = float(self.lEditJanProd_8.text())
		self.Feb_Prod_8 = float(self.lEditFebProd_8.text())
		self.Mar_Prod_8 = float(self.lEditMarProd_8.text())
		self.Apr_Prod_8 = float(self.lEditAprProd_8.text())
		self.May_Prod_8 = float(self.lEditMayProd_8.text())
		self.Jun_Prod_8 = float(self.lEditJunProd_8.text())
		self.Jul_Prod_8 = float(self.lEditJulProd_8.text())
		self.Aug_Prod_8 = float(self.lEditAugProd_8.text())
		self.Sep_Prod_8 = float(self.lEditSepProd_8.text())
		self.Oct_Prod_8 = float(self.lEditOctProd_8.text())
		self.Nov_Prod_8 = float(self.lEditNovProd_8.text())
		self.Dec_Prod_8 = float(self.lEditDecProd_8.text())

		self.Jan_Prod_9 = float(self.lEditJanProd_9.text())
		self.Feb_Prod_9 = float(self.lEditFebProd_9.text())
		self.Mar_Prod_9 = float(self.lEditMarProd_9.text())
		self.Apr_Prod_9 = float(self.lEditAprProd_9.text())
		self.May_Prod_9 = float(self.lEditMayProd_9.text())
		self.Jun_Prod_9 = float(self.lEditJunProd_9.text())
		self.Jul_Prod_9 = float(self.lEditJulProd_9.text())
		self.Aug_Prod_9 = float(self.lEditAugProd_9.text())
		self.Sep_Prod_9 = float(self.lEditSepProd_9.text())
		self.Oct_Prod_9 = float(self.lEditOctProd_9.text())
		self.Nov_Prod_9 = float(self.lEditNovProd_9.text())
		self.Dec_Prod_9 = float(self.lEditDecProd_9.text())

		self.Jan_Prod_10 = float(self.lEditJanProd_10.text())
		self.Feb_Prod_10 = float(self.lEditFebProd_10.text())
		self.Mar_Prod_10 = float(self.lEditMarProd_10.text())
		self.Apr_Prod_10 = float(self.lEditAprProd_10.text())
		self.May_Prod_10 = float(self.lEditMayProd_10.text())
		self.Jun_Prod_10 = float(self.lEditJunProd_10.text())
		self.Jul_Prod_10 = float(self.lEditJulProd_10.text())
		self.Aug_Prod_10 = float(self.lEditAugProd_10.text())
		self.Sep_Prod_10 = float(self.lEditSepProd_10.text())
		self.Oct_Prod_10 = float(self.lEditOctProd_10.text())
		self.Nov_Prod_10 = float(self.lEditNovProd_10.text())
		self.Dec_Prod_10 = float(self.lEditDecProd_10.text())

		self.Jan_Prod_11 = float(self.lEditJanProd_11.text())
		self.Feb_Prod_11 = float(self.lEditFebProd_11.text())
		self.Mar_Prod_11 = float(self.lEditMarProd_11.text())
		self.Apr_Prod_11 = float(self.lEditAprProd_11.text())
		self.May_Prod_11 = float(self.lEditMayProd_11.text())
		self.Jun_Prod_11 = float(self.lEditJunProd_11.text())
		self.Jul_Prod_11 = float(self.lEditJulProd_11.text())
		self.Aug_Prod_11 = float(self.lEditAugProd_11.text())
		self.Sep_Prod_11 = float(self.lEditSepProd_11.text())
		self.Oct_Prod_11 = float(self.lEditOctProd_11.text())
		self.Nov_Prod_11 = float(self.lEditNovProd_11.text())
		self.Dec_Prod_11 = float(self.lEditDecProd_11.text())

		self.Jan_Prod_12 = float(self.lEditJanProd_12.text())
		self.Feb_Prod_12 = float(self.lEditFebProd_12.text())
		self.Mar_Prod_12 = float(self.lEditMarProd_12.text())
		self.Apr_Prod_12 = float(self.lEditAprProd_12.text())
		self.May_Prod_12 = float(self.lEditMayProd_12.text())
		self.Jun_Prod_12 = float(self.lEditJunProd_12.text())
		self.Jul_Prod_12 = float(self.lEditJulProd_12.text())
		self.Aug_Prod_12 = float(self.lEditAugProd_12.text())
		self.Sep_Prod_12 = float(self.lEditSepProd_12.text())
		self.Oct_Prod_12 = float(self.lEditOctProd_12.text())
		self.Nov_Prod_12 = float(self.lEditNovProd_12.text())
		self.Dec_Prod_12 = float(self.lEditDecProd_12.text())

		self.Jan_Prod_13 = float(self.lEditJanProd_13.text())
		self.Feb_Prod_13 = float(self.lEditFebProd_13.text())
		self.Mar_Prod_13 = float(self.lEditMarProd_13.text())
		self.Apr_Prod_13 = float(self.lEditAprProd_13.text())
		self.May_Prod_13 = float(self.lEditMayProd_13.text())
		self.Jun_Prod_13 = float(self.lEditJunProd_13.text())
		self.Jul_Prod_13 = float(self.lEditJulProd_13.text())
		self.Aug_Prod_13 = float(self.lEditAugProd_13.text())
		self.Sep_Prod_13 = float(self.lEditSepProd_13.text())
		self.Oct_Prod_13 = float(self.lEditOctProd_13.text())
		self.Nov_Prod_13 = float(self.lEditNovProd_13.text())
		self.Dec_Prod_13 = float(self.lEditDecProd_13.text())

		self.Jan_Prod_14 = float(self.lEditJanProd_14.text())
		self.Feb_Prod_14 = float(self.lEditFebProd_14.text())
		self.Mar_Prod_14 = float(self.lEditMarProd_14.text())
		self.Apr_Prod_14 = float(self.lEditAprProd_14.text())
		self.May_Prod_14 = float(self.lEditMayProd_14.text())
		self.Jun_Prod_14 = float(self.lEditJunProd_14.text())
		self.Jul_Prod_14 = float(self.lEditJulProd_14.text())
		self.Aug_Prod_14 = float(self.lEditAugProd_14.text())
		self.Sep_Prod_14 = float(self.lEditSepProd_14.text())
		self.Oct_Prod_14 = float(self.lEditOctProd_14.text())
		self.Nov_Prod_14 = float(self.lEditNovProd_14.text())
		self.Dec_Prod_14 = float(self.lEditDecProd_14.text())

		self.Jan_Prod_15 = float(self.lEditJanProd_15.text())
		self.Feb_Prod_15 = float(self.lEditFebProd_15.text())
		self.Mar_Prod_15 = float(self.lEditMarProd_15.text())
		self.Apr_Prod_15 = float(self.lEditAprProd_15.text())
		self.May_Prod_15 = float(self.lEditMayProd_15.text())
		self.Jun_Prod_15 = float(self.lEditJunProd_15.text())
		self.Jul_Prod_15 = float(self.lEditJulProd_15.text())
		self.Aug_Prod_15 = float(self.lEditAugProd_15.text())
		self.Sep_Prod_15 = float(self.lEditSepProd_15.text())
		self.Oct_Prod_15 = float(self.lEditOctProd_15.text())
		self.Nov_Prod_15 = float(self.lEditNovProd_15.text())
		self.Dec_Prod_15 = float(self.lEditDecProd_15.text())

		self.Jan_Prod_16 = float(self.lEditJanProd_16.text())
		self.Feb_Prod_16 = float(self.lEditFebProd_16.text())
		self.Mar_Prod_16 = float(self.lEditMarProd_16.text())
		self.Apr_Prod_16 = float(self.lEditAprProd_16.text())
		self.May_Prod_16 = float(self.lEditMayProd_16.text())
		self.Jun_Prod_16 = float(self.lEditJunProd_16.text())
		self.Jul_Prod_16 = float(self.lEditJulProd_16.text())
		self.Aug_Prod_16 = float(self.lEditAugProd_16.text())
		self.Sep_Prod_16 = float(self.lEditSepProd_16.text())
		self.Oct_Prod_16 = float(self.lEditOctProd_16.text())
		self.Nov_Prod_16 = float(self.lEditNovProd_16.text())
		self.Dec_Prod_16 = float(self.lEditDecProd_16.text())

		self.Jan_Prod_17 = float(self.lEditJanProd_17.text())
		self.Feb_Prod_17 = float(self.lEditFebProd_17.text())
		self.Mar_Prod_17 = float(self.lEditMarProd_17.text())
		self.Apr_Prod_17 = float(self.lEditAprProd_17.text())
		self.May_Prod_17 = float(self.lEditMayProd_17.text())
		self.Jun_Prod_17 = float(self.lEditJunProd_17.text())
		self.Jul_Prod_17 = float(self.lEditJulProd_17.text())
		self.Aug_Prod_17 = float(self.lEditAugProd_17.text())
		self.Sep_Prod_17 = float(self.lEditSepProd_17.text())
		self.Oct_Prod_17 = float(self.lEditOctProd_17.text())
		self.Nov_Prod_17 = float(self.lEditNovProd_17.text())
		self.Dec_Prod_17 = float(self.lEditDecProd_17.text())

		self.Jan_Prod_18 = float(self.lEditJanProd_18.text())
		self.Feb_Prod_18 = float(self.lEditFebProd_18.text())
		self.Mar_Prod_18 = float(self.lEditMarProd_18.text())
		self.Apr_Prod_18 = float(self.lEditAprProd_18.text())
		self.May_Prod_18 = float(self.lEditMayProd_18.text())
		self.Jun_Prod_18 = float(self.lEditJunProd_18.text())
		self.Jul_Prod_18 = float(self.lEditJulProd_18.text())
		self.Aug_Prod_18 = float(self.lEditAugProd_18.text())
		self.Sep_Prod_18 = float(self.lEditSepProd_18.text())
		self.Oct_Prod_18 = float(self.lEditOctProd_18.text())
		self.Nov_Prod_18 = float(self.lEditNovProd_18.text())
		self.Dec_Prod_18 = float(self.lEditDecProd_18.text())

		self.Jan_Prod_19 = float(self.lEditJanProd_19.text())
		self.Feb_Prod_19 = float(self.lEditFebProd_19.text())
		self.Mar_Prod_19 = float(self.lEditMarProd_19.text())
		self.Apr_Prod_19 = float(self.lEditAprProd_19.text())
		self.May_Prod_19 = float(self.lEditMayProd_19.text())
		self.Jun_Prod_19 = float(self.lEditJunProd_19.text())
		self.Jul_Prod_19 = float(self.lEditJulProd_19.text())
		self.Aug_Prod_19 = float(self.lEditAugProd_19.text())
		self.Sep_Prod_19 = float(self.lEditSepProd_19.text())
		self.Oct_Prod_19 = float(self.lEditOctProd_19.text())
		self.Nov_Prod_19 = float(self.lEditNovProd_19.text())
		self.Dec_Prod_19 = float(self.lEditDecProd_19.text())

		self.Jan_Prod_20 = float(self.lEditJanProd_20.text())
		self.Feb_Prod_20 = float(self.lEditFebProd_20.text())
		self.Mar_Prod_20 = float(self.lEditMarProd_20.text())
		self.Apr_Prod_20 = float(self.lEditAprProd_20.text())
		self.May_Prod_20 = float(self.lEditMayProd_20.text())
		self.Jun_Prod_20 = float(self.lEditJunProd_20.text())
		self.Jul_Prod_20 = float(self.lEditJulProd_20.text())
		self.Aug_Prod_20 = float(self.lEditAugProd_20.text())
		self.Sep_Prod_20 = float(self.lEditSepProd_20.text())
		self.Oct_Prod_20 = float(self.lEditOctProd_20.text())
		self.Nov_Prod_20 = float(self.lEditNovProd_20.text())
		self.Dec_Prod_20 = float(self.lEditDecProd_20.text())

		self.Jan_Prod_21 = float(self.lEditJanProd_21.text())
		self.Feb_Prod_21 = float(self.lEditFebProd_21.text())
		self.Mar_Prod_21 = float(self.lEditMarProd_21.text())
		self.Apr_Prod_21 = float(self.lEditAprProd_21.text())
		self.May_Prod_21 = float(self.lEditMayProd_21.text())
		self.Jun_Prod_21 = float(self.lEditJunProd_21.text())
		self.Jul_Prod_21 = float(self.lEditJulProd_21.text())
		self.Aug_Prod_21 = float(self.lEditAugProd_21.text())
		self.Sep_Prod_21 = float(self.lEditSepProd_21.text())
		self.Oct_Prod_21 = float(self.lEditOctProd_21.text())
		self.Nov_Prod_21 = float(self.lEditNovProd_21.text())
		self.Dec_Prod_21 = float(self.lEditDecProd_21.text())

		self.Jan_Prod_22 = float(self.lEditJanProd_22.text())
		self.Feb_Prod_22 = float(self.lEditFebProd_22.text())
		self.Mar_Prod_22 = float(self.lEditMarProd_22.text())
		self.Apr_Prod_22 = float(self.lEditAprProd_22.text())
		self.May_Prod_22 = float(self.lEditMayProd_22.text())
		self.Jun_Prod_22 = float(self.lEditJunProd_22.text())
		self.Jul_Prod_22 = float(self.lEditJulProd_22.text())
		self.Aug_Prod_22 = float(self.lEditAugProd_22.text())
		self.Sep_Prod_22 = float(self.lEditSepProd_22.text())
		self.Oct_Prod_22 = float(self.lEditOctProd_22.text())
		self.Nov_Prod_22 = float(self.lEditNovProd_22.text())
		self.Dec_Prod_22 = float(self.lEditDecProd_22.text())

		self.Jan_Prod_23 = float(self.lEditJanProd_23.text())
		self.Feb_Prod_23 = float(self.lEditFebProd_23.text())
		self.Mar_Prod_23 = float(self.lEditMarProd_23.text())
		self.Apr_Prod_23 = float(self.lEditAprProd_23.text())
		self.May_Prod_23 = float(self.lEditMayProd_23.text())
		self.Jun_Prod_23 = float(self.lEditJunProd_23.text())
		self.Jul_Prod_23 = float(self.lEditJulProd_23.text())
		self.Aug_Prod_23 = float(self.lEditAugProd_23.text())
		self.Sep_Prod_23 = float(self.lEditSepProd_23.text())
		self.Oct_Prod_23 = float(self.lEditOctProd_23.text())
		self.Nov_Prod_23 = float(self.lEditNovProd_23.text())
		self.Dec_Prod_23 = float(self.lEditDecProd_23.text())

		self.Jan_Prod_24 = float(self.lEditJanProd_24.text())
		self.Feb_Prod_24 = float(self.lEditFebProd_24.text())
		self.Mar_Prod_24 = float(self.lEditMarProd_24.text())
		self.Apr_Prod_24 = float(self.lEditAprProd_24.text())
		self.May_Prod_24 = float(self.lEditMayProd_24.text())
		self.Jun_Prod_24 = float(self.lEditJunProd_24.text())
		self.Jul_Prod_24 = float(self.lEditJulProd_24.text())
		self.Aug_Prod_24 = float(self.lEditAugProd_24.text())
		self.Sep_Prod_24 = float(self.lEditSepProd_24.text())
		self.Oct_Prod_24 = float(self.lEditOctProd_24.text())
		self.Nov_Prod_24 = float(self.lEditNovProd_24.text())
		self.Dec_Prod_24 = float(self.lEditDecProd_24.text())

		self.Jan_Prod_25 = float(self.lEditJanProd_25.text())
		self.Feb_Prod_25 = float(self.lEditFebProd_25.text())
		self.Mar_Prod_25 = float(self.lEditMarProd_25.text())
		self.Apr_Prod_25 = float(self.lEditAprProd_25.text())
		self.May_Prod_25 = float(self.lEditMayProd_25.text())
		self.Jun_Prod_25 = float(self.lEditJunProd_25.text())
		self.Jul_Prod_25 = float(self.lEditJulProd_25.text())
		self.Aug_Prod_25 = float(self.lEditAugProd_25.text())
		self.Sep_Prod_25 = float(self.lEditSepProd_25.text())
		self.Oct_Prod_25 = float(self.lEditOctProd_25.text())
		self.Nov_Prod_25 = float(self.lEditNovProd_25.text())
		self.Dec_Prod_25 = float(self.lEditDecProd_25.text())

		self.Jan_Prod_26 = float(self.lEditJanProd_26.text())
		self.Feb_Prod_26 = float(self.lEditFebProd_26.text())
		self.Mar_Prod_26 = float(self.lEditMarProd_26.text())
		self.Apr_Prod_26 = float(self.lEditAprProd_26.text())
		self.May_Prod_26 = float(self.lEditMayProd_26.text())
		self.Jun_Prod_26 = float(self.lEditJunProd_26.text())
		self.Jul_Prod_26 = float(self.lEditJulProd_26.text())
		self.Aug_Prod_26 = float(self.lEditAugProd_26.text())
		self.Sep_Prod_26 = float(self.lEditSepProd_26.text())
		self.Oct_Prod_26 = float(self.lEditOctProd_26.text())
		self.Nov_Prod_26 = float(self.lEditNovProd_26.text())
		self.Dec_Prod_26 = float(self.lEditDecProd_26.text())

		self.Jan_Prod_27 = float(self.lEditJanProd_27.text())
		self.Feb_Prod_27 = float(self.lEditFebProd_27.text())
		self.Mar_Prod_27 = float(self.lEditMarProd_27.text())
		self.Apr_Prod_27 = float(self.lEditAprProd_27.text())
		self.May_Prod_27 = float(self.lEditMayProd_27.text())
		self.Jun_Prod_27 = float(self.lEditJunProd_27.text())
		self.Jul_Prod_27 = float(self.lEditJulProd_27.text())
		self.Aug_Prod_27 = float(self.lEditAugProd_27.text())
		self.Sep_Prod_27 = float(self.lEditSepProd_27.text())
		self.Oct_Prod_27 = float(self.lEditOctProd_27.text())
		self.Nov_Prod_27 = float(self.lEditNovProd_27.text())
		self.Dec_Prod_27 = float(self.lEditDecProd_27.text())

		self.Jan_Prod_28 = float(self.lEditJanProd_28.text())
		self.Feb_Prod_28 = float(self.lEditFebProd_28.text())
		self.Mar_Prod_28 = float(self.lEditMarProd_28.text())
		self.Apr_Prod_28 = float(self.lEditAprProd_28.text())
		self.May_Prod_28 = float(self.lEditMayProd_28.text())
		self.Jun_Prod_28 = float(self.lEditJunProd_28.text())
		self.Jul_Prod_28 = float(self.lEditJulProd_28.text())
		self.Aug_Prod_28 = float(self.lEditAugProd_28.text())
		self.Sep_Prod_28 = float(self.lEditSepProd_28.text())
		self.Oct_Prod_28 = float(self.lEditOctProd_28.text())
		self.Nov_Prod_28 = float(self.lEditNovProd_28.text())
		self.Dec_Prod_28 = float(self.lEditDecProd_28.text())

		self.Jan_Prod_29 = float(self.lEditJanProd_29.text())
		self.Feb_Prod_29 = float(self.lEditFebProd_29.text())
		self.Mar_Prod_29 = float(self.lEditMarProd_29.text())
		self.Apr_Prod_29 = float(self.lEditAprProd_29.text())
		self.May_Prod_29 = float(self.lEditMayProd_29.text())
		self.Jun_Prod_29 = float(self.lEditJunProd_29.text())
		self.Jul_Prod_29 = float(self.lEditJulProd_29.text())
		self.Aug_Prod_29 = float(self.lEditAugProd_29.text())
		self.Sep_Prod_29 = float(self.lEditSepProd_29.text())
		self.Oct_Prod_29 = float(self.lEditOctProd_29.text())
		self.Nov_Prod_29 = float(self.lEditNovProd_29.text())
		self.Dec_Prod_29 = float(self.lEditDecProd_29.text())

		self.Jan_Prod_30 = float(self.lEditJanProd_30.text())
		self.Feb_Prod_30 = float(self.lEditFebProd_30.text())
		self.Mar_Prod_30 = float(self.lEditMarProd_30.text())
		self.Apr_Prod_30 = float(self.lEditAprProd_30.text())
		self.May_Prod_30 = float(self.lEditMayProd_30.text())
		self.Jun_Prod_30 = float(self.lEditJunProd_30.text())
		self.Jul_Prod_30 = float(self.lEditJulProd_30.text())
		self.Aug_Prod_30 = float(self.lEditAugProd_30.text())
		self.Sep_Prod_30 = float(self.lEditSepProd_30.text())
		self.Oct_Prod_30 = float(self.lEditOctProd_30.text())
		self.Nov_Prod_30 = float(self.lEditNovProd_30.text())
		self.Dec_Prod_30 = float(self.lEditDecProd_30.text())

		self.Jan_Prod_31 = float(self.lEditJanProd_31.text())
		self.Feb_Prod_31 = float(self.lEditFebProd_31.text())
		self.Mar_Prod_31 = float(self.lEditMarProd_31.text())
		self.Apr_Prod_31 = float(self.lEditAprProd_31.text())
		self.May_Prod_31 = float(self.lEditMayProd_31.text())
		self.Jun_Prod_31 = float(self.lEditJunProd_31.text())
		self.Jul_Prod_31 = float(self.lEditJulProd_31.text())
		self.Aug_Prod_31 = float(self.lEditAugProd_31.text())
		self.Sep_Prod_31 = float(self.lEditSepProd_31.text())
		self.Oct_Prod_31 = float(self.lEditOctProd_31.text())
		self.Nov_Prod_31 = float(self.lEditNovProd_31.text())
		self.Dec_Prod_31 = float(self.lEditDecProd_31.text())

		self.Jan_Prod_32 = float(self.lEditJanProd_32.text())
		self.Feb_Prod_32 = float(self.lEditFebProd_32.text())
		self.Mar_Prod_32 = float(self.lEditMarProd_32.text())
		self.Apr_Prod_32 = float(self.lEditAprProd_32.text())
		self.May_Prod_32 = float(self.lEditMayProd_32.text())
		self.Jun_Prod_32 = float(self.lEditJunProd_32.text())
		self.Jul_Prod_32 = float(self.lEditJulProd_32.text())
		self.Aug_Prod_32 = float(self.lEditAugProd_32.text())
		self.Sep_Prod_32 = float(self.lEditSepProd_32.text())
		self.Oct_Prod_32 = float(self.lEditOctProd_32.text())
		self.Nov_Prod_32 = float(self.lEditNovProd_32.text())
		self.Dec_Prod_32 = float(self.lEditDecProd_32.text())

		self.Jan_Prod_33 = float(self.lEditJanProd_33.text())
		self.Feb_Prod_33 = float(self.lEditFebProd_33.text())
		self.Mar_Prod_33 = float(self.lEditMarProd_33.text())
		self.Apr_Prod_33 = float(self.lEditAprProd_33.text())
		self.May_Prod_33 = float(self.lEditMayProd_33.text())
		self.Jun_Prod_33 = float(self.lEditJunProd_33.text())
		self.Jul_Prod_33 = float(self.lEditJulProd_33.text())
		self.Aug_Prod_33 = float(self.lEditAugProd_33.text())
		self.Sep_Prod_33 = float(self.lEditSepProd_33.text())
		self.Oct_Prod_33 = float(self.lEditOctProd_33.text())
		self.Nov_Prod_33 = float(self.lEditNovProd_33.text())
		self.Dec_Prod_33 = float(self.lEditDecProd_33.text())

		self.Jan_Prod_34 = float(self.lEditJanProd_34.text())
		self.Feb_Prod_34 = float(self.lEditFebProd_34.text())
		self.Mar_Prod_34 = float(self.lEditMarProd_34.text())
		self.Apr_Prod_34 = float(self.lEditAprProd_34.text())
		self.May_Prod_34 = float(self.lEditMayProd_34.text())
		self.Jun_Prod_34 = float(self.lEditJunProd_34.text())
		self.Jul_Prod_34 = float(self.lEditJulProd_34.text())
		self.Aug_Prod_34 = float(self.lEditAugProd_34.text())
		self.Sep_Prod_34 = float(self.lEditSepProd_34.text())
		self.Oct_Prod_34 = float(self.lEditOctProd_34.text())
		self.Nov_Prod_34 = float(self.lEditNovProd_34.text())
		self.Dec_Prod_34 = float(self.lEditDecProd_34.text())


	def set_titles(self,list_ingredients):
		self.lblProd.setText(str(list_ingredients[0]))
		self.lblProd_2.setText(str(list_ingredients[1]))
		self.lblProd_3.setText(str(list_ingredients[2]))
		self.lblProd_4.setText(str(list_ingredients[3]))
		self.lblProd_5.setText(str(list_ingredients[4]))
		self.lblProd_6.setText(str(list_ingredients[5]))
		self.lblProd_7.setText(str(list_ingredients[6]))
		self.lblProd_8.setText(str(list_ingredients[7]))
		self.lblProd_9.setText(str(list_ingredients[8]))
		self.lblProd_10.setText(str(list_ingredients[9]))
		self.lblProd_11.setText(str(list_ingredients[10]))
		self.lblProd_12.setText(str(list_ingredients[11]))
		self.lblProd_13.setText(str(list_ingredients[12]))
		self.lblProd_14.setText(str(list_ingredients[13]))
		self.lblProd_15.setText(str(list_ingredients[14]))
		self.lblProd_16.setText(str(list_ingredients[15]))
		self.lblProd_17.setText(str(list_ingredients[16]))
		self.lblProd_18.setText(str(list_ingredients[17]))
		self.lblProd_19.setText(str(list_ingredients[18]))
		self.lblProd_20.setText(str(list_ingredients[19]))
		self.lblProd_21.setText(str(list_ingredients[20]))
		self.lblProd_22.setText(str(list_ingredients[21]))
		self.lblProd_23.setText(str(list_ingredients[22]))
		self.lblProd_24.setText(str(list_ingredients[23]))
		self.lblProd_25.setText(str(list_ingredients[24]))
		self.lblProd_26.setText(str(list_ingredients[25]))
		self.lblProd_27.setText(str(list_ingredients[26]))
		self.lblProd_28.setText(str(list_ingredients[27]))
		self.lblProd_29.setText(str(list_ingredients[28]))
		self.lblProd_30.setText(str(list_ingredients[29]))
		self.lblProd_31.setText(str(list_ingredients[30]))
		self.lblProd_32.setText(str(list_ingredients[31]))
		self.lblProd_33.setText(str(list_ingredients[32]))
		self.lblProd_34.setText(str(list_ingredients[33]))

		for i, valor in enumerate(list_ingredients):
			print(i, valor)
		
	
		
		print(list_ingredients[0] == 'prod')
		print(list_ingredients[1] == 'prod2')
		print(list_ingredients[2] == 'prod3')
		print(list_ingredients[3] == 'prod4')
		print(list_ingredients[4] == 'prod5')
		print(list_ingredients[5] == 'prod6')
		print(list_ingredients[6] == 'prod7')
		print(list_ingredients[7] == 'prod8')
		print(list_ingredients[8] == 'prod9')
		print(list_ingredients[9] == 'prod10')
		print(list_ingredients[10] == 'prod11')
		print(list_ingredients[11] == 'prod12')
		print(list_ingredients[12] == 'prod13')
		print(list_ingredients[13] == 'prod14')
		print(list_ingredients[14] == 'prod15')
		print(list_ingredients[15] == 'prod16')
		print(list_ingredients[16] == 'prod17')
		print(list_ingredients[17] == 'prod18')
		print(list_ingredients[18] == 'prod19')
		print(list_ingredients[19] == 'prod20')
		print(list_ingredients[20] == 'prod21')
		print(list_ingredients[21] == 'prod22')
		print(list_ingredients[22] == 'prod23')
		print(list_ingredients[23] == 'prod24')
		print(list_ingredients[24] == 'prod25')
		print(list_ingredients[25] == 'prod26')
		print(list_ingredients[26] == 'prod27')
		print(list_ingredients[27] == 'prod28')
		print(list_ingredients[28] == 'prod29')
		print(list_ingredients[29] == 'prod30')
		print(list_ingredients[30] == 'prod31')
		print(list_ingredients[31] == 'prod32')
		print(list_ingredients[32] == 'prod33')
		print(list_ingredients[33] == 'prod34')

		"""
		if list_ingredients[0] == 'prod':
			self.lblProd.setVisible(False)
			self.lEditJanProd.setVisible(False)
			self.lEditFebProd.setVisible(False)
			self.lEditMarProd.setVisible(False)
			self.lEditAprProd.setVisible(False)
			self.lEditMayProd.setVisible(False)
			self.lEditJunProd.setVisible(False)
			self.lEditJulProd.setVisible(False)
			self.lEditAugProd.setVisible(False)
			self.lEditSepProd.setVisible(False)
			self.lEditOctProd.setVisible(False)
			self.lEditNovProd.setVisible(False)
			self.lEditDecProd.setVisible(False)
			self.lblTotalAnualProd.setVisible(False)
		else:
			pass
		if list_ingredients[1] == 'prod2':
			self.lblProd_2.setVisible(False)
			self.lEditJanProd_2.setVisible(False)
			self.lEditFebProd_2.setVisible(False)
			self.lEditMarProd_2.setVisible(False)
			self.lEditAprProd_2.setVisible(False)
			self.lEditMayProd_2.setVisible(False)
			self.lEditJunProd_2.setVisible(False)
			self.lEditJulProd_2.setVisible(False)
			self.lEditAugProd_2.setVisible(False)
			self.lEditSepProd_2.setVisible(False)
			self.lEditOctProd_2.setVisible(False)
			self.lEditNovProd_2.setVisible(False)
			self.lEditDecProd_2.setVisible(False)
			self.lblTotalAnualProd_2.setVisible(False)
		else:
			pass
		if list_ingredients[2] == 'prod3':
			self.lblProd_3.setVisible(False)
			self.lEditJanProd_3.setVisible(False)
			self.lEditFebProd_3.setVisible(False)
			self.lEditMarProd_3.setVisible(False)
			self.lEditAprProd_3.setVisible(False)
			self.lEditMayProd_3.setVisible(False)
			self.lEditJunProd_3.setVisible(False)
			self.lEditJulProd_3.setVisible(False)
			self.lEditAugProd_3.setVisible(False)
			self.lEditSepProd_3.setVisible(False)
			self.lEditOctProd_3.setVisible(False)
			self.lEditNovProd_3.setVisible(False)
			self.lEditDecProd_3.setVisible(False)
			self.lblTotalAnualProd_3.setVisible(False)
		else:
			pass
		if list_ingredients[3] == 'prod4':
			self.lblProd_4.setVisible(False)
			self.lEditJanProd_4.setVisible(False)
			self.lEditFebProd_4.setVisible(False)
			self.lEditMarProd_4.setVisible(False)
			self.lEditAprProd_4.setVisible(False)
			self.lEditMayProd_4.setVisible(False)
			self.lEditJunProd_4.setVisible(False)
			self.lEditJulProd_4.setVisible(False)
			self.lEditAugProd_4.setVisible(False)
			self.lEditSepProd_4.setVisible(False)
			self.lEditOctProd_4.setVisible(False)
			self.lEditNovProd_4.setVisible(False)
			self.lEditDecProd_4.setVisible(False)
			self.lblTotalAnualProd_4.setVisible(False)
		else:
			pass
		if list_ingredients[4] == 'prod5':
			self.lblProd_5.setVisible(False)
			self.lEditJanProd_5.setVisible(False)
			self.lEditFebProd_5.setVisible(False)
			self.lEditMarProd_5.setVisible(False)
			self.lEditAprProd_5.setVisible(False)
			self.lEditMayProd_5.setVisible(False)
			self.lEditJunProd_5.setVisible(False)
			self.lEditJulProd_5.setVisible(False)
			self.lEditAugProd_5.setVisible(False)
			self.lEditSepProd_5.setVisible(False)
			self.lEditOctProd_5.setVisible(False)
			self.lEditNovProd_5.setVisible(False)
			self.lEditDecProd_5.setVisible(False)
			self.lblTotalAnualProd_5.setVisible(False)
		else:
			pass
		if list_ingredients[5] == 'prod6':
			self.lblProd_6.setVisible(False)
			self.lEditJanProd_6.setVisible(False)
			self.lEditFebProd_6.setVisible(False)
			self.lEditMarProd_6.setVisible(False)
			self.lEditAprProd_6.setVisible(False)
			self.lEditMayProd_6.setVisible(False)
			self.lEditJunProd_6.setVisible(False)
			self.lEditJulProd_6.setVisible(False)
			self.lEditAugProd_6.setVisible(False)
			self.lEditSepProd_6.setVisible(False)
			self.lEditOctProd_6.setVisible(False)
			self.lEditNovProd_6.setVisible(False)
			self.lEditDecProd_6.setVisible(False)
			self.lblTotalAnualProd_6.setVisible(False)
		else:
			pass
		if list_ingredients[6] == 'prod7':
			self.lblProd_7.setVisible(False)
			self.lEditJanProd_7.setVisible(False)
			self.lEditFebProd_7.setVisible(False)
			self.lEditMarProd_7.setVisible(False)
			self.lEditAprProd_7.setVisible(False)
			self.lEditMayProd_7.setVisible(False)
			self.lEditJunProd_7.setVisible(False)
			self.lEditJulProd_7.setVisible(False)
			self.lEditAugProd_7.setVisible(False)
			self.lEditSepProd_7.setVisible(False)
			self.lEditOctProd_7.setVisible(False)
			self.lEditNovProd_7.setVisible(False)
			self.lEditDecProd_7.setVisible(False)
			self.lblTotalAnualProd_7.setVisible(False)
		else:
			pass
		if list_ingredients[7] == 'prod8':
			self.lblProd_8.setVisible(False)
			self.lEditJanProd_8.setVisible(False)
			self.lEditFebProd_8.setVisible(False)
			self.lEditMarProd_8.setVisible(False)
			self.lEditAprProd_8.setVisible(False)
			self.lEditMayProd_8.setVisible(False)
			self.lEditJunProd_8.setVisible(False)
			self.lEditJulProd_8.setVisible(False)
			self.lEditAugProd_8.setVisible(False)
			self.lEditSepProd_8.setVisible(False)
			self.lEditOctProd_8.setVisible(False)
			self.lEditNovProd_8.setVisible(False)
			self.lEditDecProd_8.setVisible(False)
			self.lblTotalAnualProd_8.setVisible(False)
		else:
			pass
		if list_ingredients[8] == 'prod9':
			self.lblProd_9.setVisible(False)
			self.lEditJanProd_9.setVisible(False)
			self.lEditFebProd_9.setVisible(False)
			self.lEditMarProd_9.setVisible(False)
			self.lEditAprProd_9.setVisible(False)
			self.lEditMayProd_9.setVisible(False)
			self.lEditJunProd_9.setVisible(False)
			self.lEditJulProd_9.setVisible(False)
			self.lEditAugProd_9.setVisible(False)
			self.lEditSepProd_9.setVisible(False)
			self.lEditOctProd_9.setVisible(False)
			self.lEditNovProd_9.setVisible(False)
			self.lEditDecProd_9.setVisible(False)
			self.lblTotalAnualProd_9.setVisible(False)
		else:
			pass
		if list_ingredients[9] == 'prod10':
			self.lblProd_10.setVisible(False)
			self.lEditJanProd_10.setVisible(False)
			self.lEditFebProd_10.setVisible(False)
			self.lEditMarProd_10.setVisible(False)
			self.lEditAprProd_10.setVisible(False)
			self.lEditMayProd_10.setVisible(False)
			self.lEditJunProd_10.setVisible(False)
			self.lEditJulProd_10.setVisible(False)
			self.lEditAugProd_10.setVisible(False)
			self.lEditSepProd_10.setVisible(False)
			self.lEditOctProd_10.setVisible(False)
			self.lEditNovProd_10.setVisible(False)
			self.lEditDecProd_10.setVisible(False)
			self.lblTotalAnualProd_10.setVisible(False)
		else:
			pass
		if list_ingredients[10] == 'prod11':

			self.lblProd_11.setVisible(False)
			self.lEditJanProd_11.setVisible(False)
			self.lEditFebProd_11.setVisible(False)
			self.lEditMarProd_11.setVisible(False)
			self.lEditAprProd_11.setVisible(False)
			self.lEditMayProd_11.setVisible(False)
			self.lEditJunProd_11.setVisible(False)
			self.lEditJulProd_11.setVisible(False)
			self.lEditAugProd_11.setVisible(False)
			self.lEditSepProd_11.setVisible(False)
			self.lEditOctProd_11.setVisible(False)
			self.lEditNovProd_11.setVisible(False)
			self.lEditDecProd_11.setVisible(False)
			self.lblTotalAnualProd_11.setVisible(False)
		else:
			pass
		if list_ingredients[11] == 'prod12':
			self.lblProd_12.setVisible(False)
			self.lEditJanProd_12.setVisible(False)
			self.lEditFebProd_12.setVisible(False)
			self.lEditMarProd_12.setVisible(False)
			self.lEditAprProd_12.setVisible(False)
			self.lEditMayProd_12.setVisible(False)
			self.lEditJunProd_12.setVisible(False)
			self.lEditJulProd_12.setVisible(False)
			self.lEditAugProd_12.setVisible(False)
			self.lEditSepProd_12.setVisible(False)
			self.lEditOctProd_12.setVisible(False)
			self.lEditNovProd_12.setVisible(False)
			self.lEditDecProd_12.setVisible(False)
			self.lblTotalAnualProd_12.setVisible(False)
		else:
			pass
		if list_ingredients[12] == 'prod13':
			self.lblProd_13.setVisible(False)
			self.lEditJanProd_13.setVisible(False)
			self.lEditFebProd_13.setVisible(False)
			self.lEditMarProd_13.setVisible(False)
			self.lEditAprProd_13.setVisible(False)
			self.lEditMayProd_13.setVisible(False)
			self.lEditJunProd_13.setVisible(False)
			self.lEditJulProd_13.setVisible(False)
			self.lEditAugProd_13.setVisible(False)
			self.lEditSepProd_13.setVisible(False)
			self.lEditOctProd_13.setVisible(False)
			self.lEditNovProd_13.setVisible(False)
			self.lEditDecProd_13.setVisible(False)
			self.lblTotalAnualProd_13.setVisible(False)
		else:
			pass
		if list_ingredients[13] == 'prod14':
			self.lblProd_14.setVisible(False)
			self.lEditJanProd_14.setVisible(False)
			self.lEditFebProd_14.setVisible(False)
			self.lEditMarProd_14.setVisible(False)
			self.lEditAprProd_14.setVisible(False)
			self.lEditMayProd_14.setVisible(False)
			self.lEditJunProd_14.setVisible(False)
			self.lEditJulProd_14.setVisible(False)
			self.lEditAugProd_14.setVisible(False)
			self.lEditSepProd_14.setVisible(False)
			self.lEditOctProd_14.setVisible(False)
			self.lEditNovProd_14.setVisible(False)
			self.lEditDecProd_14.setVisible(False)
			self.lblTotalAnualProd_14.setVisible(False)
		else:
			pass
		if list_ingredients[14] == 'prod15':
			self.lblProd_15.setVisible(False)
			self.lEditJanProd_15.setVisible(False)
			self.lEditFebProd_15.setVisible(False)
			self.lEditMarProd_15.setVisible(False)
			self.lEditAprProd_15.setVisible(False)
			self.lEditMayProd_15.setVisible(False)
			self.lEditJunProd_15.setVisible(False)
			self.lEditJulProd_15.setVisible(False)
			self.lEditAugProd_15.setVisible(False)
			self.lEditSepProd_15.setVisible(False)
			self.lEditOctProd_15.setVisible(False)
			self.lEditNovProd_15.setVisible(False)
			self.lEditDecProd_15.setVisible(False)
			self.lblTotalAnualProd_15.setVisible(False)
		else:
			pass
		if list_ingredients[15] == 'prod16':
			self.lblProd_16.setVisible(False)
			self.lEditJanProd_16.setVisible(False)
			self.lEditFebProd_16.setVisible(False)
			self.lEditMarProd_16.setVisible(False)
			self.lEditAprProd_16.setVisible(False)
			self.lEditMayProd_16.setVisible(False)
			self.lEditJunProd_16.setVisible(False)
			self.lEditJulProd_16.setVisible(False)
			self.lEditAugProd_16.setVisible(False)
			self.lEditSepProd_16.setVisible(False)
			self.lEditOctProd_16.setVisible(False)
			self.lEditNovProd_16.setVisible(False)
			self.lEditDecProd_16.setVisible(False)
			self.lblTotalAnualProd_16.setVisible(False)
		else:
			pass
		if list_ingredients[16] == 'prod17':
			self.lblProd_17.setVisible(False)
			self.lEditJanProd_17.setVisible(False)
			self.lEditFebProd_17.setVisible(False)
			self.lEditMarProd_17.setVisible(False)
			self.lEditAprProd_17.setVisible(False)
			self.lEditMayProd_17.setVisible(False)
			self.lEditJunProd_17.setVisible(False)
			self.lEditJulProd_17.setVisible(False)
			self.lEditAugProd_17.setVisible(False)
			self.lEditSepProd_17.setVisible(False)
			self.lEditOctProd_17.setVisible(False)
			self.lEditNovProd_17.setVisible(False)
			self.lEditDecProd_17.setVisible(False)
			self.lblTotalAnualProd_17.setVisible(False)
		else:
			pass
		if list_ingredients[17] == 'prod18':
			self.lblProd_18.setVisible(False)
			self.lEditJanProd_18.setVisible(False)
			self.lEditFebProd_18.setVisible(False)
			self.lEditMarProd_18.setVisible(False)
			self.lEditAprProd_18.setVisible(False)
			self.lEditMayProd_18.setVisible(False)
			self.lEditJunProd_18.setVisible(False)
			self.lEditJulProd_18.setVisible(False)
			self.lEditAugProd_18.setVisible(False)
			self.lEditSepProd_18.setVisible(False)
			self.lEditOctProd_18.setVisible(False)
			self.lEditNovProd_18.setVisible(False)
			self.lEditDecProd_18.setVisible(False)
			self.lblTotalAnualProd_18.setVisible(False)
		else:
			pass
		if list_ingredients[18] == 'prod19':
			self.lblProd_9.setVisible(False)
			self.lEditJanProd_19.setVisible(False)
			self.lEditFebProd_19.setVisible(False)
			self.lEditMarProd_19.setVisible(False)
			self.lEditAprProd_19.setVisible(False)
			self.lEditMayProd_19.setVisible(False)
			self.lEditJunProd_19.setVisible(False)
			self.lEditJulProd_19.setVisible(False)
			self.lEditAugProd_19.setVisible(False)
			self.lEditSepProd_19.setVisible(False)
			self.lEditOctProd_19.setVisible(False)
			self.lEditNovProd_19.setVisible(False)
			self.lEditDecProd_19.setVisible(False)
			self.lblTotalAnualProd_19.setVisible(False)
		else:
			pass
		if list_ingredients[19] == 'prod20':
			self.lblProd_10.setVisible(False)
			self.lEditJanProd_20.setVisible(False)
			self.lEditFebProd_20.setVisible(False)
			self.lEditMarProd_20.setVisible(False)
			self.lEditAprProd_20.setVisible(False)
			self.lEditMayProd_20.setVisible(False)
			self.lEditJunProd_20.setVisible(False)
			self.lEditJulProd_20.setVisible(False)
			self.lEditAugProd_20.setVisible(False)
			self.lEditSepProd_20.setVisible(False)
			self.lEditOctProd_20.setVisible(False)
			self.lEditNovProd_20.setVisible(False)
			self.lEditDecProd_20.setVisible(False)
			self.lblTotalAnualProd_20.setVisible(False)
		else:
			pass
		if list_ingredients[20] == 'prod21':
			self.lblProd_21.setVisible(False)
			self.lEditJanProd_21.setVisible(False)
			self.lEditFebProd_21.setVisible(False)
			self.lEditMarProd_21.setVisible(False)
			self.lEditAprProd_21.setVisible(False)
			self.lEditMayProd_21.setVisible(False)
			self.lEditJunProd_21.setVisible(False)
			self.lEditJulProd_21.setVisible(False)
			self.lEditAugProd_21.setVisible(False)
			self.lEditSepProd_21.setVisible(False)
			self.lEditOctProd_21.setVisible(False)
			self.lEditNovProd_21.setVisible(False)
			self.lEditDecProd_21.setVisible(False)
			self.lblTotalAnualProd_21.setVisible(False)
		else:
			pass
		if list_ingredients[21] == 'prod22':
			self.lblProd_22.setVisible(False)
			self.lEditJanProd_22.setVisible(False)
			self.lEditFebProd_22.setVisible(False)
			self.lEditMarProd_22.setVisible(False)
			self.lEditAprProd_22.setVisible(False)
			self.lEditMayProd_22.setVisible(False)
			self.lEditJunProd_22.setVisible(False)
			self.lEditJulProd_22.setVisible(False)
			self.lEditAugProd_22.setVisible(False)
			self.lEditSepProd_22.setVisible(False)
			self.lEditOctProd_22.setVisible(False)
			self.lEditNovProd_22.setVisible(False)
			self.lEditDecProd_22.setVisible(False)
			self.lblTotalAnualProd_22.setVisible(False)
		else:
			pass
		if list_ingredients[22] == 'prod23':
			self.lblProd_23.setVisible(False)
			self.lEditJanProd_23.setVisible(False)
			self.lEditFebProd_23.setVisible(False)
			self.lEditMarProd_23.setVisible(False)
			self.lEditAprProd_23.setVisible(False)
			self.lEditMayProd_23.setVisible(False)
			self.lEditJunProd_23.setVisible(False)
			self.lEditJulProd_23.setVisible(False)
			self.lEditAugProd_23.setVisible(False)
			self.lEditSepProd_23.setVisible(False)
			self.lEditOctProd_23.setVisible(False)
			self.lEditNovProd_23.setVisible(False)
			self.lEditDecProd_23.setVisible(False)
			self.lblTotalAnualProd_23.setVisible(False)
		else:
			pass
		if list_ingredients[23] == 'prod24':
			self.lblProd_24.setVisible(False)
			self.lEditJanProd_24.setVisible(False)
			self.lEditFebProd_24.setVisible(False)
			self.lEditMarProd_24.setVisible(False)
			self.lEditAprProd_24.setVisible(False)
			self.lEditMayProd_24.setVisible(False)
			self.lEditJunProd_24.setVisible(False)
			self.lEditJulProd_24.setVisible(False)
			self.lEditAugProd_24.setVisible(False)
			self.lEditSepProd_24.setVisible(False)
			self.lEditOctProd_24.setVisible(False)
			self.lEditNovProd_24.setVisible(False)
			self.lEditDecProd_24.setVisible(False)
			self.lblTotalAnualProd_24.setVisible(False)
		else:
			pass
		if list_ingredients[24] == 'prod25':
			self.lblProd_25.setVisible(False)
			self.lEditJanProd_25.setVisible(False)
			self.lEditFebProd_25.setVisible(False)
			self.lEditMarProd_25.setVisible(False)
			self.lEditAprProd_25.setVisible(False)
			self.lEditMayProd_25.setVisible(False)
			self.lEditJunProd_25.setVisible(False)
			self.lEditJulProd_25.setVisible(False)
			self.lEditAugProd_25.setVisible(False)
			self.lEditSepProd_25.setVisible(False)
			self.lEditOctProd_25.setVisible(False)
			self.lEditNovProd_25.setVisible(False)
			self.lEditDecProd_25.setVisible(False)
			self.lblTotalAnualProd_25.setVisible(False)
		else:
			pass
		if list_ingredients[25] == 'prod26':
			self.lblProd_26.setVisible(False)
			self.lEditJanProd_26.setVisible(False)
			self.lEditFebProd_26.setVisible(False)
			self.lEditMarProd_26.setVisible(False)
			self.lEditAprProd_26.setVisible(False)
			self.lEditMayProd_26.setVisible(False)
			self.lEditJunProd_26.setVisible(False)
			self.lEditJulProd_26.setVisible(False)
			self.lEditAugProd_26.setVisible(False)
			self.lEditSepProd_26.setVisible(False)
			self.lEditOctProd_26.setVisible(False)
			self.lEditNovProd_26.setVisible(False)
			self.lEditDecProd_26.setVisible(False)
			self.lblTotalAnualProd_26.setVisible(False)
		else:
			pass
		if list_ingredients[26] == 'prod27':
			self.lblProd_27.setVisible(False)
			self.lEditJanProd_27.setVisible(False)
			self.lEditFebProd_27.setVisible(False)
			self.lEditMarProd_27.setVisible(False)
			self.lEditAprProd_27.setVisible(False)
			self.lEditMayProd_27.setVisible(False)
			self.lEditJunProd_27.setVisible(False)
			self.lEditJulProd_27.setVisible(False)
			self.lEditAugProd_27.setVisible(False)
			self.lEditSepProd_27.setVisible(False)
			self.lEditOctProd_27.setVisible(False)
			self.lEditNovProd_27.setVisible(False)
			self.lEditDecProd_27.setVisible(False)
			self.lblTotalAnualProd_27.setVisible(False)
		else:
			pass
		if list_ingredients[27] == 'prod28':
			self.lblProd_28.setVisible(False)
			self.lEditJanProd_28.setVisible(False)
			self.lEditFebProd_28.setVisible(False)
			self.lEditMarProd_28.setVisible(False)
			self.lEditAprProd_28.setVisible(False)
			self.lEditMayProd_28.setVisible(False)
			self.lEditJunProd_28.setVisible(False)
			self.lEditJulProd_28.setVisible(False)
			self.lEditAugProd_28.setVisible(False)
			self.lEditSepProd_28.setVisible(False)
			self.lEditOctProd_28.setVisible(False)
			self.lEditNovProd_28.setVisible(False)
			self.lEditDecProd_28.setVisible(False)
			self.lblTotalAnualProd_28.setVisible(False)
		else:
			pass
		if list_ingredients[28] == 'prod29':
			self.lblProd_9.setVisible(False)
			self.lEditJanProd_29.setVisible(False)
			self.lEditFebProd_29.setVisible(False)
			self.lEditMarProd_29.setVisible(False)
			self.lEditAprProd_29.setVisible(False)
			self.lEditMayProd_29.setVisible(False)
			self.lEditJunProd_29.setVisible(False)
			self.lEditJulProd_29.setVisible(False)
			self.lEditAugProd_29.setVisible(False)
			self.lEditSepProd_29.setVisible(False)
			self.lEditOctProd_29.setVisible(False)
			self.lEditNovProd_29.setVisible(False)
			self.lEditDecProd_29.setVisible(False)
			self.lblTotalAnualProd_29.setVisible(False)
		else:
			pass
		if list_ingredients[29] == 'prod30':
			self.lblProd_10.setVisible(False)
			self.lEditJanProd_30.setVisible(False)
			self.lEditFebProd_30.setVisible(False)
			self.lEditMarProd_30.setVisible(False)
			self.lEditAprProd_30.setVisible(False)
			self.lEditMayProd_30.setVisible(False)
			self.lEditJunProd_30.setVisible(False)
			self.lEditJulProd_30.setVisible(False)
			self.lEditAugProd_30.setVisible(False)
			self.lEditSepProd_30.setVisible(False)
			self.lEditOctProd_30.setVisible(False)
			self.lEditNovProd_30.setVisible(False)
			self.lEditDecProd_30.setVisible(False)
			self.lblTotalAnualProd_30.setVisible(False)
		else:
			pass
		if list_ingredients[30] == 'prod31':
			self.lblProd_31.setVisible(False)
			self.lEditJanProd_31.setVisible(False)
			self.lEditFebProd_31.setVisible(False)
			self.lEditMarProd_31.setVisible(False)
			self.lEditAprProd_31.setVisible(False)
			self.lEditMayProd_31.setVisible(False)
			self.lEditJunProd_31.setVisible(False)
			self.lEditJulProd_31.setVisible(False)
			self.lEditAugProd_31.setVisible(False)
			self.lEditSepProd_31.setVisible(False)
			self.lEditOctProd_31.setVisible(False)
			self.lEditNovProd_31.setVisible(False)
			self.lEditDecProd_31.setVisible(False)
			self.lblTotalAnualProd_31.setVisible(False)
		else:
			pass
		if list_ingredients[31] == 'prod32':
			self.lblProd_32.setVisible(False)
			self.lEditJanProd_32.setVisible(False)
			self.lEditFebProd_32.setVisible(False)
			self.lEditMarProd_32.setVisible(False)
			self.lEditAprProd_32.setVisible(False)
			self.lEditMayProd_32.setVisible(False)
			self.lEditJunProd_32.setVisible(False)
			self.lEditJulProd_32.setVisible(False)
			self.lEditAugProd_32.setVisible(False)
			self.lEditSepProd_32.setVisible(False)
			self.lEditOctProd_32.setVisible(False)
			self.lEditNovProd_32.setVisible(False)
			self.lEditDecProd_32.setVisible(False)
			self.lblTotalAnualProd_32.setVisible(False)
		else:
			pass
		if list_ingredients[32] == 'prod33':
			self.lblProd_33.setVisible(False)
			self.lEditJanProd_33.setVisible(False)
			self.lEditFebProd_33.setVisible(False)
			self.lEditMarProd_33.setVisible(False)
			self.lEditAprProd_33.setVisible(False)
			self.lEditMayProd_33.setVisible(False)
			self.lEditJunProd_33.setVisible(False)
			self.lEditJulProd_33.setVisible(False)
			self.lEditAugProd_33.setVisible(False)
			self.lEditSepProd_33.setVisible(False)
			self.lEditOctProd_33.setVisible(False)
			self.lEditNovProd_33.setVisible(False)
			self.lEditDecProd_33.setVisible(False)
			self.lblTotalAnualProd_33.setVisible(False)
		else:
			pass
		if list_ingredients[33] == 'prod34':
			self.lblProd_34.setVisible(False)
			self.lEditJanProd_34.setVisible(False)
			self.lEditFebProd_34.setVisible(False)
			self.lEditMarProd_34.setVisible(False)
			self.lEditAprProd_34.setVisible(False)
			self.lEditMayProd_34.setVisible(False)
			self.lEditJunProd_34.setVisible(False)
			self.lEditJulProd_34.setVisible(False)
			self.lEditAugProd_34.setVisible(False)
			self.lEditSepProd_34.setVisible(False)
			self.lEditOctProd_34.setVisible(False)
			self.lEditNovProd_34.setVisible(False)
			self.lEditDecProd_34.setVisible(False)
			self.lblTotalAnualProd_34.setVisible(False)
		else:
			pass
		"""
	def lock_fields (self):

		self.lEditJanProd.setEnabled(False)
		self.lEditFebProd.setEnabled(False)
		self.lEditMarProd.setEnabled(False)
		self.lEditAprProd.setEnabled(False)
		self.lEditMayProd.setEnabled(False)
		self.lEditJunProd.setEnabled(False)
		self.lEditJulProd.setEnabled(False)
		self.lEditAugProd.setEnabled(False)
		self.lEditSepProd.setEnabled(False)
		self.lEditOctProd.setEnabled(False)
		self.lEditNovProd.setEnabled(False)
		self.lEditDecProd.setEnabled(False)

		self.lEditJanProd_2.setEnabled(False)
		self.lEditFebProd_2.setEnabled(False)
		self.lEditMarProd_2.setEnabled(False)
		self.lEditAprProd_2.setEnabled(False)
		self.lEditMayProd_2.setEnabled(False)
		self.lEditJunProd_2.setEnabled(False)
		self.lEditJulProd_2.setEnabled(False)
		self.lEditAugProd_2.setEnabled(False)
		self.lEditSepProd_2.setEnabled(False)
		self.lEditOctProd_2.setEnabled(False)
		self.lEditNovProd_2.setEnabled(False)
		self.lEditDecProd_2.setEnabled(False)

		self.lEditJanProd_3.setEnabled(False)
		self.lEditFebProd_3.setEnabled(False)
		self.lEditMarProd_3.setEnabled(False)
		self.lEditAprProd_3.setEnabled(False)
		self.lEditMayProd_3.setEnabled(False)
		self.lEditJunProd_3.setEnabled(False)
		self.lEditJulProd_3.setEnabled(False)
		self.lEditAugProd_3.setEnabled(False)
		self.lEditSepProd_3.setEnabled(False)
		self.lEditOctProd_3.setEnabled(False)
		self.lEditNovProd_3.setEnabled(False)
		self.lEditDecProd_3.setEnabled(False)

		self.lEditJanProd_4.setEnabled(False)
		self.lEditFebProd_4.setEnabled(False)
		self.lEditMarProd_4.setEnabled(False)
		self.lEditAprProd_4.setEnabled(False)
		self.lEditMayProd_4.setEnabled(False)
		self.lEditJunProd_4.setEnabled(False)
		self.lEditJulProd_4.setEnabled(False)
		self.lEditAugProd_4.setEnabled(False)
		self.lEditSepProd_4.setEnabled(False)
		self.lEditOctProd_4.setEnabled(False)
		self.lEditNovProd_4.setEnabled(False)
		self.lEditDecProd_4.setEnabled(False)

		self.lEditJanProd_5.setEnabled(False)
		self.lEditFebProd_5.setEnabled(False)
		self.lEditMarProd_5.setEnabled(False)
		self.lEditAprProd_5.setEnabled(False)
		self.lEditMayProd_5.setEnabled(False)
		self.lEditJunProd_5.setEnabled(False)
		self.lEditJulProd_5.setEnabled(False)
		self.lEditAugProd_5.setEnabled(False)
		self.lEditSepProd_5.setEnabled(False)
		self.lEditOctProd_5.setEnabled(False)
		self.lEditNovProd_5.setEnabled(False)
		self.lEditDecProd_5.setEnabled(False)

		self.lEditJanProd_6.setEnabled(False)
		self.lEditFebProd_6.setEnabled(False)
		self.lEditMarProd_6.setEnabled(False)
		self.lEditAprProd_6.setEnabled(False)
		self.lEditMayProd_6.setEnabled(False)
		self.lEditJunProd_6.setEnabled(False)
		self.lEditJulProd_6.setEnabled(False)
		self.lEditAugProd_6.setEnabled(False)
		self.lEditSepProd_6.setEnabled(False)
		self.lEditOctProd_6.setEnabled(False)
		self.lEditNovProd_6.setEnabled(False)
		self.lEditDecProd_6.setEnabled(False)

		self.lEditJanProd_7.setEnabled(False)
		self.lEditFebProd_7.setEnabled(False)
		self.lEditMarProd_7.setEnabled(False)
		self.lEditAprProd_7.setEnabled(False)
		self.lEditMayProd_7.setEnabled(False)
		self.lEditJunProd_7.setEnabled(False)
		self.lEditJulProd_7.setEnabled(False)
		self.lEditAugProd_7.setEnabled(False)
		self.lEditSepProd_7.setEnabled(False)
		self.lEditOctProd_7.setEnabled(False)
		self.lEditNovProd_7.setEnabled(False)
		self.lEditDecProd_7.setEnabled(False)

		self.lEditJanProd_8.setEnabled(False)
		self.lEditFebProd_8.setEnabled(False)
		self.lEditMarProd_8.setEnabled(False)
		self.lEditAprProd_8.setEnabled(False)
		self.lEditMayProd_8.setEnabled(False)
		self.lEditJunProd_8.setEnabled(False)
		self.lEditJulProd_8.setEnabled(False)
		self.lEditAugProd_8.setEnabled(False)
		self.lEditSepProd_8.setEnabled(False)
		self.lEditOctProd_8.setEnabled(False)
		self.lEditNovProd_8.setEnabled(False)
		self.lEditDecProd_8.setEnabled(False)

		self.lEditJanProd_9.setEnabled(False)
		self.lEditFebProd_9.setEnabled(False)
		self.lEditMarProd_9.setEnabled(False)
		self.lEditAprProd_9.setEnabled(False)
		self.lEditMayProd_9.setEnabled(False)
		self.lEditJunProd_9.setEnabled(False)
		self.lEditJulProd_9.setEnabled(False)
		self.lEditAugProd_9.setEnabled(False)
		self.lEditSepProd_9.setEnabled(False)
		self.lEditOctProd_9.setEnabled(False)
		self.lEditNovProd_9.setEnabled(False)
		self.lEditDecProd_9.setEnabled(False)

		self.lEditJanProd_10.setEnabled(False)
		self.lEditFebProd_10.setEnabled(False)
		self.lEditMarProd_10.setEnabled(False)
		self.lEditAprProd_10.setEnabled(False)
		self.lEditMayProd_10.setEnabled(False)
		self.lEditJunProd_10.setEnabled(False)
		self.lEditJulProd_10.setEnabled(False)
		self.lEditAugProd_10.setEnabled(False)
		self.lEditSepProd_10.setEnabled(False)
		self.lEditOctProd_10.setEnabled(False)
		self.lEditNovProd_10.setEnabled(False)
		self.lEditDecProd_10.setEnabled(False)

		self.lEditJanProd_11.setEnabled(False)
		self.lEditFebProd_11.setEnabled(False)
		self.lEditMarProd_11.setEnabled(False)
		self.lEditAprProd_11.setEnabled(False)
		self.lEditMayProd_11.setEnabled(False)
		self.lEditJunProd_11.setEnabled(False)
		self.lEditJulProd_11.setEnabled(False)
		self.lEditAugProd_11.setEnabled(False)
		self.lEditSepProd_11.setEnabled(False)
		self.lEditOctProd_11.setEnabled(False)
		self.lEditNovProd_11.setEnabled(False)
		self.lEditDecProd_11.setEnabled(False)

		self.lEditJanProd_12.setEnabled(False)
		self.lEditFebProd_12.setEnabled(False)
		self.lEditMarProd_12.setEnabled(False)
		self.lEditAprProd_12.setEnabled(False)
		self.lEditMayProd_12.setEnabled(False)
		self.lEditJunProd_12.setEnabled(False)
		self.lEditJulProd_12.setEnabled(False)
		self.lEditAugProd_12.setEnabled(False)
		self.lEditSepProd_12.setEnabled(False)
		self.lEditOctProd_12.setEnabled(False)
		self.lEditNovProd_12.setEnabled(False)
		self.lEditDecProd_12.setEnabled(False)

		self.lEditJanProd_13.setEnabled(False)
		self.lEditFebProd_13.setEnabled(False)
		self.lEditMarProd_13.setEnabled(False)
		self.lEditAprProd_13.setEnabled(False)
		self.lEditMayProd_13.setEnabled(False)
		self.lEditJunProd_13.setEnabled(False)
		self.lEditJulProd_13.setEnabled(False)
		self.lEditAugProd_13.setEnabled(False)
		self.lEditSepProd_13.setEnabled(False)
		self.lEditOctProd_13.setEnabled(False)
		self.lEditNovProd_13.setEnabled(False)
		self.lEditDecProd_13.setEnabled(False)

		self.lEditJanProd_14.setEnabled(False)
		self.lEditFebProd_14.setEnabled(False)
		self.lEditMarProd_14.setEnabled(False)
		self.lEditAprProd_14.setEnabled(False)
		self.lEditMayProd_14.setEnabled(False)
		self.lEditJunProd_14.setEnabled(False)
		self.lEditJulProd_14.setEnabled(False)
		self.lEditAugProd_14.setEnabled(False)
		self.lEditSepProd_14.setEnabled(False)
		self.lEditOctProd_14.setEnabled(False)
		self.lEditNovProd_14.setEnabled(False)
		self.lEditDecProd_14.setEnabled(False)

		self.lEditJanProd_15.setEnabled(False)
		self.lEditFebProd_15.setEnabled(False)
		self.lEditMarProd_15.setEnabled(False)
		self.lEditAprProd_15.setEnabled(False)
		self.lEditMayProd_15.setEnabled(False)
		self.lEditJunProd_15.setEnabled(False)
		self.lEditJulProd_15.setEnabled(False)
		self.lEditAugProd_15.setEnabled(False)
		self.lEditSepProd_15.setEnabled(False)
		self.lEditOctProd_15.setEnabled(False)
		self.lEditNovProd_15.setEnabled(False)
		self.lEditDecProd_15.setEnabled(False)

		self.lEditJanProd_16.setEnabled(False)
		self.lEditFebProd_16.setEnabled(False)
		self.lEditMarProd_16.setEnabled(False)
		self.lEditAprProd_16.setEnabled(False)
		self.lEditMayProd_16.setEnabled(False)
		self.lEditJunProd_16.setEnabled(False)
		self.lEditJulProd_16.setEnabled(False)
		self.lEditAugProd_16.setEnabled(False)
		self.lEditSepProd_16.setEnabled(False)
		self.lEditOctProd_16.setEnabled(False)
		self.lEditNovProd_16.setEnabled(False)
		self.lEditDecProd_16.setEnabled(False)

		self.lEditJanProd_17.setEnabled(False)
		self.lEditFebProd_17.setEnabled(False)
		self.lEditMarProd_17.setEnabled(False)
		self.lEditAprProd_17.setEnabled(False)
		self.lEditMayProd_17.setEnabled(False)
		self.lEditJunProd_17.setEnabled(False)
		self.lEditJulProd_17.setEnabled(False)
		self.lEditAugProd_17.setEnabled(False)
		self.lEditSepProd_17.setEnabled(False)
		self.lEditOctProd_17.setEnabled(False)
		self.lEditNovProd_17.setEnabled(False)
		self.lEditDecProd_17.setEnabled(False)

		self.lEditJanProd_18.setEnabled(False)
		self.lEditFebProd_18.setEnabled(False)
		self.lEditMarProd_18.setEnabled(False)
		self.lEditAprProd_18.setEnabled(False)
		self.lEditMayProd_18.setEnabled(False)
		self.lEditJunProd_18.setEnabled(False)
		self.lEditJulProd_18.setEnabled(False)
		self.lEditAugProd_18.setEnabled(False)
		self.lEditSepProd_18.setEnabled(False)
		self.lEditOctProd_18.setEnabled(False)
		self.lEditNovProd_18.setEnabled(False)
		self.lEditDecProd_18.setEnabled(False)

		self.lEditJanProd_19.setEnabled(False)
		self.lEditFebProd_19.setEnabled(False)
		self.lEditMarProd_19.setEnabled(False)
		self.lEditAprProd_19.setEnabled(False)
		self.lEditMayProd_19.setEnabled(False)
		self.lEditJunProd_19.setEnabled(False)
		self.lEditJulProd_19.setEnabled(False)
		self.lEditAugProd_19.setEnabled(False)
		self.lEditSepProd_19.setEnabled(False)
		self.lEditOctProd_19.setEnabled(False)
		self.lEditNovProd_19.setEnabled(False)
		self.lEditDecProd_19.setEnabled(False)

		self.lEditJanProd_20.setEnabled(False)
		self.lEditFebProd_20.setEnabled(False)
		self.lEditMarProd_20.setEnabled(False)
		self.lEditAprProd_20.setEnabled(False)
		self.lEditMayProd_20.setEnabled(False)
		self.lEditJunProd_20.setEnabled(False)
		self.lEditJulProd_20.setEnabled(False)
		self.lEditAugProd_20.setEnabled(False)
		self.lEditSepProd_20.setEnabled(False)
		self.lEditOctProd_20.setEnabled(False)
		self.lEditNovProd_20.setEnabled(False)
		self.lEditDecProd_20.setEnabled(False)

		self.lEditJanProd_21.setEnabled(False)
		self.lEditFebProd_21.setEnabled(False)
		self.lEditMarProd_21.setEnabled(False)
		self.lEditAprProd_21.setEnabled(False)
		self.lEditMayProd_21.setEnabled(False)
		self.lEditJunProd_21.setEnabled(False)
		self.lEditJulProd_21.setEnabled(False)
		self.lEditAugProd_21.setEnabled(False)
		self.lEditSepProd_21.setEnabled(False)
		self.lEditOctProd_21.setEnabled(False)
		self.lEditNovProd_21.setEnabled(False)
		self.lEditDecProd_21.setEnabled(False)

		self.lEditJanProd_22.setEnabled(False)
		self.lEditFebProd_22.setEnabled(False)
		self.lEditMarProd_22.setEnabled(False)
		self.lEditAprProd_22.setEnabled(False)
		self.lEditMayProd_22.setEnabled(False)
		self.lEditJunProd_22.setEnabled(False)
		self.lEditJulProd_22.setEnabled(False)
		self.lEditAugProd_22.setEnabled(False)
		self.lEditSepProd_22.setEnabled(False)
		self.lEditOctProd_22.setEnabled(False)
		self.lEditNovProd_22.setEnabled(False)
		self.lEditDecProd_22.setEnabled(False)

		self.lEditJanProd_23.setEnabled(False)
		self.lEditFebProd_23.setEnabled(False)
		self.lEditMarProd_23.setEnabled(False)
		self.lEditAprProd_23.setEnabled(False)
		self.lEditMayProd_23.setEnabled(False)
		self.lEditJunProd_23.setEnabled(False)
		self.lEditJulProd_23.setEnabled(False)
		self.lEditAugProd_23.setEnabled(False)
		self.lEditSepProd_23.setEnabled(False)
		self.lEditOctProd_23.setEnabled(False)
		self.lEditNovProd_23.setEnabled(False)
		self.lEditDecProd_23.setEnabled(False)

		self.lEditJanProd_24.setEnabled(False)
		self.lEditFebProd_24.setEnabled(False)
		self.lEditMarProd_24.setEnabled(False)
		self.lEditAprProd_24.setEnabled(False)
		self.lEditMayProd_24.setEnabled(False)
		self.lEditJunProd_24.setEnabled(False)
		self.lEditJulProd_24.setEnabled(False)
		self.lEditAugProd_24.setEnabled(False)
		self.lEditSepProd_24.setEnabled(False)
		self.lEditOctProd_24.setEnabled(False)
		self.lEditNovProd_24.setEnabled(False)
		self.lEditDecProd_24.setEnabled(False)

		self.lEditJanProd_25.setEnabled(False)
		self.lEditFebProd_25.setEnabled(False)
		self.lEditMarProd_25.setEnabled(False)
		self.lEditAprProd_25.setEnabled(False)
		self.lEditMayProd_25.setEnabled(False)
		self.lEditJunProd_25.setEnabled(False)
		self.lEditJulProd_25.setEnabled(False)
		self.lEditAugProd_25.setEnabled(False)
		self.lEditSepProd_25.setEnabled(False)
		self.lEditOctProd_25.setEnabled(False)
		self.lEditNovProd_25.setEnabled(False)
		self.lEditDecProd_25.setEnabled(False)

		self.lEditJanProd_26.setEnabled(False)
		self.lEditFebProd_26.setEnabled(False)
		self.lEditMarProd_26.setEnabled(False)
		self.lEditAprProd_26.setEnabled(False)
		self.lEditMayProd_26.setEnabled(False)
		self.lEditJunProd_26.setEnabled(False)
		self.lEditJulProd_26.setEnabled(False)
		self.lEditAugProd_26.setEnabled(False)
		self.lEditSepProd_26.setEnabled(False)
		self.lEditOctProd_26.setEnabled(False)
		self.lEditNovProd_26.setEnabled(False)
		self.lEditDecProd_26.setEnabled(False)

		self.lEditJanProd_27.setEnabled(False)
		self.lEditFebProd_27.setEnabled(False)
		self.lEditMarProd_27.setEnabled(False)
		self.lEditAprProd_27.setEnabled(False)
		self.lEditMayProd_27.setEnabled(False)
		self.lEditJunProd_27.setEnabled(False)
		self.lEditJulProd_27.setEnabled(False)
		self.lEditAugProd_27.setEnabled(False)
		self.lEditSepProd_27.setEnabled(False)
		self.lEditOctProd_27.setEnabled(False)
		self.lEditNovProd_27.setEnabled(False)
		self.lEditDecProd_27.setEnabled(False)

		self.lEditJanProd_28.setEnabled(False)
		self.lEditFebProd_28.setEnabled(False)
		self.lEditMarProd_28.setEnabled(False)
		self.lEditAprProd_28.setEnabled(False)
		self.lEditMayProd_28.setEnabled(False)
		self.lEditJunProd_28.setEnabled(False)
		self.lEditJulProd_28.setEnabled(False)
		self.lEditAugProd_28.setEnabled(False)
		self.lEditSepProd_28.setEnabled(False)
		self.lEditOctProd_28.setEnabled(False)
		self.lEditNovProd_28.setEnabled(False)
		self.lEditDecProd_28.setEnabled(False)

		self.lEditJanProd_29.setEnabled(False)
		self.lEditFebProd_29.setEnabled(False)
		self.lEditMarProd_29.setEnabled(False)
		self.lEditAprProd_29.setEnabled(False)
		self.lEditMayProd_29.setEnabled(False)
		self.lEditJunProd_29.setEnabled(False)
		self.lEditJulProd_29.setEnabled(False)
		self.lEditAugProd_29.setEnabled(False)
		self.lEditSepProd_29.setEnabled(False)
		self.lEditOctProd_29.setEnabled(False)
		self.lEditNovProd_29.setEnabled(False)
		self.lEditDecProd_29.setEnabled(False)

		self.lEditJanProd_30.setEnabled(False)
		self.lEditFebProd_30.setEnabled(False)
		self.lEditMarProd_30.setEnabled(False)
		self.lEditAprProd_30.setEnabled(False)
		self.lEditMayProd_30.setEnabled(False)
		self.lEditJunProd_30.setEnabled(False)
		self.lEditJulProd_30.setEnabled(False)
		self.lEditAugProd_30.setEnabled(False)
		self.lEditSepProd_30.setEnabled(False)
		self.lEditOctProd_30.setEnabled(False)
		self.lEditNovProd_30.setEnabled(False)
		self.lEditDecProd_30.setEnabled(False)

		self.lEditJanProd_31.setEnabled(False)
		self.lEditFebProd_31.setEnabled(False)
		self.lEditMarProd_31.setEnabled(False)
		self.lEditAprProd_31.setEnabled(False)
		self.lEditMayProd_31.setEnabled(False)
		self.lEditJunProd_31.setEnabled(False)
		self.lEditJulProd_31.setEnabled(False)
		self.lEditAugProd_31.setEnabled(False)
		self.lEditSepProd_31.setEnabled(False)
		self.lEditOctProd_31.setEnabled(False)
		self.lEditNovProd_31.setEnabled(False)
		self.lEditDecProd_31.setEnabled(False)

		self.lEditJanProd_32.setEnabled(False)
		self.lEditFebProd_32.setEnabled(False)
		self.lEditMarProd_32.setEnabled(False)
		self.lEditAprProd_32.setEnabled(False)
		self.lEditMayProd_32.setEnabled(False)
		self.lEditJunProd_32.setEnabled(False)
		self.lEditJulProd_32.setEnabled(False)
		self.lEditAugProd_32.setEnabled(False)
		self.lEditSepProd_32.setEnabled(False)
		self.lEditOctProd_32.setEnabled(False)
		self.lEditNovProd_32.setEnabled(False)
		self.lEditDecProd_32.setEnabled(False)

		self.lEditJanProd_33.setEnabled(False)
		self.lEditFebProd_33.setEnabled(False)
		self.lEditMarProd_33.setEnabled(False)
		self.lEditAprProd_33.setEnabled(False)
		self.lEditMayProd_33.setEnabled(False)
		self.lEditJunProd_33.setEnabled(False)
		self.lEditJulProd_33.setEnabled(False)
		self.lEditAugProd_33.setEnabled(False)
		self.lEditSepProd_33.setEnabled(False)
		self.lEditOctProd_33.setEnabled(False)
		self.lEditNovProd_33.setEnabled(False)
		self.lEditDecProd_33.setEnabled(False)

		self.lEditJanProd_34.setEnabled(False)
		self.lEditFebProd_34.setEnabled(False)
		self.lEditMarProd_34.setEnabled(False)
		self.lEditAprProd_34.setEnabled(False)
		self.lEditMayProd_34.setEnabled(False)
		self.lEditJunProd_34.setEnabled(False)
		self.lEditJulProd_34.setEnabled(False)
		self.lEditAugProd_34.setEnabled(False)
		self.lEditSepProd_34.setEnabled(False)
		self.lEditOctProd_34.setEnabled(False)
		self.lEditNovProd_34.setEnabled(False)
		self.lEditDecProd_34.setEnabled(False)
		
	def unlock_fields(self):

		"""		self.lEditJanProd.setEnabled(True)
		self.lEditFebProd.setEnabled(True)
		self.lEditMarProd.setEnabled(True)
		self.lEditAprProd.setEnabled(True)
		self.lEditMayProd.setEnabled(True)
		self.lEditJunProd.setEnabled(True)
		self.lEditJulProd.setEnabled(True)
		self.lEditAugProd.setEnabled(True)
		self.lEditSepProd.setEnabled(True)
		self.lEditOctProd.setEnabled(True)
		self.lEditNovProd.setEnabled(True)
		self.lEditDecProd.setEnabled(True)

		self.lEditJanProd_2.setEnabled(True)
		self.lEditFebProd_2.setEnabled(True)
		self.lEditMarProd_2.setEnabled(True)
		self.lEditAprProd_2.setEnabled(True)
		self.lEditMayProd_2.setEnabled(True)
		self.lEditJunProd_2.setEnabled(True)
		self.lEditJulProd_2.setEnabled(True)
		self.lEditAugProd_2.setEnabled(True)
		self.lEditSepProd_2.setEnabled(True)
		self.lEditOctProd_2.setEnabled(True)
		self.lEditNovProd_2.setEnabled(True)
		self.lEditDecProd_2.setEnabled(True)

		self.lEditJanProd_3.setEnabled(True)
		self.lEditFebProd_3.setEnabled(True)
		self.lEditMarProd_3.setEnabled(True)
		self.lEditAprProd_3.setEnabled(True)
		self.lEditMayProd_3.setEnabled(True)
		self.lEditJunProd_3.setEnabled(True)
		self.lEditJulProd_3.setEnabled(True)
		self.lEditAugProd_3.setEnabled(True)
		self.lEditSepProd_3.setEnabled(True)
		self.lEditOctProd_3.setEnabled(True)
		self.lEditNovProd_3.setEnabled(True)
		self.lEditDecProd_3.setEnabled(True)

		self.lEditJanProd_4.setEnabled(True)
		self.lEditFebProd_4.setEnabled(True)
		self.lEditMarProd_4.setEnabled(True)
		self.lEditAprProd_4.setEnabled(True)
		self.lEditMayProd_4.setEnabled(True)
		self.lEditJunProd_4.setEnabled(True)
		self.lEditJulProd_4.setEnabled(True)
		self.lEditAugProd_4.setEnabled(True)
		self.lEditSepProd_4.setEnabled(True)
		self.lEditOctProd_4.setEnabled(True)
		self.lEditNovProd_4.setEnabled(True)
		self.lEditDecProd_4.setEnabled(True)

		self.lEditJanProd_5.setEnabled(True)
		self.lEditFebProd_5.setEnabled(True)
		self.lEditMarProd_5.setEnabled(True)
		self.lEditAprProd_5.setEnabled(True)
		self.lEditMayProd_5.setEnabled(True)
		self.lEditJunProd_5.setEnabled(True)
		self.lEditJulProd_5.setEnabled(True)
		self.lEditAugProd_5.setEnabled(True)
		self.lEditSepProd_5.setEnabled(True)
		self.lEditOctProd_5.setEnabled(True)
		self.lEditNovProd_5.setEnabled(True)
		self.lEditDecProd_5.setEnabled(True)

		self.lEditJanProd_6.setEnabled(True)
		self.lEditFebProd_6.setEnabled(True)
		self.lEditMarProd_6.setEnabled(True)
		self.lEditAprProd_6.setEnabled(True)
		self.lEditMayProd_6.setEnabled(True)
		self.lEditJunProd_6.setEnabled(True)
		self.lEditJulProd_6.setEnabled(True)
		self.lEditAugProd_6.setEnabled(True)
		self.lEditSepProd_6.setEnabled(True)
		self.lEditOctProd_6.setEnabled(True)
		self.lEditNovProd_6.setEnabled(True)
		self.lEditDecProd_6.setEnabled(True)

		self.lEditJanProd_7.setEnabled(True)
		self.lEditFebProd_7.setEnabled(True)
		self.lEditMarProd_7.setEnabled(True)
		self.lEditAprProd_7.setEnabled(True)
		self.lEditMayProd_7.setEnabled(True)
		self.lEditJunProd_7.setEnabled(True)
		self.lEditJulProd_7.setEnabled(True)
		self.lEditAugProd_7.setEnabled(True)
		self.lEditSepProd_7.setEnabled(True)
		self.lEditOctProd_7.setEnabled(True)
		self.lEditNovProd_7.setEnabled(True)
		self.lEditDecProd_7.setEnabled(True)

		self.lEditJanProd_8.setEnabled(True)
		self.lEditFebProd_8.setEnabled(True)
		self.lEditMarProd_8.setEnabled(True)
		self.lEditAprProd_8.setEnabled(True)
		self.lEditMayProd_8.setEnabled(True)
		self.lEditJunProd_8.setEnabled(True)
		self.lEditJulProd_8.setEnabled(True)
		self.lEditAugProd_8.setEnabled(True)
		self.lEditSepProd_8.setEnabled(True)
		self.lEditOctProd_8.setEnabled(True)
		self.lEditNovProd_8.setEnabled(True)
		self.lEditDecProd_8.setEnabled(True)

		self.lEditJanProd_9.setEnabled(True)
		self.lEditFebProd_9.setEnabled(True)
		self.lEditMarProd_9.setEnabled(True)
		self.lEditAprProd_9.setEnabled(True)
		self.lEditMayProd_9.setEnabled(True)
		self.lEditJunProd_9.setEnabled(True)
		self.lEditJulProd_9.setEnabled(True)
		self.lEditAugProd_9.setEnabled(True)
		self.lEditSepProd_9.setEnabled(True)
		self.lEditOctProd_9.setEnabled(True)
		self.lEditNovProd_9.setEnabled(True)
		self.lEditDecProd_9.setEnabled(True)

		self.lEditJanProd_10.setEnabled(True)
		self.lEditFebProd_10.setEnabled(True)
		self.lEditMarProd_10.setEnabled(True)
		self.lEditAprProd_10.setEnabled(True)
		self.lEditMayProd_10.setEnabled(True)
		self.lEditJunProd_10.setEnabled(True)
		self.lEditJulProd_10.setEnabled(True)
		self.lEditAugProd_10.setEnabled(True)
		self.lEditSepProd_10.setEnabled(True)
		self.lEditOctProd_10.setEnabled(True)
		self.lEditNovProd_10.setEnabled(True)
		self.lEditDecProd_10.setEnabled(True)

		self.lEditJanProd_11.setEnabled(True)
		self.lEditFebProd_11.setEnabled(True)
		self.lEditMarProd_11.setEnabled(True)
		self.lEditAprProd_11.setEnabled(True)
		self.lEditMayProd_11.setEnabled(True)
		self.lEditJunProd_11.setEnabled(True)
		self.lEditJulProd_11.setEnabled(True)
		self.lEditAugProd_11.setEnabled(True)
		self.lEditSepProd_11.setEnabled(True)
		self.lEditOctProd_11.setEnabled(True)
		self.lEditNovProd_11.setEnabled(True)
		self.lEditDecProd_11.setEnabled(True)

		self.lEditJanProd_12.setEnabled(True)
		self.lEditFebProd_12.setEnabled(True)
		self.lEditMarProd_12.setEnabled(True)
		self.lEditAprProd_12.setEnabled(True)
		self.lEditMayProd_12.setEnabled(True)
		self.lEditJunProd_12.setEnabled(True)
		self.lEditJulProd_12.setEnabled(True)
		self.lEditAugProd_12.setEnabled(True)
		self.lEditSepProd_12.setEnabled(True)
		self.lEditOctProd_12.setEnabled(True)
		self.lEditNovProd_12.setEnabled(True)
		self.lEditDecProd_12.setEnabled(True)

		self.lEditJanProd_13.setEnabled(True)
		self.lEditFebProd_13.setEnabled(True)
		self.lEditMarProd_13.setEnabled(True)
		self.lEditAprProd_13.setEnabled(True)
		self.lEditMayProd_13.setEnabled(True)
		self.lEditJunProd_13.setEnabled(True)
		self.lEditJulProd_13.setEnabled(True)
		self.lEditAugProd_13.setEnabled(True)
		self.lEditSepProd_13.setEnabled(True)
		self.lEditOctProd_13.setEnabled(True)
		self.lEditNovProd_13.setEnabled(True)
		self.lEditDecProd_13.setEnabled(True)

		self.lEditJanProd_14.setEnabled(True)
		self.lEditFebProd_14.setEnabled(True)
		self.lEditMarProd_14.setEnabled(True)
		self.lEditAprProd_14.setEnabled(True)
		self.lEditMayProd_14.setEnabled(True)
		self.lEditJunProd_14.setEnabled(True)
		self.lEditJulProd_14.setEnabled(True)
		self.lEditAugProd_14.setEnabled(True)
		self.lEditSepProd_14.setEnabled(True)
		self.lEditOctProd_14.setEnabled(True)
		self.lEditNovProd_14.setEnabled(True)
		self.lEditDecProd_14.setEnabled(True)

		self.lEditJanProd_15.setEnabled(True)
		self.lEditFebProd_15.setEnabled(True)
		self.lEditMarProd_15.setEnabled(True)
		self.lEditAprProd_15.setEnabled(True)
		self.lEditMayProd_15.setEnabled(True)
		self.lEditJunProd_15.setEnabled(True)
		self.lEditJulProd_15.setEnabled(True)
		self.lEditAugProd_15.setEnabled(True)
		self.lEditSepProd_15.setEnabled(True)
		self.lEditOctProd_15.setEnabled(True)
		self.lEditNovProd_15.setEnabled(True)
		self.lEditDecProd_15.setEnabled(True)

		self.lEditJanProd_16.setEnabled(True)
		self.lEditFebProd_16.setEnabled(True)
		self.lEditMarProd_16.setEnabled(True)
		self.lEditAprProd_16.setEnabled(True)
		self.lEditMayProd_16.setEnabled(True)
		self.lEditJunProd_16.setEnabled(True)
		self.lEditJulProd_16.setEnabled(True)
		self.lEditAugProd_16.setEnabled(True)
		self.lEditSepProd_16.setEnabled(True)
		self.lEditOctProd_16.setEnabled(True)
		self.lEditNovProd_16.setEnabled(True)
		self.lEditDecProd_16.setEnabled(True)

		self.lEditJanProd_17.setEnabled(True)
		self.lEditFebProd_17.setEnabled(True)
		self.lEditMarProd_17.setEnabled(True)
		self.lEditAprProd_17.setEnabled(True)
		self.lEditMayProd_17.setEnabled(True)
		self.lEditJunProd_17.setEnabled(True)
		self.lEditJulProd_17.setEnabled(True)
		self.lEditAugProd_17.setEnabled(True)
		self.lEditSepProd_17.setEnabled(True)
		self.lEditOctProd_17.setEnabled(True)
		self.lEditNovProd_17.setEnabled(True)
		self.lEditDecProd_17.setEnabled(True)

		self.lEditJanProd_18.setEnabled(True)
		self.lEditFebProd_18.setEnabled(True)
		self.lEditMarProd_18.setEnabled(True)
		self.lEditAprProd_18.setEnabled(True)
		self.lEditMayProd_18.setEnabled(True)
		self.lEditJunProd_18.setEnabled(True)
		self.lEditJulProd_18.setEnabled(True)
		self.lEditAugProd_18.setEnabled(True)
		self.lEditSepProd_18.setEnabled(True)
		self.lEditOctProd_18.setEnabled(True)
		self.lEditNovProd_18.setEnabled(True)
		self.lEditDecProd_18.setEnabled(True)

		self.lEditJanProd_19.setEnabled(True)
		self.lEditFebProd_19.setEnabled(True)
		self.lEditMarProd_19.setEnabled(True)
		self.lEditAprProd_19.setEnabled(True)
		self.lEditMayProd_19.setEnabled(True)
		self.lEditJunProd_19.setEnabled(True)
		self.lEditJulProd_19.setEnabled(True)
		self.lEditAugProd_19.setEnabled(True)
		self.lEditSepProd_19.setEnabled(True)
		self.lEditOctProd_19.setEnabled(True)
		self.lEditNovProd_19.setEnabled(True)
		self.lEditDecProd_19.setEnabled(True)

		self.lEditJanProd_20.setEnabled(True)
		self.lEditFebProd_20.setEnabled(True)
		self.lEditMarProd_20.setEnabled(True)
		self.lEditAprProd_20.setEnabled(True)
		self.lEditMayProd_20.setEnabled(True)
		self.lEditJunProd_20.setEnabled(True)
		self.lEditJulProd_20.setEnabled(True)
		self.lEditAugProd_20.setEnabled(True)
		self.lEditSepProd_20.setEnabled(True)
		self.lEditOctProd_20.setEnabled(True)
		self.lEditNovProd_20.setEnabled(True)
		self.lEditDecProd_20.setEnabled(True)

		self.lEditJanProd_21.setEnabled(True)
		self.lEditFebProd_21.setEnabled(True)
		self.lEditMarProd_21.setEnabled(True)
		self.lEditAprProd_21.setEnabled(True)
		self.lEditMayProd_21.setEnabled(True)
		self.lEditJunProd_21.setEnabled(True)
		self.lEditJulProd_21.setEnabled(True)
		self.lEditAugProd_21.setEnabled(True)
		self.lEditSepProd_21.setEnabled(True)
		self.lEditOctProd_21.setEnabled(True)
		self.lEditNovProd_21.setEnabled(True)
		self.lEditDecProd_21.setEnabled(True)

		self.lEditJanProd_22.setEnabled(True)
		self.lEditFebProd_22.setEnabled(True)
		self.lEditMarProd_22.setEnabled(True)
		self.lEditAprProd_22.setEnabled(True)
		self.lEditMayProd_22.setEnabled(True)
		self.lEditJunProd_22.setEnabled(True)
		self.lEditJulProd_22.setEnabled(True)
		self.lEditAugProd_22.setEnabled(True)
		self.lEditSepProd_22.setEnabled(True)
		self.lEditOctProd_22.setEnabled(True)
		self.lEditNovProd_22.setEnabled(True)
		self.lEditDecProd_22.setEnabled(True)

		self.lEditJanProd_23.setEnabled(True)
		self.lEditFebProd_23.setEnabled(True)
		self.lEditMarProd_23.setEnabled(True)
		self.lEditAprProd_23.setEnabled(True)
		self.lEditMayProd_23.setEnabled(True)
		self.lEditJunProd_23.setEnabled(True)
		self.lEditJulProd_23.setEnabled(True)
		self.lEditAugProd_23.setEnabled(True)
		self.lEditSepProd_23.setEnabled(True)
		self.lEditOctProd_23.setEnabled(True)
		self.lEditNovProd_23.setEnabled(True)
		self.lEditDecProd_23.setEnabled(True)

		self.lEditJanProd_24.setEnabled(True)
		self.lEditFebProd_24.setEnabled(True)
		self.lEditMarProd_24.setEnabled(True)
		self.lEditAprProd_24.setEnabled(True)
		self.lEditMayProd_24.setEnabled(True)
		self.lEditJunProd_24.setEnabled(True)
		self.lEditJulProd_24.setEnabled(True)
		self.lEditAugProd_24.setEnabled(True)
		self.lEditSepProd_24.setEnabled(True)
		self.lEditOctProd_24.setEnabled(True)
		self.lEditNovProd_24.setEnabled(True)
		self.lEditDecProd_24.setEnabled(True)

		self.lEditJanProd_25.setEnabled(True)
		self.lEditFebProd_25.setEnabled(True)
		self.lEditMarProd_25.setEnabled(True)
		self.lEditAprProd_25.setEnabled(True)
		self.lEditMayProd_25.setEnabled(True)
		self.lEditJunProd_25.setEnabled(True)
		self.lEditJulProd_25.setEnabled(True)
		self.lEditAugProd_25.setEnabled(True)
		self.lEditSepProd_25.setEnabled(True)
		self.lEditOctProd_25.setEnabled(True)
		self.lEditNovProd_25.setEnabled(True)
		self.lEditDecProd_25.setEnabled(True)

		self.lEditJanProd_26.setEnabled(True)
		self.lEditFebProd_26.setEnabled(True)
		self.lEditMarProd_26.setEnabled(True)
		self.lEditAprProd_26.setEnabled(True)
		self.lEditMayProd_26.setEnabled(True)
		self.lEditJunProd_26.setEnabled(True)
		self.lEditJulProd_26.setEnabled(True)
		self.lEditAugProd_26.setEnabled(True)
		self.lEditSepProd_26.setEnabled(True)
		self.lEditOctProd_26.setEnabled(True)
		self.lEditNovProd_26.setEnabled(True)
		self.lEditDecProd_26.setEnabled(True)

		self.lEditJanProd_27.setEnabled(True)
		self.lEditFebProd_27.setEnabled(True)
		self.lEditMarProd_27.setEnabled(True)
		self.lEditAprProd_27.setEnabled(True)
		self.lEditMayProd_27.setEnabled(True)
		self.lEditJunProd_27.setEnabled(True)
		self.lEditJulProd_27.setEnabled(True)
		self.lEditAugProd_27.setEnabled(True)
		self.lEditSepProd_27.setEnabled(True)
		self.lEditOctProd_27.setEnabled(True)
		self.lEditNovProd_27.setEnabled(True)
		self.lEditDecProd_27.setEnabled(True)

		self.lEditJanProd_28.setEnabled(True)
		self.lEditFebProd_28.setEnabled(True)
		self.lEditMarProd_28.setEnabled(True)
		self.lEditAprProd_28.setEnabled(True)
		self.lEditMayProd_28.setEnabled(True)
		self.lEditJunProd_28.setEnabled(True)
		self.lEditJulProd_28.setEnabled(True)
		self.lEditAugProd_28.setEnabled(True)
		self.lEditSepProd_28.setEnabled(True)
		self.lEditOctProd_28.setEnabled(True)
		self.lEditNovProd_28.setEnabled(True)
		self.lEditDecProd_28.setEnabled(True)

		self.lEditJanProd_29.setEnabled(True)
		self.lEditFebProd_29.setEnabled(True)
		self.lEditMarProd_29.setEnabled(True)
		self.lEditAprProd_29.setEnabled(True)
		self.lEditMayProd_29.setEnabled(True)
		self.lEditJunProd_29.setEnabled(True)
		self.lEditJulProd_29.setEnabled(True)
		self.lEditAugProd_29.setEnabled(True)
		self.lEditSepProd_29.setEnabled(True)
		self.lEditOctProd_29.setEnabled(True)
		self.lEditNovProd_29.setEnabled(True)
		self.lEditDecProd_29.setEnabled(True)

		self.lEditJanProd_30.setEnabled(True)
		self.lEditFebProd_30.setEnabled(True)
		self.lEditMarProd_30.setEnabled(True)
		self.lEditAprProd_30.setEnabled(True)
		self.lEditMayProd_30.setEnabled(True)
		self.lEditJunProd_30.setEnabled(True)
		self.lEditJulProd_30.setEnabled(True)
		self.lEditAugProd_30.setEnabled(True)
		self.lEditSepProd_30.setEnabled(True)
		self.lEditOctProd_30.setEnabled(True)
		self.lEditNovProd_30.setEnabled(True)
		self.lEditDecProd_30.setEnabled(True)

		self.lEditJanProd_31.setEnabled(True)
		self.lEditFebProd_31.setEnabled(True)
		self.lEditMarProd_31.setEnabled(True)
		self.lEditAprProd_31.setEnabled(True)
		self.lEditMayProd_31.setEnabled(True)
		self.lEditJunProd_31.setEnabled(True)
		self.lEditJulProd_31.setEnabled(True)
		self.lEditAugProd_31.setEnabled(True)
		self.lEditSepProd_31.setEnabled(True)
		self.lEditOctProd_31.setEnabled(True)
		self.lEditNovProd_31.setEnabled(True)
		self.lEditDecProd_31.setEnabled(True)

		self.lEditJanProd_32.setEnabled(True)
		self.lEditFebProd_32.setEnabled(True)
		self.lEditMarProd_32.setEnabled(True)
		self.lEditAprProd_32.setEnabled(True)
		self.lEditMayProd_32.setEnabled(True)
		self.lEditJunProd_32.setEnabled(True)
		self.lEditJulProd_32.setEnabled(True)
		self.lEditAugProd_32.setEnabled(True)
		self.lEditSepProd_32.setEnabled(True)
		self.lEditOctProd_32.setEnabled(True)
		self.lEditNovProd_32.setEnabled(True)
		self.lEditDecProd_32.setEnabled(True)

		self.lEditJanProd_33.setEnabled(True)
		self.lEditFebProd_33.setEnabled(True)
		self.lEditMarProd_33.setEnabled(True)
		self.lEditAprProd_33.setEnabled(True)
		self.lEditMayProd_33.setEnabled(True)
		self.lEditJunProd_33.setEnabled(True)
		self.lEditJulProd_33.setEnabled(True)
		self.lEditAugProd_33.setEnabled(True)
		self.lEditSepProd_33.setEnabled(True)
		self.lEditOctProd_33.setEnabled(True)
		self.lEditNovProd_33.setEnabled(True)
		self.lEditDecProd_33.setEnabled(True)

		self.lEditJanProd_34.setEnabled(True)
		self.lEditFebProd_34.setEnabled(True)
		self.lEditMarProd_34.setEnabled(True)
		self.lEditAprProd_34.setEnabled(True)
		self.lEditMayProd_34.setEnabled(True)
		self.lEditJunProd_34.setEnabled(True)
		self.lEditJulProd_34.setEnabled(True)
		self.lEditAugProd_34.setEnabled(True)
		self.lEditSepProd_34.setEnabled(True)
		self.lEditOctProd_34.setEnabled(True)
		self.lEditNovProd_34.setEnabled(True)
		self.lEditDecProd_34.setEnabled(True)"""
		
		self.pBtnUpdate.setEnabled(True)
	   
	def genera_excel(self,datos):
		import sales_esa_xls_report_generator
		genera_reporte = sales_esa_xls_report_generator
		genera_reporte.main(datos)

	def caja_mensaje (self, text, title, style):
		import caja_mensaje as mensaje
		mensaje.Caja_mensaje.mbox(text, title, style) 
		return 

	def close_window(self):
		self.close()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MyWindow = MyWindowClass(None)
	MyWindow.show()
	app.exec_()
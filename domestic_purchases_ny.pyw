#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In thismodule it is input the data of MB Domestic sales
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
form_class = uic.loadUiType("domestic purchases.ui")[0]

class MyWindowClass(QtWidgets.QDialog, form_class):
	def __init__(self, parent=None):
		
		QtWidgets.QDialog.__init__(self, parent)
		list_ingredients = ['Diced Red Pper', 'Strips Red Pper', 'Corn Kernels', 'Organic Broccoli Florets', 
							'prod5', 'prod6', 'prod7', 'prod8', 'prod9', 'prod10']
        


		self.setupUi(self)

		titles = self.set_titles(list_ingredients)


		self.pBtnSelectYear.setEnabled(True)
		self.pBtnUpdate.setEnabled(False)
		self.table = 'domesticpurchases'
		self.lock_fields()
		
		self.pBtnSave.clicked.connect(self.save_data)

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
			self.search_In_File(self.selected_year)
			self.inicializar_campós() # Set al fields as Zero
		

	def actual_Year(self):
		"""
		Function to get the current year from the system
		"""
		now = datetime.datetime.now()
		act_year = now.year
		return act_year 
	
	def search_In_File(self, year):
		self.list_keys = self.issue_keys()
		datos = pd.read_csv('domesticpurchases.csv', index_col = 0, encoding = 'utf-8' )
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
		dict_prod['Prod'] = list([
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
		dict_prod2['Prod2'] = list([
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
		dict_prod3['Prod3'] = list([
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
		dict_prod4['Prod4'] = list([
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
		dict_prod5['Prod5'] = list([
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
		dict_prod6['Prod6'] = list([
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
		dict_prod7['Prod7'] = list([
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
		dict_prod8['Prod8'] = list([
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
		dict_prod9['Prod9'] = list([
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
		dict_prod10['Prod10'] = list([
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

		np_total = np_prod + np_prod_2 + np_prod_3 + np_prod_4 + np_prod_5 + np_prod_6 + np_prod_7 + np_prod_8 + np_prod_9 +np_prod_10
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
		
		self.lblTotalPurchasesJan.setText(str(np_total_Jan))
		self.lblTotalPurchasesFeb.setText(str(np_total_Feb))
		self.lblTotalPurchasesMar.setText(str(np_total_Mar))
		self.lblTotalPurchasesApr.setText(str(np_total_Apr))
		self.lblTotalPurchasesMay.setText(str(np_total_May))
		self.lblTotalPurchasesJun.setText(str(np_total_Jun))
		self.lblTotalPurchasesJul.setText(str(np_total_Jul))
		self.lblTotalPurchasesAug.setText(str(np_total_Aug))
		self.lblTotalPurchasesSep.setText(str(np_total_Sep))
		self.lblTotalPurchasesOct.setText(str(np_total_Oct))
		self.lblTotalPurchasesNov.setText(str(np_total_Nov))
		self.lblTotalPurchasesDec.setText(str(np_total_Dec))

		self.lblTotalPurchasesAnual.setText(str(acum_total))

		self.pBtnSave.setEnabled(True)

	def inicializar_campós(self):
		"""

		This function set all field values as Zero
		"""
		self.lEditJanProd.insert(str(0))
		self.lEditFebProd.insert(str(0))
		self.lEditMarProd.insert(str(0))
		self.lEditAprProd.insert(str(0))
		self.lEditMayProd.insert(str(0))
		self.lEditJunProd.insert(str(0))
		self.lEditJulProd.insert(str(0))
		self.lEditAugProd.insert(str(0))
		self.lEditSepProd.insert(str(0))
		self.lEditOctProd.insert(str(0))
		self.lEditNovProd.insert(str(0))
		self.lEditDecProd.insert(str(0))

		self.lEditJanProd_2.insert(str(0))
		self.lEditFebProd_2.insert(str(0))
		self.lEditMarProd_2.insert(str(0))
		self.lEditAprProd_2.insert(str(0))
		self.lEditMayProd_2.insert(str(0))
		self.lEditJunProd_2.insert(str(0))
		self.lEditJulProd_2.insert(str(0))
		self.lEditAugProd_2.insert(str(0))
		self.lEditSepProd_2.insert(str(0))
		self.lEditOctProd_2.insert(str(0))
		self.lEditNovProd_2.insert(str(0))
		self.lEditDecProd_2.insert(str(0))

		self.lEditJanProd_3.insert(str(0))
		self.lEditFebProd_3.insert(str(0))
		self.lEditMarProd_3.insert(str(0))
		self.lEditAprProd_3.insert(str(0))
		self.lEditMayProd_3.insert(str(0))
		self.lEditJunProd_3.insert(str(0))
		self.lEditJulProd_3.insert(str(0))
		self.lEditAugProd_3.insert(str(0))
		self.lEditSepProd_3.insert(str(0))
		self.lEditOctProd_3.insert(str(0))
		self.lEditNovProd_3.insert(str(0))
		self.lEditDecProd_3.insert(str(0))

		self.lEditJanProd_4.insert(str(0))
		self.lEditFebProd_4.insert(str(0))
		self.lEditMarProd_4.insert(str(0))
		self.lEditAprProd_4.insert(str(0))
		self.lEditMayProd_4.insert(str(0))
		self.lEditJunProd_4.insert(str(0))
		self.lEditJulProd_4.insert(str(0))
		self.lEditAugProd_4.insert(str(0))
		self.lEditSepProd_4.insert(str(0))
		self.lEditOctProd_4.insert(str(0))
		self.lEditNovProd_4.insert(str(0))
		self.lEditDecProd_4.insert(str(0))

		self.lEditJanProd_5.insert(str(0))
		self.lEditFebProd_5.insert(str(0))
		self.lEditMarProd_5.insert(str(0))
		self.lEditAprProd_5.insert(str(0))
		self.lEditMayProd_5.insert(str(0))
		self.lEditJunProd_5.insert(str(0))
		self.lEditJulProd_5.insert(str(0))
		self.lEditAugProd_5.insert(str(0))
		self.lEditSepProd_5.insert(str(0))
		self.lEditOctProd_5.insert(str(0))
		self.lEditNovProd_5.insert(str(0))
		self.lEditDecProd_5.insert(str(0))

		self.lEditJanProd_6.insert(str(0))
		self.lEditFebProd_6.insert(str(0))
		self.lEditMarProd_6.insert(str(0))
		self.lEditAprProd_6.insert(str(0))
		self.lEditMayProd_6.insert(str(0))
		self.lEditJunProd_6.insert(str(0))
		self.lEditJulProd_6.insert(str(0))
		self.lEditAugProd_6.insert(str(0))
		self.lEditSepProd_6.insert(str(0))
		self.lEditOctProd_6.insert(str(0))
		self.lEditNovProd_6.insert(str(0))
		self.lEditDecProd_6.insert(str(0))

		self.lEditJanProd_7.insert(str(0))
		self.lEditFebProd_7.insert(str(0))
		self.lEditMarProd_7.insert(str(0))
		self.lEditAprProd_7.insert(str(0))
		self.lEditMayProd_7.insert(str(0))
		self.lEditJunProd_7.insert(str(0))
		self.lEditJulProd_7.insert(str(0))
		self.lEditAugProd_7.insert(str(0))
		self.lEditSepProd_7.insert(str(0))
		self.lEditOctProd_7.insert(str(0))
		self.lEditNovProd_7.insert(str(0))
		self.lEditDecProd_7.insert(str(0))

		self.lEditJanProd_8.insert(str(0))
		self.lEditFebProd_8.insert(str(0))
		self.lEditMarProd_8.insert(str(0))
		self.lEditAprProd_8.insert(str(0))
		self.lEditMayProd_8.insert(str(0))
		self.lEditJunProd_8.insert(str(0))
		self.lEditJulProd_8.insert(str(0))
		self.lEditAugProd_8.insert(str(0))
		self.lEditSepProd_8.insert(str(0))
		self.lEditOctProd_8.insert(str(0))
		self.lEditNovProd_8.insert(str(0))
		self.lEditDecProd_8.insert(str(0))

		self.lEditJanProd_9.insert(str(0))
		self.lEditFebProd_9.insert(str(0))
		self.lEditMarProd_9.insert(str(0))
		self.lEditAprProd_9.insert(str(0))
		self.lEditMayProd_9.insert(str(0))
		self.lEditJunProd_9.insert(str(0))
		self.lEditJulProd_9.insert(str(0))
		self.lEditAugProd_9.insert(str(0))
		self.lEditSepProd_9.insert(str(0))
		self.lEditOctProd_9.insert(str(0))
		self.lEditNovProd_9.insert(str(0))
		self.lEditDecProd_9.insert(str(0))

		self.lEditJanProd_10.insert(str(0))
		self.lEditFebProd_10.insert(str(0))
		self.lEditMarProd_10.insert(str(0))
		self.lEditAprProd_10.insert(str(0))
		self.lEditMayProd_10.insert(str(0))
		self.lEditJunProd_10.insert(str(0))
		self.lEditJulProd_10.insert(str(0))
		self.lEditAugProd_10.insert(str(0))
		self.lEditSepProd_10.insert(str(0))
		self.lEditOctProd_10.insert(str(0))
		self.lEditNovProd_10.insert(str(0))
		self.lEditDecProd_10.insert(str(0))
		

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
				
		
				
				
			data = {values : [ sequence, indice, year, month, prod, prod_2, prod_3, prod_4,
					prod_5, prod_6, prod_7, prod_8, prod_9, prod_10]}
			data_dict.update(data)
			

		message = 'Now we are going to save the file'
		self.caja_mensaje('Save data;', message,0)
		datos_domestic_Purchases =pd.read_csv('domesticpurchases.csv', index_col = 0, encoding = 'utf-8')
		datos_domestic_Purchases.apply(lambda x: pd.lib.infer_dtype(x.values))
		num_datos = int(datos_domestic_Purchases['indice'].count())
		datos_domestic_Purchases.index = range(datos_domestic_Purchases.shape[0])
		indice_archivo = list(datos_domestic_Purchases.indice)
		llaves = data_dict.keys()
		nuevo_Valor = num_datos+1
		valores = list(data_dict.values())
		print(valores)
			
		for i, valor in enumerate(valores):
			nuevo_valor = int(nuevo_Valor)+i
			print(nuevo_valor, i, valor)
			datos_domestic_Purchases.loc[int(nuevo_valor)]= [
				valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], 
				valor[8], valor[9], valor[10], valor[11], valor[12], 
				valor[13]]
		try: 
			datos_domestic_Purchases.to_csv('domesticpurchases.csv',  encoding = 'utf-8',) 
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

		print(list_ingredients[0])
		print(list_ingredients[1])
		print(list_ingredients[2])
		print(list_ingredients[3])
		print(list_ingredients[4])
		print(list_ingredients[5])
		print(list_ingredients[6])
		print(list_ingredients[7])
		print(list_ingredients[8])
		print(list_ingredients[9])
		
		
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
		
	def unlock_fields(self):

		self.lEditJanProd.setEnabled(True)
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

		self.pBtnUpdate.setEnabled(True)
	   
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
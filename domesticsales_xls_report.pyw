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
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem
from PyQt5 import uic
import datetime
import pandas as pd
import cajaMensajePregunta as cajaMensaje

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("domestic_sales-ny2.ui")[0]

class MyWindowClass(QtWidgets.QDialog, form_class):
	def __init__(self, parent=None):
		
		QtWidgets.QDialog.__init__(self, parent)

		self.setupUi(self)

		self.pBtnSelectYear.setEnabled(True)
		self.pBtnUpdate.setEnabled(False)
		self.table = 'domesticsales'
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
			self.read_data_from_file(self.selected_year)
	
	def read_data_from_file(self, year):	
			message = ' reading, Data from file '
			self.caja_mensaje('Message ', message,0)	
			self.list_keys = self.issue_keys()
			datos = pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8' )
			datos.apply(lambda x: pd.lib.infer_dtype(x.values))
			print(year)
			print('los datos son: \n',datos)
			datos = datos.loc [datos['year'] == year]
			datos.index = range(datos.shape[0])
	
			
			Dict_Conv_Brocc = {'Conv Brocc': list(datos['broc_Conv'])}
			Dict_Org_Brocc = {'Org Brocc': list(datos['brocc_Org'])}
			Dict_Conv_Caulif = {'Conv Cauliflower': list(datos['cauliflower'])}
			Dict_Org_Caulif = {'Org Cauliflower': list(datos['Caulif_Org'])}
			Dict_Crinkle_Carrot = {'Carrot Crinkle Conv': list(datos['Crinkle_Carrot'])}
			Dict_Diced_Carrot = {'Carrot Diced Conv': list(datos['Dcd_Carrot'])}
			Dict_Org_Carrot = {'Org Carrots': list(datos['Org_Carrot'])}
			Dict_GZucc = {'Green Zucchini': list(datos['GZucc'])}
			Dict_Peas = {'Peas': list(datos['Peas'])}
			Dict_Poblano = {'Poblano': list(datos['Poblano'])}
			Dict_WCorn = {'Whole Corn': list(datos['WCorn'])}	
			Dict_Total_Corn = {'Total Corn': list(datos['Total_Corn'])}	
			Dict_Green_Beans = {'Green Beans': list(datos['GreenBeans'])}	
			Dict_Mushrooms = {'Mushrooms': list(datos['Mushrooms'])}	
			Dict_Onion = {'Onion': list(datos['Onion'])}	
			Dict_Potatoes = {'Potatoes': list(datos['Potatoes'])}	
			Dict_RedPepper = {'Red Pepper': list(datos['RedPepper'])}	
			Dict_snowPeas = {'Red Snow Peas': list(datos['snowPeas'])}	
			Dict_Spinach = {'Spinach': list(datos['Spinach'])}	
			Dict_WCN = {'Water Ch Nuts': list(datos['WCN'])}	
			Dict_Others = {'Others': list(datos['Others'])}	


			Dict_Final = {}
			Dict_Final['Conv Brocc'] = list(datos['broc_Conv'])
			Dict_Final['Org Brocc'] = list(datos['brocc_Org'])
			Dict_Final['Conv Cauliflower'] = list(datos['cauliflower'])
			Dict_Final['Org Cauliflower'] = list(datos['Caulif_Org'])
			Dict_Final['Carrot Crinkle Conv'] = list(datos['Crinkle_Carrot'])
			Dict_Final['Carrot Diced Conv'] = list(datos['Dcd_Carrot'])
			Dict_Final['Org Carrots'] = list(datos['Org_Carrot'])
			Dict_Final['Green Zucchini'] = list(datos['GZucc'])
			Dict_Final['Peas'] = list(datos['Peas'])
			Dict_Final['Poblano'] = list(datos['Poblano'])
			Dict_Final['Whole Corn'] = list(datos['WCorn'])
			Dict_Final['Total Corn'] = list(datos['Total_Corn'])
			Dict_Final['Potatoes'] = list(datos['Potatoes'])
			Dict_Final['Onion'] = list(datos['Onion'])
			Dict_Final['Green Beans'] = list(datos['GreenBeans'])
			Dict_Final['Mushrooms'] = list(datos['Mushrooms'])
			Dict_Final['Red Pepper'] = list(datos['RedPepper'])
			Dict_Final['Snow Peas'] = list(datos['snowPeas'])
			Dict_Final['Spinach'] = list(datos['Spinach'])
			Dict_Final['Water Ch Nuts'] = list(datos['WCN'])
			Dict_Final['Others'] = list(datos['Others'])
			



			self.inicializar_campós(Dict_Final)
			

	def actual_Year(self):
		"""
		Function to get the current year from the system
		"""
		now = datetime.datetime.now()
		act_year = now.year
		return act_year 
	
	def update_labels(self,datos):
		datos2 = datos.items()
		#Jan_Total_Sales = datos.get('Total_Sales')


		
	def search_In_File(self, year):
		self.list_keys = self.issue_keys()
		datos = pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8' )
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
		"""
		This function is used to get the totals  that will be displayed 
		"""
		self.list_keys = self.issue_keys()
		self.read_data_from_fields()
		"""
		Sum of all products per month
		"""
		Tot_Conv_Carrot_Jan = self.Conv_Carrot_Month(
			self.ConvCarrCrklJan, self.ConvCarrDcdJan)
		self.lblTotalConvCarrotJan.setText(str(round(Tot_Conv_Carrot_Jan,0)))

		Tot_Conv_Carrot_Feb = self.Conv_Carrot_Month(
			self.ConvCarrCrklFeb, self.ConvCarrDcdFeb)
		self.lblTotalConvCarrotFeb.setText(str(round(Tot_Conv_Carrot_Feb,0)))

		Tot_Conv_Carrot_Feb = self.Conv_Carrot_Month(
			self.ConvCarrCrklFeb, self.ConvCarrDcdFeb)
		self.lblTotalConvCarrotFeb.setText(str(round(Tot_Conv_Carrot_Feb,0)))

		Tot_Conv_Carrot_Mar = self.Conv_Carrot_Month(
			self.ConvCarrCrklMar, self.ConvCarrDcdMar)
		self.lblTotalConvCarrotMar.setText(str(round(Tot_Conv_Carrot_Mar,0)))

		Tot_Conv_Carrot_Apr = self.Conv_Carrot_Month(
			self.ConvCarrCrklApr, self.ConvCarrDcdApr)
		self.lblTotalConvCarrotApr.setText(str(round(Tot_Conv_Carrot_Apr,0)))

		Tot_Conv_Carrot_May = self.Conv_Carrot_Month(
			self.ConvCarrCrklMay, self.ConvCarrDcdMay)
		self.lblTotalConvCarrotMay.setText(str(round(Tot_Conv_Carrot_May,0)))

		Tot_Conv_Carrot_Jun = self.Conv_Carrot_Month(
			self.ConvCarrCrklJun, self.ConvCarrDcdJun)
		self.lblTotalConvCarrotJun.setText(str(round(Tot_Conv_Carrot_Jun,0)))

		Tot_Conv_Carrot_Jul = self.Conv_Carrot_Month(
			self.ConvCarrCrklJul, self.ConvCarrDcdJul)
		self.lblTotalConvCarrotJul.setText(str(round(Tot_Conv_Carrot_Jul,0)))

		Tot_Conv_Carrot_Aug = self.Conv_Carrot_Month(
			self.ConvCarrCrklAug, self.ConvCarrDcdAug)
		self.lblTotalConvCarrotAug.setText(str(round(Tot_Conv_Carrot_Aug,0)))

		Tot_Conv_Carrot_Sep = self.Conv_Carrot_Month(
			self.ConvCarrCrklSep, self.ConvCarrDcdSep)
		self.lblTotalConvCarrotSep.setText(str(round(Tot_Conv_Carrot_Sep,0)))

		Tot_Conv_Carrot_Oct = self.Conv_Carrot_Month(
			self.ConvCarrCrklOct, self.ConvCarrDcdOct)
		self.lblTotalConvCarrotOct.setText(str(round(Tot_Conv_Carrot_Oct,0)))

		Tot_Conv_Carrot_Nov = self.Conv_Carrot_Month(
			self.ConvCarrCrklNov, self.ConvCarrDcdNov)
		self.lblTotalConvCarrotNov.setText(str(round(Tot_Conv_Carrot_Nov,0)))

		Tot_Conv_Carrot_Dec = self.Conv_Carrot_Month(
			self.ConvCarrCrklDec, self.ConvCarrDcdDec)
		self.lblTotalConvCarrotDec.setText(str(round(Tot_Conv_Carrot_Dec,0)))


		Tot_Anual_Conv_Carrots = self.suma(Tot_Conv_Carrot_Jan, Tot_Conv_Carrot_Feb, 
						Tot_Conv_Carrot_Mar, Tot_Conv_Carrot_Apr, Tot_Conv_Carrot_May,
						Tot_Conv_Carrot_Jun, Tot_Conv_Carrot_Jul, Tot_Conv_Carrot_Aug,
						Tot_Conv_Carrot_Sep, Tot_Conv_Carrot_Oct, Tot_Conv_Carrot_Nov,
						Tot_Conv_Carrot_Dec)
		self.lblTotAnualConvCarrot.setText(str(Tot_Anual_Conv_Carrots))
		
		Conv_Brocc_Total_Anual = self.suma(self.Brocc_Conv_Jan, self.Brocc_Conv_Feb, self.Brocc_Conv_Mar,
						self.Brocc_Conv_Apr, self.Brocc_Conv_May, self.Brocc_Conv_Jun,
						self.Brocc_Conv_Jul, self.Brocc_Conv_Aug, self.Brocc_Conv_Sep,
						self.Brocc_Conv_Oct, self.Brocc_Conv_Nov, self.Brocc_Conv_Dec)
		self.lblTotalAnualConvBrocc.setText(str(Conv_Brocc_Total_Anual))



		Org_Brocc_Total_Anual = self.suma(self.broc_Org_Jan, self.broc_Org_Feb, self.broc_Org_Mar,
						self.broc_Org_Apr, self.broc_Org_May, self.broc_Org_Jun,
						self.broc_Org_Jul, self.broc_Org_Aug, self.broc_Org_Sep,
						self.broc_Org_Oct, self.broc_Org_Nov, self.broc_Org_Dec)
		self.lblTotalAnualOrgBroc.setText(str(Org_Brocc_Total_Anual))
		


		Conv_Caulif_Total_Anual = self.suma(self.Caulif_Jan, self.Caulif_Feb, self.Caulif_Mar,
						self.Caulif_Apr, self.Caulif_May, self.Caulif_Jun,
						self.Caulif_Jul, self.Caulif_Aug, self.Caulif_Sep,
						self.Caulif_Oct, self.Caulif_Nov, self.Caulif_Dec)
		self.lblTotalAnualCaulif.setText(str(Conv_Caulif_Total_Anual))

		Org_Caulif_Total_Anual = self.suma(self.Caulif_Org_Jan, self.Caulif_Org_Feb, self.Caulif_Org_Mar,
						self.Caulif_Org_Apr, self.Caulif_Org_May, self.Caulif_Org_Jun,
						self.Caulif_Org_Jul, self.Caulif_Org_Aug, self.Caulif_Org_Sep,
						self.Caulif_Org_Oct, self.Caulif_Org_Nov, self.Caulif_Org_Dec)
		self.lblTotalAnualOrgCauli.setText(str(Org_Caulif_Total_Anual))

		Carrot_Crkle_Total = self.suma(self.ConvCarrCrklJan, self.ConvCarrCrklFeb, self.ConvCarrCrklMar,
						self.ConvCarrCrklApr, self.ConvCarrCrklMay, self.ConvCarrCrklJun,
						self.ConvCarrCrklJul, self.ConvCarrCrklAug, self.ConvCarrCrklSep,
						self.ConvCarrCrklOct, self.ConvCarrCrklNov, self.ConvCarrCrklDec)
		self.lblTotalAnualConvCarrCrkl.setText(str(Carrot_Crkle_Total))

		
		Carrot_Dcd_Total = self.suma(self.ConvCarrDcdJan, self.ConvCarrDcdFeb, self.ConvCarrDcdMar,
						self.ConvCarrDcdApr, self.ConvCarrDcdMay, self.ConvCarrDcdJun,
						self.ConvCarrDcdJul, self.ConvCarrDcdAug, self.ConvCarrDcdSep,
						self.ConvCarrDcdOct, self.ConvCarrDcdNov, self.ConvCarrDcdDec)	
		self.lblTotalAnualConvCarrDcd.setText(str(Carrot_Dcd_Total))


		Carrot_Org_Total = self.suma(self.OrgCarrotJan, self.OrgCarrotFeb, self.OrgCarrotMar,
						self.OrgCarrotApr, self.OrgCarrotMay, self.OrgCarrotJun,
						self.OrgCarrotJul, self.OrgCarrotAug, self.OrgCarrotSep,
						self.OrgCarrotOct, self.OrgCarrotNov, self.OrgCarrotDec)	
		self.lblTotAnualCarrotOrg.setText(str(Carrot_Org_Total))

		GZucc_Total = self.suma(self.GZucc_Jan, self.GZucc_Feb, self.GZucc_Mar,
						self.GZucc_Apr, self.GZucc_May, self.GZucc_Jun,
						self.GZucc_Jul, self.GZucc_Aug, self.GZucc_Sep,
						self.GZucc_Oct, self.GZucc_Nov, self.GZucc_Dec)	
		self.lblTotalAnualGZucc.setText(str(GZucc_Total))
		

		Peas_Total = self.suma(self.Peas_Jan, self.Peas_Feb, self.Peas_Mar,
						self.Peas_Apr, self.Peas_May, self.Peas_Jun,
						self.Peas_Jul, self.Peas_Aug, self.Peas_Sep,
						self.Peas_Oct, self.Peas_Nov, self.Peas_Dec)	
		self.lblTotalAnualPeas.setText(str(Peas_Total))

		Poblano_Total = self.suma(self.Poblano_Jan, self.Poblano_Feb, self.Poblano_Mar,
						self.Poblano_Apr, self.Poblano_May, self.Poblano_Jun,
						self.Poblano_Jul, self.Poblano_Aug, self.Poblano_Sep,
						self.Poblano_Oct, self.Poblano_Nov, self.Poblano_Dec)	
		self.lblTotalAnualPoblano.setText(str(Poblano_Total))		

		WCorn_Total = self.suma(self.WCorn_Jan, self.WCorn_Feb, self.WCorn_Mar, 
						self.WCorn_Apr, self.WCorn_May, self.WCorn_Jun,
						self.WCorn_Jul, self.WCorn_Aug, self.WCorn_Sep, 
						self.WCorn_Oct, self.WCorn_Nov, self.WCorn_Dec)	
		self.lblTotWCorn.setText(str(WCorn_Total))		

		Total_Corn_Total = self.suma(self.Total_Corn_Jan, self.Total_Corn_Feb, self.Total_Corn_Mar,
						self.Total_Corn_Apr, self.Total_Corn_May, self.Total_Corn_Jun,
						self.Total_Corn_Jul, self.Total_Corn_Aug, self.Total_Corn_Sep,
						self.Total_Corn_Oct, self.Total_Corn_Nov, self.Total_Corn_Dec)	
		self.lblTotCornAnual.setText(str(Total_Corn_Total))								

		GBreans_Total = self.suma(self.GreenBeans_Jan, self.GreenBeans_Feb, self.GreenBeans_Mar,
						self.GreenBeans_Apr, self.GreenBeans_May, self.GreenBeans_Jun,
						self.GreenBeans_Jul, self.GreenBeans_Aug, self.GreenBeans_Sep,
						self.GreenBeans_Oct, self.GreenBeans_Nov, self.GreenBeans_Dec)	
		self.lblTotalAnualGreenBeans.setText(str(GBreans_Total))				
		

		Mush_Total = self.suma(self.Mush_Jan, self.Mush_Feb, self.Mush_Mar,
						self.Mush_Apr, self.Mush_May, self.Mush_Jun,
						self.Mush_Jul, self.Mush_Aug, self.Mush_Sep,
						self.Mush_Oct, self.Mush_Nov, self.Mush_Dec)	
		self.lblTotalAnualMush.setText(str(Mush_Total))				

		Onion_Total = self.suma(self.Onion_Jan, self.Onion_Feb, self.Onion_Mar,
						self.Onion_Apr, self.Onion_May, self.Onion_Jun,
						self.Onion_Jul, self.Onion_Aug, self.Onion_Sep,
						self.Onion_Oct, self.Onion_Nov, self.Onion_Dec)	
		self.lblTotalAnualOnion.setText(str(Onion_Total))				

		Potatoes_Total = self.suma(self.Potatoes_Jan, self.Potatoes_Feb, self.Potatoes_Mar,
						self.Potatoes_Apr, self.Potatoes_May, self.Potatoes_Jun,
						self.Potatoes_Jul, self.Potatoes_Aug, self.Potatoes_Sep,
						self.Potatoes_Oct,self.Potatoes_Nov, self.Potatoes_Dec)	
		self.lblTotalAnualPotatoes.setText(str(Potatoes_Total))				

		RedPepper_Total = self.suma(self.RedPepper_Jan, self.RedPepper_Feb, self.RedPepper_Mar,
						self.RedPepper_Apr, self.RedPepper_May, self.RedPepper_Jun,
						self.RedPepper_Jul, self.RedPepper_Aug, self.RedPepper_Sep,
						self.RedPepper_Oct, self.RedPepper_Nov, self.RedPepper_Dec)	
		self.lblTotalAnualRedPepper.setText(str(RedPepper_Total))				
		
		SnowPeas_Total = self.suma(self.SnowPeas_Jan, self.SnowPeas_Feb, self.SnowPeas_Mar,
						self.SnowPeas_Apr, self.SnowPeas_May, self.SnowPeas_Jun,
						self.SnowPeas_Jul, self.SnowPeas_Aug, self.SnowPeas_Sep,
						self.SnowPeas_Oct,self.SnowPeas_Nov, self.SnowPeas_Dec)	
		self.lblTotAnualSnowPeas.setText(str(SnowPeas_Total))	

		Spinach_Total = self.suma(self.Spinach_Jan, self.Spinach_Feb, self.Spinach_Mar,
						self.Spinach_Apr, self.Spinach_May, self.Spinach_Jun,
						self.Spinach_Jul, self.Spinach_Aug, self.Spinach_Sep,
						self.Spinach_Oct, self.Spinach_Nov, self.Spinach_Dec)	
		self.lblTotalAnualSpinach.setText(str(Spinach_Total))			


		WCN_Total = self.suma(self.WCN_Jan, self.WCN_Feb, self.WCN_Mar,
						self.WCN_Apr, self.WCN_May, self.WCN_Jun,
						self.WCN_Jul, self.WCN_Aug,self.WCN_Sep,
						self.WCN_Oct,self.WCN_Nov,self.WCN_Dec)	
		self.lblTotalAnualWCN.setText(str(WCN_Total))					


		Others_Total = self.suma(self.Others_Jan, self.Others_Feb, self.Others_Mar,
						self.Others_Apr, self.Others_May, self.Others_Jun,
						self.Others_Jul, self.Others_Aug,self.Others_Sep,
						self.Others_Oct, self.Others_Nov, self.Others_Dec)	
		self.lblTotalAnualOthers.setText(str(Others_Total))							

		"""
		Sum of all Conventional products per month
		"""
		self.Total_Jan_Conv = self.suma(self.Brocc_Conv_Jan, self.Caulif_Jan, self.ConvCarrCrklJan, 
							self.ConvCarrDcdJan,self.GZucc_Jan, self.Peas_Jan, self.Poblano_Jan,
							 self.Total_Corn_Jan, self.GreenBeans_Jan,
							 self.Mush_Jan, self.Onion_Jan, self.Potatoes_Jan, self.RedPepper_Jan,
							 self.SnowPeas_Jan, self.Spinach_Jan, self.WCN_Jan, self.Others_Jan )
		self.lblTotalJanConv.setText(str(self.Total_Jan_Conv))							

		self.Total_Feb_Conv = self.suma(self.Brocc_Conv_Feb, self.Caulif_Feb, self.ConvCarrCrklFeb, 
							self.ConvCarrDcdFeb,self.GZucc_Feb, self.Peas_Feb, self.Poblano_Feb,
							 self.Total_Corn_Feb, self.GreenBeans_Feb,
							 self.Mush_Feb, self.Onion_Feb, self.Potatoes_Feb, self.RedPepper_Feb,
							 self.SnowPeas_Feb, self.Spinach_Feb, self.WCN_Feb, self.Others_Feb )
		self.lblTotalFebConv.setText(str(self.Total_Feb_Conv))							

		self.Total_Mar_Conv = self.suma(self.Brocc_Conv_Mar, self.Caulif_Mar, self.ConvCarrCrklMar, 
							self.ConvCarrDcdMar,self.GZucc_Mar, self.Peas_Mar, self.Poblano_Mar,
							 self.Total_Corn_Mar, self.GreenBeans_Mar,
							 self.Mush_Mar, self.Onion_Mar, self.Potatoes_Mar, self.RedPepper_Mar,
							 self.SnowPeas_Mar, self.Spinach_Mar, self.WCN_Mar, self.Others_Mar )
		self.lblTotalMarConv.setText(str(self.Total_Mar_Conv))							

		self.Total_Apr_Conv = self.suma(self.Brocc_Conv_Apr, self.Caulif_Apr, self.ConvCarrCrklApr, 
							self.ConvCarrDcdApr,self.GZucc_Apr, self.Peas_Apr, self.Poblano_Apr,
							 self.Total_Corn_Apr, self.GreenBeans_Apr,
							 self.Mush_Apr, self.Onion_Apr, self.Potatoes_Apr, self.RedPepper_Apr,
							 self.SnowPeas_Apr, self.Spinach_Apr, self.WCN_Apr, self.Others_Apr )
		self.lblTotalAprConv.setText(str(self.Total_Apr_Conv))							


		self.Total_May_Conv = self.suma(self.Brocc_Conv_May, self.Caulif_May, self.ConvCarrCrklMay, 
							self.ConvCarrDcdMay,self.GZucc_May, self.Peas_May, self.Poblano_May,
							 self.Total_Corn_May, self.GreenBeans_May,
							 self.Mush_May, self.Onion_May, self.Potatoes_May, self.RedPepper_May,
							 self.SnowPeas_May, self.Spinach_May, self.WCN_May, self.Others_May )
		self.lblTotalMayConv.setText(str(self.Total_May_Conv))							

		self.Total_Jun_Conv = self.suma(self.Brocc_Conv_Jun, self.Caulif_Jun, self.ConvCarrCrklJun, 
							self.ConvCarrDcdJun,self.GZucc_Jun, self.Peas_Jun, self.Poblano_Jun,
							 self.Total_Corn_Jun, self.GreenBeans_Jun,
							 self.Mush_Jun, self.Onion_Jun, self.Potatoes_Jun, self.RedPepper_Jun,
							 self.SnowPeas_Jun, self.Spinach_Jun, self.WCN_Jun, self.Others_Jun )
		self.lblTotalJunConv.setText(str(self.Total_Jun_Conv))							


		self.Total_Jul_Conv = self.suma(self.Brocc_Conv_Jul, self.Caulif_Jul, self.ConvCarrCrklJul, 
							self.ConvCarrDcdJul,self.GZucc_Jul, self.Peas_Jul, self.Poblano_Jul,
							 self.Total_Corn_Jul, self.GreenBeans_Jul,
							 self.Mush_Jul, self.Onion_Jul, self.Potatoes_Jul, self.RedPepper_Jul,
							 self.SnowPeas_Jul, self.Spinach_Jul, self.WCN_Jul, self.Others_Jul )
		self.lblTotalJulConv.setText(str(self.Total_Jul_Conv))							

		self.Total_Aug_Conv = self.suma(self.Brocc_Conv_Aug, self.Caulif_Aug, self.ConvCarrCrklAug, 
							self.ConvCarrDcdAug,self.GZucc_Aug, self.Peas_Aug, self.Poblano_Aug,
							 self.Total_Corn_Aug, self.GreenBeans_Aug,
							 self.Mush_Aug, self.Onion_Aug, self.Potatoes_Aug, self.RedPepper_Aug,
							 self.SnowPeas_Aug, self.Spinach_Aug, self.WCN_Aug, self.Others_Aug )
		self.lblTotalAugConv.setText(str(self.Total_Aug_Conv))							

		self.Total_Sep_Conv = self.suma(self.Brocc_Conv_Sep, self.Caulif_Sep, self.ConvCarrCrklSep, 
							self.ConvCarrDcdSep,self.GZucc_Sep, self.Peas_Sep, self.Poblano_Sep,
							 self.Total_Corn_Sep, self.GreenBeans_Sep,
							 self.Mush_Sep, self.Onion_Sep, self.Potatoes_Sep, self.RedPepper_Sep,
							 self.SnowPeas_Sep, self.Spinach_Sep, self.WCN_Sep, self.Others_Sep )
		self.lblTotalSepConv.setText(str(self.Total_Sep_Conv))							

		self.Total_Oct_Conv = self.suma(self.Brocc_Conv_Oct, self.Caulif_Oct, self.ConvCarrCrklOct, 
							self.ConvCarrDcdOct,self.GZucc_Oct, self.Peas_Oct, self.Poblano_Oct,
							 self.Total_Corn_Oct, self.GreenBeans_Oct,
							 self.Mush_Oct, self.Onion_Oct, self.Potatoes_Oct, self.RedPepper_Oct,
							 self.SnowPeas_Oct, self.Spinach_Oct, self.WCN_Oct, self.Others_Oct )
		self.lblTotalOctConv.setText(str(self.Total_Oct_Conv))							

		self.Total_Nov_Conv = self.suma(self.Brocc_Conv_Nov, self.Caulif_Nov, self.ConvCarrCrklNov, 
							self.ConvCarrDcdNov,self.GZucc_Nov, self.Peas_Nov, self.Poblano_Nov,
							 self.Total_Corn_Nov, self.GreenBeans_Nov,
							 self.Mush_Nov, self.Onion_Nov, self.Potatoes_Nov, self.RedPepper_Nov,
							 self.SnowPeas_Nov, self.Spinach_Nov, self.WCN_Nov, self.Others_Nov )
		self.lblTotalNovConv.setText(str(self.Total_Nov_Conv))							

		self.Total_Dec_Conv = self.suma(self.Brocc_Conv_Dec, self.Caulif_Dec, self.ConvCarrCrklDec, 
							self.ConvCarrDcdDec,self.GZucc_Dec, self.Peas_Dec, self.Poblano_Dec,
							 self.Total_Corn_Dec, self.GreenBeans_Dec,
							 self.Mush_Dec, self.Onion_Dec, self.Potatoes_Dec, self.RedPepper_Dec,
							 self.SnowPeas_Dec, self.Spinach_Dec, self.WCN_Dec, self.Others_Dec )
		self.lblTotalDecConv.setText(str(self.Total_Dec_Conv))							

		"""
		Sum of all Organic Products per month
		"""
		Tot_Org_Jan = self.suma_Org_Jan(
			self.broc_Org_Jan, self.Caulif_Org_Jan, self.OrgCarrotJan)

		Tot_Org_Feb = self.suma_Org_Feb(
			self.broc_Org_Feb, self.Caulif_Org_Feb, self.OrgCarrotFeb)

		Tot_Org_Mar = self.suma_Org_Mar(
			self.broc_Org_Mar, self.Caulif_Org_Mar, self.OrgCarrotMar)

		Tot_Org_Apr = self.suma_Org_Apr(
			self.broc_Org_Apr, self.Caulif_Org_Apr, self.OrgCarrotApr)

		Tot_Org_May = self.suma_Org_May(
			self.broc_Org_May, self.Caulif_Org_May, self.OrgCarrotMay)

		Tot_Org_Jun = self.suma_Org_Jun(
			self.broc_Org_Jun, self.Caulif_Org_Jun, self.OrgCarrotJun)

		Tot_Org_Jul = self.suma_Org_Jul(
			self.broc_Org_Jul, self.Caulif_Org_Jul, self.OrgCarrotJul)

		Tot_Org_Aug = self.suma_Org_Aug(
			self.broc_Org_Aug, self.Caulif_Org_Aug, self.OrgCarrotAug)

		Tot_Org_Sep = self.suma_Org_Sep(
			self.broc_Org_Sep, self.Caulif_Org_Sep, self.OrgCarrotSep)

		Tot_Org_Oct = self.suma_Org_Oct(
			self.broc_Org_Oct, self.Caulif_Org_Oct, self.OrgCarrotOct)

		Tot_Org_Nov = self.suma_Org_Nov(
			self.broc_Org_Nov, self.Caulif_Org_Nov, self.OrgCarrotNov)

		Tot_Org_Dec = self.suma_Org_Dec(
			self.broc_Org_Dec, self.Caulif_Org_Dec, self.OrgCarrotDec)

		Total_Org_Anual = self.suma(
			Tot_Org_Jan, Tot_Org_Feb, Tot_Org_Mar, Tot_Org_Apr, 
			Tot_Org_May, Tot_Org_Jun, Tot_Org_Jul, Tot_Org_Aug, 
			Tot_Org_Sep, Tot_Org_Oct, Tot_Org_Nov, Tot_Org_Dec)
		
		self.lblTotalAnualOrg.setText(str(Total_Org_Anual))

		"""
		Sum of Conventional Plus Orgarnic
		"""

		self.total_Sales_Jan = self.suma(self.Total_Jan_Conv,Tot_Org_Jan)
		self.lblTotalSalesJan.setText(str(self.total_Sales_Jan))

		self.total_Sales_Feb = self.suma(self.Total_Feb_Conv,Tot_Org_Feb)
		self.lblTotalSalesFeb.setText(str(self.total_Sales_Feb))

		self.total_Sales_Mar = self.suma(self.Total_Mar_Conv,Tot_Org_Mar)
		self.lblTotalSalesMar.setText(str(self.total_Sales_Mar))

		self.total_Sales_Apr = self.suma(self.Total_Apr_Conv,Tot_Org_Apr)
		self.lblTotalSalesApr.setText(str(self.total_Sales_Apr))

		self.total_Sales_May = self.suma(self.Total_May_Conv,Tot_Org_May)
		self.lblTotalSalesMay.setText(str(self.total_Sales_May))

		self.total_Sales_Jun = self.suma(self.Total_Jun_Conv,Tot_Org_Jun)
		self.lblTotalSalesJun.setText(str(self.total_Sales_Jun))

		self.total_Sales_Jul = self.suma(self.Total_Jul_Conv,Tot_Org_Jul)
		self.lblTotalSalesJul.setText(str(self.total_Sales_Jul))

		self.total_Sales_Aug = self.suma(self.Total_Aug_Conv,Tot_Org_Aug)
		self.lblTotalSalesAug.setText(str(self.total_Sales_Aug))

		self.total_Sales_Sep = self.suma(self.Total_Sep_Conv,Tot_Org_Sep)
		self.lblTotalSalesSep.setText(str(self.total_Sales_Sep))

		self.total_Sales_Oct = self.suma(self.Total_Oct_Conv,Tot_Org_Oct)
		self.lblTotalSalesOct.setText(str(self.total_Sales_Oct))

		self.total_Sales_Nov = self.suma(self.Total_Nov_Conv,Tot_Org_Nov)
		self.lblTotalSalesNov.setText(str(self.total_Sales_Nov))

		self.total_Sales_Dec = self.suma(self.Total_Dec_Conv,Tot_Org_Dec)
		self.lblTotalSalesDec.setText(str(self.total_Sales_Dec))

		Total_Sales_Anual = self.suma(
			self.total_Sales_Jan, self.total_Sales_Feb, self.total_Sales_Mar,
			self.total_Sales_Apr, self.total_Sales_May, self.total_Sales_Jun,
			self.total_Sales_Jul, self.total_Sales_Aug, self.total_Sales_Sep,
			self.total_Sales_Oct, self.total_Sales_Nov, self.total_Sales_Dec)
		
		self.lblTotalSalesAnual.setText(str(Total_Sales_Anual))


		self.Sweet_Corn_Jan = self.Sweet_Corn_Month(
			self.Total_Corn_Jan, self.WCorn_Jan)
		self.lblSweetCornJan.setText(str(self.Sweet_Corn_Jan))

		self.Sweet_Corn_Feb = self.Sweet_Corn_Month(
			self.Total_Corn_Feb, self.WCorn_Feb)
		self.lblSweetCornFeb.setText(str(self.Sweet_Corn_Feb))

		self.Sweet_Corn_Mar = self.Sweet_Corn_Month(
			self.Total_Corn_Mar, self.WCorn_Mar)
		self.lblSweetCornMar.setText(str(self.Sweet_Corn_Mar))

		self.Sweet_Corn_Apr = self.Sweet_Corn_Month(
			self.Total_Corn_Apr, self.WCorn_Apr)
		self.lblSweetCornApr.setText(str(self.Sweet_Corn_Apr))

		self.Sweet_Corn_May = self.Sweet_Corn_Month(
			self.Total_Corn_May, self.WCorn_May)
		self.lblSweetCornMay.setText(str(self.Sweet_Corn_May))

		self.Sweet_Corn_Jun = self.Sweet_Corn_Month(
			self.Total_Corn_Jun, self.WCorn_Jun)
		self.lblSweetCornJun.setText(str(self.Sweet_Corn_Jun))

		self.Sweet_Corn_Jul = self.Sweet_Corn_Month(
			self.Total_Corn_Jul, self.WCorn_Jul)
		self.lblSweetCornJul.setText(str(self.Sweet_Corn_Jul))

		self.Sweet_Corn_Aug = self.Sweet_Corn_Month(
			self.Total_Corn_Aug, self.WCorn_Aug)
		self.lblSweetCornAug.setText(str(self.Sweet_Corn_Aug))

		self.Sweet_Corn_Sep = self.Sweet_Corn_Month(
			self.Total_Corn_Sep, self.WCorn_Sep)
		self.lblSweetCornSep.setText(str(self.Sweet_Corn_Sep))

		self.Sweet_Corn_Oct = self.Sweet_Corn_Month(
			self.Total_Corn_Oct, self.WCorn_Oct)
		self.lblSweetCornOct.setText(str(self.Sweet_Corn_Oct))

		self.Sweet_Corn_Nov = self.Sweet_Corn_Month(
			self.Total_Corn_Nov, self.WCorn_Nov)
		self.lblSweetCornNov.setText(str(self.Sweet_Corn_Nov))

		self.Sweet_Corn_Dec = self.Sweet_Corn_Month(
			self.Total_Corn_Dec, self.WCorn_Dec)
		self.lblSweetCornDec.setText(str(self.Sweet_Corn_Dec))

		self.Total_Sweet_Corn = self.suma(
			self.Sweet_Corn_Jan, self.Sweet_Corn_Feb, self.Sweet_Corn_Mar, self.Sweet_Corn_Apr, 
			self.Sweet_Corn_May, self.Sweet_Corn_Jun, self.Sweet_Corn_Jul, self.Sweet_Corn_Aug, 
			self.Sweet_Corn_Sep, self.Sweet_Corn_Oct, self.Sweet_Corn_Nov, self.Sweet_Corn_Dec)
		self.lblTotAnualSweetCorn.setText(str(self.Total_Sweet_Corn))


		Total_Anual_Conv = self.suma(
			self.Total_Jan_Conv, self.Total_Feb_Conv, self.Total_Mar_Conv, self.Total_Apr_Conv, 
			self.Total_May_Conv, self.Total_Jun_Conv, self.Total_Jul_Conv, self.Total_Aug_Conv, 
			self.Total_Sep_Conv, self.Total_Oct_Conv, self.Total_Nov_Conv, self.Total_Dec_Conv)
		self.lblTotalAnualConv.setText(str(Total_Anual_Conv))


		

		Dict_Conv_Brocc = {}
		Dict_Conv_Brocc['Conventional_Broccoli'] = list([
			self.Brocc_Conv_Jan, self.Brocc_Conv_Feb, self.Brocc_Conv_Mar, 
			self.Brocc_Conv_Apr, self.Brocc_Conv_May, self.Brocc_Conv_Jun, 
			self.Brocc_Conv_Jul, self.Brocc_Conv_Aug, self.Brocc_Conv_Sep, 
			self.Brocc_Conv_Oct, self.Brocc_Conv_Nov, self.Brocc_Conv_Dec])		

		Dict_Brocc_Org = {}
		Dict_Brocc_Org['Broccoli Org'] = list([
						self.broc_Org_Jan, self.broc_Org_Feb, self.broc_Org_Mar,
						self.broc_Org_Apr, self.broc_Org_May, self.broc_Org_Jun,
						self.broc_Org_Jul, self.broc_Org_Aug, self.broc_Org_Sep,
						self.broc_Org_Oct, self.broc_Org_Nov, self.broc_Org_Dec])

		Dict_Total_Caulif = {}
		Dict_Total_Caulif['Total Cauliflower'] = list([
						self.Caulif_Jan, self.Caulif_Feb, self.Caulif_Mar,
						self.Caulif_Apr, self.Caulif_May, self.Caulif_Jun,
						self.Caulif_Jul, self.Caulif_Aug, self.Caulif_Sep,
						self.Caulif_Oct, self.Caulif_Nov, self.Caulif_Dec])

		Dict_Caulif_Org = {}
		Dict_Caulif_Org['Cauliflower Org'] = list([
						self.Caulif_Org_Jan, self.Caulif_Org_Feb, self.Caulif_Org_Mar,
						self.Caulif_Org_Apr, self.Caulif_Org_May, self.Caulif_Org_Jun,
						self.Caulif_Org_Jul, self.Caulif_Org_Aug, self.Caulif_Org_Sep,
						self.Caulif_Org_Oct, self.Caulif_Org_Nov, self.Caulif_Org_Dec])


		Dict_Crinkle_Carrot = {}
		Dict_Crinkle_Carrot['Conv. Crinke Carrots'] = list([
						self.ConvCarrCrklJan, self.ConvCarrCrklFeb, self.ConvCarrCrklMar,
						self.ConvCarrCrklApr, self.ConvCarrCrklMay, self.ConvCarrCrklJun,
						self.ConvCarrCrklJul, self.ConvCarrCrklAug, self.ConvCarrCrklSep,
						self.ConvCarrCrklOct, self.ConvCarrCrklNov, self.ConvCarrCrklDec])

		Dict_Diced_Carrot = {}
		Dict_Diced_Carrot['Conv. Diced Carrots'] = list([
						self.ConvCarrDcdJan, self.ConvCarrDcdFeb, self.ConvCarrDcdMar,
						self.ConvCarrDcdApr, self.ConvCarrDcdMay, self.ConvCarrDcdJun,
						self.ConvCarrDcdJul, self.ConvCarrDcdAug, self.ConvCarrDcdSep,
						self.ConvCarrDcdOct, self.ConvCarrDcdNov, self.ConvCarrDcdDec])

		Dict_Conv_Carrot = {}
		Dict_Conv_Carrot['Total Conv. Carrots'] = list([
						Tot_Conv_Carrot_Jan, Tot_Conv_Carrot_Feb, 
						Tot_Conv_Carrot_Mar, Tot_Conv_Carrot_Apr, Tot_Conv_Carrot_May,
						Tot_Conv_Carrot_Jun, Tot_Conv_Carrot_Jul, Tot_Conv_Carrot_Aug,
						Tot_Conv_Carrot_Sep, Tot_Conv_Carrot_Oct, Tot_Conv_Carrot_Nov,
						Tot_Conv_Carrot_Dec])


			
		Dict_Carrots_Org = {}
		Dict_Carrots_Org['Carrots Org'] = list([
						self.OrgCarrotJan, self.OrgCarrotFeb, self.OrgCarrotMar,
						self.OrgCarrotApr, self.OrgCarrotMay, self.OrgCarrotJun,
						self.OrgCarrotJul, self.OrgCarrotAug, self.OrgCarrotSep,
						self.OrgCarrotOct, self.OrgCarrotNov, self.OrgCarrotDec])


		Dict_Green_Zucc = {}
		Dict_Green_Zucc['Green Zucchini'] = list([
						self.GZucc_Jan, self.GZucc_Feb, self.GZucc_Mar,
						self.GZucc_Apr, self.GZucc_May, self.GZucc_Jun,
						self.GZucc_Jul, self.GZucc_Aug, self.GZucc_Sep,
						self.GZucc_Oct, self.GZucc_Nov, self.GZucc_Dec])
		


		Dict_Peas = {}
		Dict_Peas['Peas'] = list([
						self.Peas_Jan, self.Peas_Feb, self.Peas_Mar,
						self.Peas_Apr, self.Peas_May, self.Peas_Jun,
						self.Peas_Jul, self.Peas_Aug, self.Peas_Sep,
						self.Peas_Oct, self.Peas_Nov, self.Peas_Dec])
		
		Dict_Poblano = {}
		Dict_Poblano['Poblano'] = list([
						self.Poblano_Jan, self.Poblano_Feb, self.Poblano_Mar,
						self.Poblano_Apr, self.Poblano_May, self.Poblano_Jun,
						self.Poblano_Jul, self.Poblano_Aug, self.Poblano_Sep,
						self.Poblano_Oct, self.Poblano_Nov, self.Poblano_Dec])
		
		dict_WCorn = {}
		dict_WCorn['Whole Corn'] = list([
						self.WCorn_Jan, self.WCorn_Feb, self.WCorn_Mar, 
						self.WCorn_Apr, self.WCorn_May, self.WCorn_Jun,
						self.WCorn_Jul, self.WCorn_Aug, self.WCorn_Sep, 
						self.WCorn_Oct, self.WCorn_Nov, self.WCorn_Dec])
		
		dict_Total_Corn = {}
		dict_Total_Corn['Total Corn'] = list([
						self.Total_Corn_Jan, self.Total_Corn_Feb, self.Total_Corn_Mar,
						self.Total_Corn_Apr, self.Total_Corn_May, self.Total_Corn_Jun,
						self.Total_Corn_Jul, self.Total_Corn_Aug, self.Total_Corn_Sep,
						self.Total_Corn_Oct, self.Total_Corn_Nov, self.Total_Corn_Dec])

		dict_Sweet_Corn = {}
		dict_Sweet_Corn ['Sweet Corn'] =  list([
						self.Sweet_Corn_Jan, self.Sweet_Corn_Feb, self.Sweet_Corn_Mar, 
						self.Sweet_Corn_Apr, self.Sweet_Corn_May, self.Sweet_Corn_Jun, 
						self.Sweet_Corn_Jul, self.Sweet_Corn_Aug, self.Sweet_Corn_Sep, 
						self.Sweet_Corn_Oct, self.Sweet_Corn_Nov, self.Sweet_Corn_Dec])

		Dict_Green_Beans = {}
		Dict_Green_Beans['Green Beans'] = list([
						self.GreenBeans_Jan, self.GreenBeans_Feb, self.GreenBeans_Mar,
						self.GreenBeans_Apr, self.GreenBeans_May, self.GreenBeans_Jun,
						self.GreenBeans_Jul, self.GreenBeans_Aug, self.GreenBeans_Sep,
						self.GreenBeans_Oct, self.GreenBeans_Nov, self.GreenBeans_Dec])

		Dict_Mushrooms = {}
		Dict_Mushrooms['Mushrooms'] = list([
						self.Mush_Jan, self.Mush_Feb, self.Mush_Mar,
						self.Mush_Apr, self.Mush_May, self.Mush_Jun,
						self.Mush_Jul, self.Mush_Aug, self.Mush_Sep,
						self.Mush_Oct, self.Mush_Nov, self.Mush_Dec])

		Dict_Onion = {}
		Dict_Onion['Onion'] = list([
						self.Onion_Jan, self.Onion_Feb, self.Onion_Mar,
						self.Onion_Apr, self.Onion_May, self.Onion_Jun,
						self.Onion_Jul, self.Onion_Aug, self.Onion_Sep,
						self.Onion_Oct, self.Onion_Nov, self.Onion_Dec])

		Dict_Potatoes = {}
		Dict_Potatoes['Potatoes'] = list([
						self.Potatoes_Jan, self.Potatoes_Feb, self.Potatoes_Mar,
						self.Potatoes_Apr, self.Potatoes_May, self.Potatoes_Jun,
						self.Potatoes_Jul, self.Potatoes_Aug, self.Potatoes_Sep,
						self.Potatoes_Oct,self.Potatoes_Nov, self.Potatoes_Dec])


		Dict_RedPepper = {}
		Dict_RedPepper['Red Pepper'] = list([
						self.RedPepper_Jan, self.RedPepper_Feb, self.RedPepper_Mar,
						self.RedPepper_Apr, self.RedPepper_May, self.RedPepper_Jun,
						self.RedPepper_Jul, self.RedPepper_Aug, self.RedPepper_Sep,
						self.RedPepper_Oct, self.RedPepper_Nov, self.RedPepper_Dec])

		Dict_Snow_Peas = {}
		Dict_Snow_Peas['Snow Peas'] = list([
						self.SnowPeas_Jan, self.SnowPeas_Feb, self.SnowPeas_Mar,
						self.SnowPeas_Apr, self.SnowPeas_May, self.SnowPeas_Jun,
						self.SnowPeas_Jul, self.SnowPeas_Aug, self.SnowPeas_Sep,
						self.SnowPeas_Oct,self.SnowPeas_Nov, self.SnowPeas_Dec])
				
		Dict_Spinach = {}
		Dict_Spinach['Spinach'] = list([
						self.Spinach_Jan, self.Spinach_Feb, self.Spinach_Mar,
						self.Spinach_Apr, self.Spinach_May, self.Spinach_Jun,
						self.Spinach_Jul, self.Spinach_Aug, self.Spinach_Sep,
						self.Spinach_Oct, self.Spinach_Nov, self.Spinach_Dec])
		
		Dict_WCN = {}
		Dict_WCN['Water Chest Nuts'] = list([
						self.WCN_Jan, self.WCN_Feb, self.WCN_Mar,
						self.WCN_Apr, self.WCN_May, self.WCN_Jun,
						self.WCN_Jul, self.WCN_Aug,self.WCN_Sep,
						self.WCN_Oct,self.WCN_Nov,self.WCN_Dec])
		

		Dict_Others = {}
		Dict_Others['Others'] = list([
						self.Others_Jan, self.Others_Feb, self.Others_Mar,
						self.Others_Apr, self.Others_May, self.Others_Jun,
						self.Others_Jul, self.Others_Aug,self.Others_Sep,
						self.Others_Oct, self.Others_Nov, self.Others_Dec])
		
		
		dict_Tot_Org = {}
		dict_Tot_Org['Total_Org'] = list([
					Tot_Org_Jan, Tot_Org_Feb, Tot_Org_Mar, Tot_Org_Apr, 
					Tot_Org_May, Tot_Org_Jun, Tot_Org_Jul, Tot_Org_Aug, 
					Tot_Org_Sep, Tot_Org_Oct, Tot_Org_Nov, Tot_Org_Dec])

		dict_Tot_Conv = {}
		dict_Tot_Conv['Total Conv'] = list([
					self.Total_Jan_Conv, self.Total_Feb_Conv, self.Total_Mar_Conv, self.Total_Apr_Conv, 
					self.Total_May_Conv, self.Total_Jun_Conv, self.Total_Jul_Conv, self.Total_Aug_Conv, 
					self.Total_Sep_Conv, self.Total_Oct_Conv, self.Total_Nov_Conv, self.Total_Dec_Conv])
		
		Dict_Total_Sales = {}
		Dict_Total_Sales['Total Sales'] = list([
			self.total_Sales_Jan, self.total_Sales_Feb, self.total_Sales_Mar,
			self.total_Sales_Apr, self.total_Sales_May, self.total_Sales_Jun,
			self.total_Sales_Jul, self.total_Sales_Aug, self.total_Sales_Sep,
			self.total_Sales_Oct, self.total_Sales_Nov, self.total_Sales_Dec])
		
		
		self.data_complete = [
						Dict_Conv_Brocc, Dict_Brocc_Org, Dict_Total_Caulif, Dict_Caulif_Org,
						Dict_Crinkle_Carrot, Dict_Diced_Carrot, Dict_Conv_Carrot, Dict_Carrots_Org,
						Dict_Green_Zucc, Dict_Peas, Dict_Poblano, dict_WCorn, dict_Total_Corn, 
						dict_Sweet_Corn, Dict_Green_Beans, Dict_Mushrooms, Dict_Onion,
						 Dict_Potatoes, Dict_RedPepper, Dict_Snow_Peas, Dict_Spinach,
						 Dict_WCN, Dict_Others, dict_Tot_Org, dict_Tot_Conv, Dict_Total_Sales]
		
		print(self.data_complete)
		input()

		#self.pBtnReport.setEnabled(True)
		generaExcel =self.genera_excel(self.data_complete)
		


	
	def genera_excel(self,datos):
		import report_domesticsales_xls
		genera_reporte = report_domesticsales_xls
		genera_reporte.main(datos)


	def inicializar_campós(self,datos):

		"""
		This function set all field values as the value in the file
		"""

		Conv_Brocc = datos.get('Conv Brocc')
		print('impresion de broccoli convencional Diccionario',Conv_Brocc)
		self.lEditConvBroccJan.insert(str(Conv_Brocc[0]))
		self.lEditConvBroccFeb.insert(str(Conv_Brocc[1]))
		self.lEditConvBroccMar.insert(str(Conv_Brocc[2]))
		self.lEditConvBroccApr.insert(str(Conv_Brocc[3]))
		self.lEditConvBroccMay.insert(str(Conv_Brocc[4]))
		self.lEditConvBroccJun.insert(str(Conv_Brocc[5]))
		self.lEditConvBroccJul.insert(str(Conv_Brocc[6]))
		self.lEditConvBroccAug.insert(str(Conv_Brocc[7]))
		self.lEditConvBroccSep.insert(str(Conv_Brocc[8]))
		self.lEditConvBroccOct.insert(str(Conv_Brocc[9]))
		self.lEditConvBroccNov.insert(str(Conv_Brocc[10]))
		self.lEditConvBroccDec.insert(str(Conv_Brocc[11]))
						
								
		Org_Brocc = datos.get('Org Brocc')
		self.lEditOrgBroccJan.insert(str(Org_Brocc[0]))
		self.lEditOrgBroccFeb.insert(str(Org_Brocc[1]))
		self.lEditOrgBroccMar.insert(str(Org_Brocc[2]))
		self.lEditOrgBroccApr.insert(str(Org_Brocc[3]))
		self.lEditOrgBroccMay.insert(str(Org_Brocc[4]))
		self.lEditOrgBroccJun.insert(str(Org_Brocc[5]))
		self.lEditOrgBroccJul.insert(str(Org_Brocc[6]))
		self.lEditOrgBroccAug.insert(str(Org_Brocc[7]))
		self.lEditOrgBroccSep.insert(str(Org_Brocc[8]))
		self.lEditOrgBroccOct.insert(str(Org_Brocc[9]))
		self.lEditOrgBroccNov.insert(str(Org_Brocc[10]))
		self.lEditOrgBroccDec.insert(str(Org_Brocc[11]))
						
		Cauliflower = datos.get('Conv Cauliflower')
		self.lEditCaulifJan.insert(str(Cauliflower[0]))
		self.lEditCaulifFeb.insert(str(Cauliflower[1]))
		self.lEditCaulifMar.insert(str(Cauliflower[2]))
		self.lEditCaulifApr.insert(str(Cauliflower[3]))
		self.lEditCaulifMay.insert(str(Cauliflower[4]))
		self.lEditCaulifJun.insert(str(Cauliflower[5]))
		self.lEditCaulifJul.insert(str(Cauliflower[6]))
		self.lEditCaulifAug.insert(str(Cauliflower[7]))
		self.lEditCaulifSep.insert(str(Cauliflower[8]))
		self.lEditCaulifOct.insert(str(Cauliflower[9]))
		self.lEditCaulifNov.insert(str(Cauliflower[10]))
		self.lEditCaulifDec.insert(str(Cauliflower[11]))
						
		Org_Cauliflower = datos.get('Org Cauliflower')
		self.lEditOrgCauliJan.insert(str(Org_Cauliflower[0]))
		self.lEditOrgCauliFeb.insert(str(Org_Cauliflower[1]))
		self.lEditOrgCauliMar.insert(str(Org_Cauliflower[2]))
		self.lEditOrgCauliApr.insert(str(Org_Cauliflower[3]))
		self.lEditOrgCauliMay.insert(str(Org_Cauliflower[4]))
		self.lEditOrgCauliJun.insert(str(Org_Cauliflower[5]))
		self.lEditOrgCauliJul.insert(str(Org_Cauliflower[6]))
		self.lEditOrgCauliAug.insert(str(Org_Cauliflower[7]))
		self.lEditOrgCauliSep.insert(str(Org_Cauliflower[8]))
		self.lEditOrgCauliOct.insert(str(Org_Cauliflower[9]))
		self.lEditOrgCauliNov.insert(str(Org_Cauliflower[10]))
		self.lEditOrgCauliDec.insert(str(Org_Cauliflower[11]))
						
		Conv_Carrot_Crkl = datos.get('Carrot Crinkle Conv')
		self.lEditConvCarrCrklJan.insert(str(Conv_Carrot_Crkl[0]))
		self.lEditConvCarrCrklFeb.insert(str(Conv_Carrot_Crkl[1]))
		self.lEditConvCarrCrklMar.insert(str(Conv_Carrot_Crkl[2]))
		self.lEditConvCarrCrklApr.insert(str(Conv_Carrot_Crkl[3]))
		self.lEditConvCarrCrklMay.insert(str(Conv_Carrot_Crkl[4]))
		self.lEditConvCarrCrklJun.insert(str(Conv_Carrot_Crkl[5]))
		self.lEditConvCarrCrklJul.insert(str(Conv_Carrot_Crkl[6]))
		self.lEditConvCarrCrklAug.insert(str(Conv_Carrot_Crkl[7]))
		self.lEditConvCarrCrklSep.insert(str(Conv_Carrot_Crkl[8]))
		self.lEditConvCarrCrklOct.insert(str(Conv_Carrot_Crkl[9]))
		self.lEditConvCarrCrklNov.insert(str(Conv_Carrot_Crkl[10]))
		self.lEditConvCarrCrklDec.insert(str(Conv_Carrot_Crkl[11]))
						
		Conv_Carrot_Dcd = datos.get('Carrot Diced Conv')
		self.lEditConvCarrDcdJan.insert(str(Conv_Carrot_Dcd[0]))
		self.lEditConvCarrDcdFeb.insert(str(Conv_Carrot_Dcd[1]))
		self.lEditConvCarrDcdMar.insert(str(Conv_Carrot_Dcd[2]))
		self.lEditConvCarrDcdApr.insert(str(Conv_Carrot_Dcd[3]))
		self.lEditConvCarrDcdMay.insert(str(Conv_Carrot_Dcd[4]))
		self.lEditConvCarrDcdJun.insert(str(Conv_Carrot_Dcd[5]))
		self.lEditConvCarrDcdJul.insert(str(Conv_Carrot_Dcd[6]))
		self.lEditConvCarrDcdAug.insert(str(Conv_Carrot_Dcd[7]))
		self.lEditConvCarrDcdSep.insert(str(Conv_Carrot_Dcd[8]))
		self.lEditConvCarrDcdOct.insert(str(Conv_Carrot_Dcd[9]))
		self.lEditConvCarrDcdNov.insert(str(Conv_Carrot_Dcd[10]))
		self.lEditConvCarrDcdDec.insert(str(Conv_Carrot_Dcd[11]))
						
		Org_Carrots = datos.get('Org Carrots')
		self.lEditCarrotsOrgJan.insert(str(Org_Carrots[0]))
		self.lEditCarrotsOrgFeb.insert(str(Org_Carrots[1]))
		self.lEditCarrotsOrgMar.insert(str(Org_Carrots[2]))
		self.lEditCarrotsOrgApr.insert(str(Org_Carrots[3]))
		self.lEditCarrotsOrgMay.insert(str(Org_Carrots[4]))
		self.lEditCarrotsOrgJun.insert(str(Org_Carrots[5]))
		self.lEditCarrotsOrgJul.insert(str(Org_Carrots[6]))
		self.lEditCarrotsOrgAug.insert(str(Org_Carrots[7]))
		self.lEditCarrotsOrgSep.insert(str(Org_Carrots[8]))
		self.lEditCarrotsOrgOct.insert(str(Org_Carrots[9]))
		self.lEditCarrotsOrgNov.insert(str(Org_Carrots[10]))
		self.lEditCarrotsOrgDec.insert(str(Org_Carrots[11]))
		
		Green_Zucchini = datos.get('Green Zucchini')
		self.lEditGZuccJan.insert(str(Green_Zucchini[0]))
		self.lEditGZuccFeb.insert(str(Green_Zucchini[1]))
		self.lEditGZuccMar.insert(str(Green_Zucchini[2]))
		self.lEditGZuccApr.insert(str(Green_Zucchini[3]))
		self.lEditGZuccMay.insert(str(Green_Zucchini[4]))
		self.lEditGZuccJun.insert(str(Green_Zucchini[5]))
		self.lEditGZuccJul.insert(str(Green_Zucchini[6]))
		self.lEditGZuccAug.insert(str(Green_Zucchini[7]))
		self.lEditGZuccSep.insert(str(Green_Zucchini[8]))
		self.lEditGZuccOct.insert(str(Green_Zucchini[9]))
		self.lEditGZuccNov.insert(str(Green_Zucchini[10]))
		self.lEditGZuccDec.insert(str(Green_Zucchini[11]))
		
		Peas = datos.get('Peas')
		self.lEditPeasJan.insert(str(Peas[0]))
		self.lEditPeasFeb.insert(str(Peas[1]))
		self.lEditPeasMar.insert(str(Peas[2]))
		self.lEditPeasApr.insert(str(Peas[3]))
		self.lEditPeasMay.insert(str(Peas[4]))
		self.lEditPeasJun.insert(str(Peas[5]))
		self.lEditPeasJul.insert(str(Peas[6]))
		self.lEditPeasAug.insert(str(Peas[7]))
		self.lEditPeasSep.insert(str(Peas[8]))
		self.lEditPeasOct.insert(str(Peas[9]))
		self.lEditPeasNov.insert(str(Peas[10]))
		self.lEditPeasDec.insert(str(Peas[11]))
						
		Poblano = datos.get('Poblano')
		self.lEditPoblanoJan.insert(str(Poblano[0]))
		self.lEditPoblanoFeb.insert(str(Poblano[1]))
		self.lEditPoblanoMar.insert(str(Poblano[2]))
		self.lEditPoblanoApr.insert(str(Poblano[3]))
		self.lEditPoblanoMay.insert(str(Poblano[4]))
		self.lEditPoblanoJun.insert(str(Poblano[5]))
		self.lEditPoblanoJul.insert(str(Poblano[6]))
		self.lEditPoblanoAug.insert(str(Poblano[7]))
		self.lEditPoblanoSep.insert(str(Poblano[8]))
		self.lEditPoblanoOct.insert(str(Poblano[9]))
		self.lEditPoblanoNov.insert(str(Poblano[10]))
		self.lEditPoblanoDec.insert(str(Poblano[11]))
						
		WCorn = datos.get('Whole Corn')
		self.lEditWCornJan.insert(str(WCorn[0]))
		self.lEditWCornFeb.insert(str(WCorn[1]))
		self.lEditWCornMar.insert(str(WCorn[2]))
		self.lEditWCornApr.insert(str(WCorn[3]))
		self.lEditWCornMay.insert(str(WCorn[4]))
		self.lEditWCornJun.insert(str(WCorn[5]))
		self.lEditWCornJul.insert(str(WCorn[6]))
		self.lEditWCornAug.insert(str(WCorn[7]))
		self.lEditWCornSep.insert(str(WCorn[8]))
		self.lEditWCornOct.insert(str(WCorn[9]))
		self.lEditWCornNov.insert(str(WCorn[10]))
		self.lEditWCornDec.insert(str(WCorn[11]))
						
		total_Corn = datos.get('Total Corn')
		self.lEditTotalCornJan.insert(str(total_Corn[0]))
		self.lEditTotalCornFeb.insert(str(total_Corn[1]))
		self.lEditTotalCornMar.insert(str(total_Corn[2]))
		self.lEditTotalCornApr.insert(str(total_Corn[3]))
		self.lEditTotalCornMay.insert(str(total_Corn[4]))
		self.lEditTotalCornJun.insert(str(total_Corn[5]))
		self.lEditTotalCornJul.insert(str(total_Corn[6]))
		self.lEditTotalCornAug.insert(str(total_Corn[7]))
		self.lEditTotalCornSep.insert(str(total_Corn[8]))
		self.lEditTotalCornOct.insert(str(total_Corn[9]))
		self.lEditTotalCornNov.insert(str(total_Corn[10]))
		self.lEditTotalCornDec.insert(str(total_Corn[11]))
						
		green_Beans = datos.get('Green Beans')
		self.lEditGreenBeansJan.insert(str(green_Beans[0]))
		self.lEditGreenBeansFeb.insert(str(green_Beans[1]))
		self.lEditGreenBeansMar.insert(str(green_Beans[2]))
		self.lEditGreenBeansApr.insert(str(green_Beans[3]))
		self.lEditGreenBeansMay.insert(str(green_Beans[4]))
		self.lEditGreenBeansJun.insert(str(green_Beans[5]))
		self.lEditGreenBeansJul.insert(str(green_Beans[6]))
		self.lEditGreenBeansAug.insert(str(green_Beans[7]))
		self.lEditGreenBeansSep.insert(str(green_Beans[8]))
		self.lEditGreenBeansOct.insert(str(green_Beans[9]))
		self.lEditGreenBeansNov.insert(str(green_Beans[10]))
		self.lEditGreenBeansDec.insert(str(green_Beans[11]))
						
		mushrooms = datos.get('Mushrooms')
		self.lEditMushJan.insert(str(mushrooms[0]))
		self.lEditMushFeb.insert(str(mushrooms[1]))
		self.lEditMushMar.insert(str(mushrooms[2]))
		self.lEditMushApr.insert(str(mushrooms[3]))
		self.lEditMushMay.insert(str(mushrooms[4]))
		self.lEditMushJun.insert(str(mushrooms[5]))
		self.lEditMushJul.insert(str(mushrooms[6]))
		self.lEditMushAug.insert(str(mushrooms[7]))
		self.lEditMushSep.insert(str(mushrooms[8]))
		self.lEditMushOct.insert(str(mushrooms[9]))
		self.lEditMushNov.insert(str(mushrooms[10]))
		self.lEditMushDec.insert(str(mushrooms[11]))
						
		onion = datos.get('Onion')
		self.lEditOnionJan.insert(str(onion[0]))
		self.lEditOnionFeb.insert(str(onion[1]))
		self.lEditOnionMar.insert(str(onion[2]))
		self.lEditOnionApr.insert(str(onion[3]))
		self.lEditOnionMay.insert(str(onion[4]))
		self.lEditOnionJun.insert(str(onion[5]))
		self.lEditOnionJul.insert(str(onion[6]))
		self.lEditOnionAug.insert(str(onion[7]))
		self.lEditOnionSep.insert(str(onion[8]))
		self.lEditOnionOct.insert(str(onion[9]))
		self.lEditOnionNov.insert(str(onion[10]))
		self.lEditOnionDec.insert(str(onion[11]))
						
		potatoes = datos.get('Potatoes')
		self.lEditPotatoesJan.insert(str(potatoes[0]))
		self.lEditPotatoesFeb.insert(str(potatoes[1]))
		self.lEditPotatoesMar.insert(str(potatoes[2]))
		self.lEditPotatoesApr.insert(str(potatoes[3]))
		self.lEditPotatoesMay.insert(str(potatoes[4]))
		self.lEditPotatoesJun.insert(str(potatoes[5]))
		self.lEditPotatoesJul.insert(str(potatoes[6]))
		self.lEditPotatoesAug.insert(str(potatoes[7]))
		self.lEditPotatoesSep.insert(str(potatoes[8]))
		self.lEditPotatoesOct.insert(str(potatoes[9]))
		self.lEditPotatoesNov.insert(str(potatoes[10]))
		self.lEditPotatoesDec.insert(str(potatoes[11]))
						
		red_Pepper = datos.get('Red Pepper')
		self.lEditRedPepperJan.insert(str(red_Pepper[0]))
		self.lEditRedPepperFeb.insert(str(red_Pepper[1]))
		self.lEditRedPepperMar.insert(str(red_Pepper[2]))
		self.lEditRedPepperApr.insert(str(red_Pepper[3]))
		self.lEditRedPepperMay.insert(str(red_Pepper[4]))
		self.lEditRedPepperJun.insert(str(red_Pepper[5]))
		self.lEditRedPepperJul.insert(str(red_Pepper[6]))
		self.lEditRedPepperAug.insert(str(red_Pepper[7]))
		self.lEditRedPepperSep.insert(str(red_Pepper[8]))
		self.lEditRedPepperOct.insert(str(red_Pepper[9]))
		self.lEditRedPepperNov.insert(str(red_Pepper[10]))
		self.lEditRedPepperDec.insert(str(red_Pepper[11]))
						
		snow_Peas = datos.get('Snow Peas')
		self.lEditSnowPeasJan.insert(str(snow_Peas[0]))
		self.lEditSnowPeasFeb.insert(str(snow_Peas[1]))
		self.lEditSnowPeasMar.insert(str(snow_Peas[2]))
		self.lEditSnowPeasApr.insert(str(snow_Peas[3]))
		self.lEditSnowPeasMay.insert(str(snow_Peas[4]))
		self.lEditSnowPeasJun.insert(str(snow_Peas[5]))
		self.lEditSnowPeasJul.insert(str(snow_Peas[6]))
		self.lEditSnowPeasAug.insert(str(snow_Peas[7]))
		self.lEditSnowPeasSep.insert(str(snow_Peas[8]))
		self.lEditSnowPeasOct.insert(str(snow_Peas[9]))
		self.lEditSnowPeasNov.insert(str(snow_Peas[10]))
		self.lEditSnowPeasDec.insert(str(snow_Peas[11]))
						
		spinach = datos.get('Spinach')
		self.lEditSpinachJan.insert(str(spinach[0]))
		self.lEditSpinachFeb.insert(str(spinach[1]))
		self.lEditSpinachMar.insert(str(spinach[2]))
		self.lEditSpinachApr.insert(str(spinach[3]))
		self.lEditSpinachMay.insert(str(spinach[4]))
		self.lEditSpinachJun.insert(str(spinach[5]))
		self.lEditSpinachJul.insert(str(spinach[6]))
		self.lEditSpinachAug.insert(str(spinach[7]))
		self.lEditSpinachSep.insert(str(spinach[8]))
		self.lEditSpinachOct.insert(str(spinach[9]))
		self.lEditSpinachNov.insert(str(spinach[10]))
		self.lEditSpinachDec.insert(str(spinach[11 ]))
						
		wchn = datos.get('Water Ch Nuts')
		self.lEditWCNJan.insert(str(wchn[0]))
		self.lEditWCNFeb.insert(str(wchn[1]))
		self.lEditWCNMar.insert(str(wchn[2]))
		self.lEditWCNApr.insert(str(wchn[3]))
		self.lEditWCNMay.insert(str(wchn[4]))
		self.lEditWCNJun.insert(str(wchn[5]))
		self.lEditWCNJul.insert(str(wchn[6]))
		self.lEditWCNAug.insert(str(wchn[7]))
		self.lEditWCNSep.insert(str(wchn[8]))
		self.lEditWCNOct.insert(str(wchn[9]))
		self.lEditWCNNov.insert(str(wchn[10]))
		self.lEditWCNDec.insert(str(wchn[11]))
						
		others = datos.get('Others')
		self.lEditOthersJan.insert(str(others[0]))
		self.lEditOthersFeb.insert(str(others[1]))
		self.lEditOthersMar.insert(str(others[2]))
		self.lEditOthersApr.insert(str(others[3]))
		self.lEditOthersMay.insert(str(others[4]))
		self.lEditOthersJun.insert(str(others[5]))
		self.lEditOthersJul.insert(str(others[6]))
		self.lEditOthersAug.insert(str(others[7]))
		self.lEditOthersSep.insert(str(others[8]))
		self.lEditOthersOct.insert(str(others[9]))
		self.lEditOthersNov.insert(str(others[10]))
		self.lEditOthersDec.insert(str(others[11]))
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
				broc_Conv = self.Brocc_Conv_Jan
				brocc_Org = self.broc_Org_Jan
				cauliflower = self.Caulif_Jan
				Caulif_Org = self.Caulif_Org_Jan
				Crkl_Carrot = self.ConvCarrCrklJan
				Dcd_Carrot = self.ConvCarrDcdJan
				Org_Carrot = self.OrgCarrotJan
				GZucc = self.GZucc_Jan
				Peas = self.Peas_Jan
				Poblano = self.Poblano_Jan
				WCorn = self.WCorn_Jan
				Total_Corn = self.Total_Corn_Jan
				GreenBeans = self.GreenBeans_Jan
				Mushrooms = self.Mush_Jan
				Onion = self.Onion_Jan
				Potatoes = self.Potatoes_Jan
				RedPepper = self.RedPepper_Jan
				snowPeas = self.SnowPeas_Jan
				Spinach = self.Spinach_Jan
				WCN = self.WCN_Jan
				Others = self.Others_Jan
					
			elif values.find('feb')>0: 
				indice = values
				month = 'February'
				broc_Conv = self.Brocc_Conv_Feb
				brocc_Org = self.broc_Org_Feb
				cauliflower = self.Caulif_Feb
				Caulif_Org = self.Caulif_Org_Feb
				Crkl_Carrot = self.ConvCarrCrklFeb
				Dcd_Carrot = self.ConvCarrDcdFeb
				Org_Carrot = self.OrgCarrotFeb
				GZucc = self.GZucc_Feb
				Peas = self.Peas_Feb
				Poblano = self.Poblano_Feb
				WCorn = self.WCorn_Feb
				Total_Corn = self.Total_Corn_Feb
				GreenBeans = self.GreenBeans_Feb
				Mushrooms = self.Mush_Feb
				Onion = self.Onion_Feb
				Potatoes = self.Potatoes_Feb
				RedPepper = self.RedPepper_Feb
				snowPeas = self.SnowPeas_Feb
				Spinach = self.Spinach_Feb
				WCN = self.WCN_Feb
				Others = self.Others_Feb

			elif values.find('mar')>0: 
				indice = values
				month = 'March'
				broc_Conv = self.Brocc_Conv_Mar
				brocc_Org = self.broc_Org_Mar
				cauliflower = self.Caulif_Mar
				Caulif_Org = self.Caulif_Org_Mar
				Crkl_Carrot = self.ConvCarrCrklMar
				Dcd_Carrot = self.ConvCarrDcdMar
				Org_Carrot = self.OrgCarrotMar
				GZucc = self.GZucc_Mar
				Peas = self.Peas_Mar
				Poblano = self.Poblano_Mar
				WCorn = self.WCorn_Mar
				Total_Corn = self.Total_Corn_Mar
				GreenBeans = self.GreenBeans_Mar
				Mushrooms = self.Mush_Mar
				Onion = self.Onion_Mar
				Potatoes = self.Potatoes_Mar
				RedPepper = self.RedPepper_Mar
				snowPeas = self.SnowPeas_Mar
				Spinach = self.Spinach_Mar
				WCN = self.WCN_Mar
				Others = self.Others_Mar
				
			elif values.find('apr')>0: 
				indice = values
				month = 'April'
				broc_Conv = self.Brocc_Conv_Apr
				brocc_Org = self.broc_Org_Apr
				cauliflower = self.Caulif_Apr
				Caulif_Org = self.Caulif_Org_Apr
				Crkl_Carrot = self.ConvCarrCrklApr
				Dcd_Carrot = self.ConvCarrDcdApr
				Org_Carrot = self.OrgCarrotApr
				GZucc = self.GZucc_Apr
				Peas = self.Peas_Apr
				Poblano = self.Poblano_Apr
				WCorn = self.WCorn_Apr
				Total_Corn = self.Total_Corn_Apr
				GreenBeans = self.GreenBeans_Apr
				Mushrooms = self.Mush_Apr
				Onion = self.Onion_Apr
				Potatoes = self.Potatoes_Apr
				RedPepper = self.RedPepper_Apr
				snowPeas = self.SnowPeas_Apr
				Spinach = self.Spinach_Apr
				WCN = self.WCN_Apr
				Others = self.Others_Apr
				
			elif values.find('may')>0: 
				indice = values
				month = 'May'
				broc_Conv = self.Brocc_Conv_May
				brocc_Org = self.broc_Org_May
				cauliflower = self.Caulif_May
				Caulif_Org = self.Caulif_Org_May
				Crkl_Carrot = self.ConvCarrCrklMay
				Dcd_Carrot = self.ConvCarrDcdMay
				Org_Carrot = self.OrgCarrotMay
				GZucc = self.GZucc_May
				Peas = self.Peas_May
				Poblano = self.Poblano_May
				WCorn = self.WCorn_May
				Total_Corn = self.Total_Corn_May
				GreenBeans = self.GreenBeans_May
				Mushrooms = self.Mush_May
				Onion = self.Onion_May
				Potatoes = self.Potatoes_May
				RedPepper = self.RedPepper_May
				snowPeas = self.SnowPeas_May
				Spinach = self.Spinach_May
				WCN = self.WCN_May
				Others = self.Others_May
				
			elif values.find('jun')>0: 
				indice = values
				month = 'June'
				broc_Conv = self.Brocc_Conv_Jun
				brocc_Org = self.broc_Org_Jun
				cauliflower = self.Caulif_Jun
				Caulif_Org = self.Caulif_Org_Jun
				Crkl_Carrot = self.ConvCarrCrklJun
				Dcd_Carrot = self.ConvCarrDcdJun
				Org_Carrot = self.OrgCarrotJun
				GZucc = self.GZucc_Jun
				Peas = self.Peas_Jun
				Poblano = self.Poblano_Jun
				WCorn = self.WCorn_Jun
				Total_Corn = self.Total_Corn_Jun
				GreenBeans = self.GreenBeans_Jun
				Mushrooms = self.Mush_Jun
				Onion = self.Onion_Jun
				Potatoes = self.Potatoes_Jun
				RedPepper = self.RedPepper_Jun
				snowPeas = self.SnowPeas_Jun
				Spinach = self.Spinach_Jun
				WCN = self.WCN_Jun
				Others = self.Others_Jun
							
			elif values.find('jul')>0: 
				indice = values
				month = 'July'
				broc_Conv = self.Brocc_Conv_Jul
				brocc_Org = self.broc_Org_Jul
				cauliflower = self.Caulif_Jul
				Caulif_Org = self.Caulif_Org_Jul
				Crkl_Carrot = self.ConvCarrCrklJul
				Dcd_Carrot = self.ConvCarrDcdJul
				Org_Carrot = self.OrgCarrotJul
				GZucc = self.GZucc_Jul
				Peas = self.Peas_Jul
				Poblano = self.Poblano_Jul
				WCorn = self.WCorn_Jul
				Total_Corn = self.Total_Corn_Jul
				GreenBeans = self.GreenBeans_Jul
				Mushrooms = self.Mush_Jul
				Onion = self.Onion_Jul
				Potatoes = self.Potatoes_Jul
				RedPepper = self.RedPepper_Jul
				snowPeas = self.SnowPeas_Jul
				Spinach = self.Spinach_Jul
				WCN = self.WCN_Jul
				Others = self.Others_Jul
								
			elif values.find('aug')>0: 
				indice = values
				month = 'August'
				broc_Conv = self.Brocc_Conv_Aug
				brocc_Org = self.broc_Org_Aug
				cauliflower = self.Caulif_Aug
				Caulif_Org = self.Caulif_Org_Aug
				Crkl_Carrot = self.ConvCarrCrklAug
				Dcd_Carrot = self.ConvCarrDcdAug
				Org_Carrot = self.OrgCarrotAug
				GZucc = self.GZucc_Aug
				Peas = self.Peas_Aug
				Poblano = self.Poblano_Aug
				WCorn = self.WCorn_Aug
				Total_Corn = self.Total_Corn_Aug
				GreenBeans = self.GreenBeans_Aug
				Mushrooms = self.Mush_Aug
				Onion = self.Onion_Aug
				Potatoes = self.Potatoes_Aug
				RedPepper = self.RedPepper_Aug
				snowPeas = self.SnowPeas_Aug
				Spinach = self.Spinach_Aug
				WCN = self.WCN_Aug
				Others = self.Others_Aug
								
			elif values.find('sep')>0: 
				indice = values
				month = 'September'
				broc_Conv = self.Brocc_Conv_Sep
				brocc_Org = self.broc_Org_Sep
				cauliflower = self.Caulif_Sep
				Caulif_Org = self.Caulif_Org_Sep
				Crkl_Carrot = self.ConvCarrCrklSep
				Dcd_Carrot = self.ConvCarrDcdSep
				Org_Carrot = self.OrgCarrotSep
				GZucc = self.GZucc_Sep
				Peas = self.Peas_Sep
				Poblano = self.Poblano_Sep
				WCorn = self.WCorn_Sep
				Total_Corn = self.Total_Corn_Sep
				GreenBeans = self.GreenBeans_Sep
				Mushrooms = self.Mush_Sep
				Onion = self.Onion_Sep
				Potatoes = self.Potatoes_Sep
				RedPepper = self.RedPepper_Sep
				snowPeas = self.SnowPeas_Sep
				Spinach = self.Spinach_Sep
				WCN = self.WCN_Sep
				Others = self.Others_Sep
				
			elif values.find('oct')>0: 
				indice = values
				month = 'October'
				broc_Conv = self.Brocc_Conv_Oct
				brocc_Org = self.broc_Org_Oct
				cauliflower = self.Caulif_Oct
				Caulif_Org = self.Caulif_Org_Oct
				Crkl_Carrot = self.ConvCarrCrklOct
				Dcd_Carrot = self.ConvCarrDcdOct
				Org_Carrot = self.OrgCarrotOct
				GZucc = self.GZucc_Oct
				Peas = self.Peas_Oct
				Poblano = self.Poblano_Oct
				WCorn = self.WCorn_Oct
				Total_Corn = self.Total_Corn_Oct
				GreenBeans = self.GreenBeans_Oct
				Mushrooms = self.Mush_Oct
				Onion = self.Onion_Oct
				Potatoes = self.Potatoes_Oct
				RedPepper = self.RedPepper_Oct
				snowPeas = self.SnowPeas_Oct
				Spinach = self.Spinach_Oct
				WCN = self.WCN_Oct
				Others = self.Others_Oct
				
			elif values.find('nov')>0: 
				indice = values
				month = 'November'
				broc_Conv = self.Brocc_Conv_Nov
				brocc_Org = self.broc_Org_Nov
				cauliflower = self.Caulif_Nov
				Caulif_Org = self.Caulif_Org_Nov
				Crkl_Carrot = self.ConvCarrCrklNov
				Dcd_Carrot = self.ConvCarrDcdNov
				Org_Carrot = self.OrgCarrotNov
				GZucc = self.GZucc_Nov
				Peas = self.Peas_Nov
				Poblano = self.Poblano_Nov
				WCorn = self.WCorn_Nov
				Total_Corn = self.Total_Corn_Nov
				GreenBeans = self.GreenBeans_Nov
				Mushrooms = self.Mush_Nov
				Onion = self.Onion_Nov
				Potatoes = self.Potatoes_Nov
				RedPepper = self.RedPepper_Nov
				snowPeas = self.SnowPeas_Nov
				Spinach = self.Spinach_Nov
				WCN = self.WCN_Nov
				Others = self.Others_Nov
				
			elif values.find('dec')>0: 
				indice = values
				month = 'December'
				broc_Conv = self.Brocc_Conv_Dec
				brocc_Org = self.broc_Org_Dec
				cauliflower = self.Caulif_Dec
				Caulif_Org = self.Caulif_Org_Dec
				Crkl_Carrot = self.ConvCarrCrklDec
				Dcd_Carrot = self.ConvCarrDcdDec
				Org_Carrot = self.OrgCarrotDec
				GZucc = self.GZucc_Dec
				Peas = self.Peas_Dec
				Poblano = self.Poblano_Dec
				WCorn = self.WCorn_Dec
				Total_Corn = self.Total_Corn_Dec
				GreenBeans = self.GreenBeans_Dec
				Mushrooms = self.Mush_Dec
				Onion = self.Onion_Dec
				Potatoes = self.Potatoes_Dec
				RedPepper = self.RedPepper_Dec
				snowPeas = self.SnowPeas_Dec
				Spinach = self.Spinach_Dec
				WCN = self.WCN_Dec
				Others = self.Others_Dec
		
				
			data = {values : [sequence , indice, year, month, broc_Conv, brocc_Org, cauliflower, Caulif_Org,
				Crkl_Carrot, Dcd_Carrot, Org_Carrot, GZucc,
				Peas, Poblano, WCorn, Total_Corn,
				GreenBeans, Mushrooms, Onion, Potatoes, 
				RedPepper, snowPeas, Spinach, WCN, Others]}
			data_dict.update(data)

		message = 'Now we are going to save the file'
		self.caja_mensaje('Save data;', message,0)
		datos_Sales_Domestic =pd.read_csv('domesticsales.csv', index_col = 0, encoding = 'utf-8')
		datos_Sales_Domestic.apply(lambda x: pd.lib.infer_dtype(x.values))
		num_datos = int(datos_Sales_Domestic['indice'].count())
		datos_Sales_Domestic.index = range(datos_Sales_Domestic.shape[0])
		indice_archivo = list(datos_Sales_Domestic.indice)
		llaves = data_dict.keys()
		nuevo_Valor = num_datos+1
		valores = list(data_dict.values())
		
		for i, valor in enumerate(valores):
			nuevo_valor = int(nuevo_Valor)+i
			datos_Sales_Domestic.loc[int(nuevo_valor)]= [
				valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], 
				valor[7], valor[8], valor[9], valor[10], valor[11], 
				valor[12], valor[13], valor[14], valor [15], valor [16], valor [17], valor [18], 
				valor [19], valor [20], valor[21],  valor [22], valor [23], valor [24]]
		try: 
			datos_Sales_Domestic.to_csv('domesticsales.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
	
	def Conv_Carrot_Month(self, Conv_Carrot_Crkl, Conv_Carrot_Dcd):
		self.Total_Conv_Carrot = (Conv_Carrot_Crkl + Conv_Carrot_Dcd)
		return self.Total_Conv_Carrot     

	def Sweet_Corn_Month(self, WCorn, Total_Corn):
		self.Sweet_Corn = (WCorn -  Total_Corn)
		return self.Sweet_Corn     

	def sum_Conv_Carrots(self, Tot_Jan_Conv_Carrots, Tot_Feb_Conv_Carrots, 
			Tot_Mar_Conv_Carrots, Tot_Apr_Conv_Carrots, Tot_May_Conv_Carrots,
			Tot_Jun_Conv_Carrots, Tot_Jul_Conv_Carrots, Tot_Aug_Conv_Carrots,
			Tot_Sep_Conv_Carrots, Tot_Oct_Conv_Carrots, Tot_Nov_Conv_Carrots,
			Tot_Dec_Conv_Carrots):
		self.sum_Conv_Carrots = self.suma(Tot_Jan_Conv_Carrots, Tot_Feb_Conv_Carrots,
			Tot_Mar_Conv_Carrots, Tot_Apr_Conv_Carrots, Tot_May_Conv_Carrots,
			Tot_Jun_Conv_Carrots, Tot_Jul_Conv_Carrots, Tot_Aug_Conv_Carrots,
			Tot_Sep_Conv_Carrots, Tot_Oct_Conv_Carrots, Tot_Nov_Conv_Carrots,
			Tot_Dec_Conv_Carrots)
		return self.sum_Conv_Carrots

	def suma_Org_Jan(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Jan = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgJan.setText(str(self.sum_Org_Jan))
		return self.sum_Org_Jan
		
	def suma_Org_Feb(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Feb = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgFeb.setText(str(self.sum_Org_Feb))
		return self.sum_Org_Feb
	
	def suma_Org_Mar(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Mar = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgMar.setText(str(self.sum_Org_Mar))
		return self.sum_Org_Mar
	
	def suma_Org_Apr(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Apr = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgApr.setText(str(self.sum_Org_Apr))
		return self.sum_Org_Apr
	
	def suma_Org_May(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_May = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgMay.setText(str(self.sum_Org_May))
		return self.sum_Org_May
	
	def suma_Org_Jun(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Jun = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgJun.setText(str(self.sum_Org_Jun))
		return self.sum_Org_Jun
	
	def suma_Org_Jul(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Jul = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgJul.setText(str(self.sum_Org_Jul))
		return self.sum_Org_Jul
	
	def suma_Org_Aug(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Aug = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgAug.setText(str(self.sum_Org_Aug))
		return self.sum_Org_Aug
	
	def suma_Org_Sep(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Sep = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgSep.setText(str(self.sum_Org_Sep))
		return self.sum_Org_Sep
	
	def suma_Org_Oct(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Oct = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgOct.setText(str(self.sum_Org_Oct))
		return self.sum_Org_Oct
	
	def suma_Org_Nov(self, broccOrg, CaulifOrg, CarrotsOrg):
		self.sum_Org_Nov = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgNov.setText(str(self.sum_Org_Nov))
		return self.sum_Org_Nov
	
	def suma_Org_Dec(self, broccOrg, CaulifOrg, CarrotsOrg ):
		self.sum_Org_Dec = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg)
		self.lblTotalOrgDec.setText(str(self.sum_Org_Dec))
		return self.sum_Org_Dec
	
	def read_data_from_fields(self):

		self.Brocc_Conv_Jan = float(self.lEditConvBroccJan.text())
		self.Brocc_Conv_Feb = float(self.lEditConvBroccFeb.text())
		self.Brocc_Conv_Mar = float(self.lEditConvBroccMar.text())
		self.Brocc_Conv_Apr = float(self.lEditConvBroccApr.text())
		self.Brocc_Conv_May = float(self.lEditConvBroccMay.text())
		self.Brocc_Conv_Jun = float(self.lEditConvBroccJun.text())
		self.Brocc_Conv_Jul = float(self.lEditConvBroccJul.text())
		self.Brocc_Conv_Aug = float(self.lEditConvBroccAug.text())
		self.Brocc_Conv_Sep = float(self.lEditConvBroccSep.text())
		self.Brocc_Conv_Oct = float(self.lEditConvBroccOct.text())
		self.Brocc_Conv_Nov = float(self.lEditConvBroccNov.text())
		self.Brocc_Conv_Dec = float(self.lEditConvBroccDec.text())

		self.broc_Org_Jan = float(self.lEditOrgBroccJan.text())
		self.broc_Org_Feb = float(self.lEditOrgBroccFeb.text())
		self.broc_Org_Mar = float(self.lEditOrgBroccMar.text())
		self.broc_Org_Apr = float(self.lEditOrgBroccApr.text())
		self.broc_Org_May = float(self.lEditOrgBroccMay.text())
		self.broc_Org_Jun = float(self.lEditOrgBroccJun.text())
		self.broc_Org_Jul = float(self.lEditOrgBroccJul.text())
		self.broc_Org_Aug = float(self.lEditOrgBroccAug.text())
		self.broc_Org_Sep = float(self.lEditOrgBroccSep.text())
		self.broc_Org_Oct = float(self.lEditOrgBroccOct.text())
		self.broc_Org_Nov = float(self.lEditOrgBroccNov.text())
		self.broc_Org_Dec = float(self.lEditOrgBroccDec.text())

		self.Caulif_Jan = float(self.lEditCaulifJan.text())
		self.Caulif_Feb = float(self.lEditCaulifFeb.text())
		self.Caulif_Mar = float(self.lEditCaulifMar.text())
		self.Caulif_Apr = float(self.lEditCaulifApr.text())
		self.Caulif_May = float(self.lEditCaulifMay.text())
		self.Caulif_Jun = float(self.lEditCaulifJun.text())
		self.Caulif_Jul = float(self.lEditCaulifJul.text())
		self.Caulif_Aug = float(self.lEditCaulifAug.text())
		self.Caulif_Sep = float(self.lEditCaulifSep.text())
		self.Caulif_Oct = float(self.lEditCaulifOct.text())
		self.Caulif_Nov = float(self.lEditCaulifNov.text())
		self.Caulif_Dec = float(self.lEditCaulifDec.text())

		self.Caulif_Org_Jan = float(self.lEditOrgCauliJan.text())
		self.Caulif_Org_Feb = float(self.lEditOrgCauliFeb.text())
		self.Caulif_Org_Mar = float(self.lEditOrgCauliMar.text())
		self.Caulif_Org_Apr = float(self.lEditOrgCauliApr.text())
		self.Caulif_Org_May = float(self.lEditOrgCauliMay.text())
		self.Caulif_Org_Jun = float(self.lEditOrgCauliJun.text())
		self.Caulif_Org_Jul = float(self.lEditOrgCauliJul.text())
		self.Caulif_Org_Aug = float(self.lEditOrgCauliAug.text())
		self.Caulif_Org_Sep = float(self.lEditOrgCauliSep.text())
		self.Caulif_Org_Oct = float(self.lEditOrgCauliOct.text())
		self.Caulif_Org_Nov = float(self.lEditOrgCauliNov.text())
		self.Caulif_Org_Dec = float(self.lEditOrgCauliDec.text())

		self.ConvCarrCrklJan = float(self.lEditConvCarrCrklJan.text())
		self.ConvCarrCrklFeb = float(self.lEditConvCarrCrklFeb.text())
		self.ConvCarrCrklMar = float(self.lEditConvCarrCrklMar.text())
		self.ConvCarrCrklApr = float(self.lEditConvCarrCrklApr.text())
		self.ConvCarrCrklMay = float(self.lEditConvCarrCrklMay.text())
		self.ConvCarrCrklJun = float(self.lEditConvCarrCrklJun.text())
		self.ConvCarrCrklJul = float(self.lEditConvCarrCrklJul.text())
		self.ConvCarrCrklAug = float(self.lEditConvCarrCrklAug.text())
		self.ConvCarrCrklSep = float(self.lEditConvCarrCrklSep.text())
		self.ConvCarrCrklOct = float(self.lEditConvCarrCrklOct.text())
		self.ConvCarrCrklNov = float(self.lEditConvCarrCrklNov.text())
		self.ConvCarrCrklDec = float(self.lEditConvCarrCrklDec.text())

		self.ConvCarrDcdJan = float(self.lEditConvCarrDcdJan.text())
		self.ConvCarrDcdFeb = float(self.lEditConvCarrDcdFeb.text())
		self.ConvCarrDcdMar = float(self.lEditConvCarrDcdMar.text())
		self.ConvCarrDcdApr = float(self.lEditConvCarrDcdApr.text())
		self.ConvCarrDcdMay = float(self.lEditConvCarrDcdMay.text())
		self.ConvCarrDcdJun = float(self.lEditConvCarrDcdJun.text())
		self.ConvCarrDcdJul = float(self.lEditConvCarrDcdJul.text())
		self.ConvCarrDcdAug = float(self.lEditConvCarrDcdAug.text())
		self.ConvCarrDcdSep = float(self.lEditConvCarrDcdSep.text())
		self.ConvCarrDcdOct = float(self.lEditConvCarrDcdOct.text())
		self.ConvCarrDcdNov = float(self.lEditConvCarrDcdNov.text())
		self.ConvCarrDcdDec = float(self.lEditConvCarrDcdDec.text())

		self.OrgCarrotJan = float(self.lEditCarrotsOrgJan.text())
		self.OrgCarrotFeb = float(self.lEditCarrotsOrgFeb.text())
		self.OrgCarrotMar = float(self.lEditCarrotsOrgMar.text())
		self.OrgCarrotApr = float(self.lEditCarrotsOrgApr.text())
		self.OrgCarrotMay = float(self.lEditCarrotsOrgMay.text())
		self.OrgCarrotJun = float(self.lEditCarrotsOrgJun.text())
		self.OrgCarrotJul = float(self.lEditCarrotsOrgJul.text())
		self.OrgCarrotAug = float(self.lEditCarrotsOrgAug.text())
		self.OrgCarrotSep = float(self.lEditCarrotsOrgSep.text())
		self.OrgCarrotOct = float(self.lEditCarrotsOrgOct.text())
		self.OrgCarrotNov = float(self.lEditCarrotsOrgNov.text())
		self.OrgCarrotDec = float(self.lEditCarrotsOrgDec.text())

		self.GZucc_Jan = float(self.lEditGZuccJan.text())
		self.GZucc_Feb = float(self.lEditGZuccFeb.text())
		self.GZucc_Mar = float(self.lEditGZuccMar.text())
		self.GZucc_Apr = float(self.lEditGZuccApr.text())
		self.GZucc_May = float(self.lEditGZuccMay.text())
		self.GZucc_Jun = float(self.lEditGZuccJun.text())
		self.GZucc_Jul = float(self.lEditGZuccJul.text())
		self.GZucc_Aug = float(self.lEditGZuccAug.text())
		self.GZucc_Sep = float(self.lEditGZuccSep.text())
		self.GZucc_Oct = float(self.lEditGZuccOct.text())
		self.GZucc_Nov = float(self.lEditGZuccNov.text())
		self.GZucc_Dec = float(self.lEditGZuccDec.text())		

		self.Peas_Jan = float(self.lEditPeasJan.text())
		self.Peas_Feb = float(self.lEditPeasFeb.text())
		self.Peas_Mar = float(self.lEditPeasMar.text())
		self.Peas_Apr = float(self.lEditPeasApr.text())
		self.Peas_May = float(self.lEditPeasMay.text())
		self.Peas_Jun = float(self.lEditPeasJun.text())
		self.Peas_Jul = float(self.lEditPeasJul.text())
		self.Peas_Aug = float(self.lEditPeasAug.text())
		self.Peas_Sep = float(self.lEditPeasSep.text())
		self.Peas_Oct = float(self.lEditPeasOct.text())
		self.Peas_Nov = float(self.lEditPeasNov.text())
		self.Peas_Dec = float(self.lEditPeasDec.text())	

		self.Poblano_Jan = float(self.lEditPoblanoJan.text())
		self.Poblano_Feb = float(self.lEditPoblanoFeb.text())
		self.Poblano_Mar = float(self.lEditPoblanoMar.text())
		self.Poblano_Apr = float(self.lEditPoblanoApr.text())
		self.Poblano_May = float(self.lEditPoblanoMay.text())
		self.Poblano_Jun = float(self.lEditPoblanoJun.text())
		self.Poblano_Jul = float(self.lEditPoblanoJul.text())
		self.Poblano_Aug = float(self.lEditPoblanoAug.text())
		self.Poblano_Sep = float(self.lEditPoblanoSep.text())
		self.Poblano_Oct = float(self.lEditPoblanoOct.text())
		self.Poblano_Nov = float(self.lEditPoblanoNov.text())
		self.Poblano_Dec = float(self.lEditPoblanoDec.text())	

		self.WCorn_Jan = float(self.lEditWCornJan.text())
		self.WCorn_Feb = float(self.lEditWCornFeb.text())
		self.WCorn_Mar = float(self.lEditWCornMar.text())
		self.WCorn_Apr = float(self.lEditWCornApr.text())
		self.WCorn_May = float(self.lEditWCornMay.text())
		self.WCorn_Jun = float(self.lEditWCornJun.text())
		self.WCorn_Jul = float(self.lEditWCornJul.text())
		self.WCorn_Aug = float(self.lEditWCornAug.text())
		self.WCorn_Sep = float(self.lEditWCornSep.text())
		self.WCorn_Oct = float(self.lEditWCornOct.text())
		self.WCorn_Nov = float(self.lEditWCornNov.text())
		self.WCorn_Dec = float(self.lEditWCornDec.text())	

		self.Total_Corn_Jan = float(self.lEditTotalCornJan.text())
		self.Total_Corn_Feb = float(self.lEditTotalCornFeb.text())
		self.Total_Corn_Mar = float(self.lEditTotalCornMar.text())
		self.Total_Corn_Apr = float(self.lEditTotalCornApr.text())
		self.Total_Corn_May = float(self.lEditTotalCornMay.text())
		self.Total_Corn_Jun = float(self.lEditTotalCornJun.text())
		self.Total_Corn_Jul = float(self.lEditTotalCornJul.text())
		self.Total_Corn_Aug = float(self.lEditTotalCornAug.text())
		self.Total_Corn_Sep = float(self.lEditTotalCornSep.text())
		self.Total_Corn_Oct = float(self.lEditTotalCornOct.text())
		self.Total_Corn_Nov = float(self.lEditTotalCornNov.text())
		self.Total_Corn_Dec = float(self.lEditTotalCornDec.text())	

		self.GreenBeans_Jan = float(self.lEditGreenBeansJan.text())
		self.GreenBeans_Feb = float(self.lEditGreenBeansFeb.text())
		self.GreenBeans_Mar = float(self.lEditGreenBeansMar.text())
		self.GreenBeans_Apr = float(self.lEditGreenBeansApr.text())
		self.GreenBeans_May = float(self.lEditGreenBeansMay.text())
		self.GreenBeans_Jun = float(self.lEditGreenBeansJun.text())
		self.GreenBeans_Jul = float(self.lEditGreenBeansJul.text())
		self.GreenBeans_Aug = float(self.lEditGreenBeansAug.text())
		self.GreenBeans_Sep = float(self.lEditGreenBeansSep.text())
		self.GreenBeans_Oct = float(self.lEditGreenBeansOct.text())
		self.GreenBeans_Nov = float(self.lEditGreenBeansNov.text())
		self.GreenBeans_Dec = float(self.lEditGreenBeansDec.text())	

		self.Mush_Jan = float(self.lEditMushJan.text())
		self.Mush_Feb = float(self.lEditMushFeb.text())
		self.Mush_Mar = float(self.lEditMushMar.text())
		self.Mush_Apr = float(self.lEditMushApr.text())
		self.Mush_May = float(self.lEditMushMay.text())
		self.Mush_Jun = float(self.lEditMushJun.text())
		self.Mush_Jul = float(self.lEditMushJul.text())
		self.Mush_Aug = float(self.lEditMushAug.text())
		self.Mush_Sep = float(self.lEditMushSep.text())
		self.Mush_Oct = float(self.lEditMushOct.text())
		self.Mush_Nov = float(self.lEditMushNov.text())
		self.Mush_Dec = float(self.lEditMushDec.text())	

		self.Onion_Jan = float(self.lEditOnionJan.text())
		self.Onion_Feb = float(self.lEditOnionFeb.text())
		self.Onion_Mar = float(self.lEditOnionMar.text())
		self.Onion_Apr = float(self.lEditOnionApr.text())
		self.Onion_May = float(self.lEditOnionMay.text())
		self.Onion_Jun = float(self.lEditOnionJun.text())
		self.Onion_Jul = float(self.lEditOnionJul.text())
		self.Onion_Aug = float(self.lEditOnionAug.text())
		self.Onion_Sep = float(self.lEditOnionSep.text())
		self.Onion_Oct = float(self.lEditOnionOct.text())
		self.Onion_Nov = float(self.lEditOnionNov.text())
		self.Onion_Dec = float(self.lEditOnionDec.text())	

		self.Potatoes_Jan = float(self.lEditPotatoesJan.text())
		self.Potatoes_Feb = float(self.lEditPotatoesFeb.text())
		self.Potatoes_Mar = float(self.lEditPotatoesMar.text())
		self.Potatoes_Apr = float(self.lEditPotatoesApr.text())
		self.Potatoes_May = float(self.lEditPotatoesMay.text())
		self.Potatoes_Jun = float(self.lEditPotatoesJun.text())
		self.Potatoes_Jul = float(self.lEditPotatoesJul.text())
		self.Potatoes_Aug = float(self.lEditPotatoesAug.text())
		self.Potatoes_Sep = float(self.lEditPotatoesSep.text())
		self.Potatoes_Oct = float(self.lEditPotatoesOct.text())
		self.Potatoes_Nov = float(self.lEditPotatoesNov.text())
		self.Potatoes_Dec = float(self.lEditPotatoesDec.text())

		self.RedPepper_Jan = float(self.lEditRedPepperJan.text())
		self.RedPepper_Feb = float(self.lEditRedPepperFeb.text())
		self.RedPepper_Mar = float(self.lEditRedPepperMar.text())
		self.RedPepper_Apr = float(self.lEditRedPepperApr.text())
		self.RedPepper_May = float(self.lEditRedPepperMay.text())
		self.RedPepper_Jun = float(self.lEditRedPepperJun.text())
		self.RedPepper_Jul = float(self.lEditRedPepperJul.text())
		self.RedPepper_Aug = float(self.lEditRedPepperAug.text())
		self.RedPepper_Sep = float(self.lEditRedPepperSep.text())
		self.RedPepper_Oct = float(self.lEditRedPepperOct.text())
		self.RedPepper_Nov = float(self.lEditRedPepperNov.text())
		self.RedPepper_Dec = float(self.lEditRedPepperDec.text())

		self.SnowPeas_Jan = float(self.lEditSnowPeasJan.text())
		self.SnowPeas_Feb = float(self.lEditSnowPeasFeb.text())
		self.SnowPeas_Mar = float(self.lEditSnowPeasMar.text())
		self.SnowPeas_Apr = float(self.lEditSnowPeasApr.text())
		self.SnowPeas_May = float(self.lEditSnowPeasMay.text())
		self.SnowPeas_Jun = float(self.lEditSnowPeasJun.text())
		self.SnowPeas_Jul = float(self.lEditSnowPeasJul.text())
		self.SnowPeas_Aug = float(self.lEditSnowPeasAug.text())
		self.SnowPeas_Sep = float(self.lEditSnowPeasSep.text())
		self.SnowPeas_Oct = float(self.lEditSnowPeasOct.text())
		self.SnowPeas_Nov = float(self.lEditSnowPeasNov.text())
		self.SnowPeas_Dec = float(self.lEditSnowPeasDec.text())

		self.Spinach_Jan = float(self.lEditSpinachJan.text())
		self.Spinach_Feb = float(self.lEditSpinachFeb.text())
		self.Spinach_Mar = float(self.lEditSpinachMar.text())
		self.Spinach_Apr = float(self.lEditSpinachApr.text())
		self.Spinach_May = float(self.lEditSpinachMay.text())
		self.Spinach_Jun = float(self.lEditSpinachJun.text())
		self.Spinach_Jul = float(self.lEditSpinachJul.text())
		self.Spinach_Aug = float(self.lEditSpinachAug.text())
		self.Spinach_Sep = float(self.lEditSpinachSep.text())
		self.Spinach_Oct = float(self.lEditSpinachOct.text())
		self.Spinach_Nov = float(self.lEditSpinachNov.text())
		self.Spinach_Dec = float(self.lEditSpinachDec.text())

		self.WCN_Jan = float(self.lEditWCNJan.text())
		self.WCN_Feb = float(self.lEditWCNFeb.text())
		self.WCN_Mar = float(self.lEditWCNMar.text())
		self.WCN_Apr = float(self.lEditWCNApr.text())
		self.WCN_May = float(self.lEditWCNMay.text())
		self.WCN_Jun = float(self.lEditWCNJun.text())
		self.WCN_Jul = float(self.lEditWCNJul.text())
		self.WCN_Aug = float(self.lEditWCNAug.text())
		self.WCN_Sep = float(self.lEditWCNSep.text())
		self.WCN_Oct = float(self.lEditWCNOct.text())
		self.WCN_Nov = float(self.lEditWCNNov.text())
		self.WCN_Dec = float(self.lEditWCNDec.text())

		self.Others_Jan = float(self.lEditOthersJan.text())
		self.Others_Feb = float(self.lEditOthersFeb.text())
		self.Others_Mar = float(self.lEditOthersMar.text())
		self.Others_Apr = float(self.lEditOthersApr.text())
		self.Others_May = float(self.lEditOthersMay.text())
		self.Others_Jun = float(self.lEditOthersJun.text())
		self.Others_Jul = float(self.lEditOthersJul.text())
		self.Others_Aug = float(self.lEditOthersAug.text())
		self.Others_Sep = float(self.lEditOthersSep.text())
		self.Others_Oct = float(self.lEditOthersOct.text())
		self.Others_Nov = float(self.lEditOthersNov.text())
		self.Others_Dec = float(self.lEditOthersDec.text())
		
	def lock_fields (self):

		self.lEditConvBroccJan.setEnabled(False)
		self.lEditConvBroccFeb.setEnabled(False)
		self.lEditConvBroccMar.setEnabled(False)
		self.lEditConvBroccApr.setEnabled(False)
		self.lEditConvBroccMay.setEnabled(False)
		self.lEditConvBroccJun.setEnabled(False)
		self.lEditConvBroccJul.setEnabled(False)
		self.lEditConvBroccAug.setEnabled(False)
		self.lEditConvBroccSep.setEnabled(False)
		self.lEditConvBroccOct.setEnabled(False)
		self.lEditConvBroccNov.setEnabled(False)
		self.lEditConvBroccDec.setEnabled(False)

		self.lEditOrgBroccJan.setEnabled(False)
		self.lEditOrgBroccFeb.setEnabled(False)
		self.lEditOrgBroccMar.setEnabled(False)
		self.lEditOrgBroccApr.setEnabled(False)
		self.lEditOrgBroccMay.setEnabled(False)
		self.lEditOrgBroccJun.setEnabled(False)
		self.lEditOrgBroccJul.setEnabled(False)
		self.lEditOrgBroccAug.setEnabled(False)
		self.lEditOrgBroccSep.setEnabled(False)
		self.lEditOrgBroccOct.setEnabled(False)
		self.lEditOrgBroccNov.setEnabled(False)
		self.lEditOrgBroccDec.setEnabled(False)

		self.lEditCaulifJan.setEnabled(False)
		self.lEditCaulifFeb.setEnabled(False)
		self.lEditCaulifMar.setEnabled(False)
		self.lEditCaulifApr.setEnabled(False)
		self.lEditCaulifMay.setEnabled(False)
		self.lEditCaulifJun.setEnabled(False)
		self.lEditCaulifJul.setEnabled(False)
		self.lEditCaulifAug.setEnabled(False)
		self.lEditCaulifSep.setEnabled(False)
		self.lEditCaulifOct.setEnabled(False)
		self.lEditCaulifNov.setEnabled(False)
		self.lEditCaulifDec.setEnabled(False)

		self.lEditOrgCauliJan.setEnabled(False)
		self.lEditOrgCauliFeb.setEnabled(False)
		self.lEditOrgCauliMar.setEnabled(False)
		self.lEditOrgCauliApr.setEnabled(False)
		self.lEditOrgCauliMay.setEnabled(False)
		self.lEditOrgCauliJun.setEnabled(False)
		self.lEditOrgCauliJul.setEnabled(False)
		self.lEditOrgCauliAug.setEnabled(False)
		self.lEditOrgCauliSep.setEnabled(False)
		self.lEditOrgCauliOct.setEnabled(False)
		self.lEditOrgCauliNov.setEnabled(False)
		self.lEditOrgCauliDec.setEnabled(False)

		self.lEditConvCarrCrklJan.setEnabled(False)
		self.lEditConvCarrCrklFeb.setEnabled(False)
		self.lEditConvCarrCrklMar.setEnabled(False)
		self.lEditConvCarrCrklApr.setEnabled(False)
		self.lEditConvCarrCrklMay.setEnabled(False)
		self.lEditConvCarrCrklJun.setEnabled(False)
		self.lEditConvCarrCrklJul.setEnabled(False)
		self.lEditConvCarrCrklAug.setEnabled(False)
		self.lEditConvCarrCrklSep.setEnabled(False)
		self.lEditConvCarrCrklOct.setEnabled(False)
		self.lEditConvCarrCrklNov.setEnabled(False)
		self.lEditConvCarrCrklDec.setEnabled(False)

		self.lEditConvCarrDcdJan.setEnabled(False)
		self.lEditConvCarrDcdFeb.setEnabled(False)
		self.lEditConvCarrDcdMar.setEnabled(False)
		self.lEditConvCarrDcdApr.setEnabled(False)
		self.lEditConvCarrDcdMay.setEnabled(False)
		self.lEditConvCarrDcdJun.setEnabled(False)
		self.lEditConvCarrDcdJul.setEnabled(False)
		self.lEditConvCarrDcdAug.setEnabled(False)
		self.lEditConvCarrDcdSep.setEnabled(False)
		self.lEditConvCarrDcdOct.setEnabled(False)
		self.lEditConvCarrDcdNov.setEnabled(False)
		self.lEditConvCarrDcdDec.setEnabled(False)

		self.lEditCarrotsOrgJan.setEnabled(False)
		self.lEditCarrotsOrgFeb.setEnabled(False)
		self.lEditCarrotsOrgMar.setEnabled(False)
		self.lEditCarrotsOrgApr.setEnabled(False)
		self.lEditCarrotsOrgMay.setEnabled(False)
		self.lEditCarrotsOrgJun.setEnabled(False)
		self.lEditCarrotsOrgJul.setEnabled(False)
		self.lEditCarrotsOrgAug.setEnabled(False)
		self.lEditCarrotsOrgSep.setEnabled(False)
		self.lEditCarrotsOrgOct.setEnabled(False)
		self.lEditCarrotsOrgNov.setEnabled(False)
		self.lEditCarrotsOrgDec.setEnabled(False)

		self.lEditGZuccJan.setEnabled(False)
		self.lEditGZuccFeb.setEnabled(False)
		self.lEditGZuccMar.setEnabled(False)
		self.lEditGZuccApr.setEnabled(False)
		self.lEditGZuccMay.setEnabled(False)
		self.lEditGZuccJun.setEnabled(False)
		self.lEditGZuccJul.setEnabled(False)
		self.lEditGZuccAug.setEnabled(False)
		self.lEditGZuccSep.setEnabled(False)
		self.lEditGZuccOct.setEnabled(False)
		self.lEditGZuccNov.setEnabled(False)
		self.lEditGZuccDec.setEnabled(False)

		self.lEditPeasJan.setEnabled(False)
		self.lEditPeasFeb.setEnabled(False)
		self.lEditPeasMar.setEnabled(False)
		self.lEditPeasApr.setEnabled(False)
		self.lEditPeasMay.setEnabled(False)
		self.lEditPeasJun.setEnabled(False)
		self.lEditPeasJul.setEnabled(False)
		self.lEditPeasAug.setEnabled(False)
		self.lEditPeasSep.setEnabled(False)
		self.lEditPeasOct.setEnabled(False)
		self.lEditPeasNov.setEnabled(False)
		self.lEditPeasDec.setEnabled(False)

		self.lEditPoblanoJan.setEnabled(False)
		self.lEditPoblanoFeb.setEnabled(False)
		self.lEditPoblanoMar.setEnabled(False)
		self.lEditPoblanoApr.setEnabled(False)
		self.lEditPoblanoMay.setEnabled(False)
		self.lEditPoblanoJun.setEnabled(False)
		self.lEditPoblanoJul.setEnabled(False)
		self.lEditPoblanoAug.setEnabled(False)
		self.lEditPoblanoSep.setEnabled(False)
		self.lEditPoblanoOct.setEnabled(False)
		self.lEditPoblanoNov.setEnabled(False)
		self.lEditPoblanoDec.setEnabled(False)

		self.lEditWCornJan.setEnabled(False)
		self.lEditWCornFeb.setEnabled(False)
		self.lEditWCornMar.setEnabled(False)
		self.lEditWCornApr.setEnabled(False)
		self.lEditWCornMay.setEnabled(False)
		self.lEditWCornJun.setEnabled(False)
		self.lEditWCornJul.setEnabled(False)
		self.lEditWCornAug.setEnabled(False)
		self.lEditWCornSep.setEnabled(False)
		self.lEditWCornOct.setEnabled(False)
		self.lEditWCornNov.setEnabled(False)
		self.lEditWCornDec.setEnabled(False)

		self.lEditTotalCornJan.setEnabled(False)
		self.lEditTotalCornFeb.setEnabled(False)
		self.lEditTotalCornMar.setEnabled(False)
		self.lEditTotalCornApr.setEnabled(False)
		self.lEditTotalCornMay.setEnabled(False)
		self.lEditTotalCornJun.setEnabled(False)
		self.lEditTotalCornJul.setEnabled(False)
		self.lEditTotalCornAug.setEnabled(False)
		self.lEditTotalCornSep.setEnabled(False)
		self.lEditTotalCornOct.setEnabled(False)
		self.lEditTotalCornNov.setEnabled(False)
		self.lEditTotalCornDec.setEnabled(False)

		self.lEditGreenBeansJan.setEnabled(False)
		self.lEditGreenBeansFeb.setEnabled(False)
		self.lEditGreenBeansMar.setEnabled(False)
		self.lEditGreenBeansApr.setEnabled(False)
		self.lEditGreenBeansMay.setEnabled(False)
		self.lEditGreenBeansJun.setEnabled(False)
		self.lEditGreenBeansJul.setEnabled(False)
		self.lEditGreenBeansAug.setEnabled(False)
		self.lEditGreenBeansSep.setEnabled(False)
		self.lEditGreenBeansOct.setEnabled(False)
		self.lEditGreenBeansNov.setEnabled(False)
		self.lEditGreenBeansDec.setEnabled(False)

		self.lEditMushJan.setEnabled(False)
		self.lEditMushFeb.setEnabled(False)
		self.lEditMushMar.setEnabled(False)
		self.lEditMushApr.setEnabled(False)
		self.lEditMushMay.setEnabled(False)
		self.lEditMushJun.setEnabled(False)
		self.lEditMushJul.setEnabled(False)
		self.lEditMushAug.setEnabled(False)
		self.lEditMushSep.setEnabled(False)
		self.lEditMushOct.setEnabled(False)
		self.lEditMushNov.setEnabled(False)
		self.lEditMushDec.setEnabled(False)

		self.lEditOnionJan.setEnabled(False)
		self.lEditOnionFeb.setEnabled(False)
		self.lEditOnionMar.setEnabled(False)
		self.lEditOnionApr.setEnabled(False)
		self.lEditOnionMay.setEnabled(False)
		self.lEditOnionJun.setEnabled(False)
		self.lEditOnionJul.setEnabled(False)
		self.lEditOnionAug.setEnabled(False)
		self.lEditOnionSep.setEnabled(False)
		self.lEditOnionOct.setEnabled(False)
		self.lEditOnionNov.setEnabled(False)
		self.lEditOnionDec.setEnabled(False)

		self.lEditPotatoesJan.setEnabled(False)
		self.lEditPotatoesFeb.setEnabled(False)
		self.lEditPotatoesMar.setEnabled(False)
		self.lEditPotatoesApr.setEnabled(False)
		self.lEditPotatoesMay.setEnabled(False)
		self.lEditPotatoesJun.setEnabled(False)
		self.lEditPotatoesJul.setEnabled(False)
		self.lEditPotatoesAug.setEnabled(False)
		self.lEditPotatoesSep.setEnabled(False)
		self.lEditPotatoesOct.setEnabled(False)
		self.lEditPotatoesNov.setEnabled(False)
		self.lEditPotatoesDec.setEnabled(False)

		self.lEditRedPepperJan.setEnabled(False)
		self.lEditRedPepperFeb.setEnabled(False)
		self.lEditRedPepperMar.setEnabled(False)
		self.lEditRedPepperApr.setEnabled(False)
		self.lEditRedPepperMay.setEnabled(False)
		self.lEditRedPepperJun.setEnabled(False)
		self.lEditRedPepperJul.setEnabled(False)
		self.lEditRedPepperAug.setEnabled(False)
		self.lEditRedPepperSep.setEnabled(False)
		self.lEditRedPepperOct.setEnabled(False)
		self.lEditRedPepperNov.setEnabled(False)
		self.lEditRedPepperDec.setEnabled(False)

		self.lEditSnowPeasJan.setEnabled(False)
		self.lEditSnowPeasFeb.setEnabled(False)
		self.lEditSnowPeasMar.setEnabled(False)
		self.lEditSnowPeasApr.setEnabled(False)
		self.lEditSnowPeasMay.setEnabled(False)
		self.lEditSnowPeasJun.setEnabled(False)
		self.lEditSnowPeasJul.setEnabled(False)
		self.lEditSnowPeasAug.setEnabled(False)
		self.lEditSnowPeasSep.setEnabled(False)
		self.lEditSnowPeasOct.setEnabled(False)
		self.lEditSnowPeasNov.setEnabled(False)
		self.lEditSnowPeasDec.setEnabled(False)

		self.lEditSpinachJan.setEnabled(False)
		self.lEditSpinachFeb.setEnabled(False)
		self.lEditSpinachMar.setEnabled(False)
		self.lEditSpinachApr.setEnabled(False)
		self.lEditSpinachMay.setEnabled(False)
		self.lEditSpinachJun.setEnabled(False)
		self.lEditSpinachJul.setEnabled(False)
		self.lEditSpinachAug.setEnabled(False)
		self.lEditSpinachSep.setEnabled(False)
		self.lEditSpinachOct.setEnabled(False)
		self.lEditSpinachNov.setEnabled(False)
		self.lEditSpinachDec.setEnabled(False)

		self.lEditWCNJan.setEnabled(False)
		self.lEditWCNFeb.setEnabled(False)
		self.lEditWCNMar.setEnabled(False)
		self.lEditWCNApr.setEnabled(False)
		self.lEditWCNMay.setEnabled(False)
		self.lEditWCNJun.setEnabled(False)
		self.lEditWCNJul.setEnabled(False)
		self.lEditWCNAug.setEnabled(False)
		self.lEditWCNSep.setEnabled(False)
		self.lEditWCNOct.setEnabled(False)
		self.lEditWCNNov.setEnabled(False)
		self.lEditWCNDec.setEnabled(False)

		self.lEditOthersJan.setEnabled(False)
		self.lEditOthersFeb.setEnabled(False)
		self.lEditOthersMar.setEnabled(False)
		self.lEditOthersApr.setEnabled(False)
		self.lEditOthersMay.setEnabled(False)
		self.lEditOthersJun.setEnabled(False)
		self.lEditOthersJul.setEnabled(False)
		self.lEditOthersAug.setEnabled(False)
		self.lEditOthersSep.setEnabled(False)
		self.lEditOthersOct.setEnabled(False)
		self.lEditOthersNov.setEnabled(False)
		self.lEditOthersDec.setEnabled(False)
		
	def unlock_fields(self):
		"""self.lEditConvBroccJan.setEnabled(True)
		self.lEditConvBroccFeb.setEnabled(True)
		self.lEditConvBroccMar.setEnabled(True)
		self.lEditConvBroccApr.setEnabled(True)
		self.lEditConvBroccMay.setEnabled(True)
		self.lEditConvBroccJun.setEnabled(True)
		self.lEditConvBroccJul.setEnabled(True)
		self.lEditConvBroccAug.setEnabled(True)
		self.lEditConvBroccSep.setEnabled(True)
		self.lEditConvBroccOct.setEnabled(True)
		self.lEditConvBroccNov.setEnabled(True)
		self.lEditConvBroccDec.setEnabled(True)

		self.lEditOrgBroccJan.setEnabled(True)
		self.lEditOrgBroccFeb.setEnabled(True)
		self.lEditOrgBroccMar.setEnabled(True)
		self.lEditOrgBroccApr.setEnabled(True)
		self.lEditOrgBroccMay.setEnabled(True)
		self.lEditOrgBroccJun.setEnabled(True)
		self.lEditOrgBroccJul.setEnabled(True)
		self.lEditOrgBroccAug.setEnabled(True)
		self.lEditOrgBroccSep.setEnabled(True)
		self.lEditOrgBroccOct.setEnabled(True)
		self.lEditOrgBroccNov.setEnabled(True)
		self.lEditOrgBroccDec.setEnabled(True)

		self.lEditCaulifJan.setEnabled(True)
		self.lEditCaulifFeb.setEnabled(True)
		self.lEditCaulifMar.setEnabled(True)
		self.lEditCaulifApr.setEnabled(True)
		self.lEditCaulifMay.setEnabled(True)
		self.lEditCaulifJun.setEnabled(True)
		self.lEditCaulifJul.setEnabled(True)
		self.lEditCaulifAug.setEnabled(True)
		self.lEditCaulifSep.setEnabled(True)
		self.lEditCaulifOct.setEnabled(True)
		self.lEditCaulifNov.setEnabled(True)
		self.lEditCaulifDec.setEnabled(True)

		self.lEditOrgCauliJan.setEnabled(True)
		self.lEditOrgCauliFeb.setEnabled(True)
		self.lEditOrgCauliMar.setEnabled(True)
		self.lEditOrgCauliApr.setEnabled(True)
		self.lEditOrgCauliMay.setEnabled(True)
		self.lEditOrgCauliJun.setEnabled(True)
		self.lEditOrgCauliJul.setEnabled(True)
		self.lEditOrgCauliAug.setEnabled(True)
		self.lEditOrgCauliSep.setEnabled(True)
		self.lEditOrgCauliOct.setEnabled(True)
		self.lEditOrgCauliNov.setEnabled(True)
		self.lEditOrgCauliDec.setEnabled(True)

		self.lEditConvCarrCrklJan.setEnabled(True)
		self.lEditConvCarrCrklFeb.setEnabled(True)
		self.lEditConvCarrCrklMar.setEnabled(True)
		self.lEditConvCarrCrklApr.setEnabled(True)
		self.lEditConvCarrCrklMay.setEnabled(True)
		self.lEditConvCarrCrklJun.setEnabled(True)
		self.lEditConvCarrCrklJul.setEnabled(True)
		self.lEditConvCarrCrklAug.setEnabled(True)
		self.lEditConvCarrCrklSep.setEnabled(True)
		self.lEditConvCarrCrklOct.setEnabled(True)
		self.lEditConvCarrCrklNov.setEnabled(True)
		self.lEditConvCarrCrklDec.setEnabled(True)

		self.lEditConvCarrDcdJan.setEnabled(True)
		self.lEditConvCarrDcdFeb.setEnabled(True)
		self.lEditConvCarrDcdMar.setEnabled(True)
		self.lEditConvCarrDcdApr.setEnabled(True)
		self.lEditConvCarrDcdMay.setEnabled(True)
		self.lEditConvCarrDcdJun.setEnabled(True)
		self.lEditConvCarrDcdJul.setEnabled(True)
		self.lEditConvCarrDcdAug.setEnabled(True)
		self.lEditConvCarrDcdSep.setEnabled(True)
		self.lEditConvCarrDcdOct.setEnabled(True)
		self.lEditConvCarrDcdNov.setEnabled(True)
		self.lEditConvCarrDcdDec.setEnabled(True)

		self.lEditCarrotsOrgJan.setEnabled(True)
		self.lEditCarrotsOrgFeb.setEnabled(True)
		self.lEditCarrotsOrgMar.setEnabled(True)
		self.lEditCarrotsOrgApr.setEnabled(True)
		self.lEditCarrotsOrgMay.setEnabled(True)
		self.lEditCarrotsOrgJun.setEnabled(True)
		self.lEditCarrotsOrgJul.setEnabled(True)
		self.lEditCarrotsOrgAug.setEnabled(True)
		self.lEditCarrotsOrgSep.setEnabled(True)
		self.lEditCarrotsOrgOct.setEnabled(True)
		self.lEditCarrotsOrgNov.setEnabled(True)
		self.lEditCarrotsOrgDec.setEnabled(True)

		self.lEditGZuccJan.setEnabled(True)
		self.lEditGZuccFeb.setEnabled(True)
		self.lEditGZuccMar.setEnabled(True)
		self.lEditGZuccApr.setEnabled(True)
		self.lEditGZuccMay.setEnabled(True)
		self.lEditGZuccJun.setEnabled(True)
		self.lEditGZuccJul.setEnabled(True)
		self.lEditGZuccAug.setEnabled(True)
		self.lEditGZuccSep.setEnabled(True)
		self.lEditGZuccOct.setEnabled(True)
		self.lEditGZuccNov.setEnabled(True)
		self.lEditGZuccDec.setEnabled(True)

		self.lEditPeasJan.setEnabled(True)
		self.lEditPeasFeb.setEnabled(True)
		self.lEditPeasMar.setEnabled(True)
		self.lEditPeasApr.setEnabled(True)
		self.lEditPeasMay.setEnabled(True)
		self.lEditPeasJun.setEnabled(True)
		self.lEditPeasJul.setEnabled(True)
		self.lEditPeasAug.setEnabled(True)
		self.lEditPeasSep.setEnabled(True)
		self.lEditPeasOct.setEnabled(True)
		self.lEditPeasNov.setEnabled(True)
		self.lEditPeasDec.setEnabled(True)

		self.lEditPoblanoJan.setEnabled(True)
		self.lEditPoblanoFeb.setEnabled(True)
		self.lEditPoblanoMar.setEnabled(True)
		self.lEditPoblanoApr.setEnabled(True)
		self.lEditPoblanoMay.setEnabled(True)
		self.lEditPoblanoJun.setEnabled(True)
		self.lEditPoblanoJul.setEnabled(True)
		self.lEditPoblanoAug.setEnabled(True)
		self.lEditPoblanoSep.setEnabled(True)
		self.lEditPoblanoOct.setEnabled(True)
		self.lEditPoblanoNov.setEnabled(True)
		self.lEditPoblanoDec.setEnabled(True)

		self.lEditWCornJan.setEnabled(True)
		self.lEditWCornFeb.setEnabled(True)
		self.lEditWCornMar.setEnabled(True)
		self.lEditWCornApr.setEnabled(True)
		self.lEditWCornMay.setEnabled(True)
		self.lEditWCornJun.setEnabled(True)
		self.lEditWCornJul.setEnabled(True)
		self.lEditWCornAug.setEnabled(True)
		self.lEditWCornSep.setEnabled(True)
		self.lEditWCornOct.setEnabled(True)
		self.lEditWCornNov.setEnabled(True)
		self.lEditWCornDec.setEnabled(True)

		self.lEditTotalCornJan.setEnabled(True)
		self.lEditTotalCornFeb.setEnabled(True)
		self.lEditTotalCornMar.setEnabled(True)
		self.lEditTotalCornApr.setEnabled(True)
		self.lEditTotalCornMay.setEnabled(True)
		self.lEditTotalCornJun.setEnabled(True)
		self.lEditTotalCornJul.setEnabled(True)
		self.lEditTotalCornAug.setEnabled(True)
		self.lEditTotalCornSep.setEnabled(True)
		self.lEditTotalCornOct.setEnabled(True)
		self.lEditTotalCornNov.setEnabled(True)
		self.lEditTotalCornDec.setEnabled(True)

		self.lEditGreenBeansJan.setEnabled(True)
		self.lEditGreenBeansFeb.setEnabled(True)
		self.lEditGreenBeansMar.setEnabled(True)
		self.lEditGreenBeansApr.setEnabled(True)
		self.lEditGreenBeansMay.setEnabled(True)
		self.lEditGreenBeansJun.setEnabled(True)
		self.lEditGreenBeansJul.setEnabled(True)
		self.lEditGreenBeansAug.setEnabled(True)
		self.lEditGreenBeansSep.setEnabled(True)
		self.lEditGreenBeansOct.setEnabled(True)
		self.lEditGreenBeansNov.setEnabled(True)
		self.lEditGreenBeansDec.setEnabled(True)

		self.lEditMushJan.setEnabled(True)
		self.lEditMushFeb.setEnabled(True)
		self.lEditMushMar.setEnabled(True)
		self.lEditMushApr.setEnabled(True)
		self.lEditMushMay.setEnabled(True)
		self.lEditMushJun.setEnabled(True)
		self.lEditMushJul.setEnabled(True)
		self.lEditMushAug.setEnabled(True)
		self.lEditMushSep.setEnabled(True)
		self.lEditMushOct.setEnabled(True)
		self.lEditMushNov.setEnabled(True)
		self.lEditMushDec.setEnabled(True)

		self.lEditOnionJan.setEnabled(True)
		self.lEditOnionFeb.setEnabled(True)
		self.lEditOnionMar.setEnabled(True)
		self.lEditOnionApr.setEnabled(True)
		self.lEditOnionMay.setEnabled(True)
		self.lEditOnionJun.setEnabled(True)
		self.lEditOnionJul.setEnabled(True)
		self.lEditOnionAug.setEnabled(True)
		self.lEditOnionSep.setEnabled(True)
		self.lEditOnionOct.setEnabled(True)
		self.lEditOnionNov.setEnabled(True)
		self.lEditOnionDec.setEnabled(True)

		self.lEditPotatoesJan.setEnabled(True)
		self.lEditPotatoesFeb.setEnabled(True)
		self.lEditPotatoesMar.setEnabled(True)
		self.lEditPotatoesApr.setEnabled(True)
		self.lEditPotatoesMay.setEnabled(True)
		self.lEditPotatoesJun.setEnabled(True)
		self.lEditPotatoesJul.setEnabled(True)
		self.lEditPotatoesAug.setEnabled(True)
		self.lEditPotatoesSep.setEnabled(True)
		self.lEditPotatoesOct.setEnabled(True)
		self.lEditPotatoesNov.setEnabled(True)
		self.lEditPotatoesDec.setEnabled(True)

		self.lEditRedPepperJan.setEnabled(True)
		self.lEditRedPepperFeb.setEnabled(True)
		self.lEditRedPepperMar.setEnabled(True)
		self.lEditRedPepperApr.setEnabled(True)
		self.lEditRedPepperMay.setEnabled(True)
		self.lEditRedPepperJun.setEnabled(True)
		self.lEditRedPepperJul.setEnabled(True)
		self.lEditRedPepperAug.setEnabled(True)
		self.lEditRedPepperSep.setEnabled(True)
		self.lEditRedPepperOct.setEnabled(True)
		self.lEditRedPepperNov.setEnabled(True)
		self.lEditRedPepperDec.setEnabled(True)

		self.lEditSnowPeasJan.setEnabled(True)
		self.lEditSnowPeasFeb.setEnabled(True)
		self.lEditSnowPeasMar.setEnabled(True)
		self.lEditSnowPeasApr.setEnabled(True)
		self.lEditSnowPeasMay.setEnabled(True)
		self.lEditSnowPeasJun.setEnabled(True)
		self.lEditSnowPeasJul.setEnabled(True)
		self.lEditSnowPeasAug.setEnabled(True)
		self.lEditSnowPeasSep.setEnabled(True)
		self.lEditSnowPeasOct.setEnabled(True)
		self.lEditSnowPeasNov.setEnabled(True)
		self.lEditSnowPeasDec.setEnabled(True)

		self.lEditSpinachJan.setEnabled(True)
		self.lEditSpinachFeb.setEnabled(True)
		self.lEditSpinachMar.setEnabled(True)
		self.lEditSpinachApr.setEnabled(True)
		self.lEditSpinachMay.setEnabled(True)
		self.lEditSpinachJun.setEnabled(True)
		self.lEditSpinachJul.setEnabled(True)
		self.lEditSpinachAug.setEnabled(True)
		self.lEditSpinachSep.setEnabled(True)
		self.lEditSpinachOct.setEnabled(True)
		self.lEditSpinachNov.setEnabled(True)
		self.lEditSpinachDec.setEnabled(True)

		self.lEditWCNJan.setEnabled(True)
		self.lEditWCNFeb.setEnabled(True)
		self.lEditWCNMar.setEnabled(True)
		self.lEditWCNApr.setEnabled(True)
		self.lEditWCNMay.setEnabled(True)
		self.lEditWCNJun.setEnabled(True)
		self.lEditWCNJul.setEnabled(True)
		self.lEditWCNAug.setEnabled(True)
		self.lEditWCNSep.setEnabled(True)
		self.lEditWCNOct.setEnabled(True)
		self.lEditWCNNov.setEnabled(True)
		self.lEditWCNDec.setEnabled(True)

		self.lEditOthersJan.setEnabled(True)
		self.lEditOthersFeb.setEnabled(True)
		self.lEditOthersMar.setEnabled(True)
		self.lEditOthersApr.setEnabled(True)
		self.lEditOthersMay.setEnabled(True)
		self.lEditOthersJun.setEnabled(True)
		self.lEditOthersJul.setEnabled(True)
		self.lEditOthersAug.setEnabled(True)
		self.lEditOthersSep.setEnabled(True)
		self.lEditOthersOct.setEnabled(True)
		self.lEditOthersNov.setEnabled(True)
		self.lEditOthersDec.setEnabled(True)"""
		self.pBtnUpdate.setEnabled(True)
	
	
	def suma(self, *args ):
		result = 0
		for valor in args:
			result = result + valor
		return result

	def resta(self, total, org ):
		
		result = total - org
		print('total ', total, ' org ', org, 'conv ', result)
		return result
	   
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
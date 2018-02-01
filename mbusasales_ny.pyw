#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In thismodule it is input the data of MB USA sales
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
import cajaMensajePregunta as cajaMensaje

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("mbusasales_ny.ui")[0]

class MyWindowClass(QtWidgets.QDialog, form_class):
	def __init__(self, parent=None):
		
		QtWidgets.QDialog.__init__(self, parent)

		self.setupUi(self)

		self.pBtnSelectYear.setEnabled(True)
		self.pBtnUpdate.setEnabled(False)
		self.table = 'mbusasales'
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
		datos = pd.read_csv('mbusasales.csv', index_col = 0, encoding = 'utf-8' )
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
		Sum of all conventional products per month
		"""
		Tot_Conv_Jan = self.suma_Conv_Jan(
			self.broc_Conv_Jan, self.Caulif_Conv_Jan, self.BrSpr_Conv_Jan, 
			self.Ssp_Conv_Jan, self.YSq_Conv_Jan, self.GZucc_Conv_Jan)
		Tot_Conv_Feb = self.suma_Conv_Feb(
			self.broc_Conv_Feb, self.Caulif_Conv_Feb, self.BrSpr_Conv_Feb, 
			self.Ssp_Conv_Feb, self.YSq_Conv_Feb, self.GZucc_Conv_Feb)
		Tot_Conv_Mar = self.suma_Conv_Mar(
			self.broc_Conv_Mar, self.Caulif_Conv_Mar, self.BrSpr_Conv_Mar, 
			self.Ssp_Conv_Mar, self.YSq_Conv_Mar, self.GZucc_Conv_Mar)
		Tot_Conv_Apr = self.suma_Conv_Apr(
			self.broc_Conv_Apr, self.Caulif_Conv_Apr, self.BrSpr_Conv_Apr, 
			self.Ssp_Conv_Apr, self.YSq_Conv_Apr, self.GZucc_Conv_Apr)
		Tot_Conv_May = self.suma_Conv_May(
			self.broc_Conv_May, self.Caulif_Conv_May, self.BrSpr_Conv_May, 
			self.Ssp_Conv_May, self.YSq_Conv_May, self.GZucc_Conv_May)
		Tot_Conv_Jun = self.suma_Conv_Jun(
			self.broc_Conv_Jun, self.Caulif_Conv_Jun, self.BrSpr_Conv_Jun, 
			self.Ssp_Conv_Jun, self.YSq_Conv_Jun, self.GZucc_Conv_Jun)
		Tot_Conv_Jul = self.suma_Conv_Jul(
			self.broc_Conv_Jul, self.Caulif_Conv_Jul, self.BrSpr_Conv_Jul, 
			self.Ssp_Conv_Jul, self.YSq_Conv_Jul, self.GZucc_Conv_Jul)
		Tot_Conv_Aug = self.suma_Conv_Aug(
			self.broc_Conv_Aug, self.Caulif_Conv_Aug, self.BrSpr_Conv_Aug, 
			self.Ssp_Conv_Aug, self.YSq_Conv_Aug, self.GZucc_Conv_Aug)
		Tot_Conv_Sep = self.suma_Conv_Sep(
			self.broc_Conv_Sep, self.Caulif_Conv_Sep, self.BrSpr_Conv_Sep, 
			self.Ssp_Conv_Sep, self.YSq_Conv_Sep, self.GZucc_Conv_Sep)
		Tot_Conv_Oct = self.suma_Conv_Oct(
			self.broc_Conv_Oct, self.Caulif_Conv_Oct, self.BrSpr_Conv_Oct, 
			self.Ssp_Conv_Oct, self.YSq_Conv_Oct, self.GZucc_Conv_Oct)
		Tot_Conv_Nov = self.suma_Conv_Nov(
			self.broc_Conv_Nov, self.Caulif_Conv_Nov, self.BrSpr_Conv_Nov, 
			self.Ssp_Conv_Nov, self.YSq_Conv_Nov, self.GZucc_Conv_Nov)
		Tot_Conv_Dec = self.suma_Conv_Dec(
			self.broc_Conv_Dec, self.Caulif_Conv_Dec, self.BrSpr_Conv_Dec, 
			self.Ssp_Conv_Dec, self.YSq_Conv_Dec, self.GZucc_Conv_Dec)
		
		"""
		Sum of all Organic Products per month
		"""
		Tot_Org_Jan = self.suma_Org_Jan(
			self.broc_Org_Jan, self.Caulif_Org_Jan, self.Carrots_Org_Jan, 
			self.Corn_Org_Jan, self.Edamame_Org_Jan)
		Tot_Org_Feb = self.suma_Org_Feb(
			self.broc_Org_Feb, self.Caulif_Org_Feb, self.Carrots_Org_Feb, 
			self.Corn_Org_Feb, self.Edamame_Org_Feb)
		Tot_Org_Mar = self.suma_Org_Mar(
			self.broc_Org_Mar, self.Caulif_Org_Mar, self.Carrots_Org_Mar, 
			self.Corn_Org_Mar, self.Edamame_Org_Mar)
		Tot_Org_Apr = self.suma_Org_Apr(
			self.broc_Org_Apr, self.Caulif_Org_Apr, self.Carrots_Org_Apr, 
			self.Corn_Org_Apr, self.Edamame_Org_Apr)
		Tot_Org_May = self.suma_Org_May(
			self.broc_Org_May, self.Caulif_Org_May, self.Carrots_Org_May, 
			self.Corn_Org_May, self.Edamame_Org_May)
		Tot_Org_Jun = self.suma_Org_Jun(
			self.broc_Org_Jun, self.Caulif_Org_Jun, self.Carrots_Org_Jun, 
			self.Corn_Org_Jun, self.Edamame_Org_Jun)
		Tot_Org_Jul = self.suma_Org_Jul(
			self.broc_Org_Jul, self.Caulif_Org_Jul, self.Carrots_Org_Jul, 
			self.Corn_Org_Jul, self.Edamame_Org_Jul)
		Tot_Org_Aug = self.suma_Org_Aug(
			self.broc_Org_Aug, self.Caulif_Org_Aug, self.Carrots_Org_Aug, 
			self.Corn_Org_Aug, self.Edamame_Org_Aug)
		Tot_Org_Sep = self.suma_Org_Sep(
			self.broc_Org_Sep, self.Caulif_Org_Sep, self.Carrots_Org_Sep, 
			self.Corn_Org_Sep, self.Edamame_Org_Sep)
		Tot_Org_Oct = self.suma_Org_Oct(
			self.broc_Org_Oct, self.Caulif_Org_Oct, self.Carrots_Org_Oct, 
			self.Corn_Org_Oct, self.Edamame_Org_Oct)
		Tot_Org_Nov = self.suma_Org_Nov(
			self.broc_Org_Nov, self.Caulif_Org_Nov, self.Carrots_Org_Nov, 
			self.Corn_Org_Nov, self.Edamame_Org_Nov)
		Tot_Org_Dec = self.suma_Org_Dec(
			self.broc_Org_Dec, self.Caulif_Org_Dec, self.Carrots_Org_Dec, 
			self.Corn_Org_Dec, self.Edamame_Org_Dec)
			   
		#Sum of Conventional Broccoli
		broc_Conv_Total_Anual = self.suma_Broc_Conv(
			self.broc_Conv_Jan, self.broc_Conv_Feb, self.broc_Conv_Mar, 
			self.broc_Conv_Apr, self.broc_Conv_May, self.broc_Conv_Jun,
			self.broc_Conv_Jul, self.broc_Conv_Aug, self.broc_Conv_Sep, 
			self.broc_Conv_Oct, self.broc_Conv_Nov, self.broc_Conv_Dec)
		
		#Sum of Conventional Cauliflower
		caulif_Conv_Total_Anual = self.suma_Caulif_Conv(
			self.Caulif_Conv_Jan, self.Caulif_Conv_Feb, self.Caulif_Conv_Mar, 
			self.Caulif_Conv_Apr, self.Caulif_Conv_May, self.Caulif_Conv_Jun, 
			self.Caulif_Conv_Jul, self.Caulif_Conv_Aug, self.Caulif_Conv_Sep, 
			self.Caulif_Conv_Oct, self.Caulif_Conv_Nov, self.Caulif_Conv_Dec)
		
		brSpr_Conv_Total_Anual = self.suma_BrSpr_Conv(
			self.BrSpr_Conv_Jan, self.BrSpr_Conv_Feb, self.BrSpr_Conv_Mar, 
			self.BrSpr_Conv_Apr, self.BrSpr_Conv_May, self.BrSpr_Conv_Jun, 
			self.BrSpr_Conv_Jul, self.BrSpr_Conv_Aug, self.BrSpr_Conv_Sep, 
			self.BrSpr_Conv_Oct, self.BrSpr_Conv_Nov, self.BrSpr_Conv_Dec)
		
		Ssp_Conv_Total_Anual = self.suma_Ssp_Conv(
			self.Ssp_Conv_Jan, self.Ssp_Conv_Feb, self.Ssp_Conv_Mar, 
			self.Ssp_Conv_Apr, self.Ssp_Conv_May, self.Ssp_Conv_Jun, 
			self.Ssp_Conv_Jul, self.Ssp_Conv_Aug, self.Ssp_Conv_Sep, 
			self.Ssp_Conv_Oct, self.Ssp_Conv_Nov, self.Ssp_Conv_Dec)
		
		YSq_Conv_Total_Anual = self.suma_YSq_Conv(
			self.YSq_Conv_Jan, self.YSq_Conv_Feb, self.YSq_Conv_Mar, 
			self.YSq_Conv_Apr, self.YSq_Conv_May, self.YSq_Conv_Jun, 
			self.YSq_Conv_Jul, self.YSq_Conv_Aug, self.YSq_Conv_Sep, 
			self.YSq_Conv_Oct, self.YSq_Conv_Nov, self.YSq_Conv_Dec)
		
		GZucc_Conv_Total_Anual = self.suma_GZucc_Conv(
			self.GZucc_Conv_Jan, self.GZucc_Conv_Feb, self.GZucc_Conv_Mar, 
			self.GZucc_Conv_Apr, self.GZucc_Conv_May, self.GZucc_Conv_Jun, 
			self.GZucc_Conv_Jul, self.GZucc_Conv_Aug, self.GZucc_Conv_Sep, 
			self.GZucc_Conv_Oct, self.GZucc_Conv_Nov, self.GZucc_Conv_Dec)
		
		Brocc_Org_Total_Anual = self.suma_Brocc_Org(
			self.broc_Org_Jan, self.broc_Org_Feb, self.broc_Org_Mar, 
			self.broc_Org_Apr, self.broc_Org_May, self.broc_Org_Jun, 
			self.broc_Org_Jul, self.broc_Org_Aug, self.broc_Org_Sep, 
			self.broc_Org_Oct, self.broc_Org_Nov, self.broc_Org_Dec)
		
		Cauliflower_Org_Total_Anual = self.suma_Cauliflower_Org(
			self.Caulif_Org_Jan, self.Caulif_Org_Feb, self.Caulif_Org_Mar, 
			self.Caulif_Org_Apr, self.Caulif_Org_May, self.Caulif_Org_Jun, 
			self.Caulif_Org_Jul, self.Caulif_Org_Aug, self.Caulif_Org_Sep, 
			self.Caulif_Org_Oct, self.Caulif_Org_Nov, self.Caulif_Org_Dec)
		
		Carrots_Org_Total_Anual = self.suma_Carrots_Org(
			self.Carrots_Org_Jan, self.Carrots_Org_Feb, self.Carrots_Org_Mar,
			 self.Carrots_Org_Apr, self.Carrots_Org_May, self.Carrots_Org_Jun, 
			self.Carrots_Org_Jul, self.Carrots_Org_Aug, self.Carrots_Org_Sep, 
			self.Carrots_Org_Oct, self.Carrots_Org_Nov, self.Carrots_Org_Dec)
		
		Corm_Org_Total_Anual = self.suma_Corn_Org(
			self.Corn_Org_Jan, self.Corn_Org_Feb, self.Corn_Org_Mar, 
			self.Corn_Org_Apr, self.Corn_Org_May, self.Corn_Org_Jun, 
			self.Corn_Org_Jul, self.Corn_Org_Aug, self.Corn_Org_Sep, 
			self.Corn_Org_Oct, self.Corn_Org_Nov, self.Corn_Org_Dec)
		
		Edamame_Org_Total_Anual = self.suma_Edamame_Org(
			self.Edamame_Org_Jan, self.Edamame_Org_Feb, self.Edamame_Org_Mar, 
			self.Edamame_Org_Apr, self.Edamame_Org_May, self.Edamame_Org_Jun, 
			self.Edamame_Org_Jul, self.Edamame_Org_Aug, self.Edamame_Org_Sep, 
			self.Edamame_Org_Oct, self.Edamame_Org_Nov, self.Edamame_Org_Dec)

		self.Total_Jan = self.suma (Tot_Conv_Jan, Tot_Org_Jan )
		self.lblTotalJan.setText(str(self.Total_Jan))
		
		self.Total_Feb = self.suma (Tot_Conv_Feb, Tot_Org_Feb )
		self.lblTotalFeb.setText(str(self.Total_Feb))
		
		self.Total_Mar = self.suma (Tot_Conv_Mar, Tot_Org_Mar )
		self.lblTotalMar.setText(str(self.Total_Mar))
		
		self.Total_Apr = self.suma (Tot_Conv_Apr, Tot_Org_Apr )
		self.lblTotalApr.setText(str(self.Total_Apr))
		
		self.Total_May = self.suma (Tot_Conv_May, Tot_Org_May )
		self.lblTotalMay.setText(str(self.Total_May))
		
		self.Total_Jun = self.suma (Tot_Conv_Jun, Tot_Org_Jun )
		self.lblTotalJun.setText(str(self.Total_Jun))
		
		self.Total_Jul = self.suma (Tot_Conv_Jul, Tot_Org_Jul )
		self.lblTotalJul.setText(str(self.Total_Jul))
		
		self.Total_Aug = self.suma (Tot_Conv_Aug, Tot_Org_Aug )
		self.lblTotalAug.setText(str(self.Total_Aug))
		
		self.Total_Sep = self.suma (Tot_Conv_Sep, Tot_Org_Sep )
		self.lblTotalSep.setText(str(self.Total_Sep))
		
		self.Total_Oct = self.suma (Tot_Conv_Oct, Tot_Org_Oct )
		self.lblTotalOct.setText(str(self.Total_Oct))
		
		self.Total_Nov = self.suma (Tot_Conv_Nov, Tot_Org_Nov )
		self.lblTotalNov.setText(str(self.Total_Nov))
		
		self.Total_Dec = self.suma (Tot_Conv_Dec, Tot_Org_Dec )
		self.lblTotalDec.setText(str(self.Total_Dec))

		self.total_Anual = self.suma(
			self.Total_Jan, self.Total_Feb, self.Total_Mar, 
			self.Total_Apr, self.Total_May, self.Total_Jun,
			 self.Total_Jul, self.Total_Aug, self.Total_Sep, 
			 self.Total_Oct, self.Total_Nov, self.Total_Dec)
		self.lblTotalAnual.setText(str(self.total_Anual))
		
		Total_Conv_Anual = self.suma(
			Tot_Conv_Jan, Tot_Conv_Feb, Tot_Conv_Mar, Tot_Conv_Apr, 
			Tot_Conv_May, Tot_Conv_Jun, Tot_Conv_Jul, Tot_Conv_Aug, 
			Tot_Conv_Sep, Tot_Conv_Oct, Tot_Conv_Nov, Tot_Conv_Dec)
		self.lblTotConvAnual.setText(str(Total_Conv_Anual))
		
		Total_Org_Anual = self.suma(
			Tot_Org_Jan, Tot_Org_Feb, Tot_Org_Mar, Tot_Org_Apr, 
			Tot_Org_May, Tot_Org_Jun, Tot_Org_Jul, Tot_Org_Aug, 
			Tot_Org_Sep, Tot_Org_Oct, Tot_Org_Nov, Tot_Org_Dec)
		
		self.lblTotOrgAnual.setText(str(Total_Org_Anual))
		self.pBtnSave.setEnabled(True)

	def inicializar_campós(self):
		"""
		This function set all field values as Zero
		"""
		self.lEditBrConvJan.insert(str(0))
		self.lEditBrConvFeb.insert(str(0))
		self.lEditBrConvMar.insert(str(0))
		self.lEditBrConvApr.insert(str(0))
		self.lEditBrConvMay.insert(str(0))
		self.lEditBrConvJun.insert(str(0))
		self.lEditBrConvJul.insert(str(0))
		self.lEditBrConvAug.insert(str(0))
		self.lEditBrConvSep.insert(str(0))
		self.lEditBrConvOct.insert(str(0))
		self.lEditBrConvNov.insert(str(0))
		self.lEditBrConvDec.insert(str(0))
		
		self.lEditCaulifConvJan.insert(str(0))
		self.lEditCaulifConvFeb.insert(str(0))
		self.lEditCaulifConvMar.insert(str(0))
		self.lEditCaulifConvApr.insert(str(0))
		self.lEditCaulifConvMay.insert(str(0))
		self.lEditCaulifConvJun.insert(str(0))
		self.lEditCaulifConvJul.insert(str(0))
		self.lEditCaulifConvAug.insert(str(0))
		self.lEditCaulifConvSep.insert(str(0))
		self.lEditCaulifConvOct.insert(str(0))
		self.lEditCaulifConvNov.insert(str(0))
		self.lEditCaulifConvDec.insert(str(0))

		self.lEditSspConvJan.insert(str(0))
		self.lEditSspConvFeb.insert(str(0))
		self.lEditSspConvMar.insert(str(0))
		self.lEditSspConvApr.insert(str(0))
		self.lEditSspConvMay.insert(str(0))
		self.lEditSspConvJun.insert(str(0))
		self.lEditSspConvJul.insert(str(0))
		self.lEditSspConvAug.insert(str(0))
		self.lEditSspConvSep.insert(str(0))
		self.lEditSspConvOct.insert(str(0))
		self.lEditSspConvNov.insert(str(0))
		self.lEditSspConvDec.insert(str(0))   
		
		self.lEditBSprConvJan.insert(str(0))
		self.lEditBSprConvFeb.insert(str(0))
		self.lEditBSprConvMar.insert(str(0))
		self.lEditBSprConvApr.insert(str(0))
		self.lEditBSprConvMay.insert(str(0))
		self.lEditBSprConvJun.insert(str(0))
		self.lEditBSprConvJul.insert(str(0))
		self.lEditBSprConvAug.insert(str(0))
		self.lEditBSprConvSep.insert(str(0))
		self.lEditBSprConvOct.insert(str(0))
		self.lEditBSprConvNov.insert(str(0))
		self.lEditBSprConvDec.insert(str(0))
		
		self.lEditYSqConvJan.insert(str(0))
		self.lEditYSqConvFeb.insert(str(0))
		self.lEditYSqConvMar.insert(str(0))
		self.lEditYSqConvApr.insert(str(0))
		self.lEditYSqConvMay.insert(str(0))
		self.lEditYSqConvJun.insert(str(0))
		self.lEditYSqConvJul.insert(str(0))
		self.lEditYSqConvAug.insert(str(0))
		self.lEditYSqConvSep.insert(str(0))
		self.lEditYSqConvOct.insert(str(0))
		self.lEditYSqConvNov.insert(str(0))
		self.lEditYSqConvDec.insert(str(0))
		
		self.lEditGZuccConvJan.insert(str(0))
		self.lEditGZuccConvFeb.insert(str(0))
		self.lEditGZuccConvMar.insert(str(0))
		self.lEditGZuccConvApr.insert(str(0))
		self.lEditGZuccConvMay.insert(str(0))
		self.lEditGZuccConvJun.insert(str(0))
		self.lEditGZuccConvJul.insert(str(0))
		self.lEditGZuccConvAug.insert(str(0))
		self.lEditGZuccConvSep.insert(str(0))
		self.lEditGZuccConvOct.insert(str(0))
		self.lEditGZuccConvNov.insert(str(0))
		self.lEditGZuccConvDec.insert(str(0))
		
		self.lEditBroccOrgJan.insert(str(0))
		self.lEditBroccOrgFeb.insert(str(0))
		self.lEditBroccOrgMar.insert(str(0))
		self.lEditBroccOrgApr.insert(str(0))
		self.lEditBroccOrgMay.insert(str(0))
		self.lEditBroccOrgJun.insert(str(0))
		self.lEditBroccOrgJul.insert(str(0))
		self.lEditBroccOrgAug.insert(str(0))
		self.lEditBroccOrgSep.insert(str(0))
		self.lEditBroccOrgOct.insert(str(0))
		self.lEditBroccOrgNov.insert(str(0))
		self.lEditBroccOrgDec.insert(str(0))
		
		self.lEditCaulifOrgJan.insert(str(0))
		self.lEditCaulifOrgFeb.insert(str(0))
		self.lEditCaulifOrgMar.insert(str(0))
		self.lEditCaulifOrgApr.insert(str(0))
		self.lEditCaulifOrgMay.insert(str(0))
		self.lEditCaulifOrgJun.insert(str(0))
		self.lEditCaulifOrgJul.insert(str(0))
		self.lEditCaulifOrgAug.insert(str(0))
		self.lEditCaulifOrgSep.insert(str(0))
		self.lEditCaulifOrgOct.insert(str(0))
		self.lEditCaulifOrgNov.insert(str(0))
		self.lEditCaulifOrgDec.insert(str(0))
		
		self.lEditCarrotsOrgJan.insert(str(0))
		self.lEditCarrotsOrgFeb.insert(str(0))
		self.lEditCarrotsOrgMar.insert(str(0))
		self.lEditCarrotsOrgApr.insert(str(0))
		self.lEditCarrotsOrgMay.insert(str(0))
		self.lEditCarrotsOrgJun.insert(str(0))
		self.lEditCarrotsOrgJul.insert(str(0))
		self.lEditCarrotsOrgAug.insert(str(0))
		self.lEditCarrotsOrgSep.insert(str(0))
		self.lEditCarrotsOrgOct.insert(str(0))
		self.lEditCarrotsOrgNov.insert(str(0))
		self.lEditCarrotsOrgDec.insert(str(0))
		
		self.lEditCornOrgJan.insert(str(0))
		self.lEditCornOrgFeb.insert(str(0))
		self.lEditCornOrgMar.insert(str(0))
		self.lEditCornOrgApr.insert(str(0))
		self.lEditCornOrgMay.insert(str(0))
		self.lEditCornOrgJun.insert(str(0))
		self.lEditCornOrgJul.insert(str(0))
		self.lEditCornOrgAug.insert(str(0))
		self.lEditCornOrgSep.insert(str(0))
		self.lEditCornOrgOct.insert(str(0))
		self.lEditCornOrgNov.insert(str(0))
		self.lEditCornOrgDec.insert(str(0))
		
		self.lEditEdamameOrgJan.insert(str(0))
		self.lEditEdamameOrgFeb.insert(str(0))
		self.lEditEdamameOrgMar.insert(str(0))
		self.lEditEdamameOrgApr.insert(str(0))
		self.lEditEdamameOrgMay.insert(str(0))
		self.lEditEdamameOrgJun.insert(str(0))
		self.lEditEdamameOrgJul.insert(str(0))
		self.lEditEdamameOrgAug.insert(str(0))
		self.lEditEdamameOrgSep.insert(str(0))
		self.lEditEdamameOrgOct.insert(str(0))
		self.lEditEdamameOrgNov.insert(str(0))
		self.lEditEdamameOrgDec.insert(str(0))
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
				brocc_Conv = self.broc_Conv_Jan
				cauliflower_Conv = self.Caulif_Conv_Jan
				BrSp_Conv = self.BrSpr_Conv_Jan
				Ssp_Conv = self.Ssp_Conv_Jan
				YSq_Conv = self.YSq_Conv_Jan
				GZucc_Conv = self.GZucc_Conv_Jan
				brocc_Org = self.broc_Org_Jan
				Caulif_Org = self.Caulif_Org_Jan
				Carrots_Org = self.Carrots_Org_Jan
				Corn_Org = self.Corn_Org_Jan
				Edamame_Org = self.Edamame_Org_Jan
				
			elif values.find('feb')>0: 
				indice = values
				month = 'February'
				brocc_Conv = self.broc_Conv_Feb
				cauliflower_Conv = self.Caulif_Conv_Feb
				BrSp_Conv = self.BrSpr_Conv_Feb
				Ssp_Conv = self.Ssp_Conv_Feb
				YSq_Conv = self.YSq_Conv_Feb
				GZucc_Conv = self.GZucc_Conv_Feb
				brocc_Org = self.broc_Org_Feb
				Caulif_Org = self.Caulif_Org_Feb
				Carrots_Org = self.Carrots_Org_Feb
				Corn_Org = self.Corn_Org_Feb
				Edamame_Org = self.Edamame_Org_Feb
				
			elif values.find('mar')>0: 
				indice = values
				month = 'March'
				brocc_Conv = self.broc_Conv_Mar
				cauliflower_Conv = self.Caulif_Conv_Mar
				BrSp_Conv = self.BrSpr_Conv_Mar
				Ssp_Conv = self.Ssp_Conv_Mar
				YSq_Conv = self.YSq_Conv_Mar
				GZucc_Conv = self.GZucc_Conv_Mar
				brocc_Org = self.broc_Org_Mar
				Caulif_Org = self.Caulif_Org_Mar
				Carrots_Org = self.Carrots_Org_Mar
				Corn_Org = self.Corn_Org_Mar
				Edamame_Org = self.Edamame_Org_Mar
				
			elif values.find('apr')>0: 
				indice = values
				month = 'April'
				brocc_Conv = self.broc_Conv_Apr
				cauliflower_Conv = self.Caulif_Conv_Apr
				BrSp_Conv = self.BrSpr_Conv_Apr
				Ssp_Conv = self.Ssp_Conv_Apr
				YSq_Conv = self.YSq_Conv_Apr
				GZucc_Conv = self.GZucc_Conv_Apr
				brocc_Org = self.broc_Org_Apr
				Caulif_Org = self.Caulif_Org_Apr
				Carrots_Org = self.Carrots_Org_Apr
				Corn_Org = self.Corn_Org_Apr
				Edamame_Org = self.Edamame_Org_Apr
				
			elif values.find('may')>0: 
				indice = values
				month = 'May'
				brocc_Conv = self.broc_Conv_May
				cauliflower_Conv = self.Caulif_Conv_May
				BrSp_Conv = self.BrSpr_Conv_May
				Ssp_Conv = self.Ssp_Conv_May
				YSq_Conv = self.YSq_Conv_May
				GZucc_Conv = self.GZucc_Conv_May
				brocc_Org = self.broc_Org_May
				Caulif_Org = self.Caulif_Org_May
				Carrots_Org = self.Carrots_Org_May
				Corn_Org = self.Corn_Org_May
				Edamame_Org = self.Edamame_Org_May
				
			elif values.find('jun')>0: 
				indice = values
				month = 'June'
				brocc_Conv = self.broc_Conv_Jun
				cauliflower_Conv = self.Caulif_Conv_Jun
				BrSp_Conv = self.BrSpr_Conv_Jun
				Ssp_Conv = self.Ssp_Conv_Jun
				YSq_Conv = self.YSq_Conv_Jun
				GZucc_Conv = self.GZucc_Conv_Jun
				brocc_Org = self.broc_Org_Jun
				Caulif_Org = self.Caulif_Org_Jun
				Carrots_Org = self.Carrots_Org_Jun
				Corn_Org = self.Corn_Org_Jun
				Edamame_Org = self.Edamame_Org_Jun
				
			elif values.find('jul')>0: 
				indice = values
				month = 'July'
				brocc_Conv = self.broc_Conv_Jul
				cauliflower_Conv = self.Caulif_Conv_Jul
				BrSp_Conv = self.BrSpr_Conv_Jul
				Ssp_Conv = self.Ssp_Conv_Jul
				YSq_Conv = self.YSq_Conv_Jul
				GZucc_Conv = self.GZucc_Conv_Jul
				brocc_Org = self.broc_Org_Jul
				Caulif_Org = self.Caulif_Org_Jul
				Carrots_Org = self.Carrots_Org_Jul
				Corn_Org = self.Corn_Org_Jul
				Edamame_Org = self.Edamame_Org_Jul
				
			elif values.find('aug')>0: 
				indice = values
				month = 'August'
				brocc_Conv = self.broc_Conv_Aug
				cauliflower_Conv = self.Caulif_Conv_Aug
				BrSp_Conv = self.BrSpr_Conv_Aug
				Ssp_Conv = self.Ssp_Conv_Aug
				YSq_Conv = self.YSq_Conv_Aug
				GZucc_Conv = self.GZucc_Conv_Aug
				brocc_Org = self.broc_Org_Aug
				Caulif_Org = self.Caulif_Org_Aug
				Carrots_Org = self.Carrots_Org_Aug
				Corn_Org = self.Corn_Org_Aug
				Edamame_Org = self.Edamame_Org_Aug
				
			elif values.find('sep')>0: 
				indice = values
				month = 'September'
				brocc_Conv = self.broc_Conv_Sep
				cauliflower_Conv = self.Caulif_Conv_Sep
				BrSp_Conv = self.BrSpr_Conv_Sep
				Ssp_Conv = self.Ssp_Conv_Sep
				YSq_Conv = self.YSq_Conv_Sep
				GZucc_Conv = self.GZucc_Conv_Sep
				brocc_Org = self.broc_Org_Sep
				Caulif_Org = self.Caulif_Org_Sep
				Carrots_Org = self.Carrots_Org_Sep
				Corn_Org = self.Corn_Org_Sep
				Edamame_Org = self.Edamame_Org_Sep
				
			elif values.find('oct')>0: 
				indice = values
				month = 'October'
				brocc_Conv = self.broc_Conv_Oct
				cauliflower_Conv = self.Caulif_Conv_Oct
				BrSp_Conv = self.BrSpr_Conv_Oct
				Ssp_Conv = self.Ssp_Conv_Oct
				YSq_Conv = self.YSq_Conv_Oct
				GZucc_Conv = self.GZucc_Conv_Oct
				brocc_Org = self.broc_Org_Oct
				Caulif_Org = self.Caulif_Org_Oct
				Carrots_Org = self.Carrots_Org_Oct
				Corn_Org = self.Corn_Org_Oct
				Edamame_Org = self.Edamame_Org_Oct
				
			elif values.find('nov')>0: 
				indice = values
				month = 'November'
				brocc_Conv = self.broc_Conv_Nov
				cauliflower_Conv = self.Caulif_Conv_Nov
				BrSp_Conv = self.BrSpr_Conv_Nov
				Ssp_Conv = self.Ssp_Conv_Nov
				YSq_Conv = self.YSq_Conv_Nov
				GZucc_Conv = self.GZucc_Conv_Nov
				brocc_Org = self.broc_Org_Nov
				Caulif_Org = self.Caulif_Org_Nov
				Carrots_Org = self.Carrots_Org_Nov
				Corn_Org = self.Corn_Org_Nov
				Edamame_Org = self.Edamame_Org_Nov
				
			elif values.find('dec')>0: 
				indice = values
				month = 'December'
				brocc_Conv = self.broc_Conv_Dec
				cauliflower_Conv = self.Caulif_Conv_Dec
				BrSp_Conv = self.BrSpr_Conv_Dec
				Ssp_Conv = self.Ssp_Conv_Dec
				YSq_Conv = self.YSq_Conv_Dec
				GZucc_Conv = self.GZucc_Conv_Dec
				brocc_Org = self.broc_Org_Dec
				Caulif_Org = self.Caulif_Org_Dec
				Carrots_Org = self.Carrots_Org_Dec
				Corn_Org = self.Corn_Org_Dec
				Edamame_Org = self.Edamame_Org_Dec
				
			data = {values : [sequence , indice, year, month, brocc_Conv, 
				cauliflower_Conv, BrSp_Conv, Ssp_Conv, YSq_Conv, GZucc_Conv, 
				  brocc_Org, Caulif_Org, Carrots_Org, Corn_Org, Edamame_Org]}
			data_dict.update(data)

		message = 'Now we are going to save the file'
		self.caja_mensaje('Save data;', message,0)
		datos_Sales_Mbusa =pd.read_csv('mbusasales.csv', index_col = 0, encoding = 'utf-8')
		datos_Sales_Mbusa.apply(lambda x: pd.lib.infer_dtype(x.values))
		num_datos = int(datos_Sales_Mbusa['indice'].count())
		datos_Sales_Mbusa.index = range(datos_Sales_Mbusa.shape[0])
		indice_archivo = list(datos_Sales_Mbusa.indice)
		llaves = data_dict.keys()
		nuevo_Valor = num_datos+1
		valores = list(data_dict.values())
		
		for i, valor in enumerate(valores):
			nuevo_valor = int(nuevo_Valor)+i
			datos_Sales_Mbusa.loc[int(nuevo_valor)]= [
				valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], 
				valor[7], valor[8], valor[9], valor[10], valor[11], 
				valor[12], valor[13],valor[14]]
		try: 
			datos_Sales_Mbusa.to_csv('mbusasales.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
	
	def suma_Conv_Jan(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv,):
		self.sum_Conv_Jan = self.suma( 
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvJan.setText(str(self.sum_Conv_Jan))
		return self.sum_Conv_Jan      

	def suma_Conv_Feb(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Feb = self.suma(  
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvFeb.setText(str(self.sum_Conv_Feb))
		return self.sum_Conv_Feb
		
	def suma_Conv_Mar(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Mar = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvMar.setText(str(self.sum_Conv_Mar))
		return self.sum_Conv_Mar
		
	
	def suma_Conv_Apr(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Apr = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvApr.setText(str(self.sum_Conv_Apr))
		return self.sum_Conv_Apr
	
	def suma_Conv_May(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_May = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvMay.setText(str(self.sum_Conv_May))
		return self.sum_Conv_May
		
	def suma_Conv_Jun(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Jun = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvJun.setText(str(self.sum_Conv_Jun))
		return self.sum_Conv_Jun
		
	def suma_Conv_Jul(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Jul = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvJul.setText(str(self.sum_Conv_Jul))
		return self.sum_Conv_Jul
		
	def suma_Conv_Aug(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Aug = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvAug.setText(str(self.sum_Conv_Aug))
		return self.sum_Conv_Aug
		
	def suma_Conv_Sep(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Sep = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvSep.setText(str(self.sum_Conv_Sep))
		return self.sum_Conv_Sep
		
	def suma_Conv_Oct(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Oct = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvOct.setText(str(self.sum_Conv_Oct))
		return self.sum_Conv_Oct
		
	def suma_Conv_Nov(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Nov = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvNov.setText(str(self.sum_Conv_Nov))
		return self.sum_Conv_Nov
		
		
	def suma_Conv_Dec(self, broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv):
		self.sum_Conv_Dec = self.suma(
			broccConv, CaulifConv, BrSpCon, SspConv, QSqConv, GZuccConv)
		self.lblTotConvDec.setText(str(self.sum_Conv_Dec))
		return self.sum_Conv_Dec
		
	def suma_Org_Jan(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Jan = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgJan.setText(str(self.sum_Org_Jan))
		return self.sum_Org_Jan
		
	def suma_Org_Feb(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Feb = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgFeb.setText(str(self.sum_Org_Feb))
		return self.sum_Org_Feb
	
	def suma_Org_Mar(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Mar = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgMar.setText(str(self.sum_Org_Mar))
		return self.sum_Org_Mar
	
	def suma_Org_Apr(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Apr = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgApr.setText(str(self.sum_Org_Apr))
		return self.sum_Org_Apr
	
	def suma_Org_May(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_May = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgMay.setText(str(self.sum_Org_May))
		return self.sum_Org_May
	
	def suma_Org_Jun(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Jun = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgJun.setText(str(self.sum_Org_Jun))
		return self.sum_Org_Jun
	
	def suma_Org_Jul(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Jul = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgJul.setText(str(self.sum_Org_Jul))
		return self.sum_Org_Jul
	
	def suma_Org_Aug(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Aug = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgAug.setText(str(self.sum_Org_Aug))
		return self.sum_Org_Aug
	
	def suma_Org_Sep(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Sep = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgSep.setText(str(self.sum_Org_Sep))
		return self.sum_Org_Sep
	
	def suma_Org_Oct(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Oct = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgOct.setText(str(self.sum_Org_Oct))
		return self.sum_Org_Oct
	
	def suma_Org_Nov(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Nov = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgNov.setText(str(self.sum_Org_Nov))
		return self.sum_Org_Nov
	
	def suma_Org_Dec(self, broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg):
		self.sum_Org_Dec = self.suma(
			broccOrg, CaulifOrg, CarrotsOrg, CornOrg, EdamameOrg)
		self.lblTotalOrgDec.setText(str(self.sum_Org_Dec))
		return self.sum_Org_Dec
	
	
	def suma_Broc_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.broc_Conv_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBrocConv.setText(str(self.broc_Conv_Total_Anual))
		return self.broc_Conv_Total_Anual
		
	def suma_Brocc_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.broc_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBrocOrg.setText(str(self.broc_Org_Total_Anual))
		return self.broc_Org_Total_Anual
	
	def suma_Caulif_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.caulif_Conv_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualCaulifConv.setText(str(self.caulif_Conv_Total_Anual))
		return self.broc_Conv_Total_Anual
		
	def suma_Cauliflower_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.caulif_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualCaulOrg.setText(str(self.caulif_Org_Total_Anual))
		return self.broc_Org_Total_Anual    
	
	def suma_BrSpr_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.BrSpr_Conv_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBSprConv.setText(str(self.BrSpr_Conv_Total_Anual))
		return self.BrSpr_Conv_Total_Anual

	def suma_Carrots_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Carrots_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotAnualCarrotOrg.setText(str(self.Carrots_Org_Total_Anual))
		return self.Carrots_Org_Total_Anual

	def suma_Corn_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Corn_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualCornOrg.setText(str(self.Corn_Org_Total_Anual))
		return self.Corn_Org_Total_Anual

	def suma_Edamame_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Edamame_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotAnualEdamOrg.setText(str(self.Edamame_Org_Total_Anual))
		return self.Edamame_Org_Total_Anual

	def suma_Ssp_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Ssp_Conv_Total_Anual = self.suma(
		jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualSnpConv.setText(str(self.Ssp_Conv_Total_Anual))
		return self.Ssp_Conv_Total_Anual
		
	def suma_YSq_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.YSq_Conv_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualYSConv.setText(str(self.YSq_Conv_Total_Anual))
		return self.YSq_Conv_Total_Anual
	
	def suma_GZucc_Conv(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.GZucc_Conv_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualGZuccConv.setText(str(self.GZucc_Conv_Total_Anual))
		return self.GZucc_Conv_Total_Anual
	
	def read_data_from_fields(self):
		self.broc_Conv_Jan = int(self.lEditBrConvJan.text())
		self.broc_Conv_Feb = int(self.lEditBrConvFeb.text())
		self.broc_Conv_Mar = int(self.lEditBrConvMar.text())
		self.broc_Conv_Apr = int(self.lEditBrConvApr.text())
		self.broc_Conv_May = int(self.lEditBrConvMay.text())
		self.broc_Conv_Jun = int(self.lEditBrConvJun.text())
		self.broc_Conv_Jul = int(self.lEditBrConvJul.text())
		self.broc_Conv_Aug = int(self.lEditBrConvAug.text())
		self.broc_Conv_Sep = int(self.lEditBrConvSep.text())
		self.broc_Conv_Oct = int(self.lEditBrConvOct.text())
		self.broc_Conv_Nov = int(self.lEditBrConvNov.text())
		self.broc_Conv_Dec = int(self.lEditBrConvDec.text())
		
		self.Caulif_Conv_Jan = int(self.lEditCaulifConvJan.text())
		self.Caulif_Conv_Feb = int(self.lEditCaulifConvFeb.text())
		self.Caulif_Conv_Mar = int(self.lEditCaulifConvMar.text())
		self.Caulif_Conv_Apr = int(self.lEditCaulifConvApr.text())
		self.Caulif_Conv_May = int(self.lEditCaulifConvMay.text())
		self.Caulif_Conv_Jun = int(self.lEditCaulifConvJun.text())
		self.Caulif_Conv_Jul = int(self.lEditCaulifConvJul.text())
		self.Caulif_Conv_Aug = int(self.lEditCaulifConvAug.text())
		self.Caulif_Conv_Sep = int(self.lEditCaulifConvSep.text())
		self.Caulif_Conv_Oct = int(self.lEditCaulifConvOct.text())
		self.Caulif_Conv_Nov = int(self.lEditCaulifConvNov.text())
		self.Caulif_Conv_Dec = int(self.lEditCaulifConvDec.text())
		
		self.BrSpr_Conv_Jan = int(self.lEditBSprConvJan.text())
		self.BrSpr_Conv_Feb = int(self.lEditBSprConvFeb.text())
		self.BrSpr_Conv_Mar = int(self.lEditBSprConvMar.text())
		self.BrSpr_Conv_Apr = int(self.lEditBSprConvApr.text())
		self.BrSpr_Conv_May = int(self.lEditBSprConvMay.text())
		self.BrSpr_Conv_Jun = int(self.lEditBSprConvJun.text())
		self.BrSpr_Conv_Jul = int(self.lEditBSprConvJul.text())
		self.BrSpr_Conv_Aug = int(self.lEditBSprConvAug.text())
		self.BrSpr_Conv_Sep = int(self.lEditBSprConvSep.text())
		self.BrSpr_Conv_Oct = int(self.lEditBSprConvOct.text())
		self.BrSpr_Conv_Nov = int(self.lEditBSprConvNov.text())
		self.BrSpr_Conv_Dec = int(self.lEditBSprConvDec.text())
		
		self.Ssp_Conv_Jan = int(self.lEditSspConvJan.text())
		self.Ssp_Conv_Feb = int(self.lEditSspConvFeb.text())
		self.Ssp_Conv_Mar = int(self.lEditSspConvMar.text())
		self.Ssp_Conv_Apr = int(self.lEditSspConvApr.text())
		self.Ssp_Conv_May = int(self.lEditSspConvMay.text())
		self.Ssp_Conv_Jun = int(self.lEditSspConvJun.text())
		self.Ssp_Conv_Jul = int(self.lEditSspConvJul.text())
		self.Ssp_Conv_Aug = int(self.lEditSspConvAug.text())
		self.Ssp_Conv_Sep = int(self.lEditSspConvSep.text())
		self.Ssp_Conv_Oct = int(self.lEditSspConvOct.text())
		self.Ssp_Conv_Nov = int(self.lEditSspConvNov.text())
		self.Ssp_Conv_Dec = int(self.lEditSspConvDec.text())
		
		self.YSq_Conv_Jan = int(self.lEditYSqConvJan.text())
		self.YSq_Conv_Feb = int(self.lEditYSqConvFeb.text())
		self.YSq_Conv_Mar = int(self.lEditYSqConvMar.text())
		self.YSq_Conv_Apr = int(self.lEditYSqConvApr.text())
		self.YSq_Conv_May = int(self.lEditYSqConvMay.text())
		self.YSq_Conv_Jun = int(self.lEditYSqConvJun.text())
		self.YSq_Conv_Jul = int(self.lEditYSqConvJul.text())
		self.YSq_Conv_Aug = int(self.lEditYSqConvAug.text())
		self.YSq_Conv_Sep = int(self.lEditYSqConvSep.text())
		self.YSq_Conv_Oct = int(self.lEditYSqConvOct.text())
		self.YSq_Conv_Nov = int(self.lEditYSqConvNov.text())
		self.YSq_Conv_Dec = int(self.lEditYSqConvDec.text())
		
		self.GZucc_Conv_Jan = int(self.lEditGZuccConvJan.text())
		self.GZucc_Conv_Feb = int(self.lEditGZuccConvFeb.text())
		self.GZucc_Conv_Mar = int(self.lEditGZuccConvMar.text())
		self.GZucc_Conv_Apr = int(self.lEditGZuccConvApr.text())
		self.GZucc_Conv_May = int(self.lEditGZuccConvMay.text())
		self.GZucc_Conv_Jun = int(self.lEditGZuccConvJun.text())
		self.GZucc_Conv_Jul = int(self.lEditGZuccConvJul.text())
		self.GZucc_Conv_Aug = int(self.lEditGZuccConvAug.text())
		self.GZucc_Conv_Sep = int(self.lEditGZuccConvSep.text())
		self.GZucc_Conv_Oct = int(self.lEditGZuccConvOct.text())
		self.GZucc_Conv_Nov = int(self.lEditGZuccConvNov.text())
		self.GZucc_Conv_Dec = int(self.lEditGZuccConvDec.text())
		
		self.broc_Org_Jan = int(self.lEditBroccOrgJan.text())
		self.broc_Org_Feb = int(self.lEditBroccOrgFeb.text())
		self.broc_Org_Mar = int(self.lEditBroccOrgMar.text())
		self.broc_Org_Apr = int(self.lEditBroccOrgApr.text())
		self.broc_Org_May = int(self.lEditBroccOrgMay.text())
		self.broc_Org_Jun = int(self.lEditBroccOrgJun.text())
		self.broc_Org_Jul = int(self.lEditBroccOrgJul.text())
		self.broc_Org_Aug = int(self.lEditBroccOrgAug.text())
		self.broc_Org_Sep = int(self.lEditBroccOrgSep.text())
		self.broc_Org_Oct = int(self.lEditBroccOrgOct.text())
		self.broc_Org_Nov = int(self.lEditBroccOrgNov.text())
		self.broc_Org_Dec = int(self.lEditBroccOrgDec.text())
		
		self.Caulif_Org_Jan = int(self.lEditCaulifOrgJan.text())
		self.Caulif_Org_Feb = int(self.lEditCaulifOrgFeb.text())
		self.Caulif_Org_Mar = int(self.lEditCaulifOrgMar.text())
		self.Caulif_Org_Apr = int(self.lEditCaulifOrgApr.text())
		self.Caulif_Org_May = int(self.lEditCaulifOrgMay.text())
		self.Caulif_Org_Jun = int(self.lEditCaulifOrgJun.text())
		self.Caulif_Org_Jul = int(self.lEditCaulifOrgJul.text())
		self.Caulif_Org_Aug = int(self.lEditCaulifOrgAug.text())
		self.Caulif_Org_Sep = int(self.lEditCaulifOrgSep.text())
		self.Caulif_Org_Oct = int(self.lEditCaulifOrgOct.text())
		self.Caulif_Org_Nov = int(self.lEditCaulifOrgNov.text())
		self.Caulif_Org_Dec = int(self.lEditCaulifOrgDec.text())
		
		
		self.Carrots_Org_Jan = int(self.lEditCarrotsOrgJan.text())
		self.Carrots_Org_Feb = int(self.lEditCarrotsOrgFeb.text())
		self.Carrots_Org_Mar = int(self.lEditCarrotsOrgMar.text())
		self.Carrots_Org_Apr = int(self.lEditCarrotsOrgApr.text())
		self.Carrots_Org_May = int(self.lEditCarrotsOrgMay.text())
		self.Carrots_Org_Jun = int(self.lEditCarrotsOrgJun.text())
		self.Carrots_Org_Jul = int(self.lEditCarrotsOrgJul.text())
		self.Carrots_Org_Aug = int(self.lEditCarrotsOrgAug.text())
		self.Carrots_Org_Sep = int(self.lEditCarrotsOrgSep.text())
		self.Carrots_Org_Oct = int(self.lEditCarrotsOrgOct.text())
		self.Carrots_Org_Nov = int(self.lEditCarrotsOrgNov.text())
		self.Carrots_Org_Dec = int(self.lEditCarrotsOrgDec.text())
		
		self.Corn_Org_Jan = int(self.lEditCornOrgJan.text())
		self.Corn_Org_Feb = int(self.lEditCornOrgFeb.text())
		self.Corn_Org_Mar = int(self.lEditCornOrgMar.text())
		self.Corn_Org_Apr = int(self.lEditCornOrgApr.text())
		self.Corn_Org_May = int(self.lEditCornOrgMay.text())
		self.Corn_Org_Jun = int(self.lEditCornOrgJun.text())
		self.Corn_Org_Jul = int(self.lEditCornOrgJul.text())
		self.Corn_Org_Aug = int(self.lEditCornOrgAug.text())
		self.Corn_Org_Sep = int(self.lEditCornOrgSep.text())
		self.Corn_Org_Oct = int(self.lEditCornOrgOct.text())
		self.Corn_Org_Nov = int(self.lEditCornOrgNov.text())
		self.Corn_Org_Dec = int(self.lEditCornOrgDec.text())
		
		self.Edamame_Org_Jan = int(self.lEditEdamameOrgJan.text())
		self.Edamame_Org_Feb = int(self.lEditEdamameOrgFeb.text())
		self.Edamame_Org_Mar = int(self.lEditEdamameOrgMar.text())
		self.Edamame_Org_Apr = int(self.lEditEdamameOrgApr.text())
		self.Edamame_Org_May = int(self.lEditEdamameOrgMay.text())
		self.Edamame_Org_Jun = int(self.lEditEdamameOrgJun.text())
		self.Edamame_Org_Jul = int(self.lEditEdamameOrgJul.text())
		self.Edamame_Org_Aug = int(self.lEditEdamameOrgAug.text())
		self.Edamame_Org_Sep = int(self.lEditEdamameOrgSep.text())
		self.Edamame_Org_Oct = int(self.lEditEdamameOrgOct.text())
		self.Edamame_Org_Nov = int(self.lEditEdamameOrgNov.text())
		self.Edamame_Org_Dec = int(self.lEditEdamameOrgDec.text())
		
	def lock_fields (self):
		self.lEditBrConvJan.setEnabled(False)
		self.lEditBrConvFeb.setEnabled(False)
		self.lEditBrConvMar.setEnabled(False)
		self.lEditBrConvApr.setEnabled(False)
		self.lEditBrConvMay.setEnabled(False)
		self.lEditBrConvJun.setEnabled(False)
		self.lEditBrConvJul.setEnabled(False)
		self.lEditBrConvAug.setEnabled(False)
		self.lEditBrConvSep.setEnabled(False)
		self.lEditBrConvOct.setEnabled(False)
		self.lEditBrConvNov.setEnabled(False)
		self.lEditBrConvDec.setEnabled(False)
		
		self.lEditCaulifConvJan.setEnabled(False)
		self.lEditCaulifConvFeb.setEnabled(False)
		self.lEditCaulifConvMar.setEnabled(False)
		self.lEditCaulifConvApr.setEnabled(False)
		self.lEditCaulifConvMay.setEnabled(False)
		self.lEditCaulifConvJun.setEnabled(False)
		self.lEditCaulifConvJul.setEnabled(False)
		self.lEditCaulifConvAug.setEnabled(False)
		self.lEditCaulifConvSep.setEnabled(False)
		self.lEditCaulifConvOct.setEnabled(False)
		self.lEditCaulifConvNov.setEnabled(False)
		self.lEditCaulifConvDec.setEnabled(False)
		
		self.lEditBSprConvJan.setEnabled(False)
		self.lEditBSprConvFeb.setEnabled(False)
		self.lEditBSprConvMar.setEnabled(False)
		self.lEditBSprConvApr.setEnabled(False)
		self.lEditBSprConvMay.setEnabled(False)
		self.lEditBSprConvJun.setEnabled(False)
		self.lEditBSprConvJul.setEnabled(False)
		self.lEditBSprConvAug.setEnabled(False)
		self.lEditBSprConvSep.setEnabled(False)
		self.lEditBSprConvOct.setEnabled(False)
		self.lEditBSprConvNov.setEnabled(False)
		self.lEditBSprConvDec.setEnabled(False)
		
		self.lEditSspConvJan.setEnabled(False)
		self.lEditSspConvFeb.setEnabled(False)
		self.lEditSspConvMar.setEnabled(False)
		self.lEditSspConvApr.setEnabled(False)
		self.lEditSspConvMay.setEnabled(False)
		self.lEditSspConvJun.setEnabled(False)
		self.lEditSspConvJul.setEnabled(False)
		self.lEditSspConvAug.setEnabled(False)
		self.lEditSspConvSep.setEnabled(False)
		self.lEditSspConvOct.setEnabled(False)
		self.lEditSspConvNov.setEnabled(False)
		self.lEditSspConvDec.setEnabled(False)
		
		self.lEditYSqConvJan.setEnabled(False)
		self.lEditYSqConvFeb.setEnabled(False)
		self.lEditYSqConvMar.setEnabled(False)
		self.lEditYSqConvApr.setEnabled(False)
		self.lEditYSqConvMay.setEnabled(False)
		self.lEditYSqConvJun.setEnabled(False)
		self.lEditYSqConvJul.setEnabled(False)
		self.lEditYSqConvAug.setEnabled(False)
		self.lEditYSqConvSep.setEnabled(False)
		self.lEditYSqConvOct.setEnabled(False)
		self.lEditYSqConvNov.setEnabled(False)
		self.lEditYSqConvDec.setEnabled(False)
		
		self.lEditGZuccConvJan.setEnabled(False)
		self.lEditGZuccConvFeb.setEnabled(False)
		self.lEditGZuccConvMar.setEnabled(False)
		self.lEditGZuccConvApr.setEnabled(False)
		self.lEditGZuccConvMay.setEnabled(False)
		self.lEditGZuccConvJun.setEnabled(False)
		self.lEditGZuccConvJul.setEnabled(False)
		self.lEditGZuccConvAug.setEnabled(False)
		self.lEditGZuccConvSep.setEnabled(False)
		self.lEditGZuccConvOct.setEnabled(False)
		self.lEditGZuccConvNov.setEnabled(False)
		self.lEditGZuccConvDec.setEnabled(False)
		
		self.lEditGZuccConvJan.setEnabled(False)
		self.lEditGZuccConvFeb.setEnabled(False)
		self.lEditGZuccConvMar.setEnabled(False)
		self.lEditGZuccConvApr.setEnabled(False)
		self.lEditGZuccConvMay.setEnabled(False)
		self.lEditGZuccConvJun.setEnabled(False)
		self.lEditGZuccConvJul.setEnabled(False)
		self.lEditGZuccConvAug.setEnabled(False)
		self.lEditGZuccConvSep.setEnabled(False)
		self.lEditGZuccConvOct.setEnabled(False)
		self.lEditGZuccConvNov.setEnabled(False)
		self.lEditGZuccConvDec.setEnabled(False)
		
		self.lEditBroccOrgJan.setEnabled(False)
		self.lEditBroccOrgFeb.setEnabled(False)
		self.lEditBroccOrgMar.setEnabled(False)
		self.lEditBroccOrgApr.setEnabled(False)
		self.lEditBroccOrgMay.setEnabled(False)
		self.lEditBroccOrgJun.setEnabled(False)
		self.lEditBroccOrgJul.setEnabled(False)
		self.lEditBroccOrgAug.setEnabled(False)
		self.lEditBroccOrgSep.setEnabled(False)
		self.lEditBroccOrgOct.setEnabled(False)
		self.lEditBroccOrgNov.setEnabled(False)
		self.lEditBroccOrgDec.setEnabled(False)
		
		self.lEditCaulifOrgJan.setEnabled(False)
		self.lEditCaulifOrgFeb.setEnabled(False)
		self.lEditCaulifOrgMar.setEnabled(False)
		self.lEditCaulifOrgApr.setEnabled(False)
		self.lEditCaulifOrgMay.setEnabled(False)
		self.lEditCaulifOrgJun.setEnabled(False)
		self.lEditCaulifOrgJul.setEnabled(False)
		self.lEditCaulifOrgAug.setEnabled(False)
		self.lEditCaulifOrgSep.setEnabled(False)
		self.lEditCaulifOrgOct.setEnabled(False)
		self.lEditCaulifOrgNov.setEnabled(False)
		self.lEditCaulifOrgDec.setEnabled(False)
		
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
		
		self.lEditCornOrgJan.setEnabled(False)
		self.lEditCornOrgFeb.setEnabled(False)
		self.lEditCornOrgMar.setEnabled(False)
		self.lEditCornOrgApr.setEnabled(False)
		self.lEditCornOrgMay.setEnabled(False)
		self.lEditCornOrgJun.setEnabled(False)
		self.lEditCornOrgJul.setEnabled(False)
		self.lEditCornOrgAug.setEnabled(False)
		self.lEditCornOrgSep.setEnabled(False)
		self.lEditCornOrgOct.setEnabled(False)
		self.lEditCornOrgNov.setEnabled(False)
		self.lEditCornOrgDec.setEnabled(False)
		
		self.lEditEdamameOrgJan.setEnabled(False)
		self.lEditEdamameOrgFeb.setEnabled(False)
		self.lEditEdamameOrgMar.setEnabled(False)
		self.lEditEdamameOrgApr.setEnabled(False)
		self.lEditEdamameOrgMay.setEnabled(False)
		self.lEditEdamameOrgJun.setEnabled(False)
		self.lEditEdamameOrgJul.setEnabled(False)
		self.lEditEdamameOrgAug.setEnabled(False)
		self.lEditEdamameOrgSep.setEnabled(False)
		self.lEditEdamameOrgOct.setEnabled(False)
		self.lEditEdamameOrgNov.setEnabled(False)
		self.lEditEdamameOrgDec.setEnabled(False)
		
	def unlock_fields(self):
		self.lEditBrConvJan.setEnabled(True)
		self.lEditBrConvFeb.setEnabled(True)
		self.lEditBrConvMar.setEnabled(True)
		self.lEditBrConvApr.setEnabled(True)
		self.lEditBrConvMay.setEnabled(True)
		self.lEditBrConvJun.setEnabled(True)
		self.lEditBrConvJul.setEnabled(True)
		self.lEditBrConvAug.setEnabled(True)
		self.lEditBrConvSep.setEnabled(True)
		self.lEditBrConvOct.setEnabled(True)
		self.lEditBrConvNov.setEnabled(True)
		self.lEditBrConvDec.setEnabled(True)
		
		self.lEditCaulifConvJan.setEnabled(True)
		self.lEditCaulifConvFeb.setEnabled(True)
		self.lEditCaulifConvMar.setEnabled(True)
		self.lEditCaulifConvApr.setEnabled(True)
		self.lEditCaulifConvMay.setEnabled(True)
		self.lEditCaulifConvJun.setEnabled(True)
		self.lEditCaulifConvJul.setEnabled(True)
		self.lEditCaulifConvAug.setEnabled(True)
		self.lEditCaulifConvSep.setEnabled(True)
		self.lEditCaulifConvOct.setEnabled(True)
		self.lEditCaulifConvNov.setEnabled(True)
		self.lEditCaulifConvDec.setEnabled(True)
		
		self.lEditBSprConvJan.setEnabled(True)
		self.lEditBSprConvFeb.setEnabled(True)
		self.lEditBSprConvMar.setEnabled(True)
		self.lEditBSprConvApr.setEnabled(True)
		self.lEditBSprConvMay.setEnabled(True)
		self.lEditBSprConvJun.setEnabled(True)
		self.lEditBSprConvJul.setEnabled(True)
		self.lEditBSprConvAug.setEnabled(True)
		self.lEditBSprConvSep.setEnabled(True)
		self.lEditBSprConvOct.setEnabled(True)
		self.lEditBSprConvNov.setEnabled(True)
		self.lEditBSprConvDec.setEnabled(True)
		
		self.lEditSspConvJan.setEnabled(True)
		self.lEditSspConvFeb.setEnabled(True)
		self.lEditSspConvMar.setEnabled(True)
		self.lEditSspConvApr.setEnabled(True)
		self.lEditSspConvMay.setEnabled(True)
		self.lEditSspConvJun.setEnabled(True)
		self.lEditSspConvJul.setEnabled(True)
		self.lEditSspConvAug.setEnabled(True)
		self.lEditSspConvSep.setEnabled(True)
		self.lEditSspConvOct.setEnabled(True)
		self.lEditSspConvNov.setEnabled(True)
		self.lEditSspConvDec.setEnabled(True)
		
		self.lEditYSqConvJan.setEnabled(True)
		self.lEditYSqConvFeb.setEnabled(True)
		self.lEditYSqConvMar.setEnabled(True)
		self.lEditYSqConvApr.setEnabled(True)
		self.lEditYSqConvMay.setEnabled(True)
		self.lEditYSqConvJun.setEnabled(True)
		self.lEditYSqConvJul.setEnabled(True)
		self.lEditYSqConvAug.setEnabled(True)
		self.lEditYSqConvSep.setEnabled(True)
		self.lEditYSqConvOct.setEnabled(True)
		self.lEditYSqConvNov.setEnabled(True)
		self.lEditYSqConvDec.setEnabled(True)
		
		self.lEditGZuccConvJan.setEnabled(True)
		self.lEditGZuccConvFeb.setEnabled(True)
		self.lEditGZuccConvMar.setEnabled(True)
		self.lEditGZuccConvApr.setEnabled(True)
		self.lEditGZuccConvMay.setEnabled(True)
		self.lEditGZuccConvJun.setEnabled(True)
		self.lEditGZuccConvJul.setEnabled(True)
		self.lEditGZuccConvAug.setEnabled(True)
		self.lEditGZuccConvSep.setEnabled(True)
		self.lEditGZuccConvOct.setEnabled(True)
		self.lEditGZuccConvNov.setEnabled(True)
		self.lEditGZuccConvDec.setEnabled(True)
		
		self.lEditGZuccConvJan.setEnabled(True)
		self.lEditGZuccConvFeb.setEnabled(True)
		self.lEditGZuccConvMar.setEnabled(True)
		self.lEditGZuccConvApr.setEnabled(True)
		self.lEditGZuccConvMay.setEnabled(True)
		self.lEditGZuccConvJun.setEnabled(True)
		self.lEditGZuccConvJul.setEnabled(True)
		self.lEditGZuccConvAug.setEnabled(True)
		self.lEditGZuccConvSep.setEnabled(True)
		self.lEditGZuccConvOct.setEnabled(True)
		self.lEditGZuccConvNov.setEnabled(True)
		self.lEditGZuccConvDec.setEnabled(True)
		
		self.lEditBroccOrgJan.setEnabled(True)
		self.lEditBroccOrgFeb.setEnabled(True)
		self.lEditBroccOrgMar.setEnabled(True)
		self.lEditBroccOrgApr.setEnabled(True)
		self.lEditBroccOrgMay.setEnabled(True)
		self.lEditBroccOrgJun.setEnabled(True)
		self.lEditBroccOrgJul.setEnabled(True)
		self.lEditBroccOrgAug.setEnabled(True)
		self.lEditBroccOrgSep.setEnabled(True)
		self.lEditBroccOrgOct.setEnabled(True)
		self.lEditBroccOrgNov.setEnabled(True)
		self.lEditBroccOrgDec.setEnabled(True)
		
		self.lEditCaulifOrgJan.setEnabled(True)
		self.lEditCaulifOrgFeb.setEnabled(True)
		self.lEditCaulifOrgMar.setEnabled(True)
		self.lEditCaulifOrgApr.setEnabled(True)
		self.lEditCaulifOrgMay.setEnabled(True)
		self.lEditCaulifOrgJun.setEnabled(True)
		self.lEditCaulifOrgJul.setEnabled(True)
		self.lEditCaulifOrgAug.setEnabled(True)
		self.lEditCaulifOrgSep.setEnabled(True)
		self.lEditCaulifOrgOct.setEnabled(True)
		self.lEditCaulifOrgNov.setEnabled(True)
		self.lEditCaulifOrgDec.setEnabled(True)
		
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
		
		self.lEditCornOrgJan.setEnabled(True)
		self.lEditCornOrgFeb.setEnabled(True)
		self.lEditCornOrgMar.setEnabled(True)
		self.lEditCornOrgApr.setEnabled(True)
		self.lEditCornOrgMay.setEnabled(True)
		self.lEditCornOrgJun.setEnabled(True)
		self.lEditCornOrgJul.setEnabled(True)
		self.lEditCornOrgAug.setEnabled(True)
		self.lEditCornOrgSep.setEnabled(True)
		self.lEditCornOrgOct.setEnabled(True)
		self.lEditCornOrgNov.setEnabled(True)
		self.lEditCornOrgDec.setEnabled(True)
		
		self.lEditEdamameOrgJan.setEnabled(True)
		self.lEditEdamameOrgFeb.setEnabled(True)
		self.lEditEdamameOrgMar.setEnabled(True)
		self.lEditEdamameOrgApr.setEnabled(True)
		self.lEditEdamameOrgMay.setEnabled(True)
		self.lEditEdamameOrgJun.setEnabled(True)
		self.lEditEdamameOrgJul.setEnabled(True)
		self.lEditEdamameOrgAug.setEnabled(True)
		self.lEditEdamameOrgSep.setEnabled(True)
		self.lEditEdamameOrgOct.setEnabled(True)
		self.lEditEdamameOrgNov.setEnabled(True)
		self.lEditEdamameOrgDec.setEnabled(True)
		self.pBtnUpdate.setEnabled(True)
	
	def suma(self, *args ):
		result = 0
		for valor in args:
			result = result + valor
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
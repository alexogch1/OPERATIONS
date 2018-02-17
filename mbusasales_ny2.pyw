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
form_class = uic.loadUiType("mbusasales2_ny.ui")[0]

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
		Sum of all products per month
		"""
		Tot_Jan_Others = self.other_Month(
			self.total_Sales_Jan,
			self.broc_Jan, self.Caulif_Jan, self.BrSpr_Jan, 
			self.Ssp_Jan, self.YSq_Jan, self.GZucc_Jan)
		self.lblOtherJan.setText(str(round(Tot_Jan_Others,0)))

		Tot_Feb_Others = self.other_Month(
			self.total_Sales_Feb,
			self.broc_Feb, self.Caulif_Feb, self.BrSpr_Feb,
			self.Ssp_Feb, self.YSq_Feb, self.GZucc_Feb)
		self.lblOtherFeb.setText(str(Tot_Feb_Others))

		Tot_Mar_Others = self.other_Month(
			self.total_Sales_Mar,
			self.broc_Mar, self.Caulif_Mar, self.BrSpr_Mar, 
			self.Ssp_Mar, self.YSq_Mar, self.GZucc_Mar)
		self.lblOtherMar.setText(str(Tot_Mar_Others))

		Tot_Apr_Others = self.other_Month(
			self.total_Sales_Apr,
			self.broc_Apr, self.Caulif_Apr, self.BrSpr_Apr, 
			self.Ssp_Apr, self.YSq_Apr, self.GZucc_Apr)
		self.lblOtherApr.setText(str(Tot_Apr_Others))

		Tot_May_Others = self.other_Month(
			self.total_Sales_May,
			self.broc_May, self.Caulif_May, self.BrSpr_May, 
			self.Ssp_May, self.YSq_May, self.GZucc_May)
		self.lblOtherMay.setText(str(Tot_May_Others))

		Tot_Jun_Others = self.other_Month(
			self.total_Sales_Jun,
			self.broc_Jun, self.Caulif_Jun, self.BrSpr_Jun, 
			self.Ssp_Jun, self.YSq_Jun, self.GZucc_Jun)
		self.lblOtherJun.setText(str(Tot_Jun_Others))

		Tot_Jul_Others = self.other_Month(
			self.total_Sales_Jul,
			self.broc_Jul, self.Caulif_Jul, self.BrSpr_Jul, 
			self.Ssp_Jul, self.YSq_Jul, self.GZucc_Jul)
		self.lblOtherJul.setText(str(Tot_Jul_Others))

		Tot_Aug_Others= self.other_Month(
			self.total_Sales_Aug,
			self.broc_Aug, self.Caulif_Aug, self.BrSpr_Aug, 
			self.Ssp_Aug, self.YSq_Aug, self.GZucc_Aug)
		self.lblOtherAug.setText(str(Tot_Aug_Others))

		Tot_Sep_Others = self.other_Month(
			self.total_Sales_Sep,
			self.broc_Sep, self.Caulif_Sep, self.BrSpr_Sep, 
			self.Ssp_Sep, self.YSq_Sep, self.GZucc_Sep)
		self.lblOtherSep.setText(str(Tot_Sep_Others))

		Tot_Oct_Others = self.other_Month(
			self.total_Sales_Oct,
			self.broc_Oct, self.Caulif_Oct, self.BrSpr_Oct, 
			self.Ssp_Oct, self.YSq_Oct, self.GZucc_Oct)
		self.lblOtherOct.setText(str(Tot_Oct_Others))

		Tot_Nov_Others = self.other_Month(
			self.total_Sales_Nov,
			self.broc_Nov, self.Caulif_Nov, self.BrSpr_Nov, 
			self.Ssp_Nov, self.YSq_Nov, self.GZucc_Nov)
		self.lblOtherNov.setText(str(Tot_Nov_Others))

		Tot_Dec_Others = self.other_Month(
			self.total_Sales_Dec,
			self.broc_Dec, self.Caulif_Dec, self.BrSpr_Dec, 
			self.Ssp_Dec, self.YSq_Dec, self.GZucc_Dec)
		self.lblOtherDec.setText(str(Tot_Dec_Others))

		Tot_Anual_Others = self.sum_others(Tot_Jan_Others, Tot_Feb_Others, 
			Tot_Mar_Others, Tot_Apr_Others, Tot_May_Others,
			Tot_Jun_Others, Tot_Jul_Others, Tot_Aug_Others,
			Tot_Sep_Others, Tot_Oct_Others, Tot_Nov_Others,
			Tot_Dec_Others)
		self.lblTotAnualOther.setText(str(Tot_Anual_Others))
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
			   
		#Sum of  Total Sales
		Total_Sales_Anual = self.suma_Total_sales_Anual(
			self.total_Sales_Jan, self.total_Sales_Feb, self.total_Sales_Mar, 
			self.total_Sales_Apr, self.total_Sales_May, self.total_Sales_Jun,
			self.total_Sales_Jul, self.total_Sales_Aug, self.total_Sales_Sep, 
			self.total_Sales_Oct, self.total_Sales_Nov, self.total_Sales_Dec)

		#Sum of  Broccoli
		broc_Total_Anual = self.suma_Broc_Tot(
			self.broc_Jan, self.broc_Feb, self.broc_Mar, 
			self.broc_Apr, self.broc_May, self.broc_Jun,
			self.broc_Jul, self.broc_Aug, self.broc_Sep, 
			self.broc_Oct, self.broc_Nov, self.broc_Dec)
		
		#Sum of  Cauliflower
		caulif_Total_Anual = self.suma_Caulif_Tot(
			self.Caulif_Jan, self.Caulif_Feb, self.Caulif_Mar, 
			self.Caulif_Apr, self.Caulif_May, self.Caulif_Jun, 
			self.Caulif_Jul, self.Caulif_Aug, self.Caulif_Sep, 
			self.Caulif_Oct, self.Caulif_Nov, self.Caulif_Dec)
		
		brSpr_Total_Anual = self.suma_BrSpr_Tot(
			self.BrSpr_Jan, self.BrSpr_Feb, self.BrSpr_Mar, 
			self.BrSpr_Apr, self.BrSpr_May, self.BrSpr_Jun, 
			self.BrSpr_Jul, self.BrSpr_Aug, self.BrSpr_Sep, 
			self.BrSpr_Oct, self.BrSpr_Nov, self.BrSpr_Dec)
		
		Ssp_Total_Anual = self.suma_Ssp_Tot(
			self.Ssp_Jan, self.Ssp_Feb, self.Ssp_Mar, 
			self.Ssp_Apr, self.Ssp_May, self.Ssp_Jun, 
			self.Ssp_Jul, self.Ssp_Aug, self.Ssp_Sep, 
			self.Ssp_Oct, self.Ssp_Nov, self.Ssp_Dec)
		
		YSq_Total_Anual = self.suma_YSq_Tot(
			self.YSq_Jan, self.YSq_Feb, self.YSq_Mar, 
			self.YSq_Apr, self.YSq_May, self.YSq_Jun, 
			self.YSq_Jul, self.YSq_Aug, self.YSq_Sep, 
			self.YSq_Oct, self.YSq_Nov, self.YSq_Dec)
		
		GZucc_Total_Anual = self.suma_GZucc_Tot(
			self.GZucc_Jan, self.GZucc_Feb, self.GZucc_Mar, 
			self.GZucc_Apr, self.GZucc_May, self.GZucc_Jun, 
			self.GZucc_Jul, self.GZucc_Aug, self.GZucc_Sep, 
			self.GZucc_Oct, self.GZucc_Nov, self.GZucc_Dec)
		
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

		self.Total_Jan_Conv = self.resta(self.total_Sales_Jan, Tot_Org_Jan )
		self.lblTotalJanConv.setText(str(self.Total_Jan_Conv))
		
		self.Total_Feb_Conv = self.resta(self.total_Sales_Feb, Tot_Org_Feb )
		self.lblTotalFebConv.setText(str(self.Total_Feb_Conv))
		
		self.Total_Mar_Conv = self.resta(self.total_Sales_Mar, Tot_Org_Mar )
		self.lblTotalMarConv.setText(str(self.Total_Mar_Conv))
		
		self.Total_Apr_Conv = self.resta(self.total_Sales_Apr, Tot_Org_Apr )
		self.lblTotalAprConv.setText(str(self.Total_Apr_Conv))
		
		self.Total_May_Conv = self.resta(self.total_Sales_May, Tot_Org_May )
		self.lblTotalMayConv.setText(str(self.Total_May_Conv))
		
		self.Total_Jun_Conv = self.resta(self.total_Sales_Jun, Tot_Org_Jun )
		self.lblTotalJunConv.setText(str(self.Total_Jun_Conv))
		
		self.Total_Jul_Conv = self.resta(self.total_Sales_Jul, Tot_Org_Jul )
		self.lblTotalJulConv.setText(str(self.Total_Jul_Conv))
		
		self.Total_Aug_Conv = self.resta(self.total_Sales_Aug, Tot_Org_Aug )
		self.lblTotalAugConv.setText(str(self.Total_Aug_Conv))
		
		self.Total_Sep_Conv = self.resta(self.total_Sales_Sep, Tot_Org_Sep )
		self.lblTotalSepConv.setText(str(self.Total_Sep_Conv))
		
		self.Total_Oct_Conv = self.resta(self.total_Sales_Oct, Tot_Org_Oct )
		self.lblTotalOctConv.setText(str(self.Total_Oct_Conv))
		
		self.Total_Nov_Conv = self.resta(self.total_Sales_Nov, Tot_Org_Nov )
		self.lblTotalNovConv.setText(str(self.Total_Nov_Conv))
		
		self.Total_Dec_Conv = self.resta(self.total_Sales_Dec, Tot_Org_Dec )
		self.lblTotalDecConv.setText(str(self.Total_Dec_Conv))

		self.total_Anual = self.suma(
			self.total_Sales_Jan, self.total_Sales_Feb, self.total_Sales_Mar, 
			self.total_Sales_Apr, self.total_Sales_May, self.total_Sales_Jun,
			 self.total_Sales_Jul, self.total_Sales_Aug, self.total_Sales_Sep, 
			 self.total_Sales_Oct, self.total_Sales_Nov, self.total_Sales_Dec)
		
		
		Total_Anual_Conv = self.suma(
			self.Total_Jan_Conv, self.Total_Feb_Conv, self.Total_Mar_Conv, self.Total_Apr_Conv, 
			self.Total_May_Conv, self.Total_Jun_Conv, self.Total_Jul_Conv, self.Total_Aug_Conv, 
			self.Total_Sep_Conv, self.Total_Oct_Conv, self.Total_Nov_Conv, self.Total_Dec_Conv)
		self.lblTotalAnualConv.setText(str(Total_Anual_Conv))
		
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
		self.lEditTotSalesJan.insert(str(0))
		self.lEditTotSalesFeb.insert(str(0))
		self.lEditTotSalesMar.insert(str(0))
		self.lEditTotSalesApr.insert(str(0))
		self.lEditTotSalesMay.insert(str(0))
		self.lEditTotSalesJun.insert(str(0))
		self.lEditTotSalesJul.insert(str(0))
		self.lEditTotSalesAug.insert(str(0))
		self.lEditTotSalesSep.insert(str(0))
		self.lEditTotSalesOct.insert(str(0))
		self.lEditTotSalesNov.insert(str(0))
		self.lEditTotSalesDec.insert(str(0))


		self.lEditBrJan.insert(str(0))
		self.lEditBrFeb.insert(str(0))
		self.lEditBrMar.insert(str(0))
		self.lEditBrApr.insert(str(0))
		self.lEditBrMay.insert(str(0))
		self.lEditBrJun.insert(str(0))
		self.lEditBrJul.insert(str(0))
		self.lEditBrAug.insert(str(0))
		self.lEditBrSep.insert(str(0))
		self.lEditBrOct.insert(str(0))
		self.lEditBrNov.insert(str(0))
		self.lEditBrDec.insert(str(0))
		
		self.lEditCaulifJan.insert(str(0))
		self.lEditCaulifFeb.insert(str(0))
		self.lEditCaulifMar.insert(str(0))
		self.lEditCaulifApr.insert(str(0))
		self.lEditCaulifMay.insert(str(0))
		self.lEditCaulifJun.insert(str(0))
		self.lEditCaulifJul.insert(str(0))
		self.lEditCaulifAug.insert(str(0))
		self.lEditCaulifSep.insert(str(0))
		self.lEditCaulifOct.insert(str(0))
		self.lEditCaulifNov.insert(str(0))
		self.lEditCaulifDec.insert(str(0))

		self.lEditSspJan.insert(str(0))
		self.lEditSspFeb.insert(str(0))
		self.lEditSspMar.insert(str(0))
		self.lEditSspApr.insert(str(0))
		self.lEditSspMay.insert(str(0))
		self.lEditSspJun.insert(str(0))
		self.lEditSspJul.insert(str(0))
		self.lEditSspAug.insert(str(0))
		self.lEditSspSep.insert(str(0))
		self.lEditSspOct.insert(str(0))
		self.lEditSspNov.insert(str(0))
		self.lEditSspDec.insert(str(0))   
		
		self.lEditBSprJan.insert(str(0))
		self.lEditBSprFeb.insert(str(0))
		self.lEditBSprMar.insert(str(0))
		self.lEditBSprApr.insert(str(0))
		self.lEditBSprMay.insert(str(0))
		self.lEditBSprJun.insert(str(0))
		self.lEditBSprJul.insert(str(0))
		self.lEditBSprAug.insert(str(0))
		self.lEditBSprSep.insert(str(0))
		self.lEditBSprOct.insert(str(0))
		self.lEditBSprNov.insert(str(0))
		self.lEditBSprDec.insert(str(0))
		
		self.lEditYSqJan.insert(str(0))
		self.lEditYSqFeb.insert(str(0))
		self.lEditYSqMar.insert(str(0))
		self.lEditYSqApr.insert(str(0))
		self.lEditYSqMay.insert(str(0))
		self.lEditYSqJun.insert(str(0))
		self.lEditYSqJul.insert(str(0))
		self.lEditYSqAug.insert(str(0))
		self.lEditYSqSep.insert(str(0))
		self.lEditYSqOct.insert(str(0))
		self.lEditYSqNov.insert(str(0))
		self.lEditYSqDec.insert(str(0))
		
		self.lEditGZuccJan.insert(str(0))
		self.lEditGZuccFeb.insert(str(0))
		self.lEditGZuccMar.insert(str(0))
		self.lEditGZuccApr.insert(str(0))
		self.lEditGZuccMay.insert(str(0))
		self.lEditGZuccJun.insert(str(0))
		self.lEditGZuccJul.insert(str(0))
		self.lEditGZuccAug.insert(str(0))
		self.lEditGZuccSep.insert(str(0))
		self.lEditGZuccOct.insert(str(0))
		self.lEditGZuccNov.insert(str(0))
		self.lEditGZuccDec.insert(str(0))
		
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
				totsales = self.total_Sales_Jan
				broc = self.broc_Jan
				cauliflower = self.Caulif_Jan
				BrSp = self.BrSpr_Jan
				Ssp = self.Ssp_Jan
				YSq = self.YSq_Jan
				GZucc = self.GZucc_Jan
				brocc_Org = self.broc_Org_Jan
				Caulif_Org = self.Caulif_Org_Jan
				Carrots_Org = self.Carrots_Org_Jan
				Corn_Org = self.Corn_Org_Jan
				Edamame_Org = self.Edamame_Org_Jan
				
			elif values.find('feb')>0: 
				indice = values
				month = 'February'
				totsales = self.total_Sales_Feb
				broc = self.broc_Feb
				cauliflower = self.Caulif_Feb
				BrSp = self.BrSpr_Feb
				Ssp = self.Ssp_Feb
				YSq = self.YSq_Feb
				GZucc = self.GZucc_Feb
				brocc_Org = self.broc_Org_Feb
				Caulif_Org = self.Caulif_Org_Feb
				Carrots_Org = self.Carrots_Org_Feb
				Corn_Org = self.Corn_Org_Feb
				Edamame_Org = self.Edamame_Org_Feb
				
			elif values.find('mar')>0: 
				indice = values
				month = 'March'
				totsales = self.total_Sales_Mar
				broc = self.broc_Mar
				cauliflower = self.Caulif_Mar
				BrSp = self.BrSpr_Mar
				Ssp = self.Ssp_Mar
				YSq = self.YSq_Mar
				GZucc = self.GZucc_Mar
				brocc_Org = self.broc_Org_Mar
				Caulif_Org = self.Caulif_Org_Mar
				Carrots_Org = self.Carrots_Org_Mar
				Corn_Org = self.Corn_Org_Mar
				Edamame_Org = self.Edamame_Org_Mar
				
			elif values.find('apr')>0: 
				indice = values
				month = 'April'
				totsales = self.total_Sales_Apr
				broc = self.broc_Apr
				cauliflower = self.Caulif_Apr
				BrSp = self.BrSpr_Apr
				Ssp = self.Ssp_Apr
				YSq = self.YSq_Apr
				GZucc = self.GZucc_Apr
				brocc_Org = self.broc_Org_Apr
				Caulif_Org = self.Caulif_Org_Apr
				Carrots_Org = self.Carrots_Org_Apr
				Corn_Org = self.Corn_Org_Apr
				Edamame_Org = self.Edamame_Org_Apr
				
			elif values.find('may')>0: 
				indice = values
				month = 'May'
				totsales = self.total_Sales_May
				broc = self.broc_May
				cauliflower = self.Caulif_May
				BrSp = self.BrSpr_May
				Ssp = self.Ssp_May
				YSq = self.YSq_May
				GZucc = self.GZucc_May
				brocc_Org = self.broc_Org_May
				Caulif_Org = self.Caulif_Org_May
				Carrots_Org = self.Carrots_Org_May
				Corn_Org = self.Corn_Org_May
				Edamame_Org = self.Edamame_Org_May
				
			elif values.find('jun')>0: 
				indice = values
				month = 'June'
				totsales = self.total_Sales_Jun
				broc = self.broc_Jun
				cauliflower = self.Caulif_Jun
				BrSp = self.BrSpr_Jun
				Ssp = self.Ssp_Jun
				YSq = self.YSq_Jun
				GZucc = self.GZucc_Jun
				brocc_Org = self.broc_Org_Jun
				Caulif_Org = self.Caulif_Org_Jun
				Carrots_Org = self.Carrots_Org_Jun
				Corn_Org = self.Corn_Org_Jun
				Edamame_Org = self.Edamame_Org_Jun
				
			elif values.find('jul')>0: 
				indice = values
				month = 'July'
				totsales = self.total_Sales_Jul
				broc = self.broc_Jul
				cauliflower = self.Caulif_Jul
				BrSp = self.BrSpr_Jul
				Ssp = self.Ssp_Jul
				YSq = self.YSq_Jul
				GZucc = self.GZucc_Jul
				brocc_Org = self.broc_Org_Jul
				Caulif_Org = self.Caulif_Org_Jul
				Carrots_Org = self.Carrots_Org_Jul
				Corn_Org = self.Corn_Org_Jul
				Edamame_Org = self.Edamame_Org_Jul
				
			elif values.find('aug')>0: 
				indice = values
				month = 'August'
				totsales = self.total_Sales_Aug
				broc = self.broc_Aug
				cauliflower = self.Caulif_Aug
				BrSp = self.BrSpr_Aug
				Ssp = self.Ssp_Aug
				YSq = self.YSq_Aug
				GZucc = self.GZucc_Aug
				brocc_Org = self.broc_Org_Aug
				Caulif_Org = self.Caulif_Org_Aug
				Carrots_Org = self.Carrots_Org_Aug
				Corn_Org = self.Corn_Org_Aug
				Edamame_Org = self.Edamame_Org_Aug
				
			elif values.find('sep')>0: 
				indice = values
				month = 'September'
				totsales = self.total_Sales_Sep
				broc = self.broc_Sep
				cauliflower = self.Caulif_Sep
				BrSp = self.BrSpr_Sep
				Ssp = self.Ssp_Sep
				YSq = self.YSq_Sep
				GZucc = self.GZucc_Sep
				brocc_Org = self.broc_Org_Sep
				Caulif_Org = self.Caulif_Org_Sep
				Carrots_Org = self.Carrots_Org_Sep
				Corn_Org = self.Corn_Org_Sep
				Edamame_Org = self.Edamame_Org_Sep
				
			elif values.find('oct')>0: 
				indice = values
				month = 'October'
				totsales = self.total_Sales_Oct
				broc = self.broc_Oct
				cauliflower = self.Caulif_Oct
				BrSp = self.BrSpr_Oct
				Ssp = self.Ssp_Oct
				YSq = self.YSq_Oct
				GZucc = self.GZucc_Oct
				brocc_Org = self.broc_Org_Oct
				Caulif_Org = self.Caulif_Org_Oct
				Carrots_Org = self.Carrots_Org_Oct
				Corn_Org = self.Corn_Org_Oct
				Edamame_Org = self.Edamame_Org_Oct
				
			elif values.find('nov')>0: 
				indice = values
				month = 'November'
				totsales = self.total_Sales_Nov
				broc = self.broc_Nov
				cauliflower = self.Caulif_Nov
				BrSp = self.BrSpr_Nov
				Ssp = self.Ssp_Nov
				YSq = self.YSq_Nov
				GZucc = self.GZucc_Nov
				brocc_Org = self.broc_Org_Nov
				Caulif_Org = self.Caulif_Org_Nov
				Carrots_Org = self.Carrots_Org_Nov
				Corn_Org = self.Corn_Org_Nov
				Edamame_Org = self.Edamame_Org_Nov
				
			elif values.find('dec')>0: 
				indice = values
				month = 'December'
				totsales = self.total_Sales_Dec
				broc = self.broc_Dec
				cauliflower = self.Caulif_Dec
				BrSp = self.BrSpr_Dec
				Ssp = self.Ssp_Dec
				YSq = self.YSq_Dec
				GZucc = self.GZucc_Dec
				brocc_Org = self.broc_Org_Dec
				Caulif_Org = self.Caulif_Org_Dec
				Carrots_Org = self.Carrots_Org_Dec
				Corn_Org = self.Corn_Org_Dec
				Edamame_Org = self.Edamame_Org_Dec
				
			data = {values : [sequence , indice, year, month, totsales, broc, 
				cauliflower, BrSp, Ssp, YSq, GZucc, 
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
				valor[12], valor[13], valor[14], valor [15]]
		try: 
			datos_Sales_Mbusa.to_csv('mbusasales.csv',  encoding = 'utf-8',) 
			self.caja_mensaje('Data Saved;', 'Data saved Succesfully!!!',1)
		except Exception as ex:
			ex = 'The file wou want to save is already open: ' + str(ex)
			self.caja_mensaje('Error when saving data ', ex,0)
	
	def other_Month(self, total, brocc, Caulif, BrSp, Ssp, QSq, GZucc):
		self.other_month = total - (brocc+ Caulif+ BrSp+ Ssp+ QSq+ GZucc)
		return self.other_month     

	def sum_others(self, Tot_Jan_Others, Tot_Feb_Others, 
			Tot_Mar_Others, Tot_Apr_Others, Tot_May_Others,
			Tot_Jun_Others, Tot_Jul_Others, Tot_Aug_Others,
			Tot_Sep_Others, Tot_Oct_Others, Tot_Nov_Others,
			Tot_Dec_Others):
		self.sum_other = self.suma(Tot_Jan_Others, Tot_Feb_Others,
			Tot_Mar_Others, Tot_Apr_Others, Tot_May_Others,
			Tot_Jun_Others, Tot_Jul_Others, Tot_Aug_Others,
			Tot_Sep_Others, Tot_Oct_Others, Tot_Nov_Others,
			Tot_Dec_Others)
		return self.sum_other

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
	
	def suma_Total_sales_Anual(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Total_Sales_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualTotSales.setText(str(self.Total_Sales_Anual))
		return self.Total_Sales_Anual
	
	def suma_Broc_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.broc_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBroc.setText(str(self.broc_Total_Anual))
		return self.broc_Total_Anual
		
	def suma_Brocc_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.broc_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBrocOrg.setText(str(self.broc_Org_Total_Anual))
		return self.broc_Org_Total_Anual
	
	def suma_Caulif_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.caulif_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualCaulif.setText(str(self.caulif_Total_Anual))
		return self.broc_Total_Anual
		
	def suma_Cauliflower_Org(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.caulif_Org_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualCaulOrg.setText(str(self.caulif_Org_Total_Anual))
		return self.broc_Org_Total_Anual    
	
	def suma_BrSpr_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.BrSpr_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualBSpr.setText(str(self.BrSpr_Total_Anual))
		return self.BrSpr_Total_Anual

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

	def suma_Ssp_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.Ssp_Total_Anual = self.suma(
		jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualSsp.setText(str(self.Ssp_Total_Anual))
		return self.Ssp_Total_Anual
		
	def suma_YSq_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.YSq_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualYSq.setText(str(self.YSq_Total_Anual))
		return self.YSq_Total_Anual
	
	def suma_GZucc_Tot(self, jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec):
		self.GZucc_Total_Anual = self.suma(
			jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec)
		self.lblTotalAnualGZucc.setText(str(self.GZucc_Total_Anual))
		return self.GZucc_Total_Anual
	
	def read_data_from_fields(self):

		self.total_Sales_Jan = float(self.lEditTotSalesJan.text())
		self.total_Sales_Feb = float(self.lEditTotSalesFeb.text())
		self.total_Sales_Mar = float(self.lEditTotSalesMar.text())
		self.total_Sales_Apr = float(self.lEditTotSalesApr.text())
		self.total_Sales_May = float(self.lEditTotSalesMay.text())
		self.total_Sales_Jun = float(self.lEditTotSalesJun.text())
		self.total_Sales_Jul = float(self.lEditTotSalesJul.text())
		self.total_Sales_Aug = float(self.lEditTotSalesAug.text())
		self.total_Sales_Sep = float(self.lEditTotSalesSep.text())
		self.total_Sales_Oct = float(self.lEditTotSalesOct.text())
		self.total_Sales_Nov = float(self.lEditTotSalesNov.text())
		self.total_Sales_Dec = float(self.lEditTotSalesDec.text())


		self.broc_Jan = float(self.lEditBrJan.text())
		self.broc_Feb = float(self.lEditBrFeb.text())
		self.broc_Mar = float(self.lEditBrMar.text())
		self.broc_Apr = float(self.lEditBrApr.text())
		self.broc_May = float(self.lEditBrMay.text())
		self.broc_Jun = float(self.lEditBrJun.text())
		self.broc_Jul = float(self.lEditBrJul.text())
		self.broc_Aug = float(self.lEditBrAug.text())
		self.broc_Sep = float(self.lEditBrSep.text())
		self.broc_Oct = float(self.lEditBrOct.text())
		self.broc_Nov = float(self.lEditBrNov.text())
		self.broc_Dec = float(self.lEditBrDec.text())
		
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
		
		self.BrSpr_Jan = float(self.lEditBSprJan.text())
		self.BrSpr_Feb = float(self.lEditBSprFeb.text())
		self.BrSpr_Mar = float(self.lEditBSprMar.text())
		self.BrSpr_Apr = float(self.lEditBSprApr.text())
		self.BrSpr_May = float(self.lEditBSprMay.text())
		self.BrSpr_Jun = float(self.lEditBSprJun.text())
		self.BrSpr_Jul = float(self.lEditBSprJul.text())
		self.BrSpr_Aug = float(self.lEditBSprAug.text())
		self.BrSpr_Sep = float(self.lEditBSprSep.text())
		self.BrSpr_Oct = float(self.lEditBSprOct.text())
		self.BrSpr_Nov = float(self.lEditBSprNov.text())
		self.BrSpr_Dec = float(self.lEditBSprDec.text())
		
		self.Ssp_Jan = float(self.lEditSspJan.text())
		self.Ssp_Feb = float(self.lEditSspFeb.text())
		self.Ssp_Mar = float(self.lEditSspMar.text())
		self.Ssp_Apr = float(self.lEditSspApr.text())
		self.Ssp_May = float(self.lEditSspMay.text())
		self.Ssp_Jun = float(self.lEditSspJun.text())
		self.Ssp_Jul = float(self.lEditSspJul.text())
		self.Ssp_Aug = float(self.lEditSspAug.text())
		self.Ssp_Sep = float(self.lEditSspSep.text())
		self.Ssp_Oct = float(self.lEditSspOct.text())
		self.Ssp_Nov = float(self.lEditSspNov.text())
		self.Ssp_Dec = float(self.lEditSspDec.text())
		
		self.YSq_Jan = float(self.lEditYSqJan.text())
		self.YSq_Feb = float(self.lEditYSqFeb.text())
		self.YSq_Mar = float(self.lEditYSqMar.text())
		self.YSq_Apr = float(self.lEditYSqApr.text())
		self.YSq_May = float(self.lEditYSqMay.text())
		self.YSq_Jun = float(self.lEditYSqJun.text())
		self.YSq_Jul = float(self.lEditYSqJul.text())
		self.YSq_Aug = float(self.lEditYSqAug.text())
		self.YSq_Sep = float(self.lEditYSqSep.text())
		self.YSq_Oct = float(self.lEditYSqOct.text())
		self.YSq_Nov = float(self.lEditYSqNov.text())
		self.YSq_Dec = float(self.lEditYSqDec.text())
		
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
		
		self.broc_Org_Jan = float(self.lEditBroccOrgJan.text())
		self.broc_Org_Feb = float(self.lEditBroccOrgFeb.text())
		self.broc_Org_Mar = float(self.lEditBroccOrgMar.text())
		self.broc_Org_Apr = float(self.lEditBroccOrgApr.text())
		self.broc_Org_May = float(self.lEditBroccOrgMay.text())
		self.broc_Org_Jun = float(self.lEditBroccOrgJun.text())
		self.broc_Org_Jul = float(self.lEditBroccOrgJul.text())
		self.broc_Org_Aug = float(self.lEditBroccOrgAug.text())
		self.broc_Org_Sep = float(self.lEditBroccOrgSep.text())
		self.broc_Org_Oct = float(self.lEditBroccOrgOct.text())
		self.broc_Org_Nov = float(self.lEditBroccOrgNov.text())
		self.broc_Org_Dec = float(self.lEditBroccOrgDec.text())
		
		self.Caulif_Org_Jan = float(self.lEditCaulifOrgJan.text())
		self.Caulif_Org_Feb = float(self.lEditCaulifOrgFeb.text())
		self.Caulif_Org_Mar = float(self.lEditCaulifOrgMar.text())
		self.Caulif_Org_Apr = float(self.lEditCaulifOrgApr.text())
		self.Caulif_Org_May = float(self.lEditCaulifOrgMay.text())
		self.Caulif_Org_Jun = float(self.lEditCaulifOrgJun.text())
		self.Caulif_Org_Jul = float(self.lEditCaulifOrgJul.text())
		self.Caulif_Org_Aug = float(self.lEditCaulifOrgAug.text())
		self.Caulif_Org_Sep = float(self.lEditCaulifOrgSep.text())
		self.Caulif_Org_Oct = float(self.lEditCaulifOrgOct.text())
		self.Caulif_Org_Nov = float(self.lEditCaulifOrgNov.text())
		self.Caulif_Org_Dec = float(self.lEditCaulifOrgDec.text())
		
		
		self.Carrots_Org_Jan = float(self.lEditCarrotsOrgJan.text())
		self.Carrots_Org_Feb = float(self.lEditCarrotsOrgFeb.text())
		self.Carrots_Org_Mar = float(self.lEditCarrotsOrgMar.text())
		self.Carrots_Org_Apr = float(self.lEditCarrotsOrgApr.text())
		self.Carrots_Org_May = float(self.lEditCarrotsOrgMay.text())
		self.Carrots_Org_Jun = float(self.lEditCarrotsOrgJun.text())
		self.Carrots_Org_Jul = float(self.lEditCarrotsOrgJul.text())
		self.Carrots_Org_Aug = float(self.lEditCarrotsOrgAug.text())
		self.Carrots_Org_Sep = float(self.lEditCarrotsOrgSep.text())
		self.Carrots_Org_Oct = float(self.lEditCarrotsOrgOct.text())
		self.Carrots_Org_Nov = float(self.lEditCarrotsOrgNov.text())
		self.Carrots_Org_Dec = float(self.lEditCarrotsOrgDec.text())
		
		self.Corn_Org_Jan = float(self.lEditCornOrgJan.text())
		self.Corn_Org_Feb = float(self.lEditCornOrgFeb.text())
		self.Corn_Org_Mar = float(self.lEditCornOrgMar.text())
		self.Corn_Org_Apr = float(self.lEditCornOrgApr.text())
		self.Corn_Org_May = float(self.lEditCornOrgMay.text())
		self.Corn_Org_Jun = float(self.lEditCornOrgJun.text())
		self.Corn_Org_Jul = float(self.lEditCornOrgJul.text())
		self.Corn_Org_Aug = float(self.lEditCornOrgAug.text())
		self.Corn_Org_Sep = float(self.lEditCornOrgSep.text())
		self.Corn_Org_Oct = float(self.lEditCornOrgOct.text())
		self.Corn_Org_Nov = float(self.lEditCornOrgNov.text())
		self.Corn_Org_Dec = float(self.lEditCornOrgDec.text())
		
		self.Edamame_Org_Jan = float(self.lEditEdamameOrgJan.text())
		self.Edamame_Org_Feb = float(self.lEditEdamameOrgFeb.text())
		self.Edamame_Org_Mar = float(self.lEditEdamameOrgMar.text())
		self.Edamame_Org_Apr = float(self.lEditEdamameOrgApr.text())
		self.Edamame_Org_May = float(self.lEditEdamameOrgMay.text())
		self.Edamame_Org_Jun = float(self.lEditEdamameOrgJun.text())
		self.Edamame_Org_Jul = float(self.lEditEdamameOrgJul.text())
		self.Edamame_Org_Aug = float(self.lEditEdamameOrgAug.text())
		self.Edamame_Org_Sep = float(self.lEditEdamameOrgSep.text())
		self.Edamame_Org_Oct = float(self.lEditEdamameOrgOct.text())
		self.Edamame_Org_Nov = float(self.lEditEdamameOrgNov.text())
		self.Edamame_Org_Dec = float(self.lEditEdamameOrgDec.text())
		
	def lock_fields (self):

		self.lEditTotSalesJan.setEnabled(False)
		self.lEditTotSalesFeb.setEnabled(False)
		self.lEditTotSalesMar.setEnabled(False)
		self.lEditTotSalesApr.setEnabled(False)
		self.lEditTotSalesMay.setEnabled(False)
		self.lEditTotSalesJun.setEnabled(False)
		self.lEditTotSalesJul.setEnabled(False)
		self.lEditTotSalesAug.setEnabled(False)
		self.lEditTotSalesSep.setEnabled(False)
		self.lEditTotSalesOct.setEnabled(False)
		self.lEditTotSalesNov.setEnabled(False)
		self.lEditTotSalesDec.setEnabled(False)

		self.lEditBrJan.setEnabled(False)
		self.lEditBrFeb.setEnabled(False)
		self.lEditBrMar.setEnabled(False)
		self.lEditBrApr.setEnabled(False)
		self.lEditBrMay.setEnabled(False)
		self.lEditBrJun.setEnabled(False)
		self.lEditBrJul.setEnabled(False)
		self.lEditBrAug.setEnabled(False)
		self.lEditBrSep.setEnabled(False)
		self.lEditBrOct.setEnabled(False)
		self.lEditBrNov.setEnabled(False)
		self.lEditBrDec.setEnabled(False)
		
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
		
		self.lEditBSprJan.setEnabled(False)
		self.lEditBSprFeb.setEnabled(False)
		self.lEditBSprMar.setEnabled(False)
		self.lEditBSprApr.setEnabled(False)
		self.lEditBSprMay.setEnabled(False)
		self.lEditBSprJun.setEnabled(False)
		self.lEditBSprJul.setEnabled(False)
		self.lEditBSprAug.setEnabled(False)
		self.lEditBSprSep.setEnabled(False)
		self.lEditBSprOct.setEnabled(False)
		self.lEditBSprNov.setEnabled(False)
		self.lEditBSprDec.setEnabled(False)
		
		self.lEditSspJan.setEnabled(False)
		self.lEditSspFeb.setEnabled(False)
		self.lEditSspMar.setEnabled(False)
		self.lEditSspApr.setEnabled(False)
		self.lEditSspMay.setEnabled(False)
		self.lEditSspJun.setEnabled(False)
		self.lEditSspJul.setEnabled(False)
		self.lEditSspAug.setEnabled(False)
		self.lEditSspSep.setEnabled(False)
		self.lEditSspOct.setEnabled(False)
		self.lEditSspNov.setEnabled(False)
		self.lEditSspDec.setEnabled(False)
		
		self.lEditYSqJan.setEnabled(False)
		self.lEditYSqFeb.setEnabled(False)
		self.lEditYSqMar.setEnabled(False)
		self.lEditYSqApr.setEnabled(False)
		self.lEditYSqMay.setEnabled(False)
		self.lEditYSqJun.setEnabled(False)
		self.lEditYSqJul.setEnabled(False)
		self.lEditYSqAug.setEnabled(False)
		self.lEditYSqSep.setEnabled(False)
		self.lEditYSqOct.setEnabled(False)
		self.lEditYSqNov.setEnabled(False)
		self.lEditYSqDec.setEnabled(False)
		
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
		self.lEditTotSalesJan.setEnabled(True)
		self.lEditTotSalesFeb.setEnabled(True)
		self.lEditTotSalesMar.setEnabled(True)
		self.lEditTotSalesApr.setEnabled(True)
		self.lEditTotSalesMay.setEnabled(True)
		self.lEditTotSalesJun.setEnabled(True)
		self.lEditTotSalesJul.setEnabled(True)
		self.lEditTotSalesAug.setEnabled(True)
		self.lEditTotSalesSep.setEnabled(True)
		self.lEditTotSalesOct.setEnabled(True)
		self.lEditTotSalesNov.setEnabled(True)
		self.lEditTotSalesDec.setEnabled(True)


		self.lEditBrJan.setEnabled(True)
		self.lEditBrFeb.setEnabled(True)
		self.lEditBrMar.setEnabled(True)
		self.lEditBrApr.setEnabled(True)
		self.lEditBrMay.setEnabled(True)
		self.lEditBrJun.setEnabled(True)
		self.lEditBrJul.setEnabled(True)
		self.lEditBrAug.setEnabled(True)
		self.lEditBrSep.setEnabled(True)
		self.lEditBrOct.setEnabled(True)
		self.lEditBrNov.setEnabled(True)
		self.lEditBrDec.setEnabled(True)
		
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
		
		self.lEditBSprJan.setEnabled(True)
		self.lEditBSprFeb.setEnabled(True)
		self.lEditBSprMar.setEnabled(True)
		self.lEditBSprApr.setEnabled(True)
		self.lEditBSprMay.setEnabled(True)
		self.lEditBSprJun.setEnabled(True)
		self.lEditBSprJul.setEnabled(True)
		self.lEditBSprAug.setEnabled(True)
		self.lEditBSprSep.setEnabled(True)
		self.lEditBSprOct.setEnabled(True)
		self.lEditBSprNov.setEnabled(True)
		self.lEditBSprDec.setEnabled(True)
		
		self.lEditSspJan.setEnabled(True)
		self.lEditSspFeb.setEnabled(True)
		self.lEditSspMar.setEnabled(True)
		self.lEditSspApr.setEnabled(True)
		self.lEditSspMay.setEnabled(True)
		self.lEditSspJun.setEnabled(True)
		self.lEditSspJul.setEnabled(True)
		self.lEditSspAug.setEnabled(True)
		self.lEditSspSep.setEnabled(True)
		self.lEditSspOct.setEnabled(True)
		self.lEditSspNov.setEnabled(True)
		self.lEditSspDec.setEnabled(True)
		
		self.lEditYSqJan.setEnabled(True)
		self.lEditYSqFeb.setEnabled(True)
		self.lEditYSqMar.setEnabled(True)
		self.lEditYSqApr.setEnabled(True)
		self.lEditYSqMay.setEnabled(True)
		self.lEditYSqJun.setEnabled(True)
		self.lEditYSqJul.setEnabled(True)
		self.lEditYSqAug.setEnabled(True)
		self.lEditYSqSep.setEnabled(True)
		self.lEditYSqOct.setEnabled(True)
		self.lEditYSqNov.setEnabled(True)
		self.lEditYSqDec.setEnabled(True)
		
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
	
	def label_others (self, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec):
		print('aqui se va a generar las etiquetas de otrhos ingr.')

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
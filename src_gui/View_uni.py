# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import pandas as pd

from src_gui.generateDataframe import DataFrameModel

# Clase de la subventana
class Uni(QMainWindow):

    def __init__(self, parent=None):
        super(Uni,self).__init__(parent)
        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calculos/onefile/Resultados_Uniones_Restriccion.xlsx')

        a = read.parse('Union_VigCol')
        b = read.parse('Union_ColCol_Peralte')
        c = read.parse('Union_ColCol_Patin')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)        
        

class Uni_A(QMainWindow):

    def __init__(self, parent=None):
        super(Uni_A,self).__init__(parent)
        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calculos/files/A_Resultados_Uniones_Restriccion.xlsx')

        a = read.parse('Union_VigCol')
        b = read.parse('Union_ColCol_Peralte')
        c = read.parse('Union_ColCol_Patin')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)  
        

class Uni_B(QMainWindow):

    def __init__(self, parent=None):
        super(Uni_B,self).__init__(parent)
        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calculos/files/B_Resultados_Uniones_Restriccion.xlsx')

        a = read.parse('Union_VigCol')
        b = read.parse('Union_ColCol_Peralte')
        c = read.parse('Union_ColCol_Patin')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)  
        

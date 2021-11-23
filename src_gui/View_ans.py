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
class Ans(QMainWindow):

    def __init__(self, parent=None):
        super(Ans,self).__init__(parent)
        loadUi('Gui/View_ans.ui', self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calculos/onefile/Resultados_Analisis.xlsx')

        a = read.parse('CargasGeneralizadas')
        b = read.parse('MatrizGlobalEstructura')
        c = read.parse('Desplazamientos')
        d = read.parse('Reacciones')
        e = read.parse('FuerzasElementales')


        model = DataFrameModel(a)
        self.tableView_CG.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_MGE.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Des.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_Reac.setModel(model)        
        
        model = DataFrameModel(e)
        self.tableView_FE.setModel(model)        
        



class Ans_A(QMainWindow):

    def __init__(self, parent=None):
        super(Ans_A,self).__init__(parent)
        loadUi('Gui/View_ans.ui', self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calculos/files/A_Resultados_Analisis.xlsx')

        a = read.parse('CargasGeneralizadas')
        b = read.parse('MatrizGlobalEstructura')
        c = read.parse('Desplazamientos')
        d = read.parse('Reacciones')
        e = read.parse('FuerzasElementales')


        model = DataFrameModel(a)
        self.tableView_CG.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_MGE.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Des.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_Reac.setModel(model)        
        
        model = DataFrameModel(e)
        self.tableView_FE.setModel(model)          
        
        

class Ans_B(QMainWindow):

    def __init__(self, parent=None):
        super(Ans_B,self).__init__(parent)
        loadUi('Gui/View_ans.ui', self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calculos/files/B_Resultados_Analisis.xlsx')

        a = read.parse('CargasGeneralizadas')
        b = read.parse('MatrizGlobalEstructura')
        c = read.parse('Desplazamientos')
        d = read.parse('Reacciones')
        e = read.parse('FuerzasElementales')


        model = DataFrameModel(a)
        self.tableView_CG.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_MGE.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Des.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_Reac.setModel(model)        
        
        model = DataFrameModel(e)
        self.tableView_FE.setModel(model)                       

            
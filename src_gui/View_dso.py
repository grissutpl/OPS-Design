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
class Dso(QMainWindow):

    def __init__(self, parent=None):
        super(Dso,self).__init__(parent)
        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calculos/onefile/Resultados_Diseno_Restriccion.xlsx')

        a = read.parse('DisenioCompresion')
        b = read.parse('DisenioFlexion_X')
        c = read.parse('DisenioFlexion_Y')
        d = read.parse('Restriccion_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)        
        


class Dso_A(QMainWindow):

    def __init__(self, parent=None):
        super(Dso_A,self).__init__(parent)
        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calculos/files/A_Resultados_Diseno_Restriccion.xlsx')

        a = read.parse('DisenioCompresion')
        b = read.parse('DisenioFlexion_X')
        c = read.parse('DisenioFlexion_Y')
        d = read.parse('Restriccion_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)                 
        


class Dso_B(QMainWindow):

    def __init__(self, parent=None):
        super(Dso_B,self).__init__(parent)
        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calculos/files/B_Resultados_Diseno_Restriccion.xlsx')

        a = read.parse('DisenioCompresion')
        b = read.parse('DisenioFlexion_X')
        c = read.parse('DisenioFlexion_Y')
        d = read.parse('Restriccion_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)                 

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import pandas as pd

from src_gui.generateDataframe import DataFrameModel

from Gui.View_ans import Ui_MainWindow

# Clase de la subventana
class Ans(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ans,self).__init__(parent)
#        loadUi('Gui/View_ans.ui', self)

        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calc/onefile/AnalysisResults.xlsx')

        a = read.parse('GeneralizedLoads')
        b = read.parse('RigidMatrixGlobal')
        c = read.parse('Displacements')
        d = read.parse('Reactions')
        e = read.parse('Forces')


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
        



class Ans_A(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ans_A,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/View_ans.ui', self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calc/files/A_AnalysisResults.xlsx')

        a = read.parse('GeneralizedLoads')
        b = read.parse('RigidMatrixGlobal')
        c = read.parse('Displacements')
        d = read.parse('Reactions')
        e = read.parse('Forces')


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
        
        

class Ans_B(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ans_B,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/View_ans.ui', self)

#        self.parent = parent 

        read = pd.ExcelFile('src_calc/files/B_AnalysisResults.xlsx')

        a = read.parse('GeneralizedLoads')
        b = read.parse('RigidMatrixGlobal')
        c = read.parse('Displacements')
        d = read.parse('Reactions')
        e = read.parse('Forces')


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

            
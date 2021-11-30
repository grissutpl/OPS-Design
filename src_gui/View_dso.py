# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import pandas as pd

from src_gui.generateDataframe import DataFrameModel

from Gui.View_dso import Ui_MainWindow

# Clase de la subventana
class Dso(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Dso,self).__init__(parent)

        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calc/onefile/DesignRestrictionResult.xlsx')

        a = read.parse('CompressionDesign')
        b = read.parse('FlexuralDesign_X')
        c = read.parse('FlexuralDesign_Y')
        d = read.parse('Ratio_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)        
        


class Dso_A(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Dso_A,self).__init__(parent)

        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calc/files/A_DesignRestrictionResult.xlsx')

        a = read.parse('CompressionDesign')
        b = read.parse('FlexuralDesign_X')
        c = read.parse('FlexuralDesign_Y')
        d = read.parse('Ratio_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)                 
        


class Dso_B(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Dso_B,self).__init__(parent)

        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_dso.ui', self)
                
        read = pd.ExcelFile('src_calc/files/B_DesignRestrictionResult.xlsx')

        a = read.parse('CompressionDesign')
        b = read.parse('FlexuralDesign_X')
        c = read.parse('FlexuralDesign_Y')
        d = read.parse('Ratio_DC')


        model = DataFrameModel(a)
        self.tableView_DComp.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_Dflexx.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_Dflexy.setModel(model)        
        
        model = DataFrameModel(d)
        self.tableView_DSum.setModel(model)                 

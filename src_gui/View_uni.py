# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import pandas as pd

from src_gui.generateDataframe import DataFrameModel

from Gui.View_uni import Ui_MainWindow

# Clase de la subventana
class Uni(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Uni,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calc/onefile/JointRestrictionResults.xlsx')

        a = read.parse('BeamColJoint')
        b = read.parse('ColColJoint_Depth')
        c = read.parse('ColColJoint_Flange')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)        
        

class Uni_A(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Uni_A,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calc/files/A_JointRestrictionResults.xlsx')

        a = read.parse('BeamColJoint')
        b = read.parse('ColColJoint_Depth')
        c = read.parse('ColColJoint_Flange')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)  
        

class Uni_B(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Uni_B,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self) 

#        loadUi('Gui/View_uni.ui', self)

        read = pd.ExcelFile('src_calc/files/B_JointRestrictionResults.xlsx')

        a = read.parse('BeamColJoint')
        b = read.parse('ColColJoint_Depth')
        c = read.parse('ColColJoint_Flange')


        model = DataFrameModel(a)
        self.tableView_VC.setModel(model)
        
        model = DataFrameModel(b)
        self.tableView_CCPer.setModel(model)        
        
        model = DataFrameModel(c)
        self.tableView_CCPat.setModel(model)  
        

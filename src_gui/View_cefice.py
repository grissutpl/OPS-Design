# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

from PyQt5.QtWidgets import QMainWindow
#from PyQt5.uic import loadUi

import pandas as pd

from src_gui.generateDataframe import DataFrameModel

from Gui.View_cefice import Ui_MainWindow

# Clase de la subventana
class Cefice(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Cefice,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calc/onefile/CompEficRestrictionResults.xlsx')

        a = read.parse('CEE.BothAxes')


        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        


class Cefice_A(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Cefice_A,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calc/files/A_CompEficRestrictionResults.xlsx')

        a = read.parse('CEE.BothAxes')


        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        


class Cefice_B(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Cefice_B,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calc/files/B_CompEficRestrictionResults.xlsx')

        a = read.parse('CEE.BothAxes')


        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        

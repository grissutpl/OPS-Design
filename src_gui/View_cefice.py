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
class Cefice(QMainWindow):

    def __init__(self, parent=None):
        super(Cefice,self).__init__(parent)
        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calculos/onefile/Resultados_CompEficc_Restriccion.xlsx')

        a = read.parse('C.E_AmbosEjes')

        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        


class Cefice_A(QMainWindow):

    def __init__(self, parent=None):
        super(Cefice_A,self).__init__(parent)
        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calculos/files/A_Resultados_CompEficc_Restriccion.xlsx')

        a = read.parse('C.E_AmbosEjes')


        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        

class Cefice_B(QMainWindow):

    def __init__(self, parent=None):
        super(Cefice_B,self).__init__(parent)
        loadUi('Gui/View_cefice.ui', self)

        read = pd.ExcelFile('src_calculos/files/B_Resultados_CompEficc_Restriccion.xlsx')

        a = read.parse('C.E_AmbosEjes')


        model = DataFrameModel(a)
        self.tableView_Cefic.setModel(model)
        

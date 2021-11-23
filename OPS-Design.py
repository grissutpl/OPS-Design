# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import pandas as pd # Conectar con hojas de excel

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from src_gui.subDinamic_DataInput import DataInput
from src_gui.subDinamic_Result import Result

from src_calculos.methods.ingresos_excel import ingreso_de_datos_excel

from src_gui.viewgraphs import InfoImage

# C L A S E   V E N T A N A    PRINCIPAL
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class mainWindowInicial(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindowInicial,self).__init__(parent)
        loadUi('Gui/principal_main.ui', self)
        self.setWindowIcon(QIcon("iconoventana.jpg"))
        
        # MENUS DESPLEGABLES DE LA VENTANA DE INICIO ====================================================================================================
        
        # DATOS DE ENTRADA
        self.actionDatosDeEntrada.triggered.connect(self.open_dataInput)      
        
        # CUADRO DE RESULTADOS
        self.actionResultados.triggered.connect(self.open_result)
        
        
        self.actionSalir_2.triggered.connect(self.close)  
        self.actionOPS_Design.triggered.connect(self.ayuda)  

        self.actionSecciones_W.triggered.connect(self.open_info_image)          
        # ...
        # ...





        # V A R I A B L E S    D E    E N T R A D A:
        # ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        # A. BASE DE DATOS
        
        self.ExcelPrincipal = pd.ExcelFile('DatosExcel.xlsx')       
        self.Perfil_Data = self.ExcelPrincipal.parse('W') #---> La subbase de DatosPrincipales utilizada 'Perfil_Data' será la perteneciente 
                                                              #     a la hoja del excel que corresponda.


        # B. DATOS DE EJEMPLO DEL LLENADO DE LA MATRIZ ------------------------@
        

        self.datos_generales = [[1,    'Col',  1, 19, 20, 21, 13, 14, 15,   0,   0,   0,   3, 'W',  '16X26',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [2,    'Col',  1, 22, 23, 24, 16, 17, 18,   4,   0,   4,   3, 'W',  '16X26',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [3,    'Col',  2, 13, 14, 15,  7,  8,  9,   0,   3,   0,   6, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [4,    'Col',  2, 16, 17, 18, 10, 11, 12,   4,   3,   4,   6, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [5,    'Col',  3,  7,  8,  9,  1,  2,  3,   0,   6,   0,   9, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [6,    'Col',  3, 10, 11, 12,  4,  5,  6,   4,   6,   4,   9, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [7,    'Vig',  1, 13, 14, 15, 16, 17, 18,   0,   3,   4,   3, 'W',  '14X61', -4240, 0, 0, 0, 0, 0, 0, 0], 
                                [8,    'Vig',  2,  7,  8,  9, 10, 11, 12,   0,   6,   4,   6, 'W',  '14X61', -4240, 0, 0, 0, 0, 0, 0, 0], 
                                [9,    'Vig',  3,  1,  2,  3,  4,  5,  6,   0,   9,   4,   9, 'W',  '14X61', -4150, 0, 0, 0, 0, 0, 0, 0]]
        
        self.datos_inicializacion = [8,2] # -----------------------------------@


        # C. DATOS DE QUE SE DEBERIAN LLAMAR DE LA SUBVENTANA CUANDO EL QUE LLENA LA MATRIZ SOY YO. 
        
        self.DatosPrincipales = pd.DataFrame(columns=('Elemento', 'Tipo', 'Piso','X(i)', 'Y(i)', '⟲(i)','X(j)', 'Y(j)', '⟲(j)','x(i)','y(i)', 'x(j)', 'y(j)','14', '15', '16',
                                                                 '17', '18', '19','20','21', '22', '23'))

        self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)        

        
        
        

    # EVENTOS VENTANA DE INICIO =========================================================================================================================
        
    def open_dataInput(self):
        DataInput(self).showMaximized()
        
    def open_result(self):
        Result(self).showMaximized()





    def ayuda(self):

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Información de asistencia")
        mensaje.setIconPixmap(QPixmap("simbol_help.jpg").scaled(290, 290, Qt.KeepAspectRatio))
        mensaje.setText("<b>Gracias por usar nuestra herramienta ☺ </b>")
        mensaje.setInformativeText("La herramienta <b>OPS Design</b> en su primera versión es un software de <b>diseño óptimo preliminar de elementos</b> "
                                   "estructurales metálicos en pórticos 2D para el cumplimiento de la relaciones D/C, considerando además un ensamble "
                                   "correcto entre sus miembros y un comportamiento eficiente a compresión en ambos ejes.</p>"
                                   "<p>Para información sobre el manejo del aplicativo, características y funcionalidades, visite la web del <a href='https://www.facebook.com/danielalexander.villarreal'>Grupo de Ingeniería Sísmica y Sismología de la Universidad Técnica Particular de Loja (GRISS-UTPL)</a></p>"
                                   "<p>Si desea ver información sobre el proyecto de investigación <a href='https://www.facebook.com/danielalexander.villarreal'>visite el artículo aquí</a> </p>"
                                   "<p> Éxitos.</p>"
                                   "<p> _________________________________________________________________________________________________________________________________________________________________________")


        mensaje.exec_() 

    def open_info_image(self):
        InfoImage(self).show()        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainWindowInicial()
    widget.showMaximized()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    

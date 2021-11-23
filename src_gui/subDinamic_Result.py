# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from src_calculos.packgraphs.grafica_detalle import frame, frame_b

from src_calculos.packgraphs.grafica_objetivo import graph_objetive

from src_gui.View_ans import Ans, Ans_A, Ans_B
from src_gui.View_cefice import Cefice, Cefice_A, Cefice_B
from src_gui.View_dso import Dso, Dso_A, Dso_B
from src_gui.View_uni import Uni, Uni_A, Uni_B

from src_gui.viewgraphs import InfoImage
# CLASE DE LA SUBVENTANA DE RESULTADOS
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
class Result(QMainWindow):

    def __init__(self, parent=None):
        super(Result,self).__init__(parent)
        loadUi('Gui/subDinamic_Result.ui', self)
#        loadUi('Gui/subDinamic_Result_altern.ui', self)

        self.parent = parent 

        # BOTONES DE LA SUBVENTANA =====================================================================================================================
        
        self.pushButtonGraficaOneTime.clicked.connect(self.grafica_onetime)  

        self.pushButtonGrafica_pesos.clicked.connect(self.grafica_pesos)  
        self.pushButtonGraficaIteration.clicked.connect(self.grafica_iteration)  


        self.radioButton_op1.clicked.connect(self.option_a)
        self.radioButton_op2.clicked.connect(self.option_b)


        self.toolButton_tban_one.clicked.connect(self.ans_onetime)  
        self.toolButton_tbdis_one.clicked.connect(self.dso_onetime)  
        self.toolButton_tbuni_one.clicked.connect(self.uni_onetime)  
        self.toolButton_tbcef_one.clicked.connect(self.cefice_onetime)  
        
        self.toolButton_tban_iter.clicked.connect(self.ans_iteration)  
        self.toolButton_tbdis_iter.clicked.connect(self.dso_iteration)  
        self.toolButton_tbuni_iter.clicked.connect(self.uni_iteration)  
        self.toolButton_tbcef_iter.clicked.connect(self.cefice_iteration) 
        
        
        self.pushButtonAyuda_Ra.clicked.connect(self.ayuda)  
        self.pushButtonAyuda_Rb.clicked.connect(self.ayuda)  

        self.toolButton_visor_Ra.clicked.connect(self.open_info_image)
        self.toolButton_visor_Rb.clicked.connect(self.open_info_image)

    # SALIDAS DE RESULTADOS ============================================================================================================
    

        if self.parent.D_optimizator == 0:

            self.text = open('src_calculos/onefile/onedetailed.txt', "r", encoding="utf-8").read()
            self.textBrowser_2.setText(self.text)
            
            self.textBrowser_3.setText(None)


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

            
    def option_a(self):

        if self.parent.D_optimizator == 1 or self.parent.D_optimizator == 2:
            
            self.text = open('src_calculos/files/detailed_a.txt', "r", encoding="utf-8").read()
            self.textBrowser_3.setText(self.text)
            
            self.textBrowser_2.setText(None)

    def option_b(self):
        
        if self.parent.D_optimizator == 1 or self.parent.D_optimizator == 2:

            self.text = open('src_calculos/files/detailed_b.txt', "r", encoding="utf-8").read()
            self.textBrowser_3.setText(self.text)
            
            self.textBrowser_2.setText(None)
                

    # EVENTOS DE LA SUBVENTANA DE RESULTADOS ============================================================================================================
    
    # GRÁFICAS

    def grafica_onetime(self):
        if self.parent.D_optimizator == 0:
            frame(self.parent.ingreso_datos)

    def grafica_pesos(self):
        if self.parent.D_optimizator == 1:
            graph_objetive(self.parent.lista_Peso_estructural)

    def grafica_iteration(self):
        if self.parent.D_optimizator == 1:
            if self.radioButton_op1.isChecked()==True:
                pass
                
            elif self.radioButton_op2.isChecked()==True:
                frame_b(self.parent.ingreso_datos_b)

                

    # BOTONES PARA RESULTADOS EXCEL PESTAÑA 1

    def ans_onetime(self):
        if self.parent.D_optimizator == 0:
            Ans(self).show()

    def dso_onetime(self):
        if self.parent.D_optimizator == 0:
            Dso(self).show()
      
    def uni_onetime(self):
        if self.parent.D_optimizator == 0:
            Uni(self).show()

    def cefice_onetime(self):
        if self.parent.D_optimizator == 0:
            Cefice(self).show()



    # BOTONES PARA RESULTADOS EXCEL PESTAÑA 2
    
    def ans_iteration(self):
        if self.parent.D_optimizator == 1:
            if self.radioButton_op1.isChecked()==True:
                Ans_A(self).show()

            elif self.radioButton_op2.isChecked()==True:
                Ans_B(self).show()
    
    def dso_iteration(self):
        if self.parent.D_optimizator == 1:
            if self.radioButton_op1.isChecked()==True:
                Dso_A(self).show()

            elif self.radioButton_op2.isChecked()==True:
                Dso_B(self).show()
      
    def uni_iteration(self):
        if self.parent.D_optimizator == 1:
            if self.radioButton_op1.isChecked()==True:
                Uni_A(self).show()

            elif self.radioButton_op2.isChecked()==True:
                Uni_B(self).show()

    def cefice_iteration(self):
        if self.parent.D_optimizator == 1:
            if self.radioButton_op1.isChecked()==True:
                Cefice_A(self).show()

            elif self.radioButton_op2.isChecked()==True:
                Cefice_B(self).show()


    def open_info_image(self):
        InfoImage(self).show()      
          
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Result()
    widget.show()
    sys.exit(app.exec_())    
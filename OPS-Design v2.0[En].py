# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import pandas as pd # Conectar con hojas de excel

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QMessageBox
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from src_gui.subDinamic_DataInput import DataInput
from src_gui.subDinamic_Result import Result

from src_calc.methods.inputs_excel import ingreso_de_datos_excel

from src_gui.viewgraphs import InfoImage

# C L A S E   V E N T A N A    PRINCIPAL
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

from Gui.principal_main2 import Ui_MainWindow


counter = 0

class mainWindowInicial(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindowInicial,self).__init__(parent)
#        loadUi('Gui/principal_main2.ui', self)
#        self.setWindowIcon(QIcon("iconoventana.jpg"))

        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.ventanas = [0, 0]

        # MENUS DESPLEGABLES DE LA VENTANA DE INICIO ====================================================================================================
        
        # DATOS DE ENTRADA
        self.actionDatosDeEntrada.triggered.connect(self.open_dataInput)      
        
        # CUADRO DE RESULTADOS
        self.actionResultados.triggered.connect(self.open_result)
        
        
        self.actionSalir_2.triggered.connect(self.close)  
        self.actionOPS_Design.triggered.connect(self.ayuda)  

        self.actionSecciones_W.triggered.connect(self.open_info_image)          


        self.actionLoad.setEnabled(False)
        self.actionSave.setEnabled(False)

#        self.actionClean.triggered.connect(self.cleaningall)  

        # ...
        # ...





        # V A R I A B L E S    D E    E N T R A D A:
        # ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

        # A. BASE DE DATOS
        
        self.ExcelPrincipal = pd.ExcelFile('InfoData.xlsx')       
        self.Perfil_Data = self.ExcelPrincipal.parse('W') #---> La subbase de DatosPrincipales utilizada 'Perfil_Data' será la perteneciente 
                                                              #     a la hoja del excel que corresponda.


        # B. DATOS DE EJEMPLO DEL LLENADO DE LA MATRIZ ------------------------@
        

        self.datos_generales = [[1,    'Column',  1, 19, 20, 21, 13, 14, 15,   0,   0,   0,   3, 'W',  '16X26',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [2,    'Column',  1, 22, 23, 24, 16, 17, 18,   4,   0,   4,   3, 'W',  '16X26',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [3,    'Column',  2, 13, 14, 15,  7,  8,  9,   0,   3,   0,   6, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [4,    'Column',  2, 16, 17, 18, 10, 11, 12,   4,   3,   4,   6, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [5,    'Column',  3,  7,  8,  9,  1,  2,  3,   0,   6,   0,   9, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [6,    'Column',  3, 10, 11, 12,  4,  5,  6,   4,   6,   4,   9, 'W',  '14X53',     0, 0, 0, 0, 0, 0, 0, 0], 
                                [7,    'Beam',  1, 13, 14, 15, 16, 17, 18,   0,   3,   4,   3, 'W',  '14X61', -4240, 0, 0, 0, 0, 0, 0, 0], 
                                [8,    'Beam',  2,  7,  8,  9, 10, 11, 12,   0,   6,   4,   6, 'W',  '14X61', -4240, 0, 0, 0, 0, 0, 0, 0], 
                                [9,    'Beam',  3,  1,  2,  3,  4,  5,  6,   0,   9,   4,   9, 'W',  '14X61', -4150, 0, 0, 0, 0, 0, 0, 0]]
        
        self.datos_inicializacion = [8,2] # -----------------------------------@


        # C. DATOS DE QUE SE DEBERIAN LLAMAR DE LA SUBVENTANA CUANDO EL QUE LLENA LA MATRIZ SOY YO. 
        
        self.DatosPrincipales = pd.DataFrame(columns=('Element', 'Type', 'Floor','X(i)', 'Y(i)', '⟲(i)','X(j)', 'Y(j)', '⟲(j)','x(i)','y(i)', 'x(j)', 'y(j)','14', '15', '16',
                                                                 '17', '18', '19','20','21', '22', '23'))

        self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)        

        
        
        

#    # EVENTOS VENTANA DE INICIO =========================================================================================================================
#        
#    def open_dataInput(self):
#        
#        print(self.ventanas)
#
#        if self.ventanas[0] == 0 and self.ventanas[1] == 0:
#        
#            winw = QMdiSubWindow()
#            widget = DataInput(self)
#            winw.setWidget(widget)
#            self.mdiArea_Container1.addSubWindow(winw)
#            winw.show()
#            winw.showMaximized()
#
#            self.my_console = open("src_calc/files/optimice_motor.txt","w").close()
#            self.my_console = open("src_calc/onefile/onedetailed.txt","w").close()
#            self.my_console = open("src_calc/files/detailed_a.txt","w").close()
#            self.my_console = open("src_calc/files/detailed_b.txt","w").close()
#            self.my_console = open("src_calc/data.txt","w").close()
#        
#        elif self.ventanas[0] == 1 and self.ventanas[1] == 1:
#
#            reply = QMessageBox.question(self, 'Advise', 'This action, will delete your model. <p>We recommend that you save your model, if you have already done so, you can continue.</p> <p><b>¿Do you want to continue?</b></p>',
#            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
##            QMessageBox.setWindowIcon(QtGui.QIcon("ops_icon.jpg"))
#
#            if reply == QMessageBox.Yes:
##                event.accept()
#                
#                self.ventanas[0] = 0
#                self.ventanas[1] = 0
#                self.actionResultados.setEnabled(False)
#    
#                self.actionLoad.setEnabled(False)
#                self.actionSave.setEnabled(False)
#    
#                winw = QMdiSubWindow()
#                widget = DataInput(self)
#                winw.setWidget(widget)
#                self.mdiArea_Container1.addSubWindow(winw)
#                winw.show()
#                winw.showMaximized()
#
#                self.my_console = open("src_calc/files/optimice_motor.txt","w").close()
#                self.my_console = open("src_calc/onefile/onedetailed.txt","w").close()
#                self.my_console = open("src_calc/files/detailed_a.txt","w").close()
#                self.my_console = open("src_calc/files/detailed_b.txt","w").close()
#                self.my_console = open("src_calc/data.txt","w").close()
#
#            else:
##                event.ignore()
#                pass
#            
##            pass
#        
#        elif self.ventanas[0] == 1 or self.ventanas[0] == 2 or self.ventanas[1] == 1:
#            
#            reply = QMessageBox.question(self, 'Advise', 'This action, will delete your model. <p>We recommend that you save your model, if you have already done so, you can continue.</p> <p><b>¿Do you want to continue?</b></p>',
#            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
##            QMessageBox.setWindowIcon(QtGui.QIcon("ops_icon.jpg"))
#
#            if reply == QMessageBox.Yes:
##                event.accept()
#                self.ventanas[0] = 0
#                self.ventanas[1] = 0
#                self.actionResultados.setEnabled(False)
#    
#                self.actionLoad.setEnabled(False)
#                self.actionSave.setEnabled(False)
#    
#                winw = QMdiSubWindow()
#                widget = DataInput(self)
#                winw.setWidget(widget)
#                self.mdiArea_Container1.addSubWindow(winw)
#                winw.show()
#                winw.showMaximized()
#
#                self.my_console = open("src_calc/files/optimice_motor.txt","w").close()
#                self.my_console = open("src_calc/onefile/onedetailed.txt","w").close()
#                self.my_console = open("src_calc/files/detailed_a.txt","w").close()
#                self.my_console = open("src_calc/files/detailed_b.txt","w").close()
#                self.my_console = open("src_calc/data.txt","w").close()
#
#
#            else:
#                pass
##                event.ignore()
#            
##            pass
#        
##        DataInput(self).showMaximized()
#        
#    def open_result(self):
#
#        print(self.ventanas)
#        
#        if self.ventanas[0] == 2 and self.ventanas[1] == 0:
#            
#            winw = QMdiSubWindow()
#            widget = Result(self)
#            winw.setWidget(widget)
#            self.mdiArea_Container1.addSubWindow(winw)
#            winw.show()
#            winw.showMaximized()
#
#        elif self.ventanas[0] == 1 and self.ventanas[1] == 1:
#            
#            pass
#
#        elif self.ventanas[0] == 2 and self.ventanas[1] == 1:
#            
#            pass
#
#        elif self.ventanas[0] == 1 or self.ventanas[0] == 2  or self.ventanas[1] == 1:
#            
#            pass
#
##        Result(self).showMaximized()
#
#
#    def ayuda(self):
#
#        mensaje = QMessageBox(self)
#        mensaje.setWindowTitle("Support Information")
#        mensaje.setIconPixmap(QPixmap("simbol_help.jpg").scaled(290, 290, Qt.KeepAspectRatio))
#        mensaje.setText("<b>Thank you for using our tool. ☺ </b>")
#        mensaje.setInformativeText("The first version of this tool is a software of <b>preliminary optimal design of steel structural elements</b> "
#                                   "in 2D frames for satisfy Demand/Capacity Ratio, considering the correct assemble "
#                                   "between the pieces and an efficent development in compresion for both axes.</p>"
#                                   "<p>For information about the app, use, features and funtionality, and academic publishing visit the web page of <a href='https://ingenieriasismica.utpl.edu.ec/?q=es/OPS_Design'>Grupo de Ingeniería Sísmica y Sismología de la Universidad Técnica Particular de Loja (GRISS-UTPL)</a></p>"
#                                   "<p> Daniel Alexander Villarreal, Civil Engineer | Edwin Patricio Duque, MSc. | Henrry Vicente Rojas, MSc.</p>"
#                                   "<p> _________________________________________________________________________________________________________________________________________________________________________")
#        
#        
#        mensaje.exec_() 


































    # EVENTOS VENTANA DE INICIO =========================================================================================================================
        
    def open_dataInput(self):
        
        print(self.ventanas)

        if self.ventanas[0] == 0 and self.ventanas[1] == 0:
        
            winw = QMdiSubWindow()
            widget = DataInput(self)
            winw.setWidget(widget)
            self.mdiArea_Container1.addSubWindow(winw)
            winw.show()
            winw.showMaximized()

            self.my_console = open("src_calc/files/optimice_motor.txt","w").close()
            self.my_console = open("src_calc/onefile/onedetailed.txt","w").close()
            self.my_console = open("src_calc/files/detailed_a.txt","w").close()
            self.my_console = open("src_calc/files/detailed_b.txt","w").close()
            self.my_console = open("src_calc/data.txt","w").close()
        
        elif self.ventanas[0] == 1 and self.ventanas[1] == 1:

            pass
            
        elif self.ventanas[0] == 1 or self.ventanas[0] == 2 or self.ventanas[1] == 1:
            
            pass
        
    def open_result(self):

        print(self.ventanas)
        
        if self.ventanas[0] == 2 and self.ventanas[1] == 0:
            
            winw = QMdiSubWindow()
            widget = Result(self)
            winw.setWidget(widget)
            self.mdiArea_Container1.addSubWindow(winw)
            winw.show()
            winw.showMaximized()

        elif self.ventanas[0] == 1 and self.ventanas[1] == 1:
            
            pass

        elif self.ventanas[0] == 2 and self.ventanas[1] == 1:
            
            pass

        elif self.ventanas[0] == 1 or self.ventanas[0] == 2  or self.ventanas[1] == 1:
            
            pass

#        Result(self).showMaximized()


    def ayuda(self):

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Support Information")
        mensaje.setIconPixmap(QPixmap("simbol_help.jpg").scaled(290, 290, Qt.KeepAspectRatio))
        mensaje.setText("<b>Thank you for using our tool. ☺ </b>")
        mensaje.setInformativeText("The first version of this tool is a software of <b>preliminary optimal design of steel structural elements</b> "
                                   "in 2D frames for satisfy Demand/Capacity Ratio, considering the correct assemble "
                                   "between the pieces and an efficent development in compresion for both axes.</p>"
                                   "<p>For information about the app, use, features and funtionality, and academic publishing visit the web page of <a href='https://ingenieriasismica.utpl.edu.ec/?q=es/OPS_Design'>Grupo de Ingeniería Sísmica y Sismología de la Universidad Técnica Particular de Loja (GRISS-UTPL)</a></p>"
                                   "<p> Daniel Alexander Villarreal, Civil Engineer | Edwin Patricio Duque, MSc. | Henrry Vicente Rojas, MSc.</p>"
                                   "<p> _________________________________________________________________________________________________________________________________________________________________________")
        
        
        mensaje.exec_() 


























    def open_info_image(self):
        InfoImage(self).show()  
        
        
#    def cleaningall(self):
#        print('close')
#        Result(self).close()
#        DataInput(self).close()
#        
#        
        
        
        
        
from Gui.splash import Ui_MainWindow
        
class SplashScreen(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SplashScreen,self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#        loadUi('Gui/splash.ui', self)
        self.setWindowIcon(QIcon("iconoventana.jpg"))

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(40)

        # CHANGE DESCRIPTION

        # Initial Text
        self.label_description.setText("<strong>Welcome</strong> To OPS Design")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.label_description.setText("<strong>Loading</strong> InfoData, Icons, ShapeTypes AISC"))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText("<strong>Loading</strong> Graphic User Interface"))     
        QtCore.QTimer.singleShot(3300, lambda: self.label_description.setText("<strong>Loading</strong> Optimization Modules"))     
        QtCore.QTimer.singleShot(4000, lambda: self.label_description.setText("<strong>Loading</strong> Presentation Modules"))     

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = mainWindowInicial()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1        
        
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
#    widget = mainWindowInicial()
    widget = SplashScreen()
    widget.show()
#    widget.showMaximized()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    

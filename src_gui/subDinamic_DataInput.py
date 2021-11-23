# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys
import pandas as pd # Conectar con hojas de excel
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from threading import Thread

import matplotlib.pyplot as plt # Ploteo de gráficas
import numpy as np # Creación de matrices

from src_calculos.methods.ingresos_excel import ingreso_de_datos_excel

from src_calculos.packdetails.detalles import detallado, detallado_a, detallado_b

from src_calculos.motor.optimal import optimalframe
from src_calculos.motor.ingresos_actualizados import ingr_actual_a, ingr_actual_b

from src_calculos.loggerPrint import Logger

from src_gui.iteration import Iterations

from src_gui.viewgraphs import InfoImage
# C L A S E    D E    L A    S U B V E N T A N A    D E    D A T O S    D E    E N T R A D A 
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class DataInput(QMainWindow):

    def __init__(self, parent=None):
        super(DataInput,self).__init__(parent)
        loadUi('Gui/subDinamic_DataInput.ui', self)

        self.parent = parent # --> Variable de la clase, encargada de almacenar cosas y enviarlas a otros lugares donde se necesite, IMPORTANTE.   
                             # --> CONOCIDA TAMBIÉN COMO VARIABLE PADRE   

        # BOTONES DE LA SUBVENTANA =====================================================================================================================
        
        self.pushButtonEjemplo.clicked.connect(self.ejemplo)  
        
        self.pushButtonMas.clicked.connect(self.mas)  
        self.pushButtonMenos.clicked.connect(self.menos)  
        
        self.pushButtonGraficaInicio.clicked.connect(self.graficainicio)  
        self.pushButtonAyuda.clicked.connect(self.ayuda)
        
        self.pushButtonAnalisisDiseno.clicked.connect(self.analisisdisenio)  
#        self.pushButtonOptimizacion.clicked.connect(self.optimization)  
        self.pushButtonOptimizacion.clicked.connect(self.funcion_tread)  

        self.toolButton_Story.clicked.connect(self.info)
        self.toolButton_visor.clicked.connect(self.open_info_image)

        self.is_sending_data =False

    # EVENTOS SUBVENTANA ===============================================================================================================================

    def funcion_tread(self):
        
        msg = QMessageBox()
        msg.setWindowTitle('Mensaje de advertencia')
        msg.setText('''<b>Este proceso puede tardar unos minutos...</b>
                    <br/><br/> Presione OK para continuar.''')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


        thread_optimizator = Thread(target = self.optimization)
        thread_optimizator.start()


        Iterations(self).show()    
            
    def ejemplo(self):
        # 2.1 Aquí lleno la tabla
        for i in self.parent.datos_generales:

            inx = self.parent.datos_generales.index(i)
            self.tableWidget_DatosEntrada.insertRow(inx)

            i0 = QTableWidgetItem(str(self.tableWidget_DatosEntrada.rowCount()))
            i0.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            i2 = QTableWidgetItem(str(i[2]))
            i2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i3 = QTableWidgetItem(str(i[3]))
            i3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i4 = QTableWidgetItem(str(i[4]))
            i4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i5 = QTableWidgetItem(str(i[5]))
            i5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i6 = QTableWidgetItem(str(i[6]))
            i6.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i7 = QTableWidgetItem(str(i[7]))
            i7.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i8 = QTableWidgetItem(str(i[8]))
            i8.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i9 = QTableWidgetItem(str(i[9]))
            i9.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i10 = QTableWidgetItem(str(i[10]))
            i10.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i11 = QTableWidgetItem(str(i[11]))
            i11.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i12 = QTableWidgetItem(str(i[12]))
            i12.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#            i13 = QTableWidgetItem(str(i[13]))
#            i13.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            
            i15 = QTableWidgetItem(str(i[15]))
            i15.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i16 = QTableWidgetItem(str(i[16]))
            i16.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i17 = QTableWidgetItem(str(i[17]))
            i17.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i18 = QTableWidgetItem(str(i[18]))
            i18.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i19 = QTableWidgetItem(str(i[19]))
            i19.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i20 = QTableWidgetItem(str(i[20]))
            i20.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i21 = QTableWidgetItem(str(i[21]))
            i21.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            i22 = QTableWidgetItem(str(i[22]))
            i22.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#            i23 = QTableWidgetItem(str(i[23]))
#            i23.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#            i24 = QTableWidgetItem(str(i[24]))
#            i24.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget_DatosEntrada.setItem(inx, 0, i0)            
            
            self.tableWidget_DatosEntrada.setItem(inx, 2, i2)
            self.tableWidget_DatosEntrada.setItem(inx, 3, i3)
            self.tableWidget_DatosEntrada.setItem(inx, 4, i4)
            self.tableWidget_DatosEntrada.setItem(inx, 5, i5)
            self.tableWidget_DatosEntrada.setItem(inx, 6, i6)
            self.tableWidget_DatosEntrada.setItem(inx, 7, i7)
            self.tableWidget_DatosEntrada.setItem(inx, 8, i8)
            self.tableWidget_DatosEntrada.setItem(inx, 9, i9)
            self.tableWidget_DatosEntrada.setItem(inx, 10, i10)
            self.tableWidget_DatosEntrada.setItem(inx, 11, i11)
            self.tableWidget_DatosEntrada.setItem(inx, 12, i12)
#            self.tableWidget_DatosEntrada.setItem(inx, 13, i13)



            self.tableWidget_DatosEntrada.setItem(inx, 15, i15)
            self.tableWidget_DatosEntrada.setItem(inx, 16, i16)
            self.tableWidget_DatosEntrada.setItem(inx, 17, i17)
            self.tableWidget_DatosEntrada.setItem(inx, 18, i18)
            self.tableWidget_DatosEntrada.setItem(inx, 19, i19)
            self.tableWidget_DatosEntrada.setItem(inx, 20, i20)
            self.tableWidget_DatosEntrada.setItem(inx, 21, i21)
            self.tableWidget_DatosEntrada.setItem(inx, 22, i22)
#            self.tableWidget_DatosEntrada.setItem(inx, 23, i23)
#            self.tableWidget_DatosEntrada.setItem(inx, 24, i24)

            combobox0 = QComboBox()
            combobox0.addItems(['W'])

            combobox1 = QComboBox()
            if str(i[1]) == 'Col':
                combobox1.addItems([str(i[1]), 'Vig'])
            elif str(i[1]) == 'Vig':
                combobox1.addItems([str(i[1]), 'Col'])


            combobox2 = QComboBox()
            if str(i[14]) == '16X26' or str(i[14]) == '14X53' or str(i[14]) == '14X61':
                combobox2.addItems([str(i[14]), "4X13",	  "5X16",	  "5X19",	"6X8.5",	"6X9", 	"6X12",	"6X16",	"6X15",	"6X20",	"6X25",	
                                       "8X10",	  "8X13",	  "8X15",	"8X18",	"8X21",	"8X24",	"8X28",	"8X31",	"8X35",	"8X40",	
                                       "8X48",	  "8X58",	  "8X67",	"10X12",	"10X15",	"10X17",	"10X19",	"10X22",	"10X26",	"10X30",	
                                      "10X33",	 "10X39",	 "10X45",	"10X49",	"10X54",	"10X60",	"10X68",	"10X77",	"10X88",	"10X100",	
                                     "10X112",	 "12X14",	 "12X16",	"12X19",	"12X22",	"12X26",	"12X30",	"12X35",	"12X40",	"12X45",	
                                      "12X50",	 "12X53",	 "12X58",	"12X65",	"12X72",	"12X79",	"12X87",	"12X96",	"12X106",	"12X120",	
                                     "12X136",	"12X152",	"12X170",	"12X190",	"12X210",	"12X230",	"12X252",	"12X279",	"12X305",	"12X336",	
                                      "14X22",	 "14X26",  "14X30",	"14X34",	"14X38",	"14X43",	"14X48",	"14X68",	
                                      "14X74",	 "14X82",	 "14X90",	"14X99",	"14X109",	"14X120",	"14X132",	"14X145",	"14X159",	"14X176",	
                                     "14X193",	"14X211",	"14X233",	"14X257",	"14X283",	"14X311",	"14X342",	"14X370",	"14X398",	"14X426",	
                                     "14X455",  "14X500",	"14X550",	"14X605",	"14X665",	"14X730",	"16X31",	"16X36",	"16X40",	
                                      "16X45",	 "16X50",	 "16X57",	"16X67",	"16X77",	"16X89",	"16X100",	"18X35",	"18X40",	"18X46",	
                                      "18X50",	 "18X55",	 "18X60",	"18X65",	"18X71",	"18X76",	"18X86",	"18X97",	"18X106",	"18X119",	
                                     "18X130",	"18X143",	"18X158",	"18X175",	"18x192",	"18x211",	"18x234",	"18x258",	"18x283",	"18x311",	
                                      "21X44",	 "21X50",	 "21X57",	"21X48",	"21X55",	"21X62",	"21X68",	"21X73",	"21X83",	"21X93",	
                                     "21X101",	"21X111",	"21X122",	"21X132",	"21X147",	"21X166",	"21X182",	"21X201",	"24X55",	"24X62",	
                                      "24X68",	 "24X76",	 "24X84",	"24X94",	"24X103",	"24X104",	"24X117",	"24X131",	"24X146",	"24X162",	
                                     "24X176",	"24X192",	"24X207",	"24X229",	"24X250",	"24X279",	"24X306",	"24X335",	"24X370",	"27X84",	
                                      "27X94",	"27X102",	"27X114",	"27X129",	"27X146",	"27X161",	"27X178",	"27X194",	"27X217",	"27X235",	
                                     "27X258",	"27X281",	"27X307",	"27X336",	"27X368",	"27X539",	"30X90",	"30X99",	"30X108",	"30X116",	
                                     "30X124",	"30X132",	"30X148",	"30X173",	"30X191",	"30X211",	"30X235",	"30X261",	"30X292",	"30X326",	
                                     "30X357",	"30X391",	"33X118",	"33X130",	"33X141",	"33X152",	"33X169",	"33X201",	"33X221",	"33X241",	
                                     "33X263",	"33X291",	"33X318",	"33X354",	"33X387",	"36X135",	"36X150",	"36X160",	"36X170",	"36X182",	
                                     "36X194",	"36X210",	"36X232",	"36X256",	"36X231",	"36X247",	"36X262",	"36X282",	"36X302",	"36X330",	
                                     "36X361",	"36X395",	"36X441",	"36X487",	"36X529",	"36X652",	"36X800",	"40X149",	"40X167",	"40X183",	
                                     "40X211",	"40X235",	"40X264",	"40X278",	"40X294",	"40X327",	"40X331",	"40X392",	"40X199",	"40X215",	
                                     "40X249",	"40X277",	"40X297",	"40X324",	"40X362",	"40X372",	"40X397",	"40X431",	"40X503",	"40X593",	
                                     "44X230",	"44X262",	"44X290",	"44X335"])
            
            
            self.tableWidget_DatosEntrada.setCellWidget(inx, 1, combobox1)
            self.tableWidget_DatosEntrada.setCellWidget(inx, 14, combobox2)
            self.tableWidget_DatosEntrada.setCellWidget(inx, 13, combobox0)


        
        # 2.1 Aquí lleno los imputs de inicialización
        self.lineEdit_NodosTotales.setText(str(self.parent.datos_inicializacion[0])) 
        self.lineEdit_NodosBase.setText(str(self.parent.datos_inicializacion[1]))


        # 2.2 Aquí predetermino un checkbox habilitado para el ejemplo, en este caso (D/C)        
#        self.checkBox_DC.setChecked(True)
        
        # 2.3 Aquí coloco un mensaje de aviso

        msg1 = QMessageBox()
        msg1.setWindowTitle('Aviso')
        msg1.setText('''<b>El ejemplo se ha cargado con éxito.</b>
                    <br/><br/> Presione OK para continuar.''')
        msg1.setIconPixmap(QPixmap("checks.png"))
        msg1.exec_()        
#        self.pushButtonGraficaInicio.setEnabled(True)



    # 3. Esta función da vida al botón "+" 
    def mas(self):
        # Dar funcionalidad al botón "+" añadiendo celdas.
        row = self.tableWidget_DatosEntrada.rowCount() 
        self.tableWidget_DatosEntrada.insertRow(row)      

        # Bucles para centrar widgets a lo horizontal y vertical
        for row in range(self.tableWidget_DatosEntrada.rowCount() - 1, self.tableWidget_DatosEntrada.rowCount(), 1):
            for col in range(self.tableWidget_DatosEntrada.columnCount()):
                
                # Defino el elemento contador. --------------------------------@
                count_element = QTableWidgetItem(str(self.tableWidget_DatosEntrada.rowCount()))
                count_element.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                
                # Asigno el elemento contador.
                self.tableWidget_DatosEntrada.setItem(row, 0, count_element)
                
                # Defino los "combobox's" que necesito. -----------------------@ 
                self.combobox0 = QComboBox()
                self.combobox0.addItems(['W'])

                self.combobox1 = QComboBox()
                self.combobox1.addItems(['Col', 'Vig'])

                self.combobox2 = QComboBox()
                self.combobox2.addItems([   "4X13",	  "5X16",	  "5X19",	"6X8.5",	"6X9", 	"6X12",	"6X16",	"6X15",	"6X20",	"6X25",	
                                       "8X10",	  "8X13",	  "8X15",	"8X18",	"8X21",	"8X24",	"8X28",	"8X31",	"8X35",	"8X40",	
                                       "8X48",	  "8X58",	  "8X67",	"10X12",	"10X15",	"10X17",	"10X19",	"10X22",	"10X26",	"10X30",	
                                      "10X33",	 "10X39",	 "10X45",	"10X49",	"10X54",	"10X60",	"10X68",	"10X77",	"10X88",	"10X100",	
                                     "10X112",	 "12X14",	 "12X16",	"12X19",	"12X22",	"12X26",	"12X30",	"12X35",	"12X40",	"12X45",	
                                      "12X50",	 "12X53",	 "12X58",	"12X65",	"12X72",	"12X79",	"12X87",	"12X96",	"12X106",	"12X120",	
                                     "12X136",	"12X152",	"12X170",	"12X190",	"12X210",	"12X230",	"12X252",	"12X279",	"12X305",	"12X336",	
                                      "14X22",	 "14X26",  "14X30",	"14X34",	"14X38",	"14X43",	"14X48",	"14X53",	"14X61",	"14X68",	
                                      "14X74",	 "14X82",	 "14X90",	"14X99",	"14X109",	"14X120",	"14X132",	"14X145",	"14X159",	"14X176",	
                                     "14X193",	"14X211",	"14X233",	"14X257",	"14X283",	"14X311",	"14X342",	"14X370",	"14X398",	"14X426",	
                                     "14X455",  "14X500",	"14X550",	"14X605",	"14X665",	"14X730",	"16X26",	"16X31",	"16X36",	"16X40",	
                                      "16X45",	 "16X50",	 "16X57",	"16X67",	"16X77",	"16X89",	"16X100",	"18X35",	"18X40",	"18X46",	
                                      "18X50",	 "18X55",	 "18X60",	"18X65",	"18X71",	"18X76",	"18X86",	"18X97",	"18X106",	"18X119",	
                                     "18X130",	"18X143",	"18X158",	"18X175",	"18x192",	"18x211",	"18x234",	"18x258",	"18x283",	"18x311",	
                                      "21X44",	 "21X50",	 "21X57",	"21X48",	"21X55",	"21X62",	"21X68",	"21X73",	"21X83",	"21X93",	
                                     "21X101",	"21X111",	"21X122",	"21X132",	"21X147",	"21X166",	"21X182",	"21X201",	"24X55",	"24X62",	
                                      "24X68",	 "24X76",	 "24X84",	"24X94",	"24X103",	"24X104",	"24X117",	"24X131",	"24X146",	"24X162",	
                                     "24X176",	"24X192",	"24X207",	"24X229",	"24X250",	"24X279",	"24X306",	"24X335",	"24X370",	"27X84",	
                                      "27X94",	"27X102",	"27X114",	"27X129",	"27X146",	"27X161",	"27X178",	"27X194",	"27X217",	"27X235",	
                                     "27X258",	"27X281",	"27X307",	"27X336",	"27X368",	"27X539",	"30X90",	"30X99",	"30X108",	"30X116",	
                                     "30X124",	"30X132",	"30X148",	"30X173",	"30X191",	"30X211",	"30X235",	"30X261",	"30X292",	"30X326",	
                                     "30X357",	"30X391",	"33X118",	"33X130",	"33X141",	"33X152",	"33X169",	"33X201",	"33X221",	"33X241",	
                                     "33X263",	"33X291",	"33X318",	"33X354",	"33X387",	"36X135",	"36X150",	"36X160",	"36X170",	"36X182",	
                                     "36X194",	"36X210",	"36X232",	"36X256",	"36X231",	"36X247",	"36X262",	"36X282",	"36X302",	"36X330",	
                                     "36X361",	"36X395",	"36X441",	"36X487",	"36X529",	"36X652",	"36X800",	"40X149",	"40X167",	"40X183",	
                                     "40X211",	"40X235",	"40X264",	"40X278",	"40X294",	"40X327",	"40X331",	"40X392",	"40X199",	"40X215",	
                                     "40X249",	"40X277",	"40X297",	"40X324",	"40X362",	"40X372",	"40X397",	"40X431",	"40X503",	"40X593",	
                                     "44X230",	"44X262",	"44X290",	"44X335"])

                # Asigno los "combobox's" a sus respectivos lugares en tabla
                self.tableWidget_DatosEntrada.setCellWidget(row, 1, self.combobox1)
                self.tableWidget_DatosEntrada.setCellWidget(row, 14, self.combobox2)
                self.tableWidget_DatosEntrada.setCellWidget(row, 13, self.combobox0)
                
                # Defino items x. defecto que necesito. -----------------------@
#                d12 = QTableWidgetItem(str('W'))
#                d12.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # Asigno items x. defecto que necesito.
#                self.tableWidget_DatosEntrada.setItem(row, 13, d12)                

                # Defino items vacíos. -----------------------------@
                z2 = QTableWidgetItem()
                z2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z3 = QTableWidgetItem()
                z3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z4 = QTableWidgetItem()
                z4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z5 = QTableWidgetItem()
                z5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z6 = QTableWidgetItem()
                z6.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z7 = QTableWidgetItem()
                z7.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z8 = QTableWidgetItem()
                z8.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z9 = QTableWidgetItem()
                z9.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z10 = QTableWidgetItem()
                z10.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z11 = QTableWidgetItem()
                z11.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z12 = QTableWidgetItem()
                z12.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


                # Defino items cero que necesito. -----------------------------@ 
                z15 = QTableWidgetItem(str(0))
                z15.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z16 = QTableWidgetItem(str(0))
                z16.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z17 = QTableWidgetItem(str(0))
                z17.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z18 = QTableWidgetItem(str(0))
                z18.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z19 = QTableWidgetItem(str(0))
                z19.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z20 = QTableWidgetItem(str(0))
                z20.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z21 = QTableWidgetItem(str(0))
                z21.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                z22 = QTableWidgetItem(str(0))
                z22.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#                z23 = QTableWidgetItem(str(0))
#                z23.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
#                z24 = QTableWidgetItem(str(0))
#                z24.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                # Asigno items cero que necesito.
                self.tableWidget_DatosEntrada.setItem(row, 15, z15)
                self.tableWidget_DatosEntrada.setItem(row, 16, z16)
                self.tableWidget_DatosEntrada.setItem(row, 17, z17)
                self.tableWidget_DatosEntrada.setItem(row, 18, z18)
                self.tableWidget_DatosEntrada.setItem(row, 19, z19)
                self.tableWidget_DatosEntrada.setItem(row, 20, z20)
                self.tableWidget_DatosEntrada.setItem(row, 21, z21)
                self.tableWidget_DatosEntrada.setItem(row, 22, z22)
#                self.tableWidget_DatosEntrada.setItem(row, 23, z23)
#                self.tableWidget_DatosEntrada.setItem(row, 24, z24)
                
                self.tableWidget_DatosEntrada.setItem(row, 2, z2)
                self.tableWidget_DatosEntrada.setItem(row, 3, z3)
                self.tableWidget_DatosEntrada.setItem(row, 4, z4)
                self.tableWidget_DatosEntrada.setItem(row, 5, z5)
                self.tableWidget_DatosEntrada.setItem(row, 6, z6)
                self.tableWidget_DatosEntrada.setItem(row, 7, z7)
                self.tableWidget_DatosEntrada.setItem(row, 8, z8)
                self.tableWidget_DatosEntrada.setItem(row, 9, z9)
                self.tableWidget_DatosEntrada.setItem(row, 10, z10)
                self.tableWidget_DatosEntrada.setItem(row, 11, z11)
                self.tableWidget_DatosEntrada.setItem(row, 12, z12)



    def menos(self):
        row = self.tableWidget_DatosEntrada.rowCount()
        self.tableWidget_DatosEntrada.removeRow(row - 1)


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


    def info(self):
        # Instanciamos la clase QMessageBox
        msgi = QMessageBox(self)
        msgi.setWindowTitle("Información")
        msgi.setIcon(QMessageBox.Information)
        msgi.setText("<b>Información de recomendación</b>")
        
        msgi.setText('''<p>Se recomienda que tu estructura no sea mayor a 6 pisos, estamos en sistemas OMF, más allá de eso el proceso de optimización podría tardar mas tiempo.</p>
                    <br/><br/> Puede ver más información <a href='https://www.facebook.com/danielalexander.villarreal'>aquí.</a>''')
        msgi.exec_()   

        
    def dataframe_gen(self, table):
        try:

            num_rows = table.rowCount()
            datos_locales = []
            for i in range(num_rows):
                datos_locales.append([int(table.item(i,0).text()),table.cellWidget(i, 1).currentText(),int(table.item(i,2).text()),
                                      int(table.item(i,3).text()),int(table.item(i,4).text()),int(table.item(i,5).text()),
                                      int(table.item(i,6).text()),int(table.item(i,7).text()),int(table.item(i,8).text()),
                                      float(table.item(i,9).text()),float(table.item(i,10).text()),float(table.item(i,11).text()),
                                      float(table.item(i,12).text()),table.cellWidget(i, 13).currentText(),table.cellWidget(i, 14).currentText(),    #table.item(i,13).text()
                                      int(table.item(i,15).text()),int(table.item(i,16).text()),int(table.item(i,17).text()),
                                      int(table.item(i,18).text()),int(table.item(i,19).text()),int(table.item(i,20).text()),
                                      int(table.item(i,21).text()),int(table.item(i,22).text())])
    
            datos_frame = pd.DataFrame(datos_locales,columns=('Elemento', 'Tipo', 'Piso','X(i)', 'Y(i)', '⟲(i)','X(j)', 'Y(j)', '⟲(j)','x(i)','y(i)', 'x(j)', 'y(j)','14', '15', '16',
                                                                     '17', '18', '19','20','21', '22', '23'))

        except (ValueError):
            QMessageBox.warning(self, 'Aviso', 'Debe ingresar valores numéricos, por favor correjir')

        return datos_frame


    def graficainicio(self):
        
        self.parent.DatosPrincipales = self.dataframe_gen(self.tableWidget_DatosEntrada) # GUARDO EN LA VARIABLE PARENT, PARA USAR ESTOS DATOS DONDE QUIERA, IMPORTANTE
                                                                                         # Hacer esto donde crea necesario.
                                                                                        
        self.ingreso_datos = ingreso_de_datos_excel(self.parent.DatosPrincipales)       # Luego se ingresarán los datos.
        
        self.x = []
        self.y = []
        self.fig = plt.figure(figsize=(8,8))
        self.ax = self.fig.add_subplot(1, 1, 1)  

        for i in range(len(self.ingreso_datos)): 
        
            self.xi = self.ingreso_datos[i][9]
            self.yi = self.ingreso_datos[i][10]
            self.xf = self.ingreso_datos[i][11]
            self.yf = self.ingreso_datos[i][12]     

            self.wd_height = 0
            if abs(self.ingreso_datos[i][15])/10000 > 1:
                self.wd_height = abs(self.ingreso_datos[i][15])/100000
         
            elif abs(self.ingreso_datos[i][15])/10000 > 10:
                self.wd_height = abs(self.ingreso_datos[i][15])/1000000
        
            elif abs(self.ingreso_datos[i][15])/10000 < 0.1:
                self.wd_height = abs(self.ingreso_datos[i][15])/1000
            else:
                self.wd_height = abs(self.ingreso_datos[i][15])/10000         
                
            self.p_height = abs(self.ingreso_datos[i][16])/10000
            
            self.lateral_height = abs(self.ingreso_datos[i][21])/1000
            
            self.space = 1
    #        arrows = ((self.ingreso_datos[i][11] - self.ingreso_datos[i][9])/space)+1    
        
            self.slope = 0
            if self.ingreso_datos[i][1] == 'Vig':
                self.slope = (self.yf-self.yi)/(self.xf-self.xi)
 
            self.x.append(self.ingreso_datos[i][11])
            self.y.append(self.ingreso_datos[i][12])
            self.AreaRejilla = max(max(self.x), max(self.y))
        
#            self.major_ticks = np.arange(-30, self.AreaRejilla+20, 1)
#            self.minor_ticks = np.arange(-30, self.AreaRejilla+20, 0.25)
            
#            self.ax.set_xticks(self.major_ticks)
#            self.ax.set_xticks(self.minor_ticks, minor=True)
#            self.ax.set_yticks(self.major_ticks)
#            self.ax.set_yticks(self.minor_ticks, minor=True)
            
            # Añado el correspondiente grid
            self.ax.grid(which='both')
            
#            self.ax.grid(which='minor', alpha=0.2)
#            self.ax.grid(which='major', alpha=0.5)
            
            # Añado etiquetas a la gráfica:
            plt.title('Vista Previa del Modelo\nPórtico 2D\n',fontsize=14, fontweight='bold')
            plt.xlabel(r"$\bf{" + 'Longitud\,(m)' + "}$\n\n${Elaborado\,\,por:\,Daniel\,\,Villarreal\,\,Leiva}$")
    
            plt.ylabel('Altura (m)', fontweight='bold')
            plt.axis('equal')
        
            plt.plot((self.xi, self.xf), (self.yi, self.yf),  color='black' if self.ingreso_datos[i][1] == "Col" else "gray", linewidth=4)             


            self.anotations = plt.annotate(f"Elemento: {self.ingreso_datos[i][1]} {self.ingreso_datos[i][0]}\nPerfil {self.ingreso_datos[i][13]} - {self.ingreso_datos[i][14]}",
                         xy=(self.xi + (self.xf - self.xi) / 2, self.yi + (self.yf - self.yi) / 2), #--> Mis anotaciones estarán en medio de la línea
                         textcoords="offset points", #--> Junto con la línea anterior, me ubica en medio de la línea
                         xytext= (0, -15) if self.ingreso_datos[i][1] == "Vig" else (5, 0), #--> Ajusta la ubicación del texto
                         ha='center' if self.ingreso_datos[i][1] == "Vig" else "left", 
                         va="center")
            self.anotations.set_fontsize(9)
        
            if self.slope == 0:
        
                #Cargas Distribuidas
                if self.ingreso_datos[i][1] == 'Vig' and abs(self.ingreso_datos[i][15]) > 0:
                    plt.plot((self.xi, self.xf), (self.yi+self.wd_height, self.yf+self.wd_height), color='green', linewidth=1) 
            
                    for self.xj in np.arange(self.xi, self.xf + 1e-9, self.space):
                        plt.arrow(self.xj, self.yi + self.wd_height, 0, -self.wd_height, color='green', linewidth=1,
                                  length_includes_head=True, head_width=0.1, head_length=0.1)
            
                    anotations = plt.annotate(f"WD = {self.ingreso_datos[i][15]} kgf/m", xy=(self.xi + (self.xf - self.xi) / 2, self.yi + self.wd_height + (self.yf + self.wd_height - self.yi) / 2), 
                                 textcoords="offset points", xytext= (0, 0), ha='center', va="center")
    
                    anotations.set_fontsize(9)
                    
                #Cargas Laterales
                if self.ingreso_datos[i][1] == 'Vig' and abs(self.ingreso_datos[i][21]) > 0:
                    anotations = plt.annotate(f"SX = {round(self.ingreso_datos[i][21],3)} kgf", xy=(self.xi,self.yi), 
                                 textcoords="offset points", xytext= (-60, -10), ha='center', va="center")        
      
                    anotations.set_fontsize(9)
                  
                    plt.arrow(self.xi-self.lateral_height, self.yi, self.lateral_height, 0,color='red', linewidth=1, 
                              length_includes_head=True, head_width=0.1, head_length=0.1)  
            
                # Puntuales    
                if self.ingreso_datos[i][1] == 'Vig' and abs(self.ingreso_datos[i][16]) > 0:
            
                    plt.arrow((self.xj-self.xi)/2, self.yi + self.p_height, 0, -self.p_height, color='magenta', linewidth=2, length_includes_head=True, head_width=0.1, head_length=0.1)    
            
                    anotations = plt.annotate(f"P = {self.ingreso_datos[i][16]} kgf", xy=(self.xi + (self.xf - self.xi) / 2, self.yi + self.wd_height + (self.yf + self.wd_height - self.yi) / 2), 
                                 textcoords="offset points", xytext= (0, 10), ha='center', va="center")  
    
                    anotations.set_fontsize(9)                
            else:
                None

        
        plt.show() # -------------------------------------------------------------@


    def analisisdisenio(self):
        
        # 8.1 Mensaje de aviso.
        

        # 8.2 Datos para la ejecución, observar la función principal del proceso.
        # ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        
        '''Nota: Es importante tener el proceso organizado para establecer esto.'''

        try:
        
            my_console = Logger('src_calculos/data.txt') 
            
            self.parent.DatosPrincipales = self.dataframe_gen(self.tableWidget_DatosEntrada) # GUARDO EN LA VARIABLE PARENT, PARA USAR ESTOS DATOS DONDE QUIERA, IMPORTANTE
                                                                                             # Hacer esto donde crea necesario.

            print(self.parent.DatosPrincipales.to_string(index=False , header=False))

            my_console.close()

            self.ExcelPrincipal = self.parent.ExcelPrincipal
            
            self.DatosPrincipales = self.parent.DatosPrincipales

            self.D_nodos_totales = int(self.lineEdit_NodosTotales.text())



            self.D_nodos_restringidos = int(self.lineEdit_NodosBase.text()) 


        
            self.D_criterio = 0
            
            self.D_optimizator = 0 # -----> Este dato es inherente al botón de analisis y disenio.
            self.parent.D_optimizator = self.D_optimizator
    
    
            self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)
            self.parent.ingreso_datos = self.ingreso_datos # GUARDO EN LA VARIABLE PARENT, PARA USAR ESTOS DATOS DONDE QUIERA, IMPORTANTE
    
            
            if self.D_criterio == 0:
                
                detallado(self.ExcelPrincipal, [], self.ingreso_datos, self.D_optimizator, [],  self.D_nodos_totales, self.D_nodos_restringidos, self.D_criterio)
                
#                frame(self.ingreso_datos)

                msg = QMessageBox()
                msg.setWindowTitle('Mensaje de aviso')
                msg.setText('''<b>El proceso se ha ejecutado correctamente, proceda ahora a ver resultados...</b>
                            <br/><br/> Presione OK para continuar.''')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

        except (ValueError):
            QMessageBox.warning(self, 'Aviso', 'Aún no ha ingresado correctamente todos los datos, por favor proceda.')
            
        self.parent.actionResultados.setEnabled(True)
            
    def optimization(self):

        my_console = Logger('src_calculos/data.txt') 
        
        self.parent.DatosPrincipales = self.dataframe_gen(self.tableWidget_DatosEntrada) # GUARDO EN LA VARIABLE PARENT, PARA USAR ESTOS DATOS DONDE QUIERA, IMPORTANTE
                                                                                         # Hacer esto donde crea necesario.        

        print(self.parent.DatosPrincipales.to_string(index=False , header=False))
        
        my_console.close()
        
        self.is_sending_data = True
        

        self.ExcelPrincipal = self.parent.ExcelPrincipal
        self.Perfil_Data = self.parent.ExcelPrincipal.parse('W') 
        
        self.DatosPrincipales = self.parent.DatosPrincipales
        
        self.D_nodos_totales = int(self.lineEdit_NodosTotales.text())
        self.D_nodos_restringidos = int(self.lineEdit_NodosBase.text()) 
        
        self.D_criterio = 0
        
        self.D_optimizator = 1 # -----> Este dato es inherente al botón de analisis y disenio.
        self.parent.D_optimizator = self.D_optimizator



        self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)
        self.parent.ingreso_datos = self.ingreso_datos # GUARDO EN LA VARIABLE PARENT, PARA USAR ESTOS DATOS DONDE QUIERA, IMPORTANTE
                                                       # Luego la voy a usar como argumento de otra función definida en otra clase.



        if self.D_criterio == 0:

            self.lista_final_pv_bajo, self.lista_final_p_bajo, self.perfiles_aprobados, self.lista_los_mejores, self.lista_minimo_peso_variabilidad, self.Opcion_pesominimo, self.parent.lista_Peso_estructural, self.ingreso_datos = optimalframe(self.D_optimizator, self.D_criterio, self.D_nodos_totales, self.D_nodos_restringidos, self.ExcelPrincipal, self.DatosPrincipales, self.Perfil_Data)
 
#            graph_objetive(self.parent.lista_Peso_estructural)
            self.is_sending_data = False # Aquí finalizo el hilo de ejecución -----
         
            # Para el A 

#            self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)

            self.parent.ingreso_datos_a = ingr_actual_a(self.lista_los_mejores, self.lista_final_pv_bajo, self.lista_minimo_peso_variabilidad, self.ingreso_datos)
            
            detallado_a(self.lista_los_mejores, self.ExcelPrincipal, self.lista_final_pv_bajo, self.parent.ingreso_datos_a, self.D_optimizator, self.perfiles_aprobados,  self.D_nodos_totales, self.D_nodos_restringidos, self.D_criterio, self.lista_minimo_peso_variabilidad)
    
#            frame_a(self.parent.ingreso_datos_a)


            # Para el B 

#            self.ingreso_datos = ingreso_de_datos_excel(self.DatosPrincipales)

            self.parent.ingreso_datos_b = ingr_actual_b(self.lista_los_mejores, self.lista_final_p_bajo, self.Opcion_pesominimo, self.ingreso_datos)

            detallado_b(self.lista_los_mejores, self.ExcelPrincipal, self.lista_final_p_bajo, self.ingreso_datos, self.D_optimizator, self.perfiles_aprobados,  self.D_nodos_totales, self.D_nodos_restringidos, self.D_criterio, self.Opcion_pesominimo)

#            frame_b(self.parent.ingreso_datos_b)

#        self.is_sending_data = False # Aquí finalizo el hilo de ejecución -----

        self.parent.actionResultados.setEnabled(True)
            

    def open_info_image(self):
        InfoImage(self).show()      
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DataInput()
    widget.show()
    sys.exit(app.exec_())    
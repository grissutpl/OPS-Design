# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subDinamic_DataInput.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui/transparent.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_NodosTotales = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_NodosTotales.setObjectName("lineEdit_NodosTotales")
        self.verticalLayout.addWidget(self.lineEdit_NodosTotales)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_NodosBase = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_NodosBase.setObjectName("lineEdit_NodosBase")
        self.verticalLayout.addWidget(self.lineEdit_NodosBase)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 2, 1)
        self.tableWidget_DatosEntrada = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_DatosEntrada.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_DatosEntrada.setFont(font)
        self.tableWidget_DatosEntrada.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_DatosEntrada.setAlternatingRowColors(True)
        self.tableWidget_DatosEntrada.setObjectName("tableWidget_DatosEntrada")
        self.tableWidget_DatosEntrada.setColumnCount(23)
        self.tableWidget_DatosEntrada.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_DatosEntrada.setHorizontalHeaderItem(22, item)
        self.tableWidget_DatosEntrada.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget_DatosEntrada.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_DatosEntrada.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout_2.addWidget(self.tableWidget_DatosEntrada, 1, 1, 6, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 310, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 498, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 4, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 7, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonGraficaInicio = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonGraficaInicio.setEnabled(True)
        self.pushButtonGraficaInicio.setObjectName("pushButtonGraficaInicio")
        self.gridLayout_4.addWidget(self.pushButtonGraficaInicio, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 2, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonMenos = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonMenos.setObjectName("pushButtonMenos")
        self.gridLayout.addWidget(self.pushButtonMenos, 1, 0, 1, 1)
        self.pushButtonMas = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonMas.setObjectName("pushButtonMas")
        self.gridLayout.addWidget(self.pushButtonMas, 0, 0, 1, 1)
        self.pushButtonEjemplo = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonEjemplo.setObjectName("pushButtonEjemplo")
        self.gridLayout.addWidget(self.pushButtonEjemplo, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonAnalisisDiseno = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonAnalisisDiseno.setObjectName("pushButtonAnalisisDiseno")
        self.gridLayout_3.addWidget(self.pushButtonAnalisisDiseno, 0, 0, 1, 1)
        self.pushButtonOptimizacion = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonOptimizacion.setEnabled(True)
        self.pushButtonOptimizacion.setObjectName("pushButtonOptimizacion")
        self.gridLayout_3.addWidget(self.pushButtonOptimizacion, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 6, 2, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_4.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:15px")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButtonAyuda = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAyuda.setFont(font)
        self.pushButtonAyuda.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:0px;\n"
"border-radius:15px\n"
"")
        self.pushButtonAyuda.setAutoDefault(False)
        self.pushButtonAyuda.setFlat(False)
        self.pushButtonAyuda.setObjectName("pushButtonAyuda")
        self.gridLayout_7.addWidget(self.pushButtonAyuda, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 2)
        self.toolButton_Story = QtWidgets.QToolButton(self.groupBox_8)
        self.toolButton_Story.setObjectName("toolButton_Story")
        self.gridLayout_6.addWidget(self.toolButton_Story, 2, 1, 1, 1)
        self.toolButton_visor = QtWidgets.QToolButton(self.groupBox_8)
        self.toolButton_visor.setObjectName("toolButton_visor")
        self.gridLayout_6.addWidget(self.toolButton_visor, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_8)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 5, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OPS Design"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Initialization"))
        self.label_2.setText(_translate("MainWindow", "Total nodes \n"
"in the structure"))
        self.label_3.setText(_translate("MainWindow", "Total \n"
"base nodes"))
        self.label_5.setText(_translate("MainWindow", "Optimization: D/C"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Element"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type \n"
"Element"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Floor"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "GDL_1\n"
"\n"
"\n"
"(initial)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "GDL_2\n"
"\n"
"\n"
"(initial)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GDL_3 \n"
"\n"
"\n"
"(initial)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "GDL_1 \n"
"\n"
"\n"
"(final)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GDL_2 \n"
"\n"
"\n"
"(final)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GDL_3 \n"
"\n"
"\n"
"(final)"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "X_initial\n"
"\n"
"\n"
"[m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Y_initial\n"
"\n"
"\n"
"[m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "X_final\n"
"\n"
"\n"
"[m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Y_final\n"
"\n"
"\n"
"[m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Steel\n"
"Shape\n"
"\n"
""))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Cross \n"
"Section\n"
"Specific\n"
""))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Distributed\n"
"Loads\n"
"\n"
"[kgf/m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Center\n"
"Point Load\n"
"\n"
"[kgf]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Moment\n"
"Initial Node\n"
"\n"
"[kgf*m]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "\n"
"Moment\n"
"Initial Node\n"
"\n"
"[kgf*m]\n"
""))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "⊥\n"
"P.L. Initial\n"
"Node\n"
"[kgf]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "⊥\n"
"P.L. Final\n"
"Node\n"
"[kgf]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Axial\n"
"Initial \n"
"Node\n"
"[kgf]"))
        item = self.tableWidget_DatosEntrada.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "Axial\n"
"Final \n"
"Node\n"
"[kgf]"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">INPUT DATA: GEOMETRY, SECTIONS Y LOADS TO THE MODEL.</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Units: kgf - m - sec</p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Visualization"))
        self.pushButtonGraficaInicio.setText(_translate("MainWindow", "Preview"))
        self.pushButtonMenos.setText(_translate("MainWindow", "-"))
        self.pushButtonMas.setText(_translate("MainWindow", "+"))
        self.pushButtonEjemplo.setText(_translate("MainWindow", "Load example"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Run Model"))
        self.pushButtonAnalisisDiseno.setText(_translate("MainWindow", "Analysis and\n"
"Design"))
        self.pushButtonOptimizacion.setText(_translate("MainWindow", "Structural\n"
"Optimization"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Information"))
        self.pushButtonAyuda.setText(_translate("MainWindow", "Guide and Blog"))
        self.toolButton_Story.setText(_translate("MainWindow", "!!"))
        self.toolButton_visor.setText(_translate("MainWindow", "I"))
        self.label_4.setText(_translate("MainWindow", "Limitations"))
        self.label_7.setText(_translate("MainWindow", "Perfil Viewer"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subDinamic_Result.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1233, 762)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui/transparent.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonGraficaOneTime = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonGraficaOneTime.setObjectName("pushButtonGraficaOneTime")
        self.gridLayout_6.addWidget(self.pushButtonGraficaOneTime, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 1, 4, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 3, 0, 1, 1)
        self.toolButton_tbuni_one = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_tbuni_one.setObjectName("toolButton_tbuni_one")
        self.gridLayout_10.addWidget(self.toolButton_tbuni_one, 2, 1, 1, 1)
        self.toolButton_tbcef_one = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_tbcef_one.setObjectName("toolButton_tbcef_one")
        self.gridLayout_10.addWidget(self.toolButton_tbcef_one, 3, 1, 1, 1)
        self.toolButton_tbdis_one = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_tbdis_one.setObjectName("toolButton_tbdis_one")
        self.gridLayout_10.addWidget(self.toolButton_tbdis_one, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 2, 0, 1, 1)
        self.toolButton_tban_one = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_tban_one.setObjectName("toolButton_tban_one")
        self.gridLayout_10.addWidget(self.toolButton_tban_one, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.toolButton_visor_Ra = QtWidgets.QToolButton(self.groupBox_9)
        self.toolButton_visor_Ra.setObjectName("toolButton_visor_Ra")
        self.gridLayout_11.addWidget(self.toolButton_visor_Ra, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_5.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:15px")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButtonAyuda_Ra = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAyuda_Ra.setFont(font)
        self.pushButtonAyuda_Ra.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:0px;\n"
"border-radius:15px\n"
"")
        self.pushButtonAyuda_Ra.setAutoDefault(False)
        self.pushButtonAyuda_Ra.setFlat(False)
        self.pushButtonAyuda_Ra.setObjectName("pushButtonAyuda_Ra")
        self.gridLayout_12.addWidget(self.pushButtonAyuda_Ra, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_5, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_9, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_op2 = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.radioButton_op2.setFont(font)
        self.radioButton_op2.setObjectName("radioButton_op2")
        self.gridLayout_2.addWidget(self.radioButton_op2, 3, 0, 1, 1)
        self.radioButton_op1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_op1.setObjectName("radioButton_op1")
        self.gridLayout_2.addWidget(self.radioButton_op1, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_3.addWidget(self.textBrowser_3, 1, 1, 5, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButtonGrafica_pesos = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonGrafica_pesos.setObjectName("pushButtonGrafica_pesos")
        self.gridLayout_7.addWidget(self.pushButtonGrafica_pesos, 0, 0, 1, 1)
        self.pushButtonGraficaIteration = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonGraficaIteration.setObjectName("pushButtonGraficaIteration")
        self.gridLayout_7.addWidget(self.pushButtonGraficaIteration, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)
        self.toolButton_tban_iter = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_tban_iter.setObjectName("toolButton_tban_iter")
        self.gridLayout_5.addWidget(self.toolButton_tban_iter, 0, 4, 1, 1)
        self.toolButton_tbdis_iter = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_tbdis_iter.setObjectName("toolButton_tbdis_iter")
        self.gridLayout_5.addWidget(self.toolButton_tbdis_iter, 1, 4, 1, 1)
        self.toolButton_tbuni_iter = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_tbuni_iter.setObjectName("toolButton_tbuni_iter")
        self.gridLayout_5.addWidget(self.toolButton_tbuni_iter, 2, 4, 1, 1)
        self.toolButton_tbcef_iter = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_tbcef_iter.setObjectName("toolButton_tbcef_iter")
        self.gridLayout_5.addWidget(self.toolButton_tbcef_iter, 3, 4, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.toolButton_visor_Rb = QtWidgets.QToolButton(self.groupBox_10)
        self.toolButton_visor_Rb.setObjectName("toolButton_visor_Rb")
        self.gridLayout_13.addWidget(self.toolButton_visor_Rb, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setObjectName("label_14")
        self.gridLayout_13.addWidget(self.label_14, 2, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_8.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-radius:15px")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setFlat(False)
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButtonAyuda_Rb = QtWidgets.QPushButton(self.groupBox_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonAyuda_Rb.setFont(font)
        self.pushButtonAyuda_Rb.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"color:withe;\n"
"border-style: outset;\n"
"border-width:0px;\n"
"border-radius:15px\n"
"")
        self.pushButtonAyuda_Rb.setAutoDefault(False)
        self.pushButtonAyuda_Rb.setFlat(False)
        self.pushButtonAyuda_Rb.setObjectName("pushButtonAyuda_Rb")
        self.gridLayout_14.addWidget(self.pushButtonAyuda_Rb, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_8, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_10, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 235, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OPS Design"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DESIGN AND ANALYSIS RESULTS - [INITIALIZATION SECTIONS]</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plotting Graphics"))
        self.pushButtonGraficaOneTime.setText(_translate("MainWindow", "Frame"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Specific Details"))
        self.label_7.setText(_translate("MainWindow", "C.E.M."))
        self.toolButton_tbuni_one.setText(_translate("MainWindow", "..."))
        self.toolButton_tbcef_one.setText(_translate("MainWindow", "..."))
        self.toolButton_tbdis_one.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Analysis"))
        self.label_5.setText(_translate("MainWindow", "Design"))
        self.label_6.setText(_translate("MainWindow", "Joints"))
        self.toolButton_tban_one.setText(_translate("MainWindow", "..."))
        self.groupBox_9.setTitle(_translate("MainWindow", "Information"))
        self.toolButton_visor_Ra.setText(_translate("MainWindow", "I"))
        self.label_13.setText(_translate("MainWindow", "Profile viewer"))
        self.pushButtonAyuda_Ra.setText(_translate("MainWindow", "Guide and Blog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Simple Engine"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DESIGN AND ANALYSIS RESULTS - [OPTIMIZED SECTIONS]</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Representative Designs"))
        self.radioButton_op2.setText(_translate("MainWindow", "Option B"))
        self.radioButton_op1.setText(_translate("MainWindow", "Option A"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Plotting Graphics"))
        self.pushButtonGrafica_pesos.setText(_translate("MainWindow", "Objetive Function"))
        self.pushButtonGraficaIteration.setText(_translate("MainWindow", "Frame"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Specific Details"))
        self.label_8.setText(_translate("MainWindow", "Analysis"))
        self.label_10.setText(_translate("MainWindow", "Joints"))
        self.label_9.setText(_translate("MainWindow", "Design"))
        self.label_11.setText(_translate("MainWindow", "C.E.M."))
        self.toolButton_tban_iter.setText(_translate("MainWindow", "..."))
        self.toolButton_tbdis_iter.setText(_translate("MainWindow", "..."))
        self.toolButton_tbuni_iter.setText(_translate("MainWindow", "..."))
        self.toolButton_tbcef_iter.setText(_translate("MainWindow", "..."))
        self.groupBox_10.setTitle(_translate("MainWindow", "Information"))
        self.toolButton_visor_Rb.setText(_translate("MainWindow", "I"))
        self.label_14.setText(_translate("MainWindow", "Perfil Viewer"))
        self.pushButtonAyuda_Rb.setText(_translate("MainWindow", "Guide and Blog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Optimization Engine"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Units: kgf - m - sec<span style=\" color:#ffffff;\">.</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

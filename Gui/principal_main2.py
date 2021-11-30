# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal_main2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1564, 675)
        MainWindow.setMinimumSize(QtCore.QSize(1208, 675))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.setWindowIcon(QtGui.QIcon('ops_icon.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea_Container1 = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea_Container1.setObjectName("mdiArea_Container1")
        self.gridLayout.addWidget(self.mdiArea_Container1, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1564, 26))
        self.menubar.setObjectName("menubar")
        
        
        
        self.menuDatos = QtWidgets.QMenu(self.menubar)
        self.menuDatos.setObjectName("menuDatos")
        
        
        
        self.menuResultados = QtWidgets.QMenu(self.menubar)
        self.menuResultados.setObjectName("menuResultados")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        self.menuVisor_de_Perfiles = QtWidgets.QMenu(self.menuAcerca_de)
        self.menuVisor_de_Perfiles.setObjectName("menuVisor_de_Perfiles")
        MainWindow.setMenuBar(self.menubar)
        self.actionNuevoModelo = QtWidgets.QAction(MainWindow)
        self.actionNuevoModelo.setObjectName("actionNuevoModelo")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        
        
        self.actionDatosDeEntrada = QtWidgets.QAction(MainWindow)
        self.actionDatosDeEntrada.setObjectName("actionDatosDeEntrada")
        
#        self.actionClean = QtWidgets.QAction(MainWindow) 
#        self.actionClean.setObjectName("actionClean")

        
        self.actionResultados = QtWidgets.QAction(MainWindow)
        self.actionResultados.setEnabled(False)
        self.actionResultados.setObjectName("actionResultados")
        self.actionDise_o_A = QtWidgets.QAction(MainWindow)
        self.actionDise_o_A.setObjectName("actionDise_o_A")
        self.actionDise_o_B = QtWidgets.QAction(MainWindow)
        self.actionDise_o_B.setObjectName("actionDise_o_B")
        self.actionProceso_optimizador = QtWidgets.QAction(MainWindow)
        self.actionProceso_optimizador.setObjectName("actionProceso_optimizador")
        self.actionanalisis1 = QtWidgets.QAction(MainWindow)
        self.actionanalisis1.setObjectName("actionanalisis1")
        self.actionanalisis2 = QtWidgets.QAction(MainWindow)
        self.actionanalisis2.setObjectName("actionanalisis2")
        self.actionProcesouniones1 = QtWidgets.QAction(MainWindow)
        self.actionProcesouniones1.setObjectName("actionProcesouniones1")
        self.actionProcesouniones2 = QtWidgets.QAction(MainWindow)
        self.actionProcesouniones2.setObjectName("actionProcesouniones2")
        self.actionDesglose = QtWidgets.QAction(MainWindow)
        self.actionDesglose.setObjectName("actionDesglose")
        self.actionOPS_Design = QtWidgets.QAction(MainWindow)
        self.actionOPS_Design.setObjectName("actionOPS_Design")
        self.actionSalir_2 = QtWidgets.QAction(MainWindow)
        self.actionSalir_2.setObjectName("actionSalir_2")
        self.actionSecciones_W = QtWidgets.QAction(MainWindow)
        self.actionSecciones_W.setObjectName("actionSecciones_W")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        
        
        self.menuDatos.addAction(self.actionDatosDeEntrada)
        self.menuDatos.addAction(self.actionLoad)
        self.menuDatos.addAction(self.actionSave)
        self.menuDatos.addSeparator()
#        self.menuDatos.addAction(self.actionClean)
        self.menuDatos.addAction(self.actionSalir_2)
        
        
        
        self.menuResultados.addAction(self.actionResultados)
        self.menuVisor_de_Perfiles.addAction(self.actionSecciones_W)
        self.menuAcerca_de.addAction(self.actionOPS_Design)
        self.menuAcerca_de.addAction(self.menuVisor_de_Perfiles.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuResultados.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OPS Design"))
        
        
        self.menuDatos.setTitle(_translate("MainWindow", "Data"))
        
        
        self.menuResultados.setTitle(_translate("MainWindow", "Show"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "About..."))
        self.menuVisor_de_Perfiles.setTitle(_translate("MainWindow", "Profile Viewer"))
        self.actionNuevoModelo.setText(_translate("MainWindow", "Nuevo Modelo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionDatosDeEntrada.setText(_translate("MainWindow", "Data input and initialization"))
        self.actionResultados.setText(_translate("MainWindow", "Results"))
        self.actionDise_o_A.setText(_translate("MainWindow", "Diseño A"))
        self.actionDise_o_B.setText(_translate("MainWindow", "Diseño B"))
        self.actionProceso_optimizador.setText(_translate("MainWindow", "Proceso optimizador"))
        self.actionanalisis1.setText(_translate("MainWindow", "analisis1"))
        self.actionanalisis2.setText(_translate("MainWindow", "analisis2"))
        self.actionProcesouniones1.setText(_translate("MainWindow", "Procesouniones1"))
        self.actionProcesouniones2.setText(_translate("MainWindow", "Procesouniones2"))
        self.actionDesglose.setText(_translate("MainWindow", "Desglose"))
        self.actionOPS_Design.setText(_translate("MainWindow", "OPS Design"))
        
#        self.actionClean.setText(_translate("MainWindow", "Clean"))        
        self.actionSalir_2.setText(_translate("MainWindow", "Exit"))
        
        
        self.actionSecciones_W.setText(_translate("MainWindow", "W Sections"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


from Gui import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

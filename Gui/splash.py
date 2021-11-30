# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 515)
        MainWindow.setMinimumSize(QtCore.QSize(853, 515))
        MainWindow.setMaximumSize(QtCore.QSize(853, 515))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_description = QtWidgets.QLabel(self.centralwidget)
        self.label_description.setGeometry(QtCore.QRect(10, 490, 801, 16))
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 450, 831, 41))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"    border-radius: 10px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(220, 119, 17, 255))\n"
"\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 440, 871, 81))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 871, 20))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_Image = QtWidgets.QLabel(self.centralwidget)
        self.label_Image.setGeometry(QtCore.QRect(-10, -10, 871, 481))
        self.label_Image.setStyleSheet("image: url(:/newPrefix/iconoventana.jpg);")
        self.label_Image.setText("")
        self.label_Image.setObjectName("label_Image")
        self.label_Image.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.label_description.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_description.setText(_translate("MainWindow", "TextLabel"))


from Gui import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

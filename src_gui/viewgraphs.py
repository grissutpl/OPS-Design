# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

from os import listdir
from os.path import isfile, join



# C L A S S   
# ¯¯¯¯¯¯¯¯¯

class InfoImage(QDialog):

    def __init__(self, parent=None):
        super(InfoImage,self).__init__(parent)
        loadUi('Gui/images_viewer.ui', self)
        self.setImages()
        self.pushButton.clicked.connect(self.previousImage)
        self.pushButton_2.clicked.connect(self.nextImage)
        self.listWidget.currentItemChanged.connect(self.itemChange)
        
    def setImages(self):
        #Get all the file names
        self.mypath = "Images/"
        imageFiles = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        self.listImages = imageFiles
        try:
            for i in imageFiles:
                imageName = i.split(".")[0]
                self.listWidget.addItem(imageName)
        
            #Set first image
            self.pixmap = QPixmap(self.mypath + imageFiles[0]) 
            self.label.setPixmap(self.pixmap)
            self.listWidget.setCurrentRow(0)
        except Exception as e:
            pass
            
    
    def itemChange(self, item):
        try:
            self.pixmap = QPixmap(self.mypath + self.listImages[self.listWidget.currentRow()]) 
            self.label.setPixmap(self.pixmap)
        except Exception as e:
            pass
    def previousImage(self):
        try:
            if(self.listWidget.currentRow() != 0):
                self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)
                self.pixmap = QPixmap(self.mypath + self.listImages[self.listWidget.currentRow()]) 
                self.label.setPixmap(self.pixmap)
        except Exception as e:
            pass
    def nextImage(self):
        try:
            if(self.listWidget.currentRow() != len(self.listImages)-1):
                self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)
                self.pixmap = QPixmap(self.mypath + self.listImages[self.listWidget.currentRow()]) 
                self.label.setPixmap(self.pixmap)
        except Exception as e:
            pass

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = InfoImage()
    widget.show()
    sys.exit(app.exec_())    

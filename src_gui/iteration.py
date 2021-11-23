# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys
import time
from threading import Thread # Procesos en paralelo

from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtWidgets import QApplication, QFileDialog, QStyleFactory, QMainWindow
from PyQt5.uic import loadUi


# C L A S E    D E    L A    E J E C U C I Ó N    E N    P A R A L E L O    (H I L O    D E    E J E C U C I Ó N)
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class Helper(QObject):
    send_signal = pyqtSignal(str)
    data_signal = pyqtSignal(list)


helper = Helper()
helper2 = Helper()

# C L A S E    D E    L A    S U B V E N T A N A    D E    I T E R A T I O N
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class Iterations(QMainWindow):

    def __init__(self, parent=None):
        super(Iterations,self).__init__(parent)
        loadUi('Gui/iteration.ui', self)
        self.parent = parent
        
        # Antes de formar parte del proceso en paralelo

#        self.text = open('src_calculos/files/optimice_motor.txt', "r", encoding="utf-8").read()
#        self.textBrowser_A.setText(self.text)  
        
        # Después de formar parte del proceso en paralelo

        #self.text = open('src_calculos/files/optimice_motor.txt', "r", encoding="utf-8").read()
        thread_leer = Thread(target = self.hilo_getText)
        #print(self.parent.is_sending_data)
        #helper3.send_signal.connect(self.parent.is_sending_data, Qt.QueuedConnection)
        helper2.send_signal.connect(self.textBrowser_A.clear, Qt.QueuedConnection)
        helper.send_signal.connect(self.textBrowser_A.append, Qt.QueuedConnection)
        thread_leer.start()
        #self.isSending = 
        #self.textBrowser_A.setText(self.text)        

    def hilo_getText(self):
        while(self.parent.is_sending_data):#helper3.send_signal.emit()):
            helper2.send_signal.emit("")
            self.print_text()
            time.sleep(1.3)
        helper2.send_signal.emit("")
        self.print_text()


    def print_text(self):
        self.text = open('src_calculos/files/optimice_motor.txt', "r", encoding="utf-8").read()
        helper.send_signal.emit(self.text)
        #self.textBrowser_A.setText(self.text)         
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Iterations()
#    widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    widget.show()
    sys.exit(app.exec_()) 
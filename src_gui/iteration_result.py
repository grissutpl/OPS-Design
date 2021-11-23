# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


# C L A S E    D E    L A    E J E C U C I Ó N    E N    P A R A L E L O    (H I L O    D E    E J E C U C I Ó N)
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# C L A S E    D E    L A    S U B V E N T A N A    D E    I T E R A T I O N
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

class Iterations_result(QMainWindow):

    def __init__(self, parent=None):
        super(Iterations_result,self).__init__(parent)
        loadUi('Gui/iteration_result.ui', self)
        self.parent = parent
        
        # Antes de formar parte del proceso en paralelo

        self.text = open('src_calculos/files/optimice_motor.txt', "r", encoding="utf-8").read()
        self.textBrowser_B.setText(self.text)  
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Iterations_result()
    widget.show()
    sys.exit(app.exec_()) 
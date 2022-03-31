#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:29:27 2022

@author: astolfo
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('QPushButton Widget')
        self.displayButton()
        
        self.show()
        
    def displayButton(self):
        name_label = QLabel(self)
        name_label.setText("Don't push the button.")
        name_label.move(30, 30)
        
        button = QPushButton('Push Me', self)
        button.clicked.connect(self.buttonClicked)
        button.move(80, 70)
    
    def buttonClicked(self):
        print('The window has been closed.')
        self.close()
        
# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonWindow()
    sys.exit(app.exec_())
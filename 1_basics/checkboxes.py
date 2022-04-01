#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:50:30 2022

@author: astolfo
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt5.QtCore import Qt

class CheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QCheckBox Widget')
        self.displayCheckBoxes()
        
        self.show()
        
    def displayCheckBoxes(self):
        header_label = QLabel(self)
        header_label.setText('Choose your options')
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)
        
        a_cb = QCheckBox('Option A', self)
        a_cb.move(20, 80)
        a_cb.stateChanged.connect(self.printToTerminal)
        
        b_cb = QCheckBox('Option B', self)
        b_cb.move(20, 100)
        b_cb.stateChanged.connect(self.printToTerminal)
        
        c_cb = QCheckBox('Option C', self)
        c_cb.move(20, 120)
        c_cb.stateChanged.connect(self.printToTerminal)
        
    def printToTerminal(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print('{} Selected.'.format(sender.text()))
        else:
            print('{} Deselected.'.format(sender.text()))
            
# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())
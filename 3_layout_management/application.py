#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 20:22:52 2022

@author: astolfo
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QTextEdit, QSpinBox, QComboBoc, QHBoxLayout
from PyQt5.QtGui import QtFont
from PyQt5.QtCore import Qt

class GetAppForm(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
        
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.

        Returns
        -------
        None.

        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Application Form')
        self.formWidgets()
        
        self.show()
        
    def formWidgets(self):
        """
        Create widgets that will be used in the application form.

        Returns
        -------
        None.

        """
        # Create widgets
        title = QLabel('Appointment Submission Form')
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)
        
        name = QLineEdit()
        name.resize(100, 100)
        address = QLineEdit()
        mobile_num = QLineEdit()
        mobile_num.setInputMask('000-000-0000;')
        
        age_label = QLabel
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
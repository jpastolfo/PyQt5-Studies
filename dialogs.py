#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:35:03 2022

@author: astolfo
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

class DisplayMessageBox(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QMessageBox Example')
        self.displayWidgets()
        
        self.show()
        
    def displayWidgets(self):
        catalogue_label = QLabel('Author Catalogue', self)
        catalogue_label.move(20, 20)
        catalogue_label.setFont(QFont('Arial', 20))
        
        auth_label = QLabel('Enter the name you are searching for:', self)
        auth_label.move(40,60)
        
        author_name = QLabel('Name:', self)
        author_name.move(50,90)
        
        self.auth_entry = QLineEdit(self)
        self.auth_entry.move(95,90)
        self.auth_entry.resize(240,20)
        self.auth_entry.setPlaceholderText('first last')
        
        search_button = QPushButton('Search', self)
        search_button.move(125, 130)
        search_button.resize(150,40)
        search_button.clicked.connect(self.displayMessageBox)
        
    def displayMessageBox(self):
        not_found_msg = QMessageBox()
        # Check if authors.txt exists
        try:
            with open('files/authors.txt', 'r') as f:
                authors = [line.rstrip('\n') for line in f]
                if self.auth_entry.text() in authors:
                    QMessageBox().information(self, 'Author Found', 'Author found in catalogue!', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    not_found_msg = QMessageBox.question(self, 'Author Not Found', 'Author not found in catalogue.\nDo you wish to continue?',
                                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
        except FileNotFoundError:
            QMessageBox().critical(self, 'Missing Files', 'authors.txt could not be found.', QMessageBox.Close, QMessageBox.Close)
        
        if (not_found_msg == QMessageBox.No):
            print('Closing application.')
            self.close()
        elif not_found_msg == QMessageBox.Close:
            self.close()
        else:
            pass
        
# Run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayMessageBox()
    sys.exit(app.exec_())
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:54:16 2022

@author: astolfo
"""

import sys, os.path
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont, QPixmap

class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()
        
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle('2.1 - User Profile GUI')
        self.displayImages()
        self.displayUserInfo()
        
        self.show()
        
    def displayImages(self):
        """
        Display background and profile images.
        Check to see if file exists, if not throw an exception
        """
        
        bg_image = 'images/galaxia'
        profile_image = 'images/eu.png'
        
        try:
            with open(bg_image):
                background = QLabel(self)
                pixmap = QPixmap(bg_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print('Image not found.')
        
        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80, 20)
        except FileNotFoundError:
            print('Image not found.')
            
    def displayUserInfo(self):
        """
        Create the labels to be displayed for the User Profile.

        Returns
        -------
        None.

        """
        
        user_name = QLabel(self)
        user_name.setText('João Pedro Imbriani Astolfo')
        user_name.move(85, 140)
        user_name.setFont(QFont('Arial', 20))
        
        bio_title = QLabel(self)
        bio_title.setText('Biography')
        bio_title.move(15, 170)
        bio_title.setFont(QFont('Arial', 17))
        
        about = QLabel(self)
        about.setText("I'm a Physics Engineer working on optics simulations on SIRIUS")
        about.setWordWrap(True)
        about.move(15, 190)
        
        skills_title = QLabel(self)
        skills_title.setText('Skills')
        skills_title.move(15, 240)
        skills_title.setFont(QFont('Arial', 17))
        
        skills = QLabel(self)
        skills.setText("Python | SPECTRA | SRW | SHADOW")
        skills.move(15, 260)
        
        experience_title = QLabel(self)
        experience_title.setText('Experience')
        experience_title.move(15, 290)
        experience_title.setFont(QFont('Arial', 17))
        
        experience = QLabel(self)
        experience.setText('Physics Engineer Intern')
        experience.move(15, 310)
        
        dates = QLabel(self)
        dates.setText('Feb 2021 - Present')
        dates.move(15, 330)
        dates.setFont(QFont('Arial', 10))
    
# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec_())
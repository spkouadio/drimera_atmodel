# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""

"""
DRIMERA est une application de simulation de la dispersion atmosphérique de polluants.
Elle permet d'évaluation de risques lié à la dérive des pesticides dans les bananeraie

"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class HomeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home.ui', self)


"""Execution"""
if __name__ == '__main__':
    app = QApplication(sys.argv)

    appInit = HomeUI()
    appInit.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')

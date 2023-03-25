# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""


"""
DRIMERA est une application de simulation de la dispersion atmosphérique de polluants.
Elle permet d'évaluation de risques lié à la dérive des pesticides dans les bananeraie

"""

from ui_home import *
import ui_alert
import ui_error
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.paramStackedWidget.setCurrentIndex(0)

        self.ui.atmosBtn.clicked.connect(self.atmosWidget)
        self.ui.operaBtn.clicked.connect(self.operaWidget)
        self.ui.terrainBtn.clicked.connect(self.terrainWidget)
        self.ui.calculBtn.clicked.connect(self.calResult)


    def atmosWidget(self):
        self.ui.paramStackedWidget.setCurrentIndex(1)
        self.ui.atmosBtn.setDefault(True)
        self.ui.operaBtn.setDefault(False)
        self.ui.terrainBtn.setDefault(False)
        self.ui.atmosBtnBox.accepted.connect(self.accepter)
        self.ui.atmosBtnBox.rejected.connect(self.dialog)


    def operaWidget(self):
        self.ui.paramStackedWidget.setCurrentIndex(2)
        self.ui.atmosBtn.setDefault(False)
        self.ui.operaBtn.setDefault(True)
        self.ui.terrainBtn.setDefault(False)
        self.ui.opBtnBox.accepted.connect(self.accepter)
        self.ui.opBtnBox.rejected.connect(self.dialog)

    def terrainWidget(self):
        self.ui.paramStackedWidget.setCurrentIndex(3)
        self.ui.atmosBtn.setDefault(False)
        self.ui.operaBtn.setDefault(False)
        self.ui.terrainBtn.setDefault(True)
        self.ui.terBtnBox.accepted.connect(self.accepter)
        self.ui.terBtnBox.rejected.connect(self.uiAnnuler)

    def calResult(self):
        self.uiErreur()
        #self.ui.paramStackedWidget.setCurrentIndex(0)
        # Calculate and printing plot, tab

    def dialog(self):
        self.ui.atmosBtn.setDefault(False)
        self.ui.operaBtn.setDefault(False)
        self.ui.terrainBtn.setDefault(False)
        self.uiAnnuler()

    def uiAnnuler (self):
        annuler = QDialog()
        annuler.ui = ui_alert.Ui_Alert()
        annuler.ui.setupUi(annuler)
        annuler.ui.buttonBox.accepted.connect(self.accepter)
        annuler.exec_()

    def uiErreur (self):
        erreur = QDialog()
        erreur.ui = ui_error.Ui_Erreur()
        erreur.ui.setupUi(erreur)
        erreur.ui.buttonBox.accepted.connect(self.accepter)
        erreur.exec_()


    def accepter(self):
        self.ui.atmosBtn.setDefault(False)
        self.ui.operaBtn.setDefault(False)
        self.ui.terrainBtn.setDefault(False)
        self.ui.paramStackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')

"""
class appHome(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(self, window)
        self.atmosBtn.clicked.connect(self.atmosWidget)
        self.operaBtn.clicked.connect(self.operaWidget)
        self.terrainBtn.clicked.connect(self.terrainWidget)


    def atmosWidget(self):
        self.paramGrpBox.addWidget(self.atmosForm)


app = QApplication(sys.argv)
MainWindow = QMainWindow()

ui = appHome(MainWindow)

MainWindow.show()
app.exec_()

Execution
if __name__ == '__main__':
    app = QApplication(sys.argv)

    appInit = appHome()
    appInit.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
"""
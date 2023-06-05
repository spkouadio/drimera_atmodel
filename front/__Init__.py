# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""


"""
DRIMERA (Drift Modeling for Environmental Risk Assessment) est un outil d’aide à la décision développé 
dans la cadre de la thèse de doctorat de @Saint-Pierre KOUADIO. Ce logiciel permet la simulation de la dispersion 
atmosphérique de polluants. Il aide ainsi à évaluer les risques liés à l’utilisation de pesticides par 
voie aérienne sur cultures comme dans les bananeraies. 

"""

from ui_homeUI import *
import ui_alert
import ui_error
import sys
from script.params import parameter

#import script._init_ as calculus
#import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculBtn.clicked.connect(self.calResult)


    def calResult(self):
        activeMatCarac = self.ui.activeMatCarac_comboBox.currentText()
        supportCarac = self.ui.supportCarac_comboBox.currentText()
        dropletSize = self.ui.dropletSize_comboBox.currentText()

        activMatConc = self.ui.activMatConc_lineEdit.text()
        carrierVol = self.ui.carrierVol_lineEdit.text()
        boomHeight = self.ui.boomHeight_lineEdit.text()
        appRate = self.ui.appRate_lineEdit.text()
        residualConc = self.ui.residualConc_lineEdit.text()
        windSpeed = self.ui.windSpeed_lineEdit.text()
        temperature = self.ui.temperature_lineEdit.text()
        humidity = self.ui.humidity_lineEdit.text()
        timeStep = self.ui.timeStep_lineEdit.text()

        return [activeMatCarac, supportCarac, dropletSize, activMatConc, carrierVol, boomHeight, appRate,
                residualConc, windSpeed, temperature, humidity, timeStep]


        #self.uiErreur()
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
        if activMatConc != 0 :
            parameter.chem = activMatConc
        else : self.uiErreur()

        if carrierVol != 0 :
            parameter.supp_volume = carrierVol
        else  : self.uiErreur()

        if boomHeight != 0 :
            parameter.boomHeight = boomHeight
        else  : self.uiErreur()

        if appRate != 0 :
            parameter.application_rate = appRate
        else  : self.uiErreur()

        if residualConc != 0 :
            parameter.resConcentration = residualConc
        else  : self.uiErreur()

        if windSpeed != 0 :
           parameter.air_velocity = windSpeed
        else  : self.uiErreur()

        if temperature != 0 :
            parameter.temp = temperature
        else  : self.uiErreur()

        if humidity != 0 :
            parameter.humidity = humidity
        else  : self.uiErreur()

        if activeMatCarac != 0 :
            parameter.active_mat_conc = activeMatCarac
        else  : self.uiErreur()

        if supportCarac != 0 :
            parameter.supp_volume = supportCarac
        else  : self.uiErreur()

        if dropletSize != 0 :
            parameter.dropletSize = dropletSize
        else  : self.uiErreur()

        if timeStep != 0 :
            parameter.time_nt = timeStep
        else  : self.uiErreur()
"""
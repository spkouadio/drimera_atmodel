# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""
import os

from PySide2 import QtWidgets

"""
DRIMERA (Drift Modeling for Environmental Risk Assessment) est un outil d’aide à la décision développé 
dans la cadre de la thèse de doctorat de @Saint-Pierre KOUADIO. Ce logiciel permet la simulation de la dispersion 
atmosphérique de polluants. Il aide ainsi à évaluer les risques liés à l’utilisation de pesticides par 
voie aérienne sur cultures comme dans les bananeraies. 

"""
import sys

from ui_homeUI import *
from script.params import *
from script.air_flow import *
from script.droplet_descr import *
from script.conc_calculus import *
from script.droplet_dispersal import *

import ui_alert
import ui_error

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

#from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PySide2.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from six import BytesIO
from PySide2 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculBtn.clicked.connect(self.errorDetection)
        self.ui.downloadBtn.clicked.connect(self.exportData)

        #self.statusBar().showMessage("Ready", 0)

        #self.btn = QtWidgets.QPushButton("Download", self)
        #self.btn.move(10, 10)
        #self.btn.clicked.connect(self.runprocess)
        self.progress_bar = QtWidgets.QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()

    def startprocess(self):
        self.completed = 0
        self.progress_bar.setFixedSize(self.geometry().width() - 120, 16)
        self.progress_bar.show()
        self.statusBar().showMessage("Running ...", 0)
        self.progress_bar.setValue(int(self.completed))

    def runprocess(self):
        self.completed = 0
        self.progress_bar.setFixedSize(self.geometry().width() - 120, 16)
        self.progress_bar.show()
        self.statusBar().showMessage("Running ...", 0)

        while self.completed < 100:
            self.completed += 0.00005
            self.progress_bar.setValue(int(self.completed))

            if self.progress_bar.value() == 100:
                self.statusBar().showMessage("Process completed !", 0)
                self.progress_bar.hide()

    def calResult(self):

        self.startprocess()
        # Get parameters
        self.activeMatCarac = self.ui.activeMatCarac_comboBox.currentText()
        self.supportCarac = self.ui.supportCarac_comboBox.currentText()
        self.dropletSize = self.ui.dropletSize_comboBox.currentText()

        self.activMatConc = float(self.ui.activMatConc_lineEdit.text())
        self.carrierVol = float(self.ui.carrierVol_lineEdit.text())
        self.boomHeight = float(self.ui.boomHeight_lineEdit.text())
        self.appRate = float(self.ui.appRate_lineEdit.text())
        self.residualConc = float(self.ui.residualConc_lineEdit.text())
        self.windSpeed = float(self.ui.windSpeed_lineEdit.text())
        self.temperature = float(self.ui.temperature_lineEdit.text())
        self.humidity = float(self.ui.humidity_lineEdit.text())
        self.timeStep = int(self.ui.timeStep_lineEdit.text())

        # Parameters initialisation
        self.parameter = inputs_par(self.activeMatCarac, self.supportCarac, self.dropletSize, self.activMatConc,
                                    self.carrierVol, self.boomHeight, self.appRate, self.residualConc, self.windSpeed,
                                    self.temperature, self.humidity, self.timeStep)

        # Air flow initialisation
        self.airflow = air_flow(self.parameter.air_sp_ratio, self.parameter.air_pressure,
                           self.parameter.air_density, self.parameter.air_velocity)

        # Droplet description initialisation
        self.dropdescr = droplet_descr(self.parameter.humidity, self.parameter.temp, self.parameter.air_density,
                                       self.parameter.chem, self.parameter.chem_density, self.parameter.chem_mass,
                                       self.parameter.chem_dilrate, self.parameter.supp_volume, self.parameter.supp_density,
                                       self.parameter.rho_mix, self.parameter.vol_mix)

        # Droplet dispersal initialisation
        self.dd = droplet_dispersal(self.airflow.v, self.airflow.u, self.parameter.rho_mix, self.parameter.air_density,
                                    self.parameter.boomHeight, self.parameter.air_kviscosity, self.dropdescr.drop_distrib(),
                                    self.dropdescr.init_velocity())

        # Concentration calculus initialisation
        self.concalcul = concent_calc(self.parameter.time_nt)


        #app_rate = self.parameter.application_rate  # l/ha

        # Droplets distribution by diameter
        drop_dist = self.dropdescr.drop_distrib()

        # Droplets trajectory
        n_diam = len(drop_dist[:, 0])

        # Plot concentration profile for a specific time
        # Plot concentration profile by diameter
        concent = np.zeros((101, 101))
        for k in range(n_diam):
            i = round(self.dd.x[k, -1])
            j = self.dd.j
            u_air = self.dd.u_air
            alpha_buoy = self.dd.C_d(drop_dist[k, 0], self.dd.u_air[i, i], 0.0)
            c_0 = drop_dist[k, 1]  # *math.pow(10,6) µg/l
            # concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
            concent = np.add(concent, self.concalcul.conc_cal(u_air, alpha_buoy, c_0, i, j))

        self.runprocess()

        # Plot concentration by position in a tableView
        drift_pos = len(concent[self.dd.j,:])-1
        self.datasheet = np.empty((0, 2), float)  # m
        for xpos in range(drift_pos):
            self.datasheet = np.append(self.datasheet, np.array([[xpos, round(concent[self.dd.j, xpos] * math.pow(10, 6), 3)]]), axis=0)

        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(['position (m)', 'concentration (µg/l)'])
        for i in range(drift_pos):
            for j in range(2):
                self.model.setItem(i, j, QStandardItem(str(self.datasheet[i,j])))

        self.ui.tableView.setModel(self.model)

        # Plot concentration by position in a 2D graph
        plt.clf() # Reinitialize plot
        plt.imshow(concent, cmap='hot', origin='lower', extent=[0, 100, 0, 100])
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Concentration in g/l at time = {(self.parameter.time_nt / 60):.2f} min')

        def fig_to_pixmap(fig):
            # Save the figure to a buffer
            buf = BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0, transparent=True)
            buf.seek(0)

            # Convert the buffer to QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(buf.read())
            buf.close()

            return pixmap

        # Convert the matplotlib figure to QPixmap
        self.figure_pixmap = fig_to_pixmap(plt.gcf())

        # Create a QGraphicsPixmapItem to display the image
        self.graphicScene = QGraphicsScene()
        self.graphicScene.addPixmap(self.figure_pixmap)

        # Set the QGraphicsView
        #self.ui.result_graphicsView.c
        self.ui.result_graphicsView.setScene(self.graphicScene)

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
        error = QDialog()
        error.ui = ui_error.Ui_Error()
        error.ui.setupUi(error)
        #error.ui.buttonBox.accepted.connect(self.accepter)
        error.exec_()


    def accepter(self):
        self.ui.atmosBtn.setDefault(False)
        self.ui.operaBtn.setDefault(False)
        self.ui.terrainBtn.setDefault(False)
        self.ui.paramStackedWidget.setCurrentIndex(0)


    def exportData(self):
        if self.ui.resultTabWidget_result.currentIndex() == 0:
            plt.savefig(str(os.path.join(Path.home(), "Downloads", "drimera_dataPlot.png")))
        if self.ui.resultTabWidget_result.currentIndex() == 1:
            dt_data = pd.DataFrame(np.append(np.array([['position (m)', 'concentration (µg/l)']]), self.datasheet, axis=0))
            dt_data.to_csv(str(os.path.join(Path.home(), "Downloads", "drimera_dataSheet.csv")), index=False, header=False)


    def errorDetection(self):

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

        def is_float(string):
            try:
                float(string)
                return True
            except ValueError:
                return False

        self.truevalue = 0

        if (activeMatCarac == '') :
            self.truevalue += 0
        else : self.truevalue += 1
        if (supportCarac == '') :
            self.truevalue += 0
        else : self.truevalue += 1
        if (dropletSize == '') :
            self.truevalue += 0
        else : self.truevalue += 1

        if (is_float(activMatConc)==False) :
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(carrierVol) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(boomHeight) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(appRate) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(residualConc) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(windSpeed) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(temperature) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(humidity) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(timeStep) == False):
            self.truevalue += 0
        else : self.truevalue += 1

        if (self.truevalue == 12):
            self.calResult()
        else : self.uiErreur()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
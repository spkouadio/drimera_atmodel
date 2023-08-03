# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""
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
        self.ui.calculBtn.clicked.connect(self.calResult)


    def calResult(self):

        # Get parameters
        activeMatCarac = self.ui.activeMatCarac_comboBox.currentText()
        supportCarac = self.ui.supportCarac_comboBox.currentText()
        dropletSize = self.ui.dropletSize_comboBox.currentText()

        activMatConc = float(self.ui.activMatConc_lineEdit.text())
        carrierVol = float(self.ui.carrierVol_lineEdit.text())
        boomHeight = float(self.ui.boomHeight_lineEdit.text())
        appRate = float(self.ui.appRate_lineEdit.text())
        residualConc = float(self.ui.residualConc_lineEdit.text())
        windSpeed = float(self.ui.windSpeed_lineEdit.text())
        temperature = float(self.ui.temperature_lineEdit.text())
        humidity = float(self.ui.humidity_lineEdit.text())
        timeStep = int(self.ui.timeStep_lineEdit.text())

        # Parameters initialisation
        self.parameter = inputs_par(activeMatCarac, supportCarac, dropletSize, activMatConc, carrierVol, boomHeight, appRate,
                residualConc, windSpeed, temperature, humidity, timeStep)

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

        # Plot concentration by position in a tableView
        drift_pos = len(concent[self.dd.j,:])-1
        data = np.empty((0, 2), float)  # m
        for xpos in range(drift_pos):
            data = np.append(data, np.array([[xpos, round(concent[self.dd.j, xpos] * math.pow(10, 6), 3)]]), axis=0)

        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(['position (m)', 'concentration (µg/l)'])
        for i in range(drift_pos):
            for j in range(2):
                self.model.setItem(i, j, QStandardItem(str(data[i,j])))

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
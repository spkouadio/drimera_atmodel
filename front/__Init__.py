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
from script.const import constants

import ui_alert
import ui_error
import ui_pestsetting
import ui_carriersetting

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

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.w = MainWindow()
        self.w.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pestList = constants.chemical(self)
        self.carList = constants.carrier(self)
        self.dropClassList = constants.dropletClass(self)
        self.ui.calculBtn.clicked.connect(self.errorDetection)
        self.ui.downloadBtn.clicked.connect(self.exportData)
        self.ui.activeMatCarac_toolButton.clicked.connect(self.pestSetting)
        self.ui.supportCarac_toolButton.clicked.connect(self.carSetting)
        self.ui.actionQuitter.triggered.connect(self.closeApp)
        self.ui.actionNouveau.triggered.connect(self.newApp)

        self.ui.zposition_horizontalSlider.valueChanged.connect(self.sliderchanged)

        self.progress_bar = QtWidgets.QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()

    def closeApp(self):
        self.close()
    def newApp(self):
        self.w = AnotherWindow()

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
    def sliderchanged(self):
        self.ui.zposition_lineEdit.setText(str(self.ui.zposition_horizontalSlider.value()))

    def positionChanged(self):
        self.ui.zposition_horizontalSlider.setValue(int(self.ui.zposition_lineEdit.text()))
        self.plot(int(self.ui.zposition_lineEdit.text()))

    def calResult(self):

        self.startprocess()
        # Get parameters
        #self.activeMatCarac = self.ui.activeMatCarac_comboBox.currentText()
        #self.supportCarac = self.ui.supportCarac_comboBox.currentText()


        pest = self.ui.pesticideUsed_comboBox.currentText()
        chem_concent = self.pestList[np.where(self.pestList[:, 0] == pest), 2].item()
        pest_density = self.pestList[np.where(self.pestList[:, 0] == pest), 3].item()
        self.activeMatConcent = float(chem_concent)
        self.pesticideDensity = float(pest_density)
        self.pesticideVol = float(self.ui.pesticideVol_lineEdit.text())
        car = self.ui.supportCarac_comboBox.currentText()
        car_density = self.carList[np.where(self.carList[:, 0] == car), 1].item()
        self.carrierDensity = float(car_density)
        self.carrierVol = float(self.ui.carrierVol_lineEdit.text())
        self.boomHeight = float(self.ui.boomHeight_lineEdit.text())
        self.appRate = float(self.ui.appRate_lineEdit.text())
        droplet_class = self.ui.dropletSize_comboBox.currentText()
        droplet_size = self.dropClassList[np.where(self.dropClassList[:, 0] == droplet_class), 1].item()
        self.dropletSize = float(droplet_size)
        self.residualConc = float(self.ui.residualConc_lineEdit.text())
        self.ejectSpeed = float(self.ui.ejectionSpeed_lineEdit.text())
        self.windSpeed = float(self.ui.windSpeed_lineEdit.text())
        self.temperature = float(self.ui.temperature_lineEdit.text())
        self.humidity = float(self.ui.humidity_lineEdit.text())
        self.x0 = int(self.ui.x0_lineEdit.text())
        self.y0 = int(self.ui.y0_lineEdit.text())
        self.timeStep = int(self.ui.timeStep_lineEdit.text())

        # Altitude initialisation
        self.ui.zposition_horizontalSlider.setMaximum(int(self.boomHeight))
        self.ui.zposition_horizontalSlider.setValue(int(self.boomHeight))
        self.ui.zposition_lineEdit.textChanged.connect(self.positionChanged)

        self.z_pos = self.ui.zposition_horizontalSlider.value()

        # Parameters initialisation
        self.parameter = inputs_par(self.activeMatConcent, self.pesticideDensity, self.pesticideVol, self.carrierDensity,
                                    self.carrierVol, self.dropletSize, self.boomHeight, self.appRate, self.residualConc,
                                    self.windSpeed, self.ejectSpeed, self.temperature, self.humidity, self.timeStep, self.x0, self.y0)

        # Air flow initialisation
        self.airflow = air_flow(self.parameter.air_sp_ratio, self.parameter.air_pressure,
                           self.parameter.air_density, self.parameter.air_velocity)

        # Droplet description initialisation
        self.dropdescr = droplet_descr(self.dropletSize, self.parameter.chem_mass, self.parameter.rho_mix, self.parameter.vol_mix)

        # Droplet dispersal initialisation
        self.dd = droplet_dispersal(self.timeStep, self.airflow.v, self.airflow.u, self.parameter.rho_mix, self.parameter.air_density,
                                    self.parameter.boomHeight, self.parameter.air_kviscosity, self.dropdescr.drop_distrib(),
                                    self.dropdescr.init_velocity(), self.x0, self.y0, self.z_pos) #self.ejectSpeed

        # Concentration calculus initialisation
        self.concalcul = concent_calc(self.parameter.time_nt)


        #app_rate = self.parameter.application_rate  # l/ha

        # Droplets distribution by diameter
        drop_dist = self.dropdescr.drop_distrib()

        # Droplets trajectory
        n_diam = len(drop_dist[:, 0])

        # Plot concentration profile for a specific time
        # Plot concentration profile by diameter
        concent = np.zeros((301, 301))
        self.z_concent = [concent] * (self.z_pos+1)
        self.dd.i = self.x0
        self.dd.j = self.y0
        self.res_conc = np.ones((301, 301)) * self.parameter.resConcentration * math.pow(10, -6)

        #for k in range(n_diam):
        #   i = self.x0 #round(self.dd.x[k, -1]) +
        #   j = self.dd.j
        #   u_air = self.dd.u_air
        #   alpha_buoy = self.dd.C_d(drop_dist[k, 0], self.dd.u_air[i, j], self.dropdescr.init_velocity())
        #   c_0 = drop_dist[k, 1]  # *math.pow(10,6) µg/l
        #   # concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
        #   concent = np.add(concent, self.concalcul.conc_cal(u_air, alpha_buoy, c_0, i, j))
        #if self.parameter.resConcentration != 0 :
        #   concent = concent + self.parameter.resConcentration * math.pow(10, -6)


        for k in range(n_diam):
           i = self.x0 #round(self.dd.x[k, -1]) +
           j = self.dd.j
           u_air = self.dd.u_air
           alpha_buoy = self.dd.C_d(drop_dist[k, 0], self.dd.u_air[i, j], self.dropdescr.init_velocity())
           c_0 = drop_dist[k, 1]  # *math.pow(10,6) µg/l
           # concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
           #concent = np.add(concent, self.dd.conc_cal(u_air, alpha_buoy, c_0, i, j, k))
           concent = self.dd.conc_cal(u_air, alpha_buoy, c_0, i, j, k)
           pos = int(round(self.dd.z[k,-1], 0))
           self.z_concent[pos] = np.add(self.z_concent[pos], concent)
        if self.parameter.resConcentration != 0 :
           self.z_concent[0] = np.add(self.z_concent[0], self.res_conc) 


        #for k in range(n_diam):
        #    i = round(self.dd.x[k, -1]) + self.x0
        #    j = self.dd.j
        #    u_air = self.dd.u_air
        #    alpha_buoy = self.dd.C_d(drop_dist[k, 0], self.dd.u_air[i, j], self.ejectSpeed)
        #    c_0 = drop_dist[k, 1]  # *math.pow(10,6) µg/l
        #    # concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
        #    concent = np.add(concent, self.concalcul.conc_cal(u_air, alpha_buoy, c_0, i, j))
        #if self.parameter.resConcentration != 0 :
        #    concent = concent + self.parameter.resConcentration * math.pow(10, -6)

        self.runprocess()

        self.plot(self.z_pos)

    def plot(self, z_pos):
        # Plot concentration by position in a tableView
        drift_pos = 300 #len(concent[self.dd.j,:])-1
        #self.datasheet = np.empty((0, 2), float)  # m
        #for xpos in range(drift_pos):
        #    self.datasheet = np.append(self.datasheet, np.array([[xpos, round(concent[self.dd.j, xpos] * math.pow(10, 3), 3)]]), axis=0)

        #self.model = QStandardItemModel(0, 2, self)
        #self.model.setHorizontalHeaderLabels(['position (m)', 'value (mg/l)'])
        #for i in range(drift_pos):
        #    for j in range(2):
        #        self.model.setItem(i, j, QStandardItem(str(self.datasheet[i,j])))

        len_dim = 300 #len(concent[0,:])-1
        concent = self.z_concent[int(z_pos)]

        self.model = QStandardItemModel(0, len_dim, self)
        self.datasheet = np.round(concent * math.pow(10, 3), 6)
        #self.model.setHorizontalHeaderLabels(['position (m)', 'value (mg/l)'])
        for i in range(drift_pos):
            for j in range(len_dim):
                self.model.setItem(i, j, QStandardItem(str(self.datasheet[i, j])))

        self.ui.tableView.setModel(self.model)
        #self.ui.tableView.setMinimumWidth(100)

        # Plot concentration by position in a 2D graph
        plt.clf() # Reinitialize plot
        plt.rcParams.update({'font.size': 8}) # Set fontsize
        plt.gcf().set_size_inches(8.7, 3.7, forward=True) # Set imagesize
        plt.imshow(concent * math.pow(10, 3), cmap='hot', origin='lower', extent=[0, 300, 0, 300])
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Concentration in mg/l at time = {(self.parameter.time_nt / 60):.2f} min at altitude Z = {(z_pos):.2f} m')

        def fig_to_pixmap(fig):
            # Save the figure to a buffer
            buf = BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.2, transparent=True)
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
            #dt_data = pd.DataFrame(np.append(np.array([['position (m)', 'value (mg/l)']]), self.datasheet, axis=0))
            dt_data = pd.DataFrame(self.datasheet)
            dt_data.to_csv(str(os.path.join(Path.home(), "Downloads", "drimera_dataSheet.csv")), index=False, header=False)


    def errorDetection(self):

        pesticideUsed = self.ui.pesticideUsed_comboBox.currentText()
        supportCarac = self.ui.supportCarac_comboBox.currentText()
        dropletSize = self.ui.dropletSize_comboBox.currentText()

        pesticideVol = self.ui.pesticideVol_lineEdit.text()
        carrierVol = self.ui.carrierVol_lineEdit.text()
        boomHeight = self.ui.boomHeight_lineEdit.text()
        appRate = self.ui.appRate_lineEdit.text()
        residualConc = self.ui.residualConc_lineEdit.text()
        ejectSpeed = self.ui.ejectionSpeed_lineEdit.text()
        windSpeed = self.ui.windSpeed_lineEdit.text()
        temperature = self.ui.temperature_lineEdit.text()
        humidity = self.ui.humidity_lineEdit.text()
        x0 = self.ui.x0_lineEdit.text()
        y0 = self.ui.y0_lineEdit.text()
        timeStep = self.ui.timeStep_lineEdit.text()

        def is_float(string):
            try:
                float(string)
                return True
            except ValueError:
                return False

        self.truevalue = 0

        if (pesticideUsed == '') :
            self.truevalue += 0
        else : self.truevalue += 1
        if (supportCarac == '') :
            self.truevalue += 0
        else : self.truevalue += 1
        if (dropletSize == '') :
            self.truevalue += 0
        else : self.truevalue += 1

        if (is_float(pesticideVol)==False) :
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
        if (is_float(ejectSpeed) == False):
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
        if (is_float(x0) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(y0) == False):
            self.truevalue += 0
        else : self.truevalue += 1

        if (self.truevalue == 15):
            self.calResult()
        else : self.uiErreur()


    def pestSetting(self):
        pestSetting = QDialog()
        pestSetting.ui = ui_pestsetting.Ui_Alert()
        pestSetting.ui.setupUi(pestSetting)
        self.modelList = QStandardItemModel(self)
        pestSetting.ui.pesticide_listView.setModel(self.modelList)
        #self.modelList = QStandardItemModel(self)
        #self.pestList = constants.chemical(self)#np.empty((0, 3))
        for ichem in range(len(self.pestList[:,0])):
            item = QStandardItem(str(self.pestList[ichem,0]))
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.modelList.appendRow(item)

        def addPest():
            def is_float(string):
                try:
                    float(string)
                    return True
                except ValueError:
                    return False

            pestName = pestSetting.ui.pesticideName_lineEdit.text()
            amName = pestSetting.ui.activeMatter_lineEdit.text()
            amConcent = pestSetting.ui.amConcent_lineEdit.text()
            pestDensity = pestSetting.ui.pestDensity_lineEdit.text()
            value = 0
            if (pestName == ''): value += 0
            else: value += 1
            if (amName == ''): value += 0
            else: value += 1
            if (is_float(amConcent) == False): value += 0
            else: value += 1
            if (is_float(pestDensity) == False): value += 0
            else: value += 1
            if (value != 4):
                self.uiErreur()
            else:
                self.pestList = np.append(self.pestList, np.array([[str(pestName), str(amName), float(amConcent), float(pestDensity)]]), axis=0)
                self.ui.pesticideUsed_comboBox.addItem(pestName)
                item = QStandardItem(str(pestName))
                item.setCheckable(True)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.modelList.appendRow(item)
                pestSetting.ui.pesticide_listView.setModel(self.modelList)
                pestSetting.ui.pesticideName_lineEdit.clear()
                pestSetting.ui.activeMatter_lineEdit.clear()
                pestSetting.ui.pestDensity_lineEdit.clear()
                pestSetting.ui.amConcent_lineEdit.clear()
        def removePest():
            pestSetting.ui.pesticideName_lineEdit.clear()
            pestSetting.ui.activeMatter_lineEdit.clear()
            pestSetting.ui.pestDensity_lineEdit.clear()
            pestSetting.ui.amConcent_lineEdit.clear()
            for row in range(self.modelList.rowCount()):
                item = self.modelList.item(row)
                if item and item.checkState() == QtCore.Qt.Checked:
                    self.modelList.removeRow(row)
                    self.pestList = np.delete(self.pestList, row, axis=0)
                    self.ui.pesticideUsed_comboBox.removeItem(row)
        def displayPest():
            for row in range(self.modelList.rowCount()):
                item = self.modelList.item(row)
                if item and item.checkState() == QtCore.Qt.Checked:
                    pestSetting.ui.pesticideName_lineEdit.setText(self.pestList[row, 0])
                    pestSetting.ui.activeMatter_lineEdit.setText(self.pestList[row, 1])
                    pestSetting.ui.amConcent_lineEdit.setText(self.pestList[row, 2])
                    pestSetting.ui.pestDensity_lineEdit.setText(self.pestList[row, 3])
        def toMain():
            pestSetting.close()

        pestSetting.ui.saveBtn.clicked.connect(addPest)
        pestSetting.ui.deleteBtn.clicked.connect(removePest)
        pestSetting.ui.pesticide_listView.clicked.connect(displayPest)
        pestSetting.ui.backBtn.clicked.connect(toMain)

        pestSetting.exec_()

    def carSetting(self):
        carSetting = QDialog()
        carSetting.ui = ui_carriersetting.Ui_Alert()
        carSetting.ui.setupUi(carSetting)
        self.carmodelList = QStandardItemModel(self)
        carSetting.ui.carrier_listView.setModel(self.carmodelList)
        for icar in range(len(self.carList[:,0])):
            item = QStandardItem(str(self.carList[icar,0]))
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.carmodelList.appendRow(item)

        def addCarrier():
            def is_float(string):
                try:
                    float(string)
                    return True
                except ValueError:
                    return False

            carrierName = carSetting.ui.carrier_lineEdit.text()
            cadensity = carSetting.ui.cadensity_lineEdit.text()
            caFeatures = carSetting.ui.cafeatures_lineEdit.text()
            value = 0
            if (carrierName == ''): value += 0
            else: value += 1
            if (caFeatures == ''): value += 0
            else: value += 1
            if (is_float(cadensity) == False): value += 0
            else: value += 1
            if (value != 3):
                self.uiErreur()
            else:
                self.carList = np.append(self.carList, np.array([[str(carrierName), float(cadensity), str(caFeatures)]]), axis=0)
                self.ui.supportCarac_comboBox.addItem(carrierName)
                item = QStandardItem(str(carrierName))
                item.setCheckable(True)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.carmodelList.appendRow(item)
                carSetting.ui.carrier_listView.setModel(self.carmodelList)
                carSetting.ui.carrier_lineEdit.clear()
                carSetting.ui.cadensity_lineEdit.clear()
                carSetting.ui.cafeatures_lineEdit.clear()
        def removeCarrier():
            carSetting.ui.carrier_lineEdit.clear()
            carSetting.ui.cadensity_lineEdit.clear()
            carSetting.ui.cafeatures_lineEdit.clear()
            for row in range(self.carmodelList.rowCount()):
                item = self.carmodelList.item(row)
                if item and item.checkState() == QtCore.Qt.Checked:
                    self.carmodelList.removeRow(row)
                    self.carList = np.delete(self.carList, row, axis=0)
                    self.ui.supportCarac_comboBox.removeItem(row)
        def displayCarrier():
            for row in range(self.carmodelList.rowCount()):
                item = self.carmodelList.item(row)
                if item and item.checkState() == QtCore.Qt.Checked:
                    carSetting.ui.carrier_lineEdit.setText(self.carList[row, 0])
                    carSetting.ui.cadensity_lineEdit.setText(self.carList[row, 1])
                    carSetting.ui.cafeatures_lineEdit.setText(self.carList[row, 2])
        def toMain():
            carSetting.close()

        carSetting.ui.saveBtn.clicked.connect(addCarrier)
        carSetting.ui.deleteBtn.clicked.connect(removeCarrier)
        carSetting.ui.carrier_listView.clicked.connect(displayCarrier)
        carSetting.ui.backBtn.clicked.connect(toMain)

        carSetting.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
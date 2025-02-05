# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:18:06 2021

@author: Saimpy

"""
import os

from PySide2 import QtWidgets

import script.params

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
import ui_windrosesetting

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

#from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PySide2.QtGui import QPixmap, QStandardItemModel, QStandardItem, QDesktopServices
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
        self.ui.roseWind_toolButton.clicked.connect(self.roseSetting)
        self.ui.actionQuitter.triggered.connect(self.closeApp)
        self.ui.actionNouveau.triggered.connect(self.newApp)
        self.ui.actionAide.triggered.connect(self.helpApp)

        self.ui.zposition_horizontalSlider.valueChanged.connect(self.sliderchanged)

        self.progress_bar = QtWidgets.QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()
        self.roseSetValue = constants.roseValue(self)[:, 1].astype(float).tolist()

    def closeApp(self):
        self.close()
    def newApp(self):
        self.w = AnotherWindow()

    def helpApp(self):
        url = QUrl.fromLocalFile("Im/helpFile.pdf" )
        QDesktopServices.openUrl(url)

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
        self.forwardSpeed = float(self.ui.forwardSpeed_lineEdit.text())
        self.nozzleSpacing = float(self.ui.nozzleSpacing_lineEdit.text())
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
                                    self.windSpeed, self.forwardSpeed, self.nozzleSpacing, self.temperature, self.humidity, self.timeStep, self.x0, self.y0)

        # Air flow initialisation
        #self.airflow = air_flow(self.timeStep, self.parameter.air_sp_ratio, self.parameter.air_pressure,
                           #self.parameter.air_density, self.parameter.air_velocity)
        self.airflow = air_flow(self.windSpeed, self.roseSetValue, self.timeStep)

        # Droplet description initialisation
        self.dropdescr = droplet_descr(self.dropletSize, self.parameter.outputFlow, self.parameter.rho_mix, self.parameter.vol_mix)

        # Droplet dispersal initialisation
        self.dd = droplet_dispersal(self.timeStep, self.airflow.velocity_field_y, self.airflow.velocity_field_x, self.airflow.velocity_value,
                                    self.windSpeed, self.parameter.rho_mix, self.parameter.air_density, self.parameter.boomHeight,
                                    self.parameter.air_kviscosity, self.dropdescr.drop_distrib(),
                                    self.dropdescr.init_velocity(), self.x0, self.y0, self.z_pos) #self.ejectSpeed

        # Concentration calculus initialisation
        self.concalcul = concent_calc(self.parameter.time_nt)


        #app_rate = self.parameter.application_rate  # l/ha

        # Droplets distribution by diameter
        drop_dist = self.dropdescr.drop_distrib()

        # Droplets trajectory
        n_diam = len(drop_dist[:, 0])

        # Plot concentration profile at end of timestep
        # Plot concentration profile by diameter
        concent = np.zeros((201, 201))
        self.z_concent = [concent] * (self.z_pos+1)
        self.dd.i = self.x0
        self.dd.j = self.y0
        self.res_conc = np.ones((101, 101)) * self.parameter.resConcentration * math.pow(10, -6)

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
           v_air = self.dd.v_air
           alpha_buoy = self.dd.C_d(drop_dist[k, 0], self.dd.vel_air[i, j], self.dropdescr.init_velocity())
           c_0 = drop_dist[k, 1] * self.parameter.rho_mix #g *math.pow(10,6) µg/l
           # concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
           #concent = np.add(concent, self.dd.conc_cal(u_air, alpha_buoy, c_0, i, j, k))
           concent = self.dd.conc_cal(v_air, u_air, alpha_buoy, c_0, i, j, k)
           pos = int(round(self.dd.z[k,-1], 0))
           self.z_concent[pos] = np.add(self.z_concent[pos], concent)
        if self.parameter.resConcentration != 0 :
           self.z_concent[0] = np.add(self.z_concent[0], self.res_conc)

        #self.z_concent = convFact * self.z_concent

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
        #len(concent[self.dd.j,:])-1
        #self.datasheet = np.empty((0, 2), float)  # m
        #for xpos in range(drift_pos):
        #    self.datasheet = np.append(self.datasheet, np.array([[xpos, round(concent[self.dd.j, xpos] * math.pow(10, 3), 3)]]), axis=0)

        #self.model = QStandardItemModel(0, 2, self)
        #self.model.setHorizontalHeaderLabels(['position (m)', 'value (mg/l)'])
        #for i in range(drift_pos):
        #    for j in range(2):
        #        self.model.setItem(i, j, QStandardItem(str(self.datasheet[i,j])))

        len_dim = 201 #len(concent[0,:])-1
        concent = self.z_concent[int(z_pos)] # l
        convFact = (self.parameter.chem_concent * self.parameter.pesticide_volume) / self.parameter.vol_mix
        concent = concent * convFact * math.pow(10, 6) # µg

        self.model = QStandardItemModel(0, len_dim, self)
        self.datasheet = np.round(concent, 6)
        #self.model.setHorizontalHeaderLabels(['position (m)', 'value (g)'])
        for i in range(len_dim):
            for j in range(len_dim):
                self.model.setItem(i, j, QStandardItem(str(self.datasheet[i, j])))

        self.ui.tableView.setModel(self.model)
        #self.ui.tableView.setMinimumWidth(100)

        # Plot concentration by position in a 2D graph
        plt.clf() # Reinitialize plot
        plt.rcParams.update({'font.size': 8, 'axes.titlepad': 18}) # Set fontsize & title padding
        #plt.gcf().set_size_inches(8.7, 3.7, forward=True) # Set imagesize
        plt.imshow(concent, cmap='hot', origin='lower', extent=[0, 200, 0, 200])
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Active matter in µg at time = {(self.parameter.time_nt / 60):.2f} min at altitude Z = {(z_pos):.2f} m')

        width_pixels = 1.6*self.ui.result_graphicsView.width()
        height_pixels = 1.6*self.ui.result_graphicsView.height()

        # Convert dimensions in inches
        dpi_x = QApplication.desktop().physicalDpiX()
        dpi_y = QApplication.desktop().physicalDpiY()
        width_pouces = width_pixels / dpi_x
        height_pouces = height_pixels / dpi_y

        # Set display size
        plt.gcf().set_size_inches(width_pouces, height_pouces, forward=True)

        # Inforce graphic displaying
        plt.gcf().canvas.draw()

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
        forwardSpeed = self.ui.forwardSpeed_lineEdit.text()
        nozzleSpacing = self.ui.nozzleSpacing_lineEdit.text()
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
        if (is_float(forwardSpeed) == False):
            self.truevalue += 0
        else : self.truevalue += 1
        if (is_float(nozzleSpacing) == False):
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

        if (self.truevalue == 16):
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


    def roseSetting(self):
        roseSetting = QDialog()
        roseSetting.ui = ui_windrosesetting.Ui_Alert()
        roseSetting.ui.setupUi(roseSetting)

        #self.roseSetValue = constants.roseValue(self)[:, 1]
        #self.roseInitValue = self.roseSetValue

        roseSetting.ui.North_lineEdit.setText(str(self.roseSetValue[0]))
        roseSetting.ui.NorthEast_lineEdit.setText(str(self.roseSetValue[1]))
        roseSetting.ui.East_lineEdit.setText(str(self.roseSetValue[2]))
        roseSetting.ui.SouthEast_lineEdit.setText(str(self.roseSetValue[3]))
        roseSetting.ui.South_lineEdit.setText(str(self.roseSetValue[4]))
        roseSetting.ui.SouthWest_lineEdit.setText(str(self.roseSetValue[5]))
        roseSetting.ui.West_lineEdit.setText(str(self.roseSetValue[6]))
        roseSetting.ui.NorthWest_lineEdit.setText(str(self.roseSetValue[7]))

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

        def graphic_wind_rose(roseValue):
            probas = {
                'N': float(roseValue[0]),
                'NE': float(roseValue[1]),
                'E': float(roseValue[2]),
                'SE': float(roseValue[3]),
                'S': float(roseValue[4]),
                'SW': float(roseValue[5]),
                'W': float(roseValue[6]),
                'NW': float(roseValue[7])
            }
            # Data validation
            if len(probas) != 8:
                #raise ValueError("Le dictionnaire doit contenir 8 directions.")
                self.uiErreur()
            if not all(0 <= probas[direction] <= 1 for direction in probas):
                #raise ValueError("Les probabilités doivent être entre 0 et 1.")
                self.uiErreur()

            # Conversion des probabilités en fréquences (pour l'affichage)
            freqs = np.array(list(probas.values())) * 100

            # Création des directions en radians
            dirs_rad = np.deg2rad(np.array([0, 45, 90, 135, 180, 225, 270, 315]))

            # Création de la figure et des axes polaires
            fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

            # Largeur des barres
            width = np.deg2rad(45)  # 45 degrés en radians

            # Création des barres
            bars = ax.bar(dirs_rad, freqs, width=width, bottom=0.0)

            # Mise en page
            ax.set_theta_zero_location("N")  # Le zéro est au Nord
            ax.set_theta_direction(-1)  # Sens horaire
            ax.set_thetagrids(np.degrees(dirs_rad))  # Affiche les degrés
            #ax.set_title("Rose des vents des probabilités directionnelles")
            ax.set_rlabel_position(0)  # Position labels des rayons
            ax.set_rticks(np.linspace(0, max(freqs) + 10, 4))  # Ajuste les ticks radiaux
            ax.set_rlabel_position(22.5)  # Positionne les labels radiaux au milieu des barres

            # Ajout des étiquettes de direction (N, NE, E, etc.)
            direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
            ax.set_xticklabels(direction_labels)

            plt.gcf().set_size_inches(4.0, 2.7, forward=True)  # Set imagesize

            # Convert the matplotlib figure to QPixmap
            self.figure_pixmap = fig_to_pixmap(plt.gcf())

            # Create a QGraphicsPixmapItem to display the image
            self.graphicSceneWindRose = QGraphicsScene()
            self.graphicSceneWindRose.addPixmap(self.figure_pixmap)

            # Set the QGraphicsView
            roseSetting.ui.roseWind_graphicsView.setScene(self.graphicSceneWindRose)

        graphic_wind_rose(self.roseSetValue)

        def addRose():
            def is_float(string):
                try:
                    float(string)
                    return True
                except ValueError:
                    return False

            self.N_value = roseSetting.ui.North_lineEdit.text()
            self.NE_value = roseSetting.ui.NorthEast_lineEdit.text()
            self.E_value = roseSetting.ui.East_lineEdit.text()
            self.SE_value = roseSetting.ui.SouthEast_lineEdit.text()
            self.S_value = roseSetting.ui.South_lineEdit.text()
            self.SW_value = roseSetting.ui.SouthWest_lineEdit.text()
            self.W_value = roseSetting.ui.West_lineEdit.text()
            self.NW_value = roseSetting.ui.NorthWest_lineEdit.text()

            value = 0
            som = 0
            if (is_float(self.N_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.N_value)
            if (is_float(self.NE_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.NE_value)
            if (is_float(self.E_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.E_value)
            if (is_float(self.SE_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.SE_value)
            if (is_float(self.S_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.S_value)
            if (is_float(self.SW_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.SW_value)
            if (is_float(self.W_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.W_value)
            if (is_float(self.NW_value) == False):
                value += 0
            else:
                value += 1
                som += float(self.NW_value)
            if (value != 8 or round(som, 6) != 1.000000):
                self.uiErreur()
            else:
                self.roseSetValue = [self.N_value, self.NE_value, self.E_value, self.SE_value,
                                     self.S_value, self.SW_value, self.W_value, self.NW_value]
                graphic_wind_rose(self.roseSetValue)


        def resetRose():
            self.roseInitValue = constants.roseValue(self)[:, 1]
            roseSetting.ui.North_lineEdit.setText(self.roseInitValue[0])
            roseSetting.ui.NorthEast_lineEdit.setText(self.roseInitValue[1])
            roseSetting.ui.East_lineEdit.setText(self.roseInitValue[2])
            roseSetting.ui.SouthEast_lineEdit.setText(self.roseInitValue[3])
            roseSetting.ui.South_lineEdit.setText(self.roseInitValue[4])
            roseSetting.ui.SouthWest_lineEdit.setText(self.roseInitValue[5])
            roseSetting.ui.West_lineEdit.setText(self.roseInitValue[6])
            roseSetting.ui.NorthWest_lineEdit.setText(self.roseInitValue[7])
            graphic_wind_rose(self.roseInitValue)
            self.roseSetValue = self.roseInitValue

        def toMain():
            roseSetting.close()

        roseSetting.ui.saveBtn.clicked.connect(addRose)
        roseSetting.ui.resetBtn.clicked.connect(resetRose)
        roseSetting.ui.backBtn.clicked.connect(toMain)

        roseSetting.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
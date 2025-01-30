# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeJjGYNu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QRectF)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QPen, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(950, 665)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        #MainWindow.setMinimumSize(QSize(950, 665))
        #MainWindow.setMaximumSize(QSize(950, 665))
        icon = QIcon()
        icon.addFile(u"Im/Ico_DRIMERA.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(30, 24))
        self.actionOuvrir = QAction(MainWindow)
        self.actionOuvrir.setObjectName(u"actionOuvrir")
        self.actionNouveau = QAction(MainWindow)
        self.actionNouveau.setObjectName(u"actionNouveau")
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionAide = QAction(MainWindow) ###
        self.actionAide.setObjectName(u"actionAide") ###
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralLayout = QHBoxLayout()
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setContentsMargins(10, 10, 10, 10)
        self.inputLayout = QVBoxLayout()
        self.inputLayout.setSpacing(10)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputGrpBox = QGroupBox(self.centralwidget)
        self.inputGrpBox.setObjectName(u"inputGrpBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputGrpBox.sizePolicy().hasHeightForWidth())
        self.inputGrpBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(False)
        self.inputGrpBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.inputGrpBox)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.groupBox_spray_mixture = QGroupBox(self.inputGrpBox)
        self.groupBox_spray_mixture.setObjectName(u"groupBox_spray_mixture")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_spray_mixture)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_spray_mixture = QGridLayout()
        self.gridLayout_spray_mixture.setObjectName(u"gridLayout_spray_mixture")
        self.gridLayout_spray_mixture.setVerticalSpacing(6)
        self.carrierVol_lineEdit = QLineEdit(self.groupBox_spray_mixture)
        self.carrierVol_lineEdit.setObjectName(u"carrierVol_lineEdit")

        self.gridLayout_spray_mixture.addWidget(self.carrierVol_lineEdit, 3, 1, 1, 1)

        self.supportCarac_comboBox = QComboBox(self.groupBox_spray_mixture)
        self.supportCarac_comboBox.addItem(u"Oil")
        self.supportCarac_comboBox.addItem(u"Water")
        self.supportCarac_comboBox.setObjectName(u"supportCarac_comboBox")

        self.gridLayout_spray_mixture.addWidget(self.supportCarac_comboBox, 2, 1, 1, 1)

        self.supportCarac_toolButton = QToolButton(self.groupBox_spray_mixture)
        self.supportCarac_toolButton.setObjectName(u"supportCarac_toolButton")
        icon1 = QIcon()
        icon1.addFile(u"Im/tools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supportCarac_toolButton.setIcon(icon1)

        self.gridLayout_spray_mixture.addWidget(self.supportCarac_toolButton, 2, 2, 1, 1)

        self.label_pesticideUsed = QLabel(self.groupBox_spray_mixture)
        self.label_pesticideUsed.setObjectName(u"label_pesticideUsed")
        self.label_pesticideUsed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_spray_mixture.addWidget(self.label_pesticideUsed, 0, 0, 1, 1)

        self.pesticideUsed_comboBox = QComboBox(self.groupBox_spray_mixture)
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.addItem("")
        self.pesticideUsed_comboBox.setObjectName(u"pesticideUsed_comboBox")

        self.gridLayout_spray_mixture.addWidget(self.pesticideUsed_comboBox, 0, 1, 1, 1)

        self.label_pesticideVol = QLabel(self.groupBox_spray_mixture)
        self.label_pesticideVol.setObjectName(u"label_pesticideVol")
        self.label_pesticideVol.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_spray_mixture.addWidget(self.label_pesticideVol, 1, 0, 1, 1)

        self.label_supportCarac = QLabel(self.groupBox_spray_mixture)
        self.label_supportCarac.setObjectName(u"label_supportCarac")
        self.label_supportCarac.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_spray_mixture.addWidget(self.label_supportCarac, 2, 0, 1, 1)

        self.activeMatCarac_toolButton = QToolButton(self.groupBox_spray_mixture)
        self.activeMatCarac_toolButton.setObjectName(u"activeMatCarac_toolButton")
        self.activeMatCarac_toolButton.setIcon(icon1)

        self.gridLayout_spray_mixture.addWidget(self.activeMatCarac_toolButton, 0, 2, 1, 1)

        self.label_CarrierVol = QLabel(self.groupBox_spray_mixture)
        self.label_CarrierVol.setObjectName(u"label_CarrierVol")
        self.label_CarrierVol.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_spray_mixture.addWidget(self.label_CarrierVol, 3, 0, 1, 1)

        self.pesticideVol_lineEdit = QLineEdit(self.groupBox_spray_mixture)
        self.pesticideVol_lineEdit.setObjectName(u"pesticideVol_lineEdit")

        self.gridLayout_spray_mixture.addWidget(self.pesticideVol_lineEdit, 1, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_spray_mixture)


        self.verticalLayout_2.addWidget(self.groupBox_spray_mixture)

        self.groupBox_operational_data = QGroupBox(self.inputGrpBox)
        self.groupBox_operational_data.setObjectName(u"groupBox_operational_data")
        sizePolicy.setHeightForWidth(self.groupBox_operational_data.sizePolicy().hasHeightForWidth())
        self.groupBox_operational_data.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_operational_data)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_operational_data = QGridLayout()
        self.gridLayout_operational_data.setObjectName(u"gridLayout_operational_data")
        self.residualConc_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.residualConc_lineEdit.setObjectName(u"residualConc_lineEdit")

        self.gridLayout_operational_data.addWidget(self.residualConc_lineEdit, 5, 1, 1, 1)

        self.dropletSize_comboBox = QComboBox(self.groupBox_operational_data)
        self.dropletSize_comboBox.addItem(u"Fog")
        self.dropletSize_comboBox.addItem(u"Very fine")
        self.dropletSize_comboBox.addItem(u"Medium")
        self.dropletSize_comboBox.addItem(u"Coarse")
        self.dropletSize_comboBox.addItem(u"Fine rain")
        self.dropletSize_comboBox.setObjectName(u"dropletSize_comboBox")

        self.gridLayout_operational_data.addWidget(self.dropletSize_comboBox, 3, 1, 1, 1)

        self.boomHeight_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.boomHeight_lineEdit.setObjectName(u"boomHeight_lineEdit")

        self.gridLayout_operational_data.addWidget(self.boomHeight_lineEdit, 0, 1, 1, 1)

        self.appRate_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.appRate_lineEdit.setObjectName(u"appRate_lineEdit")

        self.gridLayout_operational_data.addWidget(self.appRate_lineEdit, 1, 1, 1, 1)

        self.label_boomHeight = QLabel(self.groupBox_operational_data)
        self.label_boomHeight.setObjectName(u"label_boomHeight")
        self.label_boomHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_boomHeight, 0, 0, 1, 1)

        self.label_appRate = QLabel(self.groupBox_operational_data)
        self.label_appRate.setObjectName(u"label_appRate")
        self.label_appRate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_appRate, 1, 0, 1, 1)

        self.label_residualConc = QLabel(self.groupBox_operational_data)
        self.label_residualConc.setObjectName(u"label_residualConc")
        self.label_residualConc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_residualConc, 5, 0, 1, 1)

        self.nozzleSpacing_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.nozzleSpacing_lineEdit.setObjectName(u"nozzleSpacing_lineEdit")

        self.gridLayout_operational_data.addWidget(self.nozzleSpacing_lineEdit, 2, 1, 1, 1)

        self.label_dropletSize = QLabel(self.groupBox_operational_data)
        self.label_dropletSize.setObjectName(u"label_dropletSize")
        self.label_dropletSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_dropletSize, 3, 0, 1, 1)

        self.forwardSpeed_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.forwardSpeed_lineEdit.setObjectName(u"forwardSpeed_lineEdit")

        self.gridLayout_operational_data.addWidget(self.forwardSpeed_lineEdit, 4, 1, 1, 1)

        self.label_nozzleSpac = QLabel(self.groupBox_operational_data)
        self.label_nozzleSpac.setObjectName(u"label_nozzleSpac")
        self.label_nozzleSpac.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_nozzleSpac, 2, 0, 1, 1)

        self.label_forwardSpeed = QLabel(self.groupBox_operational_data)
        self.label_forwardSpeed.setObjectName(u"label_forwardSpeed")
        self.label_forwardSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_forwardSpeed, 4, 0, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_operational_data)


        self.verticalLayout_2.addWidget(self.groupBox_operational_data)

        self.groupBox_meteorological_data = QGroupBox(self.inputGrpBox)
        self.groupBox_meteorological_data.setObjectName(u"groupBox_meteorological_data")
        sizePolicy.setHeightForWidth(self.groupBox_meteorological_data.sizePolicy().hasHeightForWidth())
        self.groupBox_meteorological_data.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_meteorological_data)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_meteorological_data = QGridLayout()
        self.gridLayout_meteorological_data.setObjectName(u"gridLayout_meteorological_data")
        self.label_windSpeed = QLabel(self.groupBox_meteorological_data)
        self.label_windSpeed.setObjectName(u"label_windSpeed")
        self.label_windSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_meteorological_data.addWidget(self.label_windSpeed, 0, 0, 1, 1)

        self.label_temperature = QLabel(self.groupBox_meteorological_data)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_meteorological_data.addWidget(self.label_temperature, 1, 0, 1, 1)

        self.windSpeed_lineEdit = QLineEdit(self.groupBox_meteorological_data)
        self.windSpeed_lineEdit.setObjectName(u"windSpeed_lineEdit")

        self.gridLayout_meteorological_data.addWidget(self.windSpeed_lineEdit, 0, 1, 1, 1)



        self.roseWind_toolButton = QToolButton(self.groupBox_meteorological_data)
        self.roseWind_toolButton.setObjectName(u"roseWind_toolButton")
        self.roseWind_toolButton.setIcon(icon1)

        self.gridLayout_meteorological_data.addWidget(self.roseWind_toolButton, 0, 2, 1, 1)



        self.temperature_lineEdit = QLineEdit(self.groupBox_meteorological_data)
        self.temperature_lineEdit.setObjectName(u"temperature_lineEdit")

        self.gridLayout_meteorological_data.addWidget(self.temperature_lineEdit, 1, 1, 1, 1)

        self.label_humidity = QLabel(self.groupBox_meteorological_data)
        self.label_humidity.setObjectName(u"label_humidity")
        self.label_humidity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_meteorological_data.addWidget(self.label_humidity, 2, 0, 1, 1)

        self.humidity_lineEdit = QLineEdit(self.groupBox_meteorological_data)
        self.humidity_lineEdit.setObjectName(u"humidity_lineEdit")

        self.gridLayout_meteorological_data.addWidget(self.humidity_lineEdit, 2, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_meteorological_data)


        self.verticalLayout_2.addWidget(self.groupBox_meteorological_data)


        self.inputLayout.addWidget(self.inputGrpBox)


        self.centralLayout.addLayout(self.inputLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.centralLayout.addWidget(self.line)

        self.resultLayout = QHBoxLayout()
        self.resultLayout.setObjectName(u"resultLayout")
        self.resultGrpBox = QGroupBox(self.centralwidget)
        self.resultGrpBox.setObjectName(u"resultGrpBox")
        sizePolicy.setHeightForWidth(self.resultGrpBox.sizePolicy().hasHeightForWidth())
        self.resultGrpBox.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.resultGrpBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_calculus = QGridLayout()
        self.gridLayout_calculus.setObjectName(u"gridLayout_calculus")
        self.label_timeStep = QLabel(self.resultGrpBox)
        self.label_timeStep.setObjectName(u"label_timeStep")
        self.label_timeStep.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_calculus.addWidget(self.label_timeStep, 1, 6, 1, 1)

        self.label_y0 = QLabel(self.resultGrpBox)
        self.label_y0.setObjectName(u"label_y0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_y0.sizePolicy().hasHeightForWidth())
        self.label_y0.setSizePolicy(sizePolicy2)

        self.gridLayout_calculus.addWidget(self.label_y0, 1, 3, 1, 1)

        self.y0_lineEdit = QLineEdit(self.resultGrpBox)
        self.y0_lineEdit.setObjectName(u"y0_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.y0_lineEdit.sizePolicy().hasHeightForWidth())
        self.y0_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_calculus.addWidget(self.y0_lineEdit, 1, 4, 1, 1)

        self.label_hotspot = QLabel(self.resultGrpBox)
        self.label_hotspot.setObjectName(u"label_hotspot")
        self.label_hotspot.setLayoutDirection(Qt.LeftToRight)
        self.label_hotspot.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_calculus.addWidget(self.label_hotspot, 1, 0, 1, 1)

        self.label_x0 = QLabel(self.resultGrpBox)
        self.label_x0.setObjectName(u"label_x0")
        sizePolicy2.setHeightForWidth(self.label_x0.sizePolicy().hasHeightForWidth())
        self.label_x0.setSizePolicy(sizePolicy2)

        self.gridLayout_calculus.addWidget(self.label_x0, 1, 1, 1, 1)

        self.timeStep_lineEdit = QLineEdit(self.resultGrpBox)
        self.timeStep_lineEdit.setObjectName(u"timeStep_lineEdit")
        sizePolicy3.setHeightForWidth(self.timeStep_lineEdit.sizePolicy().hasHeightForWidth())
        self.timeStep_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_calculus.addWidget(self.timeStep_lineEdit, 1, 7, 1, 1)

        self.x0_lineEdit = QLineEdit(self.resultGrpBox)
        self.x0_lineEdit.setObjectName(u"x0_lineEdit")
        sizePolicy3.setHeightForWidth(self.x0_lineEdit.sizePolicy().hasHeightForWidth())
        self.x0_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_calculus.addWidget(self.x0_lineEdit, 1, 2, 1, 1)

        self.calculBtn = QPushButton(self.resultGrpBox)
        self.calculBtn.setObjectName(u"calculBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calculBtn.sizePolicy().hasHeightForWidth())
        self.calculBtn.setSizePolicy(sizePolicy4)
        self.calculBtn.setFocusPolicy(Qt.StrongFocus)
        icon2 = QIcon()
        icon2.addFile(u"Im/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calculBtn.setIcon(icon2)
        self.calculBtn.setIconSize(QSize(20, 20))

        self.gridLayout_calculus.addWidget(self.calculBtn, 1, 9, 1, 1)

        self.label = QLabel(self.resultGrpBox)
        self.label.setObjectName(u"label")

        self.gridLayout_calculus.addWidget(self.label, 1, 5, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_calculus)


        self.resultTabWidget_result = QTabWidget(self.resultGrpBox)
        self.resultTabWidget_result.setObjectName(u"resultTabWidget_result")
        self.resultTabWidget_result.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.resultTabWidget_result.sizePolicy().hasHeightForWidth())
        self.resultTabWidget_result.setSizePolicy(sizePolicy5)
        #self.resultTabWidget_result.setMinimumSize(QSize(565, 431))
        #self.resultTabWidget_result.setMaximumSize(QSize(565, 431))
        self.resultTabWidget_result.setTabShape(QTabWidget.Rounded)
        self.resultTabWidget_result.setIconSize(QSize(13, 20))
        self.resultTabWidget_result.setElideMode(Qt.ElideRight)
        self.resultTabWidget_result.setDocumentMode(False)
        self.resultTabWidget_result.setTabsClosable(False)
        self.resultTabWidget_result.setMovable(False)
        self.resultTabWidget_result.setTabBarAutoHide(False)
        """
        self.tabPlot_result = QWidget()
        self.tabPlot_result.setObjectName(u"tabPlot_result")
        self.tabPlot_result.setSizeIncrement(QSize(0, 0))
        self.result_graphicsView = QGraphicsView(self.tabPlot_result)
        self.result_graphicsView.setObjectName(u"result_graphicsView")
        #self.result_graphicsView.setGeometry(QRect(1, 1, 557, 397)) ##
        self.result_graphicsView.setGeometry(QRect(1, 1, self.tabPlot_result.width(), self.tabPlot_result.height()))  ##
        sizePolicy5.setHeightForWidth(self.result_graphicsView.sizePolicy().hasHeightForWidth())
        self.result_graphicsView.setSizePolicy(sizePolicy5)
        #self.result_graphicsView.setMinimumSize(QSize(557, 397))
        #self.result_graphicsView.setMaximumSize(QSize(557, 397))
        icon3 = QIcon()
        icon3.addFile(u"Im/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabPlot_result, icon3, "")
        self.tabData_result = QWidget()
        self.tabData_result.setObjectName(u"tabData_result")
        sizePolicy5.setHeightForWidth(self.tabData_result.sizePolicy().hasHeightForWidth())
        self.tabData_result.setSizePolicy(sizePolicy5)
        self.tableView = QTableView(self.tabData_result)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(1, 1, 557, 397)) ##
        sizePolicy5.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy5)
        self.tableView.setMinimumSize(QSize(557, 397))
        self.tableView.setMaximumSize(QSize(557, 397))"""


        # Tab Plot
        self.tabPlot_result = QWidget()
        self.tabPlot_result.setObjectName(u"tabPlot_result")
        plot_layout = QVBoxLayout(self.tabPlot_result)  # Layout pour le tabPlot
        self.result_graphicsView = QGraphicsView(self.tabPlot_result)
        self.result_graphicsView.setObjectName(u"result_graphicsView")
        self.result_graphicsView.setSizePolicy(sizePolicy5)
        plot_layout.addWidget(self.result_graphicsView)  # Ajout du graphicsView au layout
        icon3 = QIcon()
        icon3.addFile(u"Im/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabPlot_result, icon3, "Plot")  # Ajout du tab avec le layout

        # Tab Data
        self.tabData_result = QWidget()
        self.tabData_result.setObjectName(u"tabData_result")
        data_layout = QVBoxLayout(self.tabData_result)  # Layout pour le tabData
        self.tableView = QTableView(self.tabData_result)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSizePolicy(sizePolicy)
        data_layout.addWidget(self.tableView)  # Ajout du tableView au layout
        icon4 = QIcon()
        icon4.addFile(u"Im/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabData_result, icon4, "Data")  # Ajout du tab avec le layout

        # Ajout du tabwidget au groupbox
        layoutGroupBox = QVBoxLayout(self.resultGrpBox)
        layoutGroupBox.addWidget(self.resultTabWidget_result)

        self.scene = QGraphicsScene()
        self.result_graphicsView.setScene(self.scene)
        self.scene_rect = self.scene.addRect(QRectF(0, 0, 0, 0), QPen(Qt.black), QBrush(Qt.white))
        self.resizeEvent = self.onResize




        icon4 = QIcon()
        icon4.addFile(u"Im/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabData_result, icon4, "")

        self.verticalLayout_8.addWidget(self.resultTabWidget_result)

        self.gridLayout_zposition = QGridLayout()
        self.gridLayout_zposition.setObjectName(u"gridLayout_zposition")
        self.zposition_lineEdit = QLineEdit(self.resultGrpBox)
        self.zposition_lineEdit.setObjectName(u"zposition_lineEdit")
        #sizePolicy5.setHeightForWidth(self.zposition_lineEdit.sizePolicy().hasHeightForWidth())
        self.zposition_lineEdit.setSizePolicy(sizePolicy4)
        self.zposition_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_zposition.addWidget(self.zposition_lineEdit, 0, 1, 1, 1)

        self.label_z = QLabel(self.resultGrpBox)
        self.label_z.setObjectName(u"label_z")

        self.gridLayout_zposition.addWidget(self.label_z, 0, 0, 1, 1)

        self.zposition_horizontalSlider = QSlider(self.resultGrpBox)
        self.zposition_horizontalSlider.setObjectName(u"zposition_horizontalSlider")
        self.zposition_horizontalSlider.setMaximum(9)
        self.zposition_horizontalSlider.setPageStep(1)
        self.zposition_horizontalSlider.setValue(9)
        self.zposition_horizontalSlider.setSliderPosition(9)
        self.zposition_horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_zposition.addWidget(self.zposition_horizontalSlider, 0, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_zposition)

        self.downloadBtn = QPushButton(self.resultGrpBox)
        self.downloadBtn.setObjectName(u"downloadBtn")
        sizePolicy4.setHeightForWidth(self.downloadBtn.sizePolicy().hasHeightForWidth())
        self.downloadBtn.setSizePolicy(sizePolicy4)
        self.downloadBtn.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"Im/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downloadBtn.setIcon(icon5)
        self.downloadBtn.setIconSize(QSize(17, 19))

        self.verticalLayout_8.addWidget(self.downloadBtn)


        self.resultLayout.addWidget(self.resultGrpBox)


        self.centralLayout.addLayout(self.resultLayout)


        self.verticalLayout.addLayout(self.centralLayout)

        self.appversion = QLabel(self.centralwidget)
        self.appversion.setObjectName(u"appversion")
        self.appversion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.appversion.setMargin(0)
        self.appversion.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.appversion)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        #self.menubar.addAction(self.menuAide.menuAction())
        self.menubar.addAction(self.actionAide)
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        self.supportCarac_comboBox.setCurrentIndex(-1)
        self.pesticideUsed_comboBox.setCurrentIndex(-1)
        self.dropletSize_comboBox.setCurrentIndex(-1)
        self.resultTabWidget_result.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def onResize(self, event):
        self.scene.setSceneRect(
            QRectF(0, 0, self.result_graphicsView.viewport().width(), self.result_graphicsView.viewport().height()))
        self.scene_rect.setRect(
            QRectF(0, 0, self.result_graphicsView.viewport().width(), self.result_graphicsView.viewport().height()))
        QWidget.resizeEvent(self, event)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DRIMERA", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNouveau.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAide.setIconText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.inputGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.groupBox_spray_mixture.setTitle(QCoreApplication.translate("MainWindow", u"Spray mixture", None))

        self.supportCarac_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_pesticideUsed.setText(QCoreApplication.translate("MainWindow", u"Pesticide used", None))
        self.pesticideUsed_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Bankit 25 SC", None))
        self.pesticideUsed_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Banko 720 SC", None))
        self.pesticideUsed_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Cabrio EG", None))
        self.pesticideUsed_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Calixine 75 EC", None))
        self.pesticideUsed_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Callis 400 OL", None))
        self.pesticideUsed_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Folicur 250 EW-Junior", None))
        self.pesticideUsed_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Impulse 075 EC", None))
        self.pesticideUsed_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Ivory 80 WP", None))
        self.pesticideUsed_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Opal 7.5 EC", None))
        self.pesticideUsed_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Sico 250 EC", None))
        self.pesticideUsed_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Siganex 600 SC", None))
        self.pesticideUsed_comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Syllit 400 SC", None))
        self.pesticideUsed_comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"T\u00e9ga 075 EC", None))
        self.pesticideUsed_comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"Thiram 75 WP", None))
        self.pesticideUsed_comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Tilt 250 EC", None))
        self.pesticideUsed_comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Trical 250 EC", None))
        self.pesticideUsed_comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Volley 88 OL", None))

        self.label_pesticideVol.setText(QCoreApplication.translate("MainWindow", u"Pesticide volume (l)", None))
        self.label_supportCarac.setText(QCoreApplication.translate("MainWindow", u"Carrier material", None))
        self.activeMatCarac_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.roseWind_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_CarrierVol.setText(QCoreApplication.translate("MainWindow", u"Carrier volume (l)", None))
        self.groupBox_operational_data.setTitle(QCoreApplication.translate("MainWindow", u"Operational data", None))

        self.label_boomHeight.setText(QCoreApplication.translate("MainWindow", u"Boom height (m)", None))
        self.label_appRate.setText(QCoreApplication.translate("MainWindow", u"Application rate (l/ha)", None))
        self.label_residualConc.setText(QCoreApplication.translate("MainWindow", u"Ground concentration (\u00b5g/l)", None))
        self.label_dropletSize.setText(QCoreApplication.translate("MainWindow", u"Spray particle size", None))
        self.label_nozzleSpac.setText(QCoreApplication.translate("MainWindow", u"Nozzle spacing (cm)", None))
        self.label_forwardSpeed.setText(QCoreApplication.translate("MainWindow", u"Forward speed (m/s)", None))
        self.groupBox_meteorological_data.setTitle(QCoreApplication.translate("MainWindow", u"Meteorological data", None))
        self.label_windSpeed.setText(QCoreApplication.translate("MainWindow", u"Wind speed (m/s)", None))
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0C)", None))
        self.label_humidity.setText(QCoreApplication.translate("MainWindow", u"Relative humidity (%)", None))
        self.resultGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.label_timeStep.setText(QCoreApplication.translate("MainWindow", u"Times step (s)", None))
        self.label_y0.setText(QCoreApplication.translate("MainWindow", u", y =", None))
        self.label_hotspot.setText(QCoreApplication.translate("MainWindow", u"Ejection point (m) :", None))
        self.label_x0.setText(QCoreApplication.translate("MainWindow", u"x =", None))
        self.calculBtn.setText(QCoreApplication.translate("MainWindow", u"Calculus", None))
        self.label.setText("")
        self.resultTabWidget_result.setTabText(self.resultTabWidget_result.indexOf(self.tabPlot_result), QCoreApplication.translate("MainWindow", u"Plot", None))
        self.resultTabWidget_result.setTabText(self.resultTabWidget_result.indexOf(self.tabData_result), QCoreApplication.translate("MainWindow", u"Datasheet", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"Z position (m) :", None))
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.appversion.setText(QCoreApplication.translate("MainWindow", u"v 1.0.0   ", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


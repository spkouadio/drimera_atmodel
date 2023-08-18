# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homejJnZKP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(797, 526)
        MainWindow.setMaximumSize(QSize(797, 526))
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        self.supportCarac_comboBox.addItem(u"Water")
        self.supportCarac_comboBox.addItem(u"Oil")
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
        self.pesticideUsed_comboBox.addItem(u"Chlorothalonil")
        self.pesticideUsed_comboBox.addItem(u"Difenoconazol")
        self.pesticideUsed_comboBox.addItem(u"Dodin")
        self.pesticideUsed_comboBox.addItem(u"Epoxiconazol")
        self.pesticideUsed_comboBox.addItem(u"Fenpropimorph")
        self.pesticideUsed_comboBox.addItem(u"Mancozeb")
        self.pesticideUsed_comboBox.addItem(u"Propiconazol")
        self.pesticideUsed_comboBox.addItem(u"Pyraclostrobin")
        self.pesticideUsed_comboBox.addItem(u"Pyrimethanil")
        self.pesticideUsed_comboBox.addItem(u"Spiroxamin")
        self.pesticideUsed_comboBox.addItem(u"Thiram")
        self.pesticideUsed_comboBox.addItem(u"Tebuconazol")
        self.pesticideUsed_comboBox.addItem(u"Triadimefon")
        self.pesticideUsed_comboBox.addItem(u"Tridemorph")
        self.pesticideUsed_comboBox.addItem(u"Trifloxystrobin")
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
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_operational_data)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_operational_data = QGridLayout()
        self.gridLayout_operational_data.setObjectName(u"gridLayout_operational_data")
        self.label_residualConc = QLabel(self.groupBox_operational_data)
        self.label_residualConc.setObjectName(u"label_residualConc")
        self.label_residualConc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_residualConc, 3, 0, 1, 1)

        self.label_boomHeight = QLabel(self.groupBox_operational_data)
        self.label_boomHeight.setObjectName(u"label_boomHeight")
        self.label_boomHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_boomHeight, 0, 0, 1, 1)

        self.residualConc_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.residualConc_lineEdit.setObjectName(u"residualConc_lineEdit")

        self.gridLayout_operational_data.addWidget(self.residualConc_lineEdit, 3, 1, 1, 1)

        self.boomHeight_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.boomHeight_lineEdit.setObjectName(u"boomHeight_lineEdit")

        self.gridLayout_operational_data.addWidget(self.boomHeight_lineEdit, 0, 1, 1, 1)

        self.appRate_lineEdit = QLineEdit(self.groupBox_operational_data)
        self.appRate_lineEdit.setObjectName(u"appRate_lineEdit")

        self.gridLayout_operational_data.addWidget(self.appRate_lineEdit, 1, 1, 1, 1)

        self.label_appRate = QLabel(self.groupBox_operational_data)
        self.label_appRate.setObjectName(u"label_appRate")
        self.label_appRate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_appRate, 1, 0, 1, 1)

        self.label_dropletSize = QLabel(self.groupBox_operational_data)
        self.label_dropletSize.setObjectName(u"label_dropletSize")
        self.label_dropletSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_operational_data.addWidget(self.label_dropletSize, 2, 0, 1, 1)

        self.dropletSize_comboBox = QComboBox(self.groupBox_operational_data)
        self.dropletSize_comboBox.addItem(u"Fog")
        self.dropletSize_comboBox.addItem(u"Very fine")
        self.dropletSize_comboBox.addItem(u"Medium")
        self.dropletSize_comboBox.addItem(u"Coarse")
        self.dropletSize_comboBox.addItem(u"Fine rain")
        self.dropletSize_comboBox.setObjectName(u"dropletSize_comboBox")

        self.gridLayout_operational_data.addWidget(self.dropletSize_comboBox, 2, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_operational_data)


        self.verticalLayout_2.addWidget(self.groupBox_operational_data)

        self.groupBox_meteorological_data = QGroupBox(self.inputGrpBox)
        self.groupBox_meteorological_data.setObjectName(u"groupBox_meteorological_data")
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
        self.verticalLayout_8 = QVBoxLayout(self.resultGrpBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_calculus = QGridLayout()
        self.gridLayout_calculus.setObjectName(u"gridLayout_calculus")
        self.label_timeStep = QLabel(self.resultGrpBox)
        self.label_timeStep.setObjectName(u"label_timeStep")
        self.label_timeStep.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_calculus.addWidget(self.label_timeStep, 0, 0, 1, 1)

        self.timeStep_lineEdit = QLineEdit(self.resultGrpBox)
        self.timeStep_lineEdit.setObjectName(u"timeStep_lineEdit")

        self.gridLayout_calculus.addWidget(self.timeStep_lineEdit, 0, 1, 1, 1)

        self.calculBtn = QPushButton(self.resultGrpBox)
        self.calculBtn.setObjectName(u"calculBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.calculBtn.sizePolicy().hasHeightForWidth())
        self.calculBtn.setSizePolicy(sizePolicy2)
        self.calculBtn.setFocusPolicy(Qt.StrongFocus)
        icon2 = QIcon()
        icon2.addFile(u"Im/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calculBtn.setIcon(icon2)
        self.calculBtn.setIconSize(QSize(20, 20))

        self.gridLayout_calculus.addWidget(self.calculBtn, 0, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_calculus)

        self.resultTabWidget_result = QTabWidget(self.resultGrpBox)
        self.resultTabWidget_result.setObjectName(u"resultTabWidget_result")
        self.resultTabWidget_result.setEnabled(True)
        self.resultTabWidget_result.setMaximumSize(QSize(850, 630))
        self.resultTabWidget_result.setTabShape(QTabWidget.Rounded)
        self.resultTabWidget_result.setIconSize(QSize(13, 20))
        self.resultTabWidget_result.setElideMode(Qt.ElideRight)
        self.resultTabWidget_result.setDocumentMode(False)
        self.resultTabWidget_result.setTabsClosable(False)
        self.resultTabWidget_result.setMovable(False)
        self.resultTabWidget_result.setTabBarAutoHide(False)
        self.tabPlot_result = QWidget()
        self.tabPlot_result.setObjectName(u"tabPlot_result")
        self.tabPlot_result.setSizeIncrement(QSize(0, 0))
        self.result_graphicsView = QGraphicsView(self.tabPlot_result)
        self.result_graphicsView.setObjectName(u"result_graphicsView")
        self.result_graphicsView.setGeometry(QRect(-5, -9, 551, 491))
        self.result_graphicsView.setMaximumSize(QSize(850, 630))
        icon3 = QIcon()
        icon3.addFile(u"Im/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabPlot_result, icon3, "")
        self.tabData_result = QWidget()
        self.tabData_result.setObjectName(u"tabData_result")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabData_result.sizePolicy().hasHeightForWidth())
        self.tabData_result.setSizePolicy(sizePolicy3)
        self.tableView = QTableView(self.tabData_result)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 551, 471))
        icon4 = QIcon()
        icon4.addFile(u"Im/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget_result.addTab(self.tabData_result, icon4, "")

        self.verticalLayout_8.addWidget(self.resultTabWidget_result)

        self.downloadBtn = QPushButton(self.resultGrpBox)
        self.downloadBtn.setObjectName(u"downloadBtn")
        sizePolicy2.setHeightForWidth(self.downloadBtn.sizePolicy().hasHeightForWidth())
        self.downloadBtn.setSizePolicy(sizePolicy2)
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
        self.menubar.setGeometry(QRect(0, 0, 797, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        self.supportCarac_comboBox.setCurrentIndex(-1)
        self.pesticideUsed_comboBox.setCurrentIndex(-1)
        self.dropletSize_comboBox.setCurrentIndex(-1)
        self.resultTabWidget_result.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DRIMERA", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNouveau.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionQuitter.setIconText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.inputGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.groupBox_spray_mixture.setTitle(QCoreApplication.translate("MainWindow", u"Spray mixture", None))

        self.supportCarac_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_pesticideUsed.setText(QCoreApplication.translate("MainWindow", u"Pesticide used", None))

        self.label_pesticideVol.setText(QCoreApplication.translate("MainWindow", u"Pesticide volume (l)", None))
        self.label_supportCarac.setText(QCoreApplication.translate("MainWindow", u"Carrier material", None))
        self.activeMatCarac_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_CarrierVol.setText(QCoreApplication.translate("MainWindow", u"Carrier volume (l)", None))
        self.groupBox_operational_data.setTitle(QCoreApplication.translate("MainWindow", u"Operational data", None))
        self.label_residualConc.setText(QCoreApplication.translate("MainWindow", u"Residual concentration (\u00b5g/l)", None))
        self.label_boomHeight.setText(QCoreApplication.translate("MainWindow", u"Boom height (m)", None))
        self.label_appRate.setText(QCoreApplication.translate("MainWindow", u"Application rate (l/ha)", None))
        self.label_dropletSize.setText(QCoreApplication.translate("MainWindow", u"Spray particle size", None))

        self.groupBox_meteorological_data.setTitle(QCoreApplication.translate("MainWindow", u"Meteorological data", None))
        self.label_windSpeed.setText(QCoreApplication.translate("MainWindow", u"Wind speed (m/s)", None))
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0C)", None))
        self.label_humidity.setText(QCoreApplication.translate("MainWindow", u"Relative humidity (%)", None))
        self.resultGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.label_timeStep.setText(QCoreApplication.translate("MainWindow", u"Times step (s)", None))
        self.calculBtn.setText(QCoreApplication.translate("MainWindow", u"Calculus", None))
        self.resultTabWidget_result.setTabText(self.resultTabWidget_result.indexOf(self.tabPlot_result), QCoreApplication.translate("MainWindow", u"Plot", None))
        self.resultTabWidget_result.setTabText(self.resultTabWidget_result.indexOf(self.tabData_result), QCoreApplication.translate("MainWindow", u"Datasheet", None))
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.appversion.setText(QCoreApplication.translate("MainWindow", u"v 1.0.0   ", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


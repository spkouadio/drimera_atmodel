# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeOvdYgY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(800, 655)
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
        self.horizontalLayout = QHBoxLayout(self.inputGrpBox)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.atmosBtn = QPushButton(self.inputGrpBox)
        self.atmosBtn.setObjectName(u"atmosBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.atmosBtn.sizePolicy().hasHeightForWidth())
        self.atmosBtn.setSizePolicy(sizePolicy2)
        self.atmosBtn.setFocusPolicy(Qt.StrongFocus)
        icon1 = QIcon()
        icon1.addFile(u"Im/wind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.atmosBtn.setIcon(icon1)
        self.atmosBtn.setIconSize(QSize(20, 20))
        self.atmosBtn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.atmosBtn)

        self.terrainBtn = QPushButton(self.inputGrpBox)
        self.terrainBtn.setObjectName(u"terrainBtn")
        icon2 = QIcon()
        icon2.addFile(u"Im/terrain.png", QSize(), QIcon.Normal, QIcon.Off)
        self.terrainBtn.setIcon(icon2)
        self.terrainBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.terrainBtn)

        self.operaBtn = QPushButton(self.inputGrpBox)
        self.operaBtn.setObjectName(u"operaBtn")
        icon3 = QIcon()
        icon3.addFile(u"Im/airplane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.operaBtn.setIcon(icon3)
        self.operaBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.operaBtn)


        self.inputLayout.addWidget(self.inputGrpBox)

        self.paramStackedWidget = QStackedWidget(self.centralwidget)
        self.paramStackedWidget.setObjectName(u"paramStackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.paramStackedWidget.sizePolicy().hasHeightForWidth())
        self.paramStackedWidget.setSizePolicy(sizePolicy3)
        self.inputHome = QWidget()
        self.inputHome.setObjectName(u"inputHome")
        self.inputResume = QVBoxLayout(self.inputHome)
        self.inputResume.setObjectName(u"inputResume")
        self.paramGridLayout = QGridLayout()
        self.paramGridLayout.setObjectName(u"paramGridLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar_3 = QProgressBar(self.inputHome)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy2.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy2)
        self.progressBar_3.setValue(24)

        self.gridLayout.addWidget(self.progressBar_3, 2, 1, 1, 1)

        self.progressBar_2 = QProgressBar(self.inputHome)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy2.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy2)
        self.progressBar_2.setValue(24)

        self.gridLayout.addWidget(self.progressBar_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.inputHome)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.inputHome)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.inputHome)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 0, 1, 1, 1)

        self.label_4 = QLabel(self.inputHome)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)


        self.paramGridLayout.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.paramLevel = QLabel(self.inputHome)
        self.paramLevel.setObjectName(u"paramLevel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.paramLevel.sizePolicy().hasHeightForWidth())
        self.paramLevel.setSizePolicy(sizePolicy4)
        self.paramLevel.setAlignment(Qt.AlignCenter)

        self.paramGridLayout.addWidget(self.paramLevel, 0, 0, 1, 1)


        self.inputResume.addLayout(self.paramGridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.inputResume.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.inputHome)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.inputResume.addWidget(self.line_2)

        self.calculBtn = QPushButton(self.inputHome)
        self.calculBtn.setObjectName(u"calculBtn")
        self.calculBtn.setFocusPolicy(Qt.StrongFocus)
        icon4 = QIcon()
        icon4.addFile(u"Im/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calculBtn.setIcon(icon4)
        self.calculBtn.setIconSize(QSize(20, 20))

        self.inputResume.addWidget(self.calculBtn)

        self.asriskBtn = QPushButton(self.inputHome)
        self.asriskBtn.setObjectName(u"asriskBtn")
        icon5 = QIcon()
        icon5.addFile(u"Im/operation_risk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.asriskBtn.setIcon(icon5)
        self.asriskBtn.setIconSize(QSize(20, 20))

        self.inputResume.addWidget(self.asriskBtn)

        self.paramStackedWidget.addWidget(self.inputHome)
        self.paramAtmosphere = QWidget()
        self.paramAtmosphere.setObjectName(u"paramAtmosphere")
        self.parAtm = QVBoxLayout(self.paramAtmosphere)
        self.parAtm.setObjectName(u"parAtm")
        self.groupBox = QGroupBox(self.paramAtmosphere)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_5.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_5.addWidget(self.lineEdit_8, 1, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_5)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_6.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_6.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_6.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_6.addWidget(self.lineEdit_12, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_6)


        self.parAtm.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.paramAtmosphere)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.parAtm.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.paramAtmosphere)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.parAtm.addWidget(self.groupBox_4)

        self.atmosBtnBox = QDialogButtonBox(self.paramAtmosphere)
        self.atmosBtnBox.setObjectName(u"atmosBtnBox")
        self.atmosBtnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.parAtm.addWidget(self.atmosBtnBox)

        self.paramStackedWidget.addWidget(self.paramAtmosphere)
        self.paramTerrain = QWidget()
        self.paramTerrain.setObjectName(u"paramTerrain")
        self.parTer = QVBoxLayout(self.paramTerrain)
        self.parTer.setObjectName(u"parTer")
        self.groupBox_6 = QGroupBox(self.paramTerrain)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_15 = QLineEdit(self.groupBox_6)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_8.addWidget(self.lineEdit_15, 0, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_8.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_8)


        self.parTer.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.paramTerrain)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.checkBox = QCheckBox(self.groupBox_7)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_9.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_7)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_9.addWidget(self.checkBox_2, 0, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_9)


        self.parTer.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.paramTerrain)
        self.groupBox_8.setObjectName(u"groupBox_8")

        self.parTer.addWidget(self.groupBox_8)

        self.terBtnBox = QDialogButtonBox(self.paramTerrain)
        self.terBtnBox.setObjectName(u"terBtnBox")
        self.terBtnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.parTer.addWidget(self.terBtnBox)

        self.paramStackedWidget.addWidget(self.paramTerrain)
        self.paramOpera = QWidget()
        self.paramOpera.setObjectName(u"paramOpera")
        self.parOp = QVBoxLayout(self.paramOpera)
        self.parOp.setObjectName(u"parOp")
        self.groupBox_11 = QGroupBox(self.paramOpera)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_29 = QLabel(self.groupBox_11)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_29, 1, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.groupBox_11)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_12.addWidget(self.lineEdit_25, 0, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_30, 2, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.groupBox_11)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_12.addWidget(self.lineEdit_26, 1, 1, 1, 1)

        self.lineEdit_27 = QLineEdit(self.groupBox_11)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_12.addWidget(self.lineEdit_27, 2, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_32, 3, 0, 1, 1)

        self.lineEdit_28 = QLineEdit(self.groupBox_11)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.gridLayout_12.addWidget(self.lineEdit_28, 3, 1, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_12)


        self.parOp.addWidget(self.groupBox_11)

        self.groupBox_10 = QGroupBox(self.paramOpera)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineEdit_22 = QLineEdit(self.groupBox_10)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_11.addWidget(self.lineEdit_22, 1, 1, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox_10)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_11.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_28, 2, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.groupBox_10)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_11.addWidget(self.lineEdit_24, 2, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_11)


        self.parOp.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.paramOpera)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_20 = QLabel(self.groupBox_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_20, 5, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox_9)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_10.addWidget(self.lineEdit_17, 3, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_22, 3, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_23, 4, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.groupBox_9)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_10.addWidget(self.lineEdit_18, 5, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.groupBox_9)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_10.addWidget(self.lineEdit_19, 1, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.groupBox_9)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_10.addWidget(self.lineEdit_20, 4, 1, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_9)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_10.addWidget(self.lineEdit_21, 0, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_25, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_9)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_10.addWidget(self.comboBox, 2, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_10)


        self.parOp.addWidget(self.groupBox_9)

        self.opBtnBox = QDialogButtonBox(self.paramOpera)
        self.opBtnBox.setObjectName(u"opBtnBox")
        self.opBtnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.parOp.addWidget(self.opBtnBox)

        self.paramStackedWidget.addWidget(self.paramOpera)

        self.inputLayout.addWidget(self.paramStackedWidget)


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
        self.resultTabWidget = QTabWidget(self.resultGrpBox)
        self.resultTabWidget.setObjectName(u"resultTabWidget")
        self.resultTabWidget.setTabShape(QTabWidget.Rounded)
        self.resultTabWidget.setIconSize(QSize(13, 20))
        self.resultTabWidget.setElideMode(Qt.ElideRight)
        self.resultTabWidget.setDocumentMode(False)
        self.resultTabWidget.setTabsClosable(False)
        self.resultTabWidget.setMovable(False)
        self.resultTabWidget.setTabBarAutoHide(False)
        self.tabgraph = QWidget()
        self.tabgraph.setObjectName(u"tabgraph")
        icon6 = QIcon()
        icon6.addFile(u"Im/picture.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget.addTab(self.tabgraph, icon6, "")
        self.tabdata = QWidget()
        self.tabdata.setObjectName(u"tabdata")
        icon7 = QIcon()
        icon7.addFile(u"Im/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resultTabWidget.addTab(self.tabdata, icon7, "")

        self.verticalLayout_8.addWidget(self.resultTabWidget)

        self.downloadBtn = QPushButton(self.resultGrpBox)
        self.downloadBtn.setObjectName(u"downloadBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.downloadBtn.sizePolicy().hasHeightForWidth())
        self.downloadBtn.setSizePolicy(sizePolicy5)
        self.downloadBtn.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u"Im/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downloadBtn.setIcon(icon8)
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
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuEditer = QMenu(self.menubar)
        self.menuEditer.setObjectName(u"menuEditer")
        self.menuRechercher = QMenu(self.menubar)
        self.menuRechercher.setObjectName(u"menuRechercher")
        self.menuOutils = QMenu(self.menubar)
        self.menuOutils.setObjectName(u"menuOutils")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEditer.menuAction())
        self.menubar.addAction(self.menuRechercher.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        self.paramStackedWidget.setCurrentIndex(3)
        self.pushButton_2.setDefault(False)
        self.resultTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DRIMERA", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
        self.actionNouveau.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.inputGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Entr\u00e9es", None))
        self.atmosBtn.setText(QCoreApplication.translate("MainWindow", u"Atmosph\u00e9riques", None))
        self.terrainBtn.setText(QCoreApplication.translate("MainWindow", u"Terrain", None))
        self.operaBtn.setText(QCoreApplication.translate("MainWindow", u"Op\u00e9rationnels", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Atmosph\u00e9rique", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Terrain", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Op\u00e9rationnel", None))
        self.paramLevel.setText(QCoreApplication.translate("MainWindow", u"Niveau de param\u00e9trage", None))
        self.calculBtn.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.asriskBtn.setText(QCoreApplication.translate("MainWindow", u"Evaluer risques", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Donn\u00e9es m\u00e9t\u00e9orologiques", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Coordonn\u00e9es UTM", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y (m)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"X (m)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9charger donn\u00e9es", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Humidit\u00e9 relative (%)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Direction du vent (N\u00b0)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Temp\u00e9rature (\u00b0C)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Vitesse du vent (km/h)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Turbulences", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Bruit de fond", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"V\u00e9g\u00e9tation", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Densit\u00e9", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Hauteur (m)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Termes source", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9sence", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Absence", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Zones sensibles", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Carat\u00e9ristiques appareil", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Masse (kg)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Diam\u00e8tre rotor (mm)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Avancement (m/s)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Vitesse rotor (m/s)", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Donn\u00e9es d'\u00e9mission", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Taux d'application (%)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Taux de mati\u00e8re active (%)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Temp\u00e9rature du produit (\u00b0C)", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Caract\u00e9ristiques traitement", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Distance lignes de passage (m)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Largeur rampe (m)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Hauteur application (m)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre de passage", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Orientation buses (\u00b0)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Classe gouettelettes", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Extr\u00eamement fin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Tr\u00e8s fin", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fin", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Moyen", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Grossier", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Tr\u00e8s grossier", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Extr\u00eamement grossier", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Ultra grossier", None))

        self.resultGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"R\u00e9sultats", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.tabgraph), QCoreApplication.translate("MainWindow", u"Graphe", None))
        self.resultTabWidget.setTabText(self.resultTabWidget.indexOf(self.tabdata), QCoreApplication.translate("MainWindow", u"Donn\u00e9es", None))
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"Exporter", None))
        self.appversion.setText(QCoreApplication.translate("MainWindow", u"v 1.0.0   ", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuEditer.setTitle(QCoreApplication.translate("MainWindow", u"Editer", None))
        self.menuRechercher.setTitle(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.menuOutils.setTitle(QCoreApplication.translate("MainWindow", u"Outils", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
    # retranslateUi


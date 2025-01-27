# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windRoseParamaAEHDn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Alert(object):
    def setupUi(self, Alert):
        if not Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(375, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Alert.sizePolicy().hasHeightForWidth())
        Alert.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Im/info.png", QSize(), QIcon.Normal, QIcon.Off)
        Alert.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Alert)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.im = QLabel(Alert)
        self.im.setObjectName(u"im")
        self.im.setMaximumSize(QSize(25, 25))
        self.im.setBaseSize(QSize(0, 0))
        self.im.setAutoFillBackground(False)
        self.im.setPixmap(QPixmap(u"Im/settings.png"))
        self.im.setScaledContents(True)

        self.horizontalLayout.addWidget(self.im)

        self.label_windRoseSetting = QLabel(Alert)
        self.label_windRoseSetting.setObjectName(u"label_windRoseSetting")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_windRoseSetting.setFont(font)
        self.label_windRoseSetting.setAutoFillBackground(False)
        self.label_windRoseSetting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_windRoseSetting)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_setting = QGridLayout()
        self.gridLayout_setting.setObjectName(u"gridLayout_setting")
        self.East_lineEdit = QLineEdit(Alert)
        self.East_lineEdit.setObjectName(u"East_lineEdit")

        self.gridLayout_setting.addWidget(self.East_lineEdit, 2, 1, 1, 1)

        self.North_lineEdit = QLineEdit(Alert)
        self.North_lineEdit.setObjectName(u"North_lineEdit")

        self.gridLayout_setting.addWidget(self.North_lineEdit, 0, 1, 1, 1)

        self.label_SouthEast = QLabel(Alert)
        self.label_SouthEast.setObjectName(u"label_SouthEast")

        self.gridLayout_setting.addWidget(self.label_SouthEast, 3, 0, 1, 1)

        self.label_North = QLabel(Alert)
        self.label_North.setObjectName(u"label_North")

        self.gridLayout_setting.addWidget(self.label_North, 0, 0, 1, 1)

        self.label_West = QLabel(Alert)
        self.label_West.setObjectName(u"label_West")

        self.gridLayout_setting.addWidget(self.label_West, 6, 0, 1, 1)

        self.label_East = QLabel(Alert)
        self.label_East.setObjectName(u"label_East")

        self.gridLayout_setting.addWidget(self.label_East, 2, 0, 1, 1)

        self.label_South = QLabel(Alert)
        self.label_South.setObjectName(u"label_South")

        self.gridLayout_setting.addWidget(self.label_South, 4, 0, 1, 1)

        self.NorthEast_lineEdit = QLineEdit(Alert)
        self.NorthEast_lineEdit.setObjectName(u"NorthEast_lineEdit")

        self.gridLayout_setting.addWidget(self.NorthEast_lineEdit, 1, 1, 1, 1)

        self.label_SouthWest = QLabel(Alert)
        self.label_SouthWest.setObjectName(u"label_SouthWest")

        self.gridLayout_setting.addWidget(self.label_SouthWest, 5, 0, 1, 1)

        self.label_NorthEast = QLabel(Alert)
        self.label_NorthEast.setObjectName(u"label_NorthEast")

        self.gridLayout_setting.addWidget(self.label_NorthEast, 1, 0, 1, 1)

        self.label_NorthWest = QLabel(Alert)
        self.label_NorthWest.setObjectName(u"label_NorthWest")

        self.gridLayout_setting.addWidget(self.label_NorthWest, 7, 0, 1, 1)

        self.SouthEast_lineEdit = QLineEdit(Alert)
        self.SouthEast_lineEdit.setObjectName(u"SouthEast_lineEdit")

        self.gridLayout_setting.addWidget(self.SouthEast_lineEdit, 3, 1, 1, 1)

        self.South_lineEdit = QLineEdit(Alert)
        self.South_lineEdit.setObjectName(u"South_lineEdit")

        self.gridLayout_setting.addWidget(self.South_lineEdit, 4, 1, 1, 1)

        self.SouthWest_lineEdit = QLineEdit(Alert)
        self.SouthWest_lineEdit.setObjectName(u"SouthWest_lineEdit")

        self.gridLayout_setting.addWidget(self.SouthWest_lineEdit, 5, 1, 1, 1)

        self.West_lineEdit = QLineEdit(Alert)
        self.West_lineEdit.setObjectName(u"West_lineEdit")

        self.gridLayout_setting.addWidget(self.West_lineEdit, 6, 1, 1, 1)

        self.NorthWest_lineEdit = QLineEdit(Alert)
        self.NorthWest_lineEdit.setObjectName(u"NorthWest_lineEdit")

        self.gridLayout_setting.addWidget(self.NorthWest_lineEdit, 7, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_setting)

        self.roseWind_graphicsView = QGraphicsView(Alert)
        self.roseWind_graphicsView.setObjectName(u"roseWind_graphicsView")

        self.verticalLayout.addWidget(self.roseWind_graphicsView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backBtn = QPushButton(Alert)
        self.backBtn.setObjectName(u"backBtn")

        self.horizontalLayout_2.addWidget(self.backBtn)

        self.saveBtn = QPushButton(Alert)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.resetBtn = QPushButton(Alert)
        self.resetBtn.setObjectName(u"resetBtn")

        self.horizontalLayout_2.addWidget(self.resetBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Alert)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"DRIMERA", None))
        self.im.setText("")
        self.label_windRoseSetting.setText(QCoreApplication.translate("Alert", u"Wind Rose setting", None))
        self.label_SouthEast.setText(QCoreApplication.translate("Alert", u"South-East (SE)", None))
        self.label_North.setText(QCoreApplication.translate("Alert", u"North (N)", None))
        self.label_West.setText(QCoreApplication.translate("Alert", u"West (West)", None))
        self.label_East.setText(QCoreApplication.translate("Alert", u"East (E)", None))
        self.label_South.setText(QCoreApplication.translate("Alert", u"South (S)", None))
        self.label_SouthWest.setText(QCoreApplication.translate("Alert", u"South-West (SW)", None))
        self.label_NorthEast.setText(QCoreApplication.translate("Alert", u"North-East (NE)", None))
        self.label_NorthWest.setText(QCoreApplication.translate("Alert", u"North-West (NW)", None))
        self.backBtn.setText(QCoreApplication.translate("Alert", u"Back", None))
        self.saveBtn.setText(QCoreApplication.translate("Alert", u"Save", None))
        self.resetBtn.setText(QCoreApplication.translate("Alert", u"Reset", None))
    # retranslateUi


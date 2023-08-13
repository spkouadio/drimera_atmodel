# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorxTaHod.ui'
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

class Ui_Alert(object):
    def setupUi(self, Alert):
        if not Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(375, 361)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Alert.sizePolicy().hasHeightForWidth())
        Alert.setSizePolicy(sizePolicy)
        Alert.setContextMenuPolicy(Qt.DefaultContextMenu)
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

        self.label_carrierSetting = QLabel(Alert)
        self.label_carrierSetting.setObjectName(u"label_carrierSetting")
        font = QFont()
        font.setBold(True)
        self.label_carrierSetting.setFont(font)
        self.label_carrierSetting.setAutoFillBackground(False)
        self.label_carrierSetting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_carrierSetting)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_setting = QGridLayout()
        self.gridLayout_setting.setObjectName(u"gridLayout_setting")
        self.label_carrierName = QLabel(Alert)
        self.label_carrierName.setObjectName(u"label_carrierName")

        self.gridLayout_setting.addWidget(self.label_carrierName, 0, 0, 1, 1)

        self.cadensity_lineEdit = QLineEdit(Alert)
        self.cadensity_lineEdit.setObjectName(u"cadensity_lineEdit")

        self.gridLayout_setting.addWidget(self.cadensity_lineEdit, 1, 1, 1, 1)

        self.carrier_lineEdit = QLineEdit(Alert)
        self.carrier_lineEdit.setObjectName(u"carrier_lineEdit")

        self.gridLayout_setting.addWidget(self.carrier_lineEdit, 0, 1, 1, 1)

        self.cafeatures_lineEdit = QLineEdit(Alert)
        self.cafeatures_lineEdit.setObjectName(u"cafeatures_lineEdit")

        self.gridLayout_setting.addWidget(self.cafeatures_lineEdit, 2, 1, 1, 1)

        self.label_cafeatures = QLabel(Alert)
        self.label_cafeatures.setObjectName(u"label_cafeatures")

        self.gridLayout_setting.addWidget(self.label_cafeatures, 2, 0, 1, 1)

        self.label_cadensity = QLabel(Alert)
        self.label_cadensity.setObjectName(u"label_cadensity")

        self.gridLayout_setting.addWidget(self.label_cadensity, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_setting)

        self.carrier_listView = QListView(Alert)
        self.carrier_listView.setObjectName(u"carrier_listView")

        self.verticalLayout.addWidget(self.carrier_listView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backBtn = QPushButton(Alert)
        self.backBtn.setObjectName(u"backBtn")

        self.horizontalLayout_2.addWidget(self.backBtn)

        self.saveBtn = QPushButton(Alert)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.deleteBtn = QPushButton(Alert)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.horizontalLayout_2.addWidget(self.deleteBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Alert)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"DRIMERA", None))
        self.im.setText("")
        self.label_carrierSetting.setText(QCoreApplication.translate("Alert", u"Carrier setting", None))
        self.label_carrierName.setText(QCoreApplication.translate("Alert", u"Carrier name", None))
        self.label_cafeatures.setText(QCoreApplication.translate("Alert", u"Features", None))
        self.label_cadensity.setText(QCoreApplication.translate("Alert", u"Density (g/l)", None))
        self.backBtn.setText(QCoreApplication.translate("Alert", u"Back", None))
        self.saveBtn.setText(QCoreApplication.translate("Alert", u"Save", None))
        self.deleteBtn.setText(QCoreApplication.translate("Alert", u"Delete", None))
    # retranslateUi


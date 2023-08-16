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
        Alert.resize(375, 387)
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

        self.label_pestcideSetting = QLabel(Alert)
        self.label_pestcideSetting.setObjectName(u"label_pestcideSetting")
        font = QFont()
        font.setBold(True)
        self.label_pestcideSetting.setFont(font)
        self.label_pestcideSetting.setAutoFillBackground(False)
        self.label_pestcideSetting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_pestcideSetting)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_setting = QGridLayout()
        self.gridLayout_setting.setObjectName(u"gridLayout_setting")
        self.amConcent_lineEdit = QLineEdit(Alert)
        self.amConcent_lineEdit.setObjectName(u"amConcent_lineEdit")

        self.gridLayout_setting.addWidget(self.amConcent_lineEdit, 4, 1, 1, 1)

        self.pesticideName_lineEdit = QLineEdit(Alert)
        self.pesticideName_lineEdit.setObjectName(u"pesticideName_lineEdit")

        self.gridLayout_setting.addWidget(self.pesticideName_lineEdit, 0, 1, 1, 1)

        self.label_amConcent = QLabel(Alert)
        self.label_amConcent.setObjectName(u"label_amConcent")
        self.label_amConcent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_setting.addWidget(self.label_amConcent, 4, 0, 1, 1)

        self.pestDensity_lineEdit = QLineEdit(Alert)
        self.pestDensity_lineEdit.setObjectName(u"pestDensity_lineEdit")

        self.gridLayout_setting.addWidget(self.pestDensity_lineEdit, 1, 1, 1, 1)

        self.label_pesticideName = QLabel(Alert)
        self.label_pesticideName.setObjectName(u"label_pesticideName")
        self.label_pesticideName.setEnabled(True)
        self.label_pesticideName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_setting.addWidget(self.label_pesticideName, 0, 0, 1, 1)

        self.label_activeMatter = QLabel(Alert)
        self.label_activeMatter.setObjectName(u"label_activeMatter")
        self.label_activeMatter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_setting.addWidget(self.label_activeMatter, 3, 0, 1, 1)

        self.label_pestDensity = QLabel(Alert)
        self.label_pestDensity.setObjectName(u"label_pestDensity")
        self.label_pestDensity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_setting.addWidget(self.label_pestDensity, 1, 0, 1, 1)

        self.activeMatter_lineEdit = QLineEdit(Alert)
        self.activeMatter_lineEdit.setObjectName(u"activeMatter_lineEdit")

        self.gridLayout_setting.addWidget(self.activeMatter_lineEdit, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_setting)

        self.pesticide_listView = QListView(Alert)
        self.pesticide_listView.setObjectName(u"pesticide_listView")

        self.verticalLayout.addWidget(self.pesticide_listView)

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
        self.label_pestcideSetting.setText(QCoreApplication.translate("Alert", u"Pesticide setting", None))
        self.label_amConcent.setText(QCoreApplication.translate("Alert", u"Active matter concentration (g/l)", None))
        self.label_pesticideName.setText(QCoreApplication.translate("Alert", u"Pesticide name", None))
        self.label_activeMatter.setText(QCoreApplication.translate("Alert", u"Active matter name", None))
        self.label_pestDensity.setText(QCoreApplication.translate("Alert", u"Pesticide density (g/l)", None))
        self.backBtn.setText(QCoreApplication.translate("Alert", u"Back", None))
        self.saveBtn.setText(QCoreApplication.translate("Alert", u"Save", None))
        self.deleteBtn.setText(QCoreApplication.translate("Alert", u"Delete", None))
    # retranslateUi
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alertOiNPQW.ui'
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
        if Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.resize(375, 92)
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
        self.im.setPixmap(QPixmap(u"Im/alert.png"))
        self.im.setScaledContents(True)

        self.horizontalLayout.addWidget(self.im)

        self.label = QLabel(Alert)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Alert)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Alert)
        self.buttonBox.accepted.connect(Alert.accept)
        self.buttonBox.rejected.connect(Alert.reject)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"DRIMERA", None))
        self.im.setText("")
        self.label.setText(QCoreApplication.translate("Alert", u"Les saisies ne seront pas prises en compte. Voulez-vous continuer ?", None))
    # retranslateUi


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


class Ui_Erreur(object):
    def setupUi(self, Erreur):
        if Erreur.objectName():
            Erreur.setObjectName(u"Erreur")
        Erreur.resize(344, 91)
        icon = QIcon()
        icon.addFile(u"Im/info.png", QSize(), QIcon.Normal, QIcon.Off)
        Erreur.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Erreur)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Erreur)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setPixmap(QPixmap(u"Im/dangerflat.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(Erreur)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Erreur)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Erreur)
        self.buttonBox.accepted.connect(Erreur.accept)
        self.buttonBox.rejected.connect(Erreur.reject)

        QMetaObject.connectSlotsByName(Erreur)
    # setupUi

    def retranslateUi(self, Erreur):
        Erreur.setWindowTitle(QCoreApplication.translate("Erreur", u"DRIMERA", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Erreur", u"Param\u00e9trage erron\u00e9 ! Veuillez renseigner tous les champs.", None))
    # retranslateUi


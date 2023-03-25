# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terrainParambvJfuN.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout.addWidget(self.groupBox_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"V\u00e9g\u00e9tation", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Densit\u00e9", None))
        self.label.setText(QCoreApplication.translate("Form", u"Hauteur (m)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Termes source", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Pr\u00e9sence", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Absence", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Zones sensibles", None))
    # retranslateUi


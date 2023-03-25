# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atmosParamSXYTjC.ui'
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
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Donn\u00e9es m\u00e9t\u00e9orologiques", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Coordonn\u00e9es UTM", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Y (m)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"X (m)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"T\u00e9l\u00e9charger donn\u00e9es", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Humidit\u00e9 relative (%)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Direction du vent (N\u00b0)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Temp\u00e9rature (\u00b0C)", None))
        self.label.setText(QCoreApplication.translate("Form", u"Vitesse du vent (km/h)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Turbulences", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Bruit de fond", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atparamLNfQsR.ui'
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


class Ui_Frame(QWidget):
    def setupUi(self, Frame):
        if Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_4.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_4.addWidget(self.lineEdit_8, 1, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_4)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_2.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_2.addWidget(self.lineEdit_12, 3, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(Frame)
        self.groupBox_4.setObjectName(u"groupBox_4")

        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Frame)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.verticalLayout.addWidget(self.groupBox_5)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.groupBox.setTitle(QCoreApplication.translate("Frame", u"Donn\u00e9es m\u00e9t\u00e9orologiques", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Frame", u"Coordonn\u00e9es UTM", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"Y (m)", None))
        self.label_9.setText(QCoreApplication.translate("Frame", u"X (m)", None))
        self.pushButton_2.setText(QCoreApplication.translate("Frame", u"T\u00e9l\u00e9charger donn\u00e9es", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Humidit\u00e9 relative (%)", None))
        self.label_10.setText(QCoreApplication.translate("Frame", u"Direction du vent (N\u00b0)", None))
        self.label_11.setText(QCoreApplication.translate("Frame", u"Temp\u00e9rature (\u00b0C)", None))
        self.label_12.setText(QCoreApplication.translate("Frame", u"Vitesse du vent (km/h)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Frame", u"Turbulences", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Frame", u"Bruit de fond", None))
    # retranslateUi


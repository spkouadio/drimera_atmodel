#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QStandardItemModel, QFont, QPalette, QStandardItem
from PyQt5.QtWidgets import QDialog, QListView, QListWidget, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QApplication
from PySide2 import QtCore, QtGui


class Try(QDialog):
    def __init__(self):
        super(Try, self).__init__()
        self.setWindowTitle("Trying stuff")
        self.list_view = QListView(self)
        self.lview = QListWidget(self)
        self.EditText = QLineEdit()
        self.EditText.setPlaceholderText("add stuff")
        self.EditText.setMaximumWidth(200)
        self.setWindowFlags(QtCore.Qt.Window)
        self.model = QStandardItemModel(self.list_view)
        self.resize(600, 500)
        self.font = QFont()
        self.font.setBold(True)
        self.font2 = QFont()
        self.font2.setBold(False)
        palette = QPalette()
        palette.setColor(QPalette.Foreground, QtCore.Qt.red)
        self.label = QLabel()
        self.buttonRemove = QPushButton()
        self.buttonAdd = QPushButton()
        self.buttonCommit =QPushButton()
        self.buttonRemove.setText("Remove from list")
        self.buttonRemove.clicked.connect(self.removeItems)
        self.buttonAdd.setText("Add to list")
        self.buttonAdd.clicked.connect(self.addItems)
        self.buttonCommit.setText("print all item in list")

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.EditText)
        horizontalLayout.addWidget(self.buttonAdd)

        horizontalLayout.setAlignment(QtCore.Qt.AlignRight)
        horizontalLayout2 = QHBoxLayout()
        horizontalLayout2.addWidget(self.buttonRemove)
        horizontalLayout2.addWidget(self.buttonCommit)
        horizontalLayout2.setAlignment(QtCore.Qt.AlignRight)

        verticalLayout = QVBoxLayout(self)
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addWidget(self.list_view)
        verticalLayout.addWidget(self.lview)
        verticalLayout.addWidget(self.label)
        verticalLayout.addLayout(horizontalLayout2)


    def addItems(self):
        x = self.EditText.text()
        self.lview.addItem(x)
        self.lview.setAutoScroll(True)
        item = QStandardItem(x)
        item.setCheckable(True)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.model.appendRow(item)
        self.list_view.setModel(self.model)
        self.EditText.clear()

    def removeItems(self):
        x = self.EditText.text()
        item = QStandardItem(x)
        todelete = self.list_view.selectionModel().currentIndex().data().toString()
        print (todelete)
        self.model.removeRow(todelete)
        self.lview.takeItem(item.row())
        #self.model.removeRow(item.row())

        self.list_view.setModel(self.model)
        self.EditText.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Try()
    t.show()
    sys.exit(app.exec_())
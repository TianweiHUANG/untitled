# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTest_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        #self.pushButton.clicked.connect(self.pushButton_clicked)
        #self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "按 钮"))
        self.pushButton_2.setText(_translate("Dialog", "按 钮_2"))

"""
    def pushButton_clicked(self):
      print("Hello world")
    def pushButton_2_clicked(self):
      print("Hello world_2")
"""




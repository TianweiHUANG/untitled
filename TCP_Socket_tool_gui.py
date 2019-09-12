# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCP_Socket_tool_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(411, 321)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Server_IP = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Server_IP.setGeometry(QtCore.QRect(20, 50, 113, 41))
        self.lineEdit_Server_IP.setObjectName("lineEdit_Server_IP")
        self.lineEdit_Server_PORT = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Server_PORT.setGeometry(QtCore.QRect(150, 49, 113, 41))
        self.lineEdit_Server_PORT.setObjectName("lineEdit_Server_PORT")
        self.lineEdit_Send_Message = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Send_Message.setGeometry(QtCore.QRect(280, 50, 113, 41))
        self.lineEdit_Send_Message.setObjectName("lineEdit_Send_Message")
        self.pushButton_Connect = QtWidgets.QPushButton(Dialog)
        self.pushButton_Connect.setGeometry(QtCore.QRect(20, 110, 111, 41))
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.pushButton_Send = QtWidgets.QPushButton(Dialog)
        self.pushButton_Send.setGeometry(QtCore.QRect(150, 110, 111, 41))
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.pushButton_Close = QtWidgets.QPushButton(Dialog)
        self.pushButton_Close.setGeometry(QtCore.QRect(280, 110, 111, 41))
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.pushButton_Receive = QtWidgets.QPushButton(Dialog)
        self.pushButton_Receive.setGeometry(QtCore.QRect(80, 260, 111, 41))
        self.pushButton_Receive.setObjectName("pushButton_Receive")
        self.lineEdit_Receive_Message = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Receive_Message.setGeometry(QtCore.QRect(20, 200, 371, 41))
        self.lineEdit_Receive_Message.setObjectName("lineEdit_Receive_Message")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 170, 91, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_Show_Message = QtWidgets.QPushButton(Dialog)
        self.pushButton_Show_Message.setGeometry(QtCore.QRect(220, 260, 111, 41))
        self.pushButton_Show_Message.setObjectName("pushButton_Show_Message")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TCP_Socket_tool_Dialog"))
        self.label.setText(_translate("Dialog", "Server_IP"))
        self.label_2.setText(_translate("Dialog", "Server_PORT"))
        self.label_3.setText(_translate("Dialog", "Send_Message"))
        self.pushButton_Connect.setText(_translate("Dialog", "Connect"))
        self.pushButton_Send.setText(_translate("Dialog", "Send"))
        self.pushButton_Close.setText(_translate("Dialog", "Close"))
        self.pushButton_Receive.setText(_translate("Dialog", "Receive"))
        self.label_4.setText(_translate("Dialog", "Receive_Message"))
        self.pushButton_Show_Message.setText(_translate("Dialog", "Show_Message"))


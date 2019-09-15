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
        self.pushButton_Send.setGeometry(QtCore.QRect(280, 110, 111, 41))
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.pushButton_Close = QtWidgets.QPushButton(Dialog)
        self.pushButton_Close.setGeometry(QtCore.QRect(150, 110, 111, 41))
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.lineEdit_Receive_Message = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Receive_Message.setGeometry(QtCore.QRect(410, 50, 111, 41))
        self.lineEdit_Receive_Message.setObjectName("lineEdit_Receive_Message")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_sys_log = QtWidgets.QLabel(Dialog)
        self.label_sys_log.setGeometry(QtCore.QRect(20, 180, 511, 41))
        self.label_sys_log.setObjectName("label_sys_log")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_Receive_Enable = QtWidgets.QLabel(Dialog)
        self.label_Receive_Enable.setGeometry(QtCore.QRect(410, 110, 111, 41))
        self.label_Receive_Enable.setObjectName("label_Receive_Enable")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 511, 16))
        self.label_6.setObjectName("label_6")
        self.textBrowser_sys_log = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_sys_log.setGeometry(QtCore.QRect(20, 220, 501, 251))
        self.textBrowser_sys_log.setObjectName("textBrowser_sys_log")

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
        self.label_4.setText(_translate("Dialog", "Receive_Message"))
        self.label_sys_log.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "sys_log"))
        self.label_Receive_Enable.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "___________________________________________________________________________________"))


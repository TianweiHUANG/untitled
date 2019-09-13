"""
import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool

import sys
from TCP_Socket_tool_gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog,self).__init__(parent)
        self.setupUi(self)

        #self.lineEdit.textChanged.connect(self.label.setText)
        self.lineEdit_Server_IP.textChanged.connect(self.lineEdit_Server_IP_Func)
        self.lineEdit_Server_PORT.textChanged.connect(self.lineEdit_Server_PORT_Func)
        self.lineEdit_Send_Message.textChanged.connect(self.lineEdit_Send_Message_Func)

        self.pushButton_Connect.clicked.connect(self.pushButton_Connect_Func)
        self.pushButton_Send.clicked.connect(self.pushButton_Send_Func)
        self.pushButton_Close.clicked.connect(self.pushButton_Close_Func)
        self.pushButton_Receive.clicked.connect(self.pushButton_Receive_Func)
        self.pushButton_Show_Message.clicked.connect(self.pushButton_Show_Message_Func)

    def lineEdit_Server_IP_Func(self,lineEdit_Server_IP_textChanged):
        globalvar.set_value("Server_IP", lineEdit_Server_IP_textChanged)
    def lineEdit_Server_PORT_Func(self,lineEdit_Server_PORT_textChanged):
        globalvar.set_value("Server_PORT", lineEdit_Server_PORT_textChanged)
    def lineEdit_Send_Message_Func(self,lineEdit_Send_Message_textChanged):
        globalvar.set_value("send_Message", lineEdit_Send_Message_textChanged)

    def pushButton_Connect_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_Send_Func(self):
        globalvar.set_value("Send",True)
    def pushButton_Close_Func(self):
        globalvar.set_value("Close", True)
    def pushButton_Receive_Func(self):
        globalvar.set_value("Receive", True)
    def pushButton_Show_Message_Func(self):
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))

if __name__ == '__main__':
  globalvar._init()

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())
"""
#「LittleHUANG: 窗口命名 部件命名 创建套接字 初始值设定 简化Qtimer Try... 按钮取消 实时消息栏」
"""
This_is_def MyQtimer(self):
This_is_self.MyQtimer()
This_is_def Real_time_Display_Func(self):
This_is_def Real_time_Display_Func(self):
This_is_def Real_time_Display_Func(self):
... ...
"""
import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool

import sys
from TCP_Socket_tool_gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import QTimer #PyQt5.QtCore_QTimer_Real-time Show

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog,self).__init__(parent)
        self.setupUi(self)

        #全局变量初始化...
        self.lineEdit_Server_IP.setText(globalvar.get_value("Server_IP"))
        self.lineEdit_Server_PORT.setText(globalvar.get_value("Server_PORT"))
        self.lineEdit_Send_Message.setText(globalvar.get_value("send_Message"))

        #self.lineEdit.textChanged.connect(self.label.setText)
        #LineEdit_Text作为槽函数self.label.setText(...)的参数。
        self.lineEdit_Server_IP.textChanged.connect(self.lineEdit_Server_IP_Func)
        self.lineEdit_Server_PORT.textChanged.connect(self.lineEdit_Server_PORT_Func)
        self.lineEdit_Send_Message.textChanged.connect(self.lineEdit_Send_Message_Func)

        self.pushButton_Connect.clicked.connect(self.pushButton_Connect_Func)
        self.pushButton_Close.clicked.connect(self.pushButton_Close_Func)
        self.pushButton_Send.clicked.connect(self.pushButton_Send_Func)
        self.pushButton_Receive.clicked.connect(self.pushButton_Receive_Func)

        #PyQt5.QtCore_QTimer_Real-time Show
        #self.pushButton_Show_Message.clicked.connect(self.pushButton_Show_Message_Func)
        self.MyQtimer()
        #print("This_is_self.MyQtimer()")

    def lineEdit_Server_IP_Func(self,lineEdit_Server_IP_textChanged):
        globalvar.set_value("Server_IP", lineEdit_Server_IP_textChanged)
    def lineEdit_Server_PORT_Func(self,lineEdit_Server_PORT_textChanged):
        globalvar.set_value("Server_PORT", lineEdit_Server_PORT_textChanged)
    def lineEdit_Send_Message_Func(self,lineEdit_Send_Message_textChanged):
        globalvar.set_value("send_Message", lineEdit_Send_Message_textChanged)

    def pushButton_Connect_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_Close_Func(self):
        globalvar.set_value("Close", True)
    def pushButton_Send_Func(self):
        globalvar.set_value("Send",True)
    def pushButton_Receive_Func(self):
        globalvar.set_value("Receive", True)

    #PyQt5.QtCore_QTimer_Real-time Show
    def MyQtimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.Real_time_Display_Func)
        timer.start(100)#100ms
        #print("This_is_def MyQtimer(self):")
    #def pushButton_Show_Message_Func(self):
        #self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))
    def Real_time_Display_Func(self):
        self.label_sys_log.setText(globalvar.get_value("sys_log"))
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))
        #print("This_is_def Real_time_Display_Func(self):")

if __name__ == '__main__':
  #全局变量初始化...
  globalvar._init()
  globalvar.set_value("Server_IP", "192.168.1.101")
  globalvar.set_value("Server_PORT", "1234")
  globalvar.set_value("send_Message", "Hello WuPingping")

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())

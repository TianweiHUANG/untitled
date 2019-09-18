import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool
from TCP_Socket_Receive import TCP_Socket_Receive

import sys,time
from TCP_Socket_tool_gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import QTimer

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog,self).__init__(parent)
        self.setupUi(self)

        #全局变量初始化...
        self.lineEdit_Server_IP.setText(globalvar.get_value("Server_IP"))
        self.lineEdit_Server_PORT.setText(globalvar.get_value("Server_PORT"))
        self.lineEdit_Send_Message.setText(globalvar.get_value("send_Message"))

        self.lineEdit_Server_IP.textChanged.connect(self.lineEdit_Server_IP_Func)
        self.lineEdit_Server_PORT.textChanged.connect(self.lineEdit_Server_PORT_Func)
        self.lineEdit_Send_Message.textChanged.connect(self.lineEdit_Send_Message_Func)

        self.pushButton_TCP_select.clicked.connect(self.pushButton_TCP_select_Func)
        self.pushButton_Connect.clicked.connect(self.pushButton_Connect_Func)
        self.pushButton_Close.clicked.connect(self.pushButton_Close_Func)
        self.pushButton_Send.clicked.connect(self.pushButton_Send_Func)

        self.MyQtimer=QTimer(self)
        self.MyQtimer.start(100)
        self.MyQtimer.timeout.connect(self.Real_time_Display_Func)

    def lineEdit_Server_IP_Func(self,lineEdit_Server_IP_textChanged):
        globalvar.set_value("Server_IP", lineEdit_Server_IP_textChanged)
    def lineEdit_Server_PORT_Func(self,lineEdit_Server_PORT_textChanged):
        globalvar.set_value("Server_PORT", lineEdit_Server_PORT_textChanged)
    def lineEdit_Send_Message_Func(self,lineEdit_Send_Message_textChanged):
        globalvar.set_value("send_Message", lineEdit_Send_Message_textChanged)

    def pushButton_TCP_select_Func(self):
        if globalvar.get_value("TCP_select")=="As TCP Server":
            globalvar.set_value("TCP_select","As TCP Client")
            self.pushButton_TCP_select.setText("As TCP Client")
            self.printf_sys_log_Func("TCP_select:As TCP Client")
        elif globalvar.get_value("TCP_select")=="As TCP Client":
            globalvar.set_value("TCP_select", "As TCP Server")
            self.pushButton_TCP_select.setText("As TCP Server")
            self.printf_sys_log_Func("TCP_select:As TCP Server")
    def pushButton_Connect_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_Close_Func(self):
        globalvar.set_value("Close", True)
    def pushButton_Send_Func(self):
        globalvar.set_value("Send",True)

    def Real_time_Display_Func(self):
        self.label_Receive_Enable.setText("Receive_Enable:"+str(globalvar.get_value("Receive_Enable")))
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))

    def printf_sys_log_Func(self,sys_log_str):
        self.textBrowser_sys_log.append(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime())+sys_log_str)#文本框逐条添加数据
        #self.textBrowser_sys_log.moveCursor(self.textBrowser_sys_log.textCursor().End)#文本框显示到底部
        #print(sys_log_str)

if __name__ == '__main__':
  #全局变量初始化...
  globalvar._init()
  globalvar.set_value("TCP_select", "As TCP Client")
  globalvar.set_value("Server_IP", "192.168.43.1")
  globalvar.set_value("Server_PORT", "1234")
  globalvar.set_value("send_Message", "Hello vivo_X21A")
  globalvar.set_value("Receive_Enable", False)

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_Receive_Thread = threading.Thread(target=TCP_Socket_Receive)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_Receive_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()
  TCP_Socket_Receive_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  globalvar.set_value("myWindow",myWindow)
  myWindow.show()
  sys.exit(myApp.exec_())
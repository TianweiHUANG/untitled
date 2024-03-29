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
"""
This_is_def MyQtimer(self):
This_is_self.MyQtimer()
This_is_def Real_time_Display_Func(self):
This_is_def Real_time_Display_Func(self):
This_is_def Real_time_Display_Func(self):
... ...
"""
"""
import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool
from TCP_Socket_Receive import TCP_Socket_Receive

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
        self.label_Receive_Enable.setText(str(globalvar.get_value("tcp_socket"))+"\n"
                                          +"Receive_Enable:"+str(globalvar.get_value("Receive_Enable")))
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))
        #print("This_is_def Real_time_Display_Func(self):")

if __name__ == '__main__':
  #全局变量初始化...
  globalvar._init()
  globalvar.set_value("Server_IP", "192.168.1.101")
  globalvar.set_value("Server_PORT", "1234")
  globalvar.set_value("Receive_Enable", False)#Reset_Receive_Enable
  globalvar.set_value("send_Message", "Hello WuPingping")

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_Receive_Thread = threading.Thread(target=TCP_Socket_Receive)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_Receive_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()
  TCP_Socket_Receive_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())
"""
"""
import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool
from TCP_Socket_Receive import TCP_Socket_Receive

import sys,time
from TCP_Socket_tool_gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import QTimer#PyQt5.QtCore_QTimer_Real-time Show

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
        self.lineEdit_sys_log.textChanged.connect(self.lineEdit_sys_log_Func)#textBrowser_sys_log

        self.pushButton_Connect.clicked.connect(self.pushButton_Connect_Func)
        self.pushButton_Close.clicked.connect(self.pushButton_Close_Func)
        self.pushButton_Send.clicked.connect(self.pushButton_Send_Func)
        self.pushButton_TCP_select.clicked.connect(self.pushButton_TCP_select_Func)
        #self.MyQtimer()#PyQt5.QtCore_QTimer_Real-time Show
        self.MyQtimer=QTimer(self)
        self.MyQtimer.start(100)#100ms
        self.MyQtimer.timeout.connect(self.Real_time_Display_Func)

    def lineEdit_Server_IP_Func(self,lineEdit_Server_IP_textChanged):
        globalvar.set_value("Server_IP", lineEdit_Server_IP_textChanged)
    def lineEdit_Server_PORT_Func(self,lineEdit_Server_PORT_textChanged):
        globalvar.set_value("Server_PORT", lineEdit_Server_PORT_textChanged)
    def lineEdit_Send_Message_Func(self,lineEdit_Send_Message_textChanged):
        globalvar.set_value("send_Message", lineEdit_Send_Message_textChanged)
    def lineEdit_sys_log_Func(self,lineEdit_sys_log_textChanged):#textBrowser_sys_log
        self.textBrowser_sys_log.append(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime())+
                                        lineEdit_sys_log_textChanged)#文本框逐条添加数据
        #self.textBrowser_sys_log.moveCursor(self.textBrowser_sys_log.textCursor().End)#文本框显示到底部

    def pushButton_Connect_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_Close_Func(self):
        globalvar.set_value("Close", True)
    def pushButton_Send_Func(self):
        globalvar.set_value("Send",True)
    #def MyQtimer(self):#PyQt5.QtCore_QTimer_Real-time Show
        #timer=QTimer(self)
        #timer.timeout.connect(self.Real_time_Display_Func)
        #timer.start(100)#100ms
    def pushButton_TCP_select_Func(self):
        if globalvar.get_value("TCP_select")=="As TCP Server":
            globalvar.set_value("TCP_select","As TCP Client")
            self.pushButton_TCP_select.setText("As TCP Client")
            globalvar.set_value("sys_log","TCP_select:As TCP Client")
            print("TCP_select:As TCP Client")
        elif globalvar.get_value("TCP_select")=="As TCP Client":
            globalvar.set_value("TCP_select", "As TCP Server")
            self.pushButton_TCP_select.setText("As TCP Server")
            globalvar.set_value("sys_log", "TCP_select:As TCP Server")
            print("TCP_select:As TCP Server")
    def Real_time_Display_Func(self):
        #self.label_sys_log.setText(globalvar.get_value("sys_log"))
        self.lineEdit_sys_log.setText(globalvar.get_value("sys_log"))#textBrowser_sys_log
        self.label_Receive_Enable.setText(str(globalvar.get_value("tcp_socket"))+"\n"
                                          +"Receive_Enable:"+str(globalvar.get_value("Receive_Enable")))
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))
    def call_MyDialogclass_method(self,say_words):
        print(say_words)

if __name__ == '__main__':
  #全局变量初始化...
  globalvar._init()
  globalvar.set_value("Server_IP", "192.168.1.200")
  globalvar.set_value("Server_PORT", "60000")
  globalvar.set_value("send_Message", "Hello adlink_iPC")
  globalvar.set_value("Receive_Enable", False)#Reset_Receive_Enable
  globalvar.set_value("TCP_select","As TCP Client")

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_Receive_Thread = threading.Thread(target=TCP_Socket_Receive)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_Receive_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()
  TCP_Socket_Receive_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  globalvar.set_value("myWindow",myWindow)
  #myWindow.call_MyDialogclass_method()
  myWindow.show()
  sys.exit(myApp.exec_())
"""
import globalvar
import threading
from TCP_Socket_tool import TCP_Socket_tool
from TCP_Socket_Receive import TCP_Socket_Receive

import sys,time
from TCP_Socket_tool_gui import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import QTimer#PyQt5.QtCore_QTimer_Real-time Show

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
        #self.lineEdit_sys_log.textChanged.connect(self.lineEdit_sys_log_Func)#textBrowser_sys_log

        self.pushButton_TCP_select.clicked.connect(self.pushButton_TCP_select_Func)
        self.pushButton_Connect.clicked.connect(self.pushButton_Connect_Func)
        self.pushButton_Close.clicked.connect(self.pushButton_Close_Func)
        self.pushButton_Send.clicked.connect(self.pushButton_Send_Func)
        #self.MyQtimer()#PyQt5.QtCore_QTimer_Real-time Show
        self.MyQtimer=QTimer(self)
        self.MyQtimer.start(100)#100ms
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
            #globalvar.set_value("sys_log","TCP_select:As TCP Client")
            #print("TCP_select:As TCP Client")
            self.printf_sys_log_Func("TCP_select:As TCP Client")
        elif globalvar.get_value("TCP_select")=="As TCP Client":
            globalvar.set_value("TCP_select", "As TCP Server")
            self.pushButton_TCP_select.setText("As TCP Server")
            #globalvar.set_value("sys_log", "TCP_select:As TCP Server")
            #print("TCP_select:As TCP Server")
            self.printf_sys_log_Func("TCP_select:As TCP Server")
    def pushButton_Connect_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_Close_Func(self):
        globalvar.set_value("Close", True)
    def pushButton_Send_Func(self):
        globalvar.set_value("Send",True)
    #def MyQtimer(self):#PyQt5.QtCore_QTimer_Real-time Show
        #timer=QTimer(self)
        #timer.timeout.connect(self.Real_time_Display_Func)
        #timer.start(100)#100ms
    def Real_time_Display_Func(self):
        #self.label_sys_log.setText(globalvar.get_value("sys_log"))
        #self.lineEdit_sys_log.setText(globalvar.get_value("sys_log"))#textBrowser_sys_log
        # self.label_Receive_Enable.setText(str(globalvar.get_value("tcp_socket"))+"\n"
        # +"Receive_Enable:"+str(globalvar.get_value("Receive_Enable")))
        self.label_Receive_Enable.setText("Receive_Enable:"+str(globalvar.get_value("Receive_Enable")))
        self.lineEdit_Receive_Message.setText(globalvar.get_value("Receive_Message"))

    def printf_sys_log_Func(self,sys_log_str):
        self.textBrowser_sys_log.append(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime())+sys_log_str)#文本框逐条添加数据
        self.textBrowser_sys_log.moveCursor(self.textBrowser_sys_log.textCursor().End)#文本框显示到底部
        print(sys_log_str)

if __name__ == '__main__':
  #全局变量初始化...
  globalvar._init()
  globalvar.set_value("TCP_select", "As TCP Client")
  globalvar.set_value("Server_IP", "192.168.43.1")
  globalvar.set_value("Server_PORT", "1234")
  globalvar.set_value("send_Message", "Hello vivo_X21A")
  globalvar.set_value("Receive_Enable", False)#Reset_Receive_Enable

  TCP_Socket_tool_Thread = threading.Thread(target=TCP_Socket_tool)
  TCP_Socket_Receive_Thread = threading.Thread(target=TCP_Socket_Receive)
  TCP_Socket_tool_Thread.setDaemon(True)
  TCP_Socket_Receive_Thread.setDaemon(True)
  TCP_Socket_tool_Thread.start()
  TCP_Socket_Receive_Thread.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  globalvar.set_value("myWindow",myWindow)#myWindow.call_MyDialogclass_method()
  myWindow.show()
  sys.exit(myApp.exec_())
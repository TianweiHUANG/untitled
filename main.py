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

        self.lineEdit.textChanged.connect(self.lineEdit_Func)
        self.lineEdit_2.textChanged.connect(self.lineEdit_2_Func)
        self.lineEdit_3.textChanged.connect(self.lineEdit_3_Func)
        self.pushButton.clicked.connect(self.pushButton_Func)
        self.pushButton_2.clicked.connect(self.pushButton_2_Func)
        self.pushButton_3.clicked.connect(self.pushButton_3_Func)

    def lineEdit_Func(self,lineEdit_textChanged):
        globalvar.set_value("Server_IP", lineEdit_textChanged)
    def lineEdit_2_Func(self,lineEdit_2_textChanged):
        globalvar.set_value("Server_PORT", lineEdit_2_textChanged)
    def lineEdit_3_Func(self,lineEdit_3_textChanged):
        globalvar.set_value("send_Message", lineEdit_3_textChanged)
    def pushButton_Func(self):
        globalvar.set_value("Connect",True)
    def pushButton_2_Func(self):
        globalvar.set_value("Send",True)
    def pushButton_3_Func(self):
        globalvar.set_value("Close", True)
if __name__ == '__main__':
  globalvar._init()

  t1 = threading.Thread(target=TCP_Socket_tool)
  t1.setDaemon(True)
  t1.start()

  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())

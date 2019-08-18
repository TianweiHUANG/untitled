"""
        self.num = 0
        self.pushButton.clicked.connect(self.showText)
    def showText(self):
        self.num+=1
        self.label.setText(str(self.num))
        print(self.num)
"""
"""
import sys
import QtTest_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  myWindow = QMainWindow()

  myUi = QtTest_MainWindow.Ui_MainWindow()
  myUi.setupUi(myWindow)

  myWindow.show()
  sys.exit(myApp.exec_())
"""
"""
import sys
from QtTest_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.num = 0
        self.pushButton.clicked.connect(self.showText)

    def showText(self):
        self.num+=1
        self.label.setText(str(self.num))
        print(self.num)

if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  myWindow = MainWindow()
  myWindow.show()
  sys.exit(myApp.exec_())
"""

import sys
from LogicInterface import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog,self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_func)
        self.num = 0
        self.pushButton_2.clicked.connect(self.pushButton_2_func)
        self.pushButton_3.clicked.connect(self.pushButton_3_func)

    def pushButton_func(self):
        self.lineEdit.setText("Hello World")
    def pushButton_2_func(self):
        self.num += 1
        self.label.setText(str(self.num))
    def pushButton_3_func(self):
        self.lineEdit.setText("")
        self.num = 0
        self.label.setText(str(self.num))
if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())

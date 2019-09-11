#########################-Pyqt5_Logic_Interface_Separate_demo_$.01-#########################
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
#########################-Pyqt5_Logic_Interface_Separate_demo_$.02-#########################

import sys
from LogicInterface import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog,self).__init__(parent)
        self.setupUi(self)

        self.lineEdit.textChanged.connect(self.label_2.setText)
        #self.lineEdit.textChanged.connect(self.lineEdit_Func)
        self.pushButton.clicked.connect(self.pushButton_Func)
        self.num = 0
        self.pushButton_2.clicked.connect(self.pushButton_2_Func)
        self.pushButton_3.clicked.connect(self.pushButton_3_Func)

    def lineEdit_Func(self,lineEdit_textChanged):
        self.label_2.setText(lineEdit_textChanged)
        print(lineEdit_textChanged)
    def pushButton_Func(self):
        self.lineEdit.setText("Hello world")
    def pushButton_2_Func(self):
        self.num += 1
        self.label.setText(str(self.num))
    def pushButton_3_Func(self):
        self.lineEdit.setText("")
        self.num = 0
        self.label.setText("TextLabel")
if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  myWindow = MyDialog()
  myWindow.show()
  sys.exit(myApp.exec_())

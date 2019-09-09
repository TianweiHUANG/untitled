#########################-01$.demo_PyQt5_CreatWindow.py_20190706-#########################
"""
import sys
from PyQt5 import QtWidgets

myApp=QtWidgets.QApplication(sys.argv)  #创建Application类的实例
myWindow=QtWidgets.QWidget()            #创建一个窗口

myWindow.resize(640,480)                #设置窗口的尺寸
myWindow.move(500,100)                  #移动窗口
myWindow.setWindowTitle('myWindow')     #设置窗口的标题

myWindow.show()                         #显示窗口
#print("Test_for_PyQt5")                 #Test_for_PyQt5
sys.exit(myApp.exec_())                 #进入程序的主循环,并通过exit函数确保主循环安全结束
#print("Test for PyQt5")                 #Test for PyQt5
"""
#########################-02$.demo_PyQt5_First.py_20190706.JPG-#########################
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
  myApp=QApplication(sys.argv)         #创建Application类的实例
  myWindow=QWidget()                   #创建一个窗口

  myWindow.resize(640,480)             #设置窗口的尺寸
  myWindow.move(500,100)               #移动窗口
  myWindow.setWindowTitle('myWindow')  #设置窗口的标题

  myWindow.show()                      #显示窗口
  #print("Test_for_PyQt5")              #Test_for_PyQt5
  sys.exit(myApp.exec_())              #进入程序的主循环,并通过exit函数确保主循环安全结束
  #print("Test for PyQt5")              #Test for PyQt5
"""
#########################-03$.demo_PyQt5_main.py_20190706.JPG-#########################
"""
import sys
import QtTest_Dialog_backups,QtTest_DialogBb,QtTest_DialogBr,QtTest_Widget,QtTest_MainWindow
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QMainWindow
if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  #myWindow = QDialog()
  #myWindow = QWidget()
  #myWindow = QMainWindow()

  #myUi = QtTest_Dialog_backups.Ui_Dialog()
  #myUi = QtTest_DialogBb.Ui_Dialog()
  #myUi = QtTest_DialogBr.Ui_Dialog()
  #myUi = QtTest_Widget.Ui_Form()
  #myUi = QtTest_MainWindow.Ui_MainWindow()
  myUi.setupUi(myWindow)

  myWindow.show()
  sys.exit(myApp.exec_())
"""
#########################-04$.signal_slot_TEST_20190810.Py-#########################

import sys
from QtTest_Dialog import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QDialog

class Ui_Dialog_subclass(Ui_Dialog):
  #pass
  def setupUi(self, Dialog):
    super().setupUi(Dialog)
    self.pushButton.clicked.connect(self.pushButton_clicked)
    #self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
    self.pushButton_2.clicked.connect(Dialog.close)
  def pushButton_clicked(self):
    print("Hello world")
  def pushButton_2_clicked(self):
    Dialog.close
    #self.Dialog.close

if __name__ == '__main__':
  myApp = QApplication(sys.argv)
  myWindow = QDialog()

  #myUi = QtTest_Dialog.Ui_Dialog()
  myUi = Ui_Dialog_subclass()
  myUi.setupUi(myWindow)

  myWindow.show()
  sys.exit(myApp.exec_())


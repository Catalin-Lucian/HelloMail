from designer.uic.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

class CustomMainWindow(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # make comenctions
        print("ok")
        self.button_f4.clicked.connect(partial(self.myfunction,self.frame_4,self.button_f4))
        self.button_f3.clicked.connect(partial(self.myfunction, self.frame_3, self.button_f3))
        self.button_f.clicked.connect(partial(self.myfunction, self.frame, self.button_f))

    def myfunction(self,frame,button,selected):
        print("x"*10)
        self.selected.setMinimumSize(QtCore.QSize(393, 80))
        self.selected.setMaximumSize(QtCore.QSize(393, 80))
        self.hideButton.show()

        frame.setMinimumSize(QtCore.QSize(431, 90))
        frame.setMaximumSize(QtCore.QSize(431, 90))
        button.hide()
        self.hideButton = button
        frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), stop:1 rgba(59, 67, 80, 255));\nborder-radius:10px;")
        self.selected = frame

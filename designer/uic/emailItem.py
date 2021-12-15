from PyQt5 import QtCore, QtGui, QtWidgets


class EmailItem(QtWidgets.QFrame,QtWidgets.QPushButton):
    def __init__(self):
        self.frame.setObjectName("frame")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(393, 80))
        self.frame.setMaximumSize(QtCore.QSize(393, 100))
        self.frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), stop:1 rgba(34, 38, 49, 255));\n"
            "border-radius:10px;")
        self.button = QtWidgets.QPushButton(self.frame_4)
        self.button.setGeometry(QtCore.QRect(0, 0, 393, 80))
        self.button.setMinimumSize(QtCore.QSize(393, 80))
        self.button.setMaximumSize(QtCore.QSize(393, 80))
        self.button.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), stop:1 rgba(34, 38, 49, 255));\n"
            "border-radius:10px;")
        self.button_f4.setObjectName("button_f4")

    def actionItem(self,bool):
        if bool:
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
            self.frame.setSizePolicy(sizePolicy)
            self.frame.setMinimumSize(QtCore.QSize(431, 90))
            self.frame.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), stop:1 rgba(59, 67, 80, 255));\n"
                "border-radius:10px;")
            self.button.hide()


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal


class MailItem(QtWidgets.QFrame):
    clicked = pyqtSignal(QtWidgets.QFrame)

    def __init__(self, container, mailData):
        super(MailItem, self).__init__(container)

        self.mailData = mailData

        self.setupUi()

    def setupUi(self):
        self.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(393, 80))
        self.setMaximumSize(QtCore.QSize(393, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(34, 38, 49, 255));\n "
            "border-radius:10px;")

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.clicked.emit(self)

    def select(self):
        self.setMinimumSize(QtCore.QSize(431, 90))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(59, 67, 80, 255));\n "
            "border-radius:10px;")

    def deselect(self):
        self.setMinimumSize(QtCore.QSize(393, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(34, 38, 49, 255));\n "
            "border-radius:10px;")

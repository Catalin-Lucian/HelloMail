from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QFrame


class MailView(QFrame):
    def __init__(self, container):
        super(MailView, self).__init__(container)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(675, 87, 745, 793))
        self.setMinimumSize(QSize(745, 793))
        self.setStyleSheet("background-color: rgb(59, 67, 80);border-radius:10px;")

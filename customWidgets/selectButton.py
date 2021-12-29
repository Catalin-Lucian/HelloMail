from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect, pyqtSignal, Qt, QEvent
from PyQt5.QtGui import QMouseEvent


class SelectButton(QFrame):
    checked = pyqtSignal(bool)

    def __init__(self, container, settings=None):
        super(SelectButton, self).__init__(container)
        self.settings = settings
        self.settings.subscribe(self)

        self.checkedFlag = False
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(6, 6, 20, 20))
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                           "border: 2px solid rgb(199, 199, 199);\n"
                           "border-radius: 10px;")

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            if self.checkedFlag:
                self.uncheck()
            else:
                self.check()

    def check(self):
        self.setStyleSheet("background-color: rgb(48, 229, 132);\n"
                           "border: 2px solid rgb(48, 229, 132);\n"
                           "border-radius: 10px;")
        self.checkedFlag = True
        self.checked.emit(self.checkedFlag)

    def uncheck(self):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                           "border: 2px solid rgb(199, 199, 199);\n"
                           "border-radius: 10px;")
        self.checkedFlag = False
        self.checked.emit(self.checkedFlag)

    def enterEvent(self, e: QEvent) -> None:
        if not self.checkedFlag:
            self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                               "border: 2px solid rgb(48, 229, 132);\n"
                               "border-radius: 10px;")
        super(SelectButton, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        if not self.checkedFlag:
            self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                               "border: 2px solid rgb(199, 199, 199);\n"
                               "border-radius: 10px;")
        super(SelectButton, self).leaveEvent(e)

    def notify(self):
        pass


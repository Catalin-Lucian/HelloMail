import logging

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect, pyqtSignal, Qt, QEvent
from PyQt5.QtGui import QMouseEvent, QCursor


class SelectButton(QFrame):
    check_signal = pyqtSignal(bool)

    def __init__(self, container):
        super(SelectButton, self).__init__(container)
        self.settings = None

        self.checkedFlag = False
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(6, 6, 20, 20))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        # self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        #                    "border: 2px solid rgb(199, 199, 199);\n"
        #                    "border-radius: 10px;")

    def setSettings(self, settings):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.applyStyleSheet("default")

    def applyStyleSheet(self, state):
        if self.settings:
            style = self.settings.getStyleSheet(self.objectName(), state)
            if style:
                self.setStyleSheet(style)
            else:
                logging.info(f"{self.objectName()} - styleSheet:{state} was empty")
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def check(self):
        # self.setStyleSheet("background-color: rgb(48, 229, 132);\n"
        #                    "border: 2px solid rgb(48, 229, 132);\n"
        #                    "border-radius: 10px;")
        self.applyStyleSheet('pressed')
        self.checkedFlag = True
        self.check_signal.emit(self.checkedFlag)

    def uncheck(self):
        # self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
        #                    "border: 2px solid rgb(199, 199, 199);\n"
        #                    "border-radius: 10px;")
        self.applyStyleSheet('default')
        self.checkedFlag = False
        self.check_signal.emit(self.checkedFlag)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            if self.checkedFlag:
                self.uncheck()
            else:
                self.check()

    def enterEvent(self, e: QEvent) -> None:
        if not self.checkedFlag:
            # self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
            #                    "border: 2px solid rgb(48, 229, 132);\n"
            #                    "border-radius: 10px;")
            self.applyStyleSheet('hover')
        super(SelectButton, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        if not self.checkedFlag:
            # self.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
            #                    "border: 2px solid rgb(199, 199, 199);\n"
            #                    "border-radius: 10px;")
            self.applyStyleSheet('default')
        super(SelectButton, self).leaveEvent(e)

    def notify(self):
        pass


from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QRect, pyqtSignal, Qt
from PyQt5.QtGui import QMouseEvent, QCursor
import logging


class AvatarIcon(QLabel):
    click_signal = pyqtSignal()

    def __init__(self, container):
        super(AvatarIcon, self).__init__(container)
        self.settings = None

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(30, 20, 40, 40))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        # self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                    "border: 0px solid rgb(199, 199, 199);\n"
        #                    "border-radius: 20px;")

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.click_signal.emit()

    def setSettings(self, settings):
        self.settings = settings
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

    def notify(self):
        self.applyStyleSheet("default")

import logging

from PyQt5.QtCore import QRect, QEvent, QPoint, Qt, pyqtSignal
from PyQt5.QtGui import QFont, QMouseEvent
from PyQt5.QtWidgets import QFrame, QPushButton

from HelloMail.customWidgets.buttons.iconClickButton import IconClickButton


class SettingsButton(QFrame):
    click_signal = pyqtSignal()

    def __init__(self, container):
        super(SettingsButton, self).__init__(container)
        self.settingsButton = IconClickButton(self, "settings.svg", "settings.svg", "settings.svg")
        self.setupUi()



    def setupUi(self):
        self.setGeometry(QRect(1405, 384, 188, 59))
        self.setStyleSheet("background-color: rgba(20, 107, 226, 255);"
                           "border-radius:10px;"
                           "text-align:left;"
                           "padding:10px;")
        self.settingsButton.setGeometry(QRect(0, 2, 188, 59))
        self.settingsButton.setText("Settings")
        self.settingsButton.setStyleSheet("color:#FFFFFF;")
        self.settingsButton.click_signal.connect(lambda :self.onClick())

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.settingsButton.setFont(font)


    def setSettings(self, settings):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.searchButton.setSettings(settings)
            self.applyStyleSheet("default")

            style = self.settings.getStyleSheet(self.searchInput.objectName(), 'default')
            self.searchInput.setStyleSheet(style)

        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def applyStyleSheet(self, state):
        if self.settings:
            style = self.settings.getStyleSheet(self.objectName(), state)
            if style:
                self.setStyleSheet(style)
            else:
                logging.info(f"{self.objectName()} - styleSheet:{state} was empty")
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def enterEvent(self, a0: QEvent) -> None:
        pos = self.pos()
        self.move(QPoint(pos.x() - 90, pos.y()))
        super(SettingsButton, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        pos = self.pos()
        self.move(QPoint(pos.x() + 90, pos.y()))
        super(SettingsButton, self).enterEvent(a0)

    def mouseReleaseEvent(self, a0: QMouseEvent):
        if a0.button() == Qt.LeftButton:
            self.onClick()
        super(SettingsButton, self).mouseReleaseEvent(a0)


    def onClick(self):
        self.click_signal.emit()
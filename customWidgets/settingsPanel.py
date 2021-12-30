import logging

from PyQt5.QtCore import QRect, QEvent
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.iconClickButton import IconClickButton


class SettingsPanel(QFrame):

    def __init__(self, container):
        super(SettingsPanel, self).__init__(container)
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
        self.setGeometry(QRect(1310, 384, 188, 59))
        super(SettingsPanel, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self.setGeometry(QRect(1405, 384, 188, 59))
        super(SettingsPanel, self).enterEvent(a0)

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
        self.setStyleSheet("background-color: rgba(20, 107, 226, 1);"
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

    def enterEvent(self, a0: QEvent) -> None:
        self.setGeometry(QRect(1310, 384, 188, 59))
        super(SettingsPanel, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self.setGeometry(QRect(1405, 384, 188, 59))
        super(SettingsPanel, self).enterEvent(a0)

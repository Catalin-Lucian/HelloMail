<<<<<<<< HEAD:customWidgets/buttons/settingsButton.py
import logging

from PyQt5.QtCore import QRect, QEvent, QPoint, pyqtSignal, Qt
from PyQt5.QtGui import QFont, QMouseEvent
========
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QIcon, QFont
>>>>>>>> Cezar:customWidgets/settingsPanel.py
from PyQt5.QtWidgets import QFrame

from HelloMail.customWidgets.buttons.iconClickButton import IconClickButton
from HelloMail.customWidgets.buttons.settingsButton import SettingsButton


class SettingsButton(QFrame):
    click_signal = pyqtSignal()

<<<<<<<< HEAD:customWidgets/buttons/settingsButton.py
    def __init__(self, container):
        super(SettingsButton, self).__init__(container)
        self.settings = None

        self.settingsButton = IconClickButton(self, "settings.svg", "settings.svg", "settings.svg")
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(1405, 384, 188, 59))

        self.settingsButton.setObjectName("settingButton")
        self.settingsButton.setGeometry(QRect(0, 2, 188, 59))
        self.settingsButton.setText("Settings")
        # self.settingsButton.setStyleSheet("color:#FFFFFF;")
        self.settingsButton.click_signal.connect(lambda: self.onClick())
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.settingsButton.setFont(font)

    def setSettings(self, settings):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.settingsButton.setSettings(settings)
            self.applyStyleSheets()

        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def applyStyleSheets(self):
        if self.settings:
            self.settings.applyStylesheet(self)
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def enterEvent(self, a0: QEvent) -> None:
        pos = self.pos()
        self.move(QPoint(pos.x()-90, pos.y()))
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

    def notify(self):
        self.applyStyleSheet()
========
    def __init__(self, parrent):
        super(SettingsPanel, self).__init__(parrent)
        self.cancelButton = IconClickButton(self, "exit_chat_unselected.svg",
                                            "exit_chat_selected.svg",
                                            "exit_chat_selected.svg")
        self.settingsButton = SettingsButton(parrent)
        self.settingsButton.hide()
        self.setupUI()

    def setupUI(self):


        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(20, 20, 1400, 860)
        self.setStyleSheet("background-color: #146BE2;\n"
                           "border-radius: 10px;")

        self.cancelButton.setGeometry(QRect(1346, 12, 35, 35))

        self.cancelButton.click_signal.connect(self.closeSettings)
        self.settingsButton.click_signal.connect(self.openSettings)

        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setGeometry(QRect(1405, 384, 188, 59))
        self.settingsButton.setWindowFlags(Qt.WindowStaysOnTopHint)


    def resizeContent(self, difSize):
        self.resize(difSize.width()+self.size().width(), difSize.height()+self.size().height())
        self.cancelButton.move(difSize.width()+self.cancelButton.pos().x(), self.cancelButton.pos().y())
        self.settingsButton.move(QPoint(self.settingsButton.pos().x() + difSize.width(), self.settingsButton.pos().y()))

    def openSettings(self):
        self.show()
        self.settingsButton.hide()

    def closeSettings(self):
        self.hide()
        self.settingsButton.show()
>>>>>>>> Cezar:customWidgets/settingsPanel.py

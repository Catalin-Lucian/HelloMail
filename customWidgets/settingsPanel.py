from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QFrame

from HelloMail.customWidgets.buttons.iconClickButton import IconClickButton
from HelloMail.customWidgets.buttons.settingsButton import SettingsButton


class SettingsPanel(QFrame):

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
from PyQt5.QtCore import QRect, QEvent
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLineEdit

from customWidgets.iconClickButton import IconClickButton
from customWidgets.settingsPanel import SettingsPanel


class SearchBar(QFrame):

    def __init__(self, parent):
        super(SearchBar, self).__init__(parent)
        self.searchButton = IconClickButton(self, "search_button.svg", "search_button_hover.svg",
                                            "search_button_hover.svg")
        self.searchInput = QLineEdit(self)
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(968, 50, 388, 24))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("background-color: rgba(59, 67, 80, 255);"
                           "border-radius:10px;")
        self.searchButton.setGeometry(QRect(7, 2, 20, 21))
        self.searchButton.setStyleSheet("color:#FFFFFF;")

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.searchButton.setFont(font)

        self.searchInput.setGeometry(QRect(30, 1, 355, 21))
        self.searchInput.setFont(font)
        self.searchInput.setStyleSheet("color: #FFFFFF")

    def enterEvent(self, a0: QEvent) -> None:
        super(SearchBar, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        super(SearchBar, self).enterEvent(a0)

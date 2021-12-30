import logging

from PyQt5.QtCore import QRect, QEvent, pyqtSignal
from PyQt5.QtGui import QFont, QFocusEvent
from PyQt5.QtWidgets import QFrame, QLineEdit

from customWidgets.iconClickButton import IconClickButton


class CustomLineEdit(QLineEdit):
    focus_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)

    def focusInEvent(self, a0: QFocusEvent) -> None:
        self.focus_signal.emit(True)
        super(CustomLineEdit, self).focusInEvent(a0)

    def focusOutEvent(self, a0: QFocusEvent) -> None:
        self.focus_signal.emit(False)
        super(CustomLineEdit, self).focusOutEvent(a0)


class SearchBar(QFrame):

    def __init__(self, parent):
        super(SearchBar, self).__init__(parent)
        self.settings = None

        self.searchButton = IconClickButton(self, "search_button.svg", "search_button_hover.svg",
                                            "search_button_hover.svg")
        self.searchInput = CustomLineEdit(self)
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(968, 50, 388, 24))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        # self.setStyleSheet("background-color: rgba(59, 67, 80, 255);"
        #                    "border-radius:10px;")

        self.searchButton.setObjectName("searchInput")
        self.searchButton.setGeometry(QRect(7, 2, 20, 21))
        # self.searchButton.setStyleSheet("color:#FFFFFF;")

        self.searchInput.setObjectName('searchInput')
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.searchInput.setGeometry(QRect(30, 1, 355, 21))
        self.searchInput.setFont(font)
        self.searchInput.focus_signal.connect(lambda focused: self.onFocusSignal(focused))
        # self.searchInput.setStyleSheet("color: #FFFFFF")

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
        super(SearchBar, self).enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        super(SearchBar, self).enterEvent(a0)

    def onFocusSignal(self, focused):
        if focused:
            self.applyStyleSheet('pressed')
        else:
            self.applyStyleSheet('default')

    def notify(self):
        self.applyStyleSheet('default')
        style = self.settings.getStyleSheet(self.searchInput.objectName(), 'default')
        self.searchInput.setStyleSheet(style)

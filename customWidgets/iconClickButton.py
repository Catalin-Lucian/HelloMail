import logging

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, pyqtSignal, QSize, Qt, QEvent
from PyQt5.QtGui import QMouseEvent, QIcon, QCursor


class IconClickButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, container, iconUnClicked, iconClicked, iconHover):
        super(IconClickButton, self).__init__(container)
        self.settings = None

        self.clickedIcon = QIcon("customWidgets\icons\\" + iconClicked)
        self.unClickedIcon = QIcon("customWidgets\icons\\" + iconUnClicked)
        self.hoverIcon = QIcon("customWidgets\icons\\" + iconHover)

        self.onTop = False
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setText("")
        self.setIcon(self.unClickedIcon)
        self.setCursor(QCursor(Qt.PointingHandCursor))

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
                logging.warning(f"!! {self.objectName()} styleSheet:{state} did not load !!")
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.setIcon(self.clickedIcon)
            self.applyStyleSheet('pressed')
        super(IconClickButton, self).mousePressEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            if self.onTop:
                self.setIcon(self.hoverIcon)
                self.applyStyleSheet('hover')
            else:
                self.setIcon(self.unClickedIcon)
                self.applyStyleSheet('default')
            self.click_signal.emit()

    def enterEvent(self, e: QEvent) -> None:
        self.onTop = True
        self.setIcon(self.hoverIcon)
        self.applyStyleSheet('hover')
        super(IconClickButton, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        self.onTop = False
        self.setIcon(self.unClickedIcon)
        self.applyStyleSheet('default')
        super(IconClickButton, self).enterEvent(e)

    def notify(self):
        if self.onTop:
            self.setIcon(self.hoverIcon)
            self.applyStyleSheet('hover')
        else:
            self.setIcon(self.unClickedIcon)
            self.applyStyleSheet('default')

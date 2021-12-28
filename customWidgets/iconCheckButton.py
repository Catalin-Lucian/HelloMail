from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, pyqtSignal, QSize, Qt, QEvent
from PyQt5.QtGui import QMouseEvent, QIcon


class IconCheckButton(QPushButton):
    check_signal = pyqtSignal(bool)

    def __init__(self, container, iconUnselectedPath, iconSelectedPath, iconHoverPath):
        super(IconCheckButton, self).__init__(container)
        self.selectedIcon = QIcon("customWidgets\icons\\" + iconSelectedPath)
        self.unselectedIcon = QIcon("customWidgets\icons\\" + iconUnselectedPath)
        self.hoverIcon = QIcon("customWidgets\icons\\" + iconHoverPath)

        self.active = False
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setText("")
        self.setIcon(self.unselectedIcon)

    def check(self):
        self.setIcon(self.selectedIcon)
        self.active = True

    def uncheck(self):
        self.setIcon(self.unselectedIcon)
        self.active = False

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            if self.active:
                self.uncheck()
            else:
                self.check()

            self.check_signal.emit(self.active)

    def enterEvent(self, e: QEvent) -> None:
        if not self.active:
            self.setIcon(self.hoverIcon)
        super(IconCheckButton, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        if not self.active:
            self.setIcon(self.unselectedIcon)
        super(IconCheckButton, self).enterEvent(e)

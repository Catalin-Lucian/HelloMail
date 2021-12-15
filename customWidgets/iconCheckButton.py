from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, pyqtSignal, QSize, Qt
from PyQt5.QtGui import QMouseEvent, QIcon


class IconCheckButton(QPushButton):

    checked = pyqtSignal(bool)

    def __init__(self, container, iconUnselectedPath, iconSelectedPath):
        super(IconCheckButton, self).__init__(container)
        self.selectedIcon = QIcon("customWidgets\icons\\" + iconSelectedPath)
        self.unselectedIcon = QIcon("customWidgets\icons\\" + iconUnselectedPath)

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

            self.checked.emit(self.active)


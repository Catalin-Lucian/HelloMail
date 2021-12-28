from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QRect, pyqtSignal, QSize, Qt, QEvent
from PyQt5.QtGui import QMouseEvent, QIcon


class IconClickButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, container, iconUnClicked, iconClicked, iconHover):
        super(IconClickButton, self).__init__(container)
        self.clickedIcon = QIcon("customWidgets\icons\\" + iconClicked)
        self.unClickedIcon = QIcon("customWidgets\icons\\" + iconUnClicked)
        self.hoverIcon = QIcon("customWidgets\icons\\" + iconHover)

        self.onTop = False
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setText("")
        self.setIcon(self.unClickedIcon)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.setIcon(self.clickedIcon)
        super(IconClickButton, self).mousePressEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            if self.onTop:
                self.setIcon(self.hoverIcon)
            else:
                self.setIcon(self.unClickedIcon)
            self.click_signal.emit()

    def enterEvent(self, e: QEvent) -> None:
        self.onTop = True
        self.setIcon(self.hoverIcon)
        super(IconClickButton, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        self.onTop = False
        self.setIcon(self.unClickedIcon)
        super(IconClickButton, self).enterEvent(e)

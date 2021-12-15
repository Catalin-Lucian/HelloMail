from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect, pyqtSignal, Qt
from PyQt5.QtGui import QMouseEvent


class AvatarIcon(QFrame):
    clicked = pyqtSignal()

    def __init__(self, container):
        super(AvatarIcon, self).__init__(container)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(30, 20, 40, 40))
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border: 0px solid rgb(199, 199, 199);\n"
                           "border-radius: 20px;")
        # self.setFrameShape(QFrame.StyledPanel)
        # self.setFrameShadow(QFrame.Raised)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.clicked.emit()

    def setImage(self):
        pass

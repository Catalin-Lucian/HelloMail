import requests
from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtCore import QRect, pyqtSignal, Qt
from PyQt5.QtGui import QMouseEvent, QImage, QPixmap, QBitmap


class AvatarIcon(QLabel):
    click_signal = pyqtSignal()

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
            self.click_signal.emit()

    def setImage(self, imageUrl):
        image = QImage()
        # image.loadFromData(requests.get(imageUrl).content)
        # pixMap = QPixmap(image)
        # pixMap = pixMap.scaled(self.size().width(), self.size().height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # self.setImage(pixMap)
        # self.setScaledContents(True)
        # self.setStyleSheet(f"background-color: transparent;"
        #                    "border: 0px solid rgb(199, 199, 199);"
        #                    "border-radius: 20px;")

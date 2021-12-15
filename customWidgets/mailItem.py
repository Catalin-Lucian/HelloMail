from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel
from customWidgets.selectButton import SelectButton
from customWidgets.avatarIcon import AvatarIcon
from customWidgets.iconCheckButton import IconCheckButton


class MailItem(QtWidgets.QFrame):
    clicked = pyqtSignal(QtWidgets.QFrame)

    def __init__(self, container, mailData):
        super(MailItem, self).__init__(container)
        self.mailData = mailData

        self.selectButton = SelectButton(self)
        self.avatarIcon = AvatarIcon(self)
        self.subjectLabel = QLabel(self)
        self.senderNameLabel = QLabel(self)
        self.dateTimeLabel = QLabel(self)
        self.starIcon = IconCheckButton(self, "star_unselected.svg", "star_selected.svg")

        self.setupUi()
        self.translate()

    def setupUi(self):
        self.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(393, 80))
        self.setMaximumSize(QtCore.QSize(393, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(34, 38, 49, 255));\n "
            "border-radius:10px;")

        self.avatarIcon.clicked.connect(lambda: self.onAvatarIconClick())

        self.subjectLabel.setGeometry(QtCore.QRect(98, 12, 265, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color:#FFFFFF")

        self.senderNameLabel.setGeometry(QtCore.QRect(100, 50, 158, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.senderNameLabel.setFont(font)
        self.senderNameLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "color:#FFFFFF")

        self.dateTimeLabel.setGeometry(QtCore.QRect(295, 65, 90, 8))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.dateTimeLabel.setFont(font)
        self.dateTimeLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "color:#FFFFFF")

        self.starIcon.setGeometry(QtCore.QRect(370, 2, 20, 20))
        self.starIcon.checked.connect(lambda ch: self.onStarChecked(ch))

    def translate(self):
        self.subjectLabel.setText("Email Subject Details")
        self.senderNameLabel.setText("Nume Prenume")
        self.dateTimeLabel.setText("12/12/2021 12:40")

    @QtCore.pyqtSlot()
    def onAvatarIconClick(self):
        self.clicked.emit(self)

    @QtCore.pyqtSlot()
    def onStarChecked(self, checked):
        print("star:" + str(checked))

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.clicked.emit(self)

    def select(self):
        self.setMinimumSize(QtCore.QSize(431, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(59, 67, 80, 255));\n "
            "border-radius:10px;")

    def deselect(self):
        self.setMinimumSize(QtCore.QSize(393, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(34, 38, 49, 255));\n "
            "border-radius:10px;")

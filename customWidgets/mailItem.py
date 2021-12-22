from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel
from customWidgets.selectButton import SelectButton
from customWidgets.avatarIcon import AvatarIcon
from customWidgets.iconCheckButton import IconCheckButton


class MailItem(QtWidgets.QFrame):
    clicked = pyqtSignal(QtWidgets.QFrame)
    checked = pyqtSignal(bool)

    def __init__(self, container, mailData):
        super(MailItem, self).__init__(container)
        self.mailData = mailData

        self.selectButton = SelectButton(self)
        self.avatarIcon = AvatarIcon(self)
        self.subjectLabel = QLabel(self)
        self.senderNameLabel = QLabel(self)
        self.dateTimeLabel = QLabel(self)
        self.starIcon = IconCheckButton(self, "star_unselected.svg", "star_selected.svg", "star_hover.svg")


        self.active = False

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

        self.subjectLabel.setGeometry(QtCore.QRect(98, 13, 265, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color:#FFFFFF")

        self.senderNameLabel.setGeometry(QtCore.QRect(100, 50, 158, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.senderNameLabel.setFont(font)
        self.senderNameLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                           "color:#FFFFFF")

        self.dateTimeLabel.setGeometry(QtCore.QRect(275, 60, 120, 8))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.dateTimeLabel.setFont(font)
        self.dateTimeLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                         "color:#FFFFFF")

        self.selectButton.checked.connect(lambda ch: self.onSelectChecked(ch))

        self.starIcon.setGeometry(QtCore.QRect(370, 2, 20, 20))
        self.starIcon.checked.connect(lambda ch: self.onStarChecked(ch))

    def translate(self):
        self.subjectLabel.setText(self.mailData["subject"])
        self.senderNameLabel.setText(self.mailData["fromName"])
        self.dateTimeLabel.setText(self.mailData["date"])

    @QtCore.pyqtSlot()
    def onAvatarIconClick(self):
        self.clicked.emit(self)

    @QtCore.pyqtSlot()
    def onStarChecked(self, checked):
        print("star:" + str(checked))

    @QtCore.pyqtSlot()
    def onSelectChecked(self, checked):
        self.checked.emit(checked)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.clicked.emit(self)

    def select(self):
        self.active = True
        self.setMinimumSize(QtCore.QSize(431, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(59, 67, 80, 255));\n "
            "border-radius:10px;")

    def deselect(self):
        self.active = False
        self.setMinimumSize(QtCore.QSize(393, 80))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
            "stop:1 rgba(34, 38, 49, 255));\n "
            "border-radius:10px;")

    def enterEvent(self, e: QtCore.QEvent) -> None:
        if not self.active:
            self.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(54, 45, 66, "
                "255), stop:1 rgba(24, 33, 60, 255)); "
                "border-radius:10px;")
        super(MailItem, self).enterEvent(e)

    def leaveEvent(self, e: QtCore.QEvent) -> None:
        if not self.active:
            self.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
                "stop:1 rgba(34, 38, 49, 255));\n "
                "border-radius:10px;")
        super(MailItem, self).enterEvent(e)

import hashlib
import logging
import urllib

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel

from customWidgets.avatarIcon import AvatarIcon
from customWidgets.iconCheckButton import IconCheckButton
from customWidgets.selectButton import SelectButton


class MailItem(QtWidgets.QFrame):
    click_signal = pyqtSignal(QtWidgets.QFrame)
    select_check_signal = pyqtSignal(bool)
    star_check_signal = pyqtSignal(bool, QtWidgets.QFrame)

    def __init__(self, container, mailData):
        super(MailItem, self).__init__(container)
        self.mailData = mailData
        self.settings = None

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

        self.avatarIcon.setObjectName("mailItemAvatarIcon")
        self.avatarIcon.click_signal.connect(lambda: self.onAvatarIconClick())

        self.subjectLabel.setObjectName("mailItemLabel")
        self.subjectLabel.setGeometry(QtCore.QRect(98, 13, 265, 22))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subjectLabel.setFont(font)

        self.senderNameLabel.setObjectName("mailItemLabel")
        self.senderNameLabel.setGeometry(QtCore.QRect(100, 50, 158, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.senderNameLabel.setFont(font)

        self.dateTimeLabel.setObjectName("mailItemLabel")
        self.dateTimeLabel.setGeometry(QtCore.QRect(258, 60, 120, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.dateTimeLabel.setFont(font)

        self.selectButton.setObjectName("mailItemSelectButton")
        self.selectButton.check_signal.connect(lambda ch: self.onSelectChecked(ch))

        self.starIcon.setObjectName("mailItemCheckButton")
        self.starIcon.setGeometry(QtCore.QRect(370, 2, 20, 20))
        self.starIcon.check_signal.connect(lambda ch: self.onStarChecked(ch))

    def translate(self):
        if self.mailData.get('subject'):
            self.subjectLabel.setText(self.mailData.get('subject'))
        else:
            self.subjectLabel.setText("(no subject)")
        self.senderNameLabel.setText(self.mailData.get('from').get('name'))
        self.dateTimeLabel.setText(self.mailData.get('date'))

    def setSettings(self, settings):
        if settings:
            self.settings = settings
            self.avatarIcon.setSettings(settings)
            self.selectButton.setSettings(settings)
            self.starIcon.setSettings(settings)
            if settings:
                self.settings.subscribe(self)
                if "STARRED" in self.mailData.get('labelIds'):
                    self.starIcon.check()

                if 'UNREAD' in self.mailData.get('labelIds'):
                    self.unread()
                else:
                    self.read()
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def applyStyleSheet(self, state):
        if self.settings:
            style = self.settings.getStyleSheet(self.objectName(), state)
            if style:
                self.setStyleSheet(style)
            else:
                logging.warning(f"!! {self.objectName()} styleSheet:{state} did not load !!")
        else:
            logging.warning("-- settings value noneType")

    @QtCore.pyqtSlot()
    def onAvatarIconClick(self):
        self.click_signal.emit(self)
        print(self.mailData.get("id"))

    @QtCore.pyqtSlot()
    def onStarChecked(self, checked):
        self.star_check_signal.emit(checked, self)

    @QtCore.pyqtSlot()
    def onSelectChecked(self, checked):
        self.select_check_signal.emit(checked)

    def enterEvent(self, e: QtCore.QEvent) -> None:
        if not self.active:
            # self.setStyleSheet(
            #     "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(54, 45, 66, "
            #     "255), stop:1 rgba(24, 33, 60, 255)); "
            #     "border-radius:10px;")
            self.applyStyleSheet("hover")
        super(MailItem, self).enterEvent(e)

    def leaveEvent(self, e: QtCore.QEvent) -> None:
        if not self.active:
            if 'UNREAD' in self.mailData['labelIds']:
                self.unread()
            else:
                self.read()
        super(MailItem, self).enterEvent(e)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.click_signal.emit(self)

    def select(self):
        self.active = True
        self.setMinimumSize(QtCore.QSize(431, 80))
        # self.setStyleSheet(
        #     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
        #     "stop:1 rgba(59, 67, 80, 255));\n "
        #     "border-radius:10px;")
        self.applyStyleSheet('pressed')

    def deselect(self):
        self.active = False
        self.setMinimumSize(QtCore.QSize(393, 80))
        if 'UNREAD' in self.mailData['labelIds']:
            self.unread()
        else:
            self.read()

    def read(self):
        self.applyStyleSheet('default_deep')
        style = self.settings.getStyleSheet(self.subjectLabel.objectName(), 'default_deep')
        self.subjectLabel.setStyleSheet(style)

        style = self.settings.getStyleSheet(self.senderNameLabel.objectName(), 'default_deep')
        self.senderNameLabel.setStyleSheet(style)

        style = self.settings.getStyleSheet(self.dateTimeLabel.objectName(), 'default_deep')
        self.dateTimeLabel.setStyleSheet(style)

    def unread(self):
        self.applyStyleSheet('default')
        style = self.settings.getStyleSheet(self.subjectLabel.objectName(), 'default')
        self.subjectLabel.setStyleSheet(style)

        style = self.settings.getStyleSheet(self.senderNameLabel.objectName(), 'default')
        self.senderNameLabel.setStyleSheet(style)

        style = self.settings.getStyleSheet(self.dateTimeLabel.objectName(), 'default')
        self.dateTimeLabel.setStyleSheet(style)

    # def setUnreadStyle(self, isUnread):
    #     if isUnread:
    #         self.setStyleSheet(
    #             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 50, 66, 255), "
    #             "stop:1 rgba(34, 38, 49, 255));\n "
    #             "border-radius:10px;")
    #         self.subjectLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                         "color:#FFFFFF")
    #         self.senderNameLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                            "color:#FFFFFF")
    #         self.dateTimeLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                          "color:#FFFFFF")
    #     else:
    #         self.setStyleSheet(
    #             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 39, 51, 255), "
    #             "stop:1 rgba(31, 34, 45, 255));\n "
    #             "border-radius:10px;")
    #         self.subjectLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                         "color:#8A8A8A")
    #         self.senderNameLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                            "color:#8A8A8A")
    #         self.dateTimeLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
    #                                          "color:#8A8A8A")

    def notify(self):
        pass

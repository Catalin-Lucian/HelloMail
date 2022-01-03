import logging

from PyQt5.QtCore import QRect, QSize, Qt, QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

from customWidgets.buttons.avatarIcon import AvatarIcon
from customWidgets.buttons.iconClickButton import IconClickButton


class MailView(QFrame):
    def __init__(self, container):
        super(MailView, self).__init__(container)
        self.settings = None

        self.mailContentView = QWebEngineView(self)
        self.avatarIcon = AvatarIcon(self)
        self.senderNameLabel = QLabel(self)
        self.senderEmailLabel = QLabel(self)
        self.dateTimeLabel = QLabel(self)
        self.subjectLabel = QLabel(self)

        self.buttonsContainer = QFrame(self)
        self.forwardButton = IconClickButton(self.buttonsContainer, "forward_unselected.svg", "forward_hover.svg",
                                             "forward_hover.svg")
        self.replyButton = IconClickButton(self.buttonsContainer, "reply_unselected.svg", "reply_hover.svg",
                                           "reply_hover.svg")
        self.trashButton = IconClickButton(self.buttonsContainer, "trash_unselected.svg", "trash_hover.svg",
                                           "trash_hover.svg")
        self.starButton = IconClickButton(self, "star_view_unselected.svg", "star_view_hover.svg",
                                          "star_view_hover.svg")

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(675, 87, 745, 793))
        self.setMinimumSize(QSize(745, 793))
        self.setStyleSheet("background-color: rgb(59, 67, 80)")

        self.mailContentView.setObjectName("mailContentView")
        self.mailContentView.setGeometry(QRect(20, 145, 705, 647))
        self.mailContentView.setMinimumSize(QSize(705, 647))
        self.mailContentView.page().setBackgroundColor(Qt.transparent)
        self.mailContentView.setWindowFlag(Qt.WindowStaysOnBottomHint)

        self.avatarIcon.setObjectName("mailViewAvatarIcon")
        self.avatarIcon.setGeometry(QRect(30, 30, 50, 50))
        self.avatarIcon.hide()

        self.senderNameLabel.setObjectName("label")
        self.senderNameLabel.setGeometry(QRect(100, 20, 275, 30))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.senderNameLabel.setFont(font)

        self.senderEmailLabel.setObjectName("label")
        self.senderEmailLabel.setGeometry(QRect(100, 50, 275, 30))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.senderEmailLabel.setFont(font)

        self.dateTimeLabel.setObjectName("label")
        self.dateTimeLabel.setGeometry(QRect(403, 35, 135, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.dateTimeLabel.setFont(font)

        self.subjectLabel.setObjectName("label")
        self.subjectLabel.setGeometry(QRect(20, 100, 705, 35))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setAlignment(Qt.AlignCenter)
        self.subjectLabel.setScaledContents(True)

        self.buttonsContainer.setGeometry(QRect(563, 26, 128, 38))
        self.buttonsContainer.setStyleSheet("background-color: rgb(41, 48, 58);\n""border-radius:10px;")
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.buttonsContainer.hide()

        self.forwardButton.setGeometry(QRect(8, 4, 30, 30))
        self.replyButton.setGeometry(QRect(52, 4, 30, 30))
        self.trashButton.setGeometry(QRect(92, 4, 30, 30))

        self.starButton.setGeometry(QRect(700, 30, 30, 30))
        self.starButton.hide()

    def setSettings(self, settings):
        if settings:
            self.settings = settings
            self.settings.subscribe(self)
            self.avatarIcon.setSettings(settings)
            self.applyStyleSheets()
        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def applyStyleSheets(self):
        if self.settings:
            self.settings.applyStylesheet(self)
            self.settings.applyStylesheet(self.mailContentView)
            self.settings.applyStylesheet(self.avatarIcon)
            self.settings.applyStylesheet(self.senderNameLabel)
            self.settings.applyStylesheet(self.senderEmailLabel)
            self.settings.applyStylesheet(self.dateTimeLabel)
            self.settings.applyStylesheet(self.subjectLabel)

        else:
            logging.warning(f"{self.objectName()}: settings value noneType")

    def setMailContentView(self, mailData):
        if mailData.get('body'):
            self.mailContentView.setHtml(mailData.get('body'))
        self.mailContentView.page().setBackgroundColor(Qt.transparent)
        self.avatarIcon.show()
        self.senderNameLabel.setText(mailData.get('from').get('name'))
        self.senderEmailLabel.setText(mailData.get('from').get('email'))
        self.dateTimeLabel.setText(mailData.get('date'))
        self.subjectLabel.setText(mailData.get('subject'))
        self.buttonsContainer.show()
        self.starButton.show()

    def resizeContent(self, e: QSize):
        self.resize(QSize(self.size().width() + e.width(), self.size().height() + e.height()))
        self.mailContentView.resize(self.mailContentView.size().width() + e.width(),
                                    self.mailContentView.size().height() + e.height())
        self.dateTimeLabel.move(QPoint(self.dateTimeLabel.pos().x() + e.width(), self.dateTimeLabel.pos().y()))
        self.subjectLabel.resize(QSize(self.subjectLabel.size().width() + e.width(), self.subjectLabel.size().height()))

    def notify(self):
        self.applyStyleSheets()

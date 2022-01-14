import logging
import string

from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QSize, Qt, QPoint, QUrl, pyqtSignal, QEvent
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtWidgets import QFrame, QLabel, QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLayout, \
    QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from customWidgets.buttons.avatarIcon import AvatarIcon
from customWidgets.buttons.iconCheckButton import IconCheckButton
from customWidgets.buttons.iconClickButton import IconClickButton


class MailView(QFrame):
    star_check_signal = pyqtSignal(bool)
    reply_check_signal = pyqtSignal(bool)

    def __init__(self, container):
        super(MailView, self).__init__(container)
        self.settings = None

        self.last_time_move = 0

        self.mailContentView = QWebEngineView(self)
        self.customPage = CustomWebPage(self.mailContentView)
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
        self.starButton = IconCheckButton(self, "star_view_unselected.svg", "star_view_selected.svg",
                                          "star_view_hover.svg")

        self.attachmentsScrollArea = QScrollArea(self)
        self.scrollAreaWidgetContents = QWidget(self.attachmentsScrollArea)
        self.verticalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(675, 87, 745, 793))
        self.setMinimumSize(QSize(745, 793))
        self.setStyleSheet("background-color: rgb(59, 67, 80)")

        self.mailContentView.setObjectName("mailContentView")
        self.mailContentView.setGeometry(QRect(20, 180, 705, 647))
        self.mailContentView.setMinimumSize(QSize(705, 647))
        self.mailContentView.setPage(self.customPage)
        self.mailContentView.setWindowFlag(Qt.WindowStaysOnBottomHint)
        self.mailContentView.hide()

        self.avatarIcon.setObjectName("mailViewAvatarIcon")
        self.avatarIcon.setGeometry(QRect(30, 30, 40, 40))
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
        self.subjectLabel.setGeometry(QRect(20, 135, 705, 35))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setAlignment(Qt.AlignCenter)
        self.subjectLabel.setScaledContents(True)
        self.subjectLabel.setWordWrap(True)

        self.buttonsContainer.setGeometry(QRect(563, 26, 128, 38))
        self.buttonsContainer.setStyleSheet("background-color: rgb(41, 48, 58);\n""border-radius:10px;")
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.buttonsContainer.hide()

        self.forwardButton.setGeometry(QRect(8, 4, 30, 30))

        self.replyButton.setGeometry(QRect(52, 4, 30, 30))
        self.replyButton.click_signal.connect(lambda: self.onReplyClicked())

        self.trashButton.setGeometry(QRect(92, 4, 30, 30))

        self.starButton.setGeometry(QRect(700, 30, 30, 30))
        self.starButton.hide()
        self.starButton.check_signal.connect(lambda ch: self.onStarClicked(ch))

        self.attachmentsScrollArea.setEnabled(True)
        self.attachmentsScrollArea.setGeometry(QtCore.QRect(20, 87, 705, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.attachmentsScrollArea.setSizePolicy(sizePolicy)
        self.attachmentsScrollArea.setMinimumSize(QtCore.QSize(705, 40))
        self.attachmentsScrollArea.setMaximumSize(QtCore.QSize(705, 40))
        self.attachmentsScrollArea.setFrameShape(QFrame.NoFrame)
        self.attachmentsScrollArea.setLineWidth(0)
        self.attachmentsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.attachmentsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.attachmentsScrollArea.setWidgetResizable(False)
        self.attachmentsScrollArea.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 705, 40))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 5, 5)
        self.verticalLayout.setSpacing(5)

        self.attachmentsScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scroll_bar = self.attachmentsScrollArea.horizontalScrollBar()
        self.attachmentsScrollArea.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove:
            print(event.pos().x())

            if self.last_time_move == 0:
                self.last_time_move = event.pos().x()

            distance = self.last_time_move - event.pos().x()
            self.scroll_bar.setValue(self.scroll_bar.value() + distance)
            self.last_time_move = event.pos().x()

        elif event.type() == QEvent.MouseButtonRelease:
            self.last_time_move = 0
        return QWidget.eventFilter(self, source, event)

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
        self.mailContentView.show()
        if mailData.get('body'):
            self.mailContentView.setHtml(mailData.get('body'))
        self.avatarIcon.setImage(mailData.get('from').get('email')[0] + ".png")
        self.avatarIcon.show()
        self.senderNameLabel.setText(mailData.get('from').get('name'))
        self.senderEmailLabel.setText(mailData.get('from').get('email'))
        self.dateTimeLabel.setText(mailData.get('date'))
        self.subjectLabel.setText(mailData.get('subject'))
        self.buttonsContainer.show()
        self.starButton.show()

        attachments = mailData.get("attachments")
        if attachments:
            for attachment in attachments:
                attachmentItem = AttachmentButtonIcon(self.scrollAreaWidgetContents)
                attachmentItem.setGeometry(QRect(0, 0, 123, 30))
                attachmentItem.setMinimumSize(123, 30)
                attachmentItem.setObjectName("mailViewAttachment")
                attachmentItem.setSettings(self.settings)
                attachmentItem.setAttachment(attachment)
                self.verticalLayout.addWidget(attachmentItem)

        if "STARRED" in mailData.get('labelIds'):
            self.starButton.check()
        else:
            self.starButton.uncheck()

    def resizeContent(self, e: QSize):
        self.resize(QSize(self.size().width() + e.width(), self.size().height() + e.height()))
        self.mailContentView.resize(self.mailContentView.size().width() + e.width(),
                                    self.mailContentView.size().height() + e.height())
        self.dateTimeLabel.move(QPoint(self.dateTimeLabel.pos().x() + e.width(), self.dateTimeLabel.pos().y()))
        self.subjectLabel.resize(QSize(self.subjectLabel.size().width() + e.width(), self.subjectLabel.size().height()))

        self.buttonsContainer.move(QPoint(self.buttonsContainer.pos().x()+e.width(), self.buttonsContainer.pos().y()))
        self.starButton.move(QPoint(self.starButton.pos().x()+e.width(), self.starButton.pos().y()))

    def notify(self):
        self.applyStyleSheets()

    def checkStar(self, check):
        if check:
            self.starButton.check()
        else:
            self.starButton.uncheck()

    @QtCore.pyqtSlot()
    def onStarClicked(self, check):
        self.star_check_signal.emit(check)

    @QtCore.pyqtSlot()
    def onReplyClicked(self):
        self.reply_check_signal.emit(True)

    def hideMail(self):
        self.mailContentView.hide()
        self.avatarIcon.hide()
        self.senderNameLabel.setText("")
        self.senderEmailLabel.setText("")
        self.dateTimeLabel.setText("")
        self.subjectLabel.setText("")
        self.buttonsContainer.hide()
        self.starButton.hide()


class CustomWebPage(QWebEnginePage):
    def __init__(self, parent):
        super(CustomWebPage, self).__init__(parent)

    def acceptNavigationRequest(self, url: QUrl, type: 'QWebEnginePage.NavigationType', isMainFrame: bool) -> bool:
        if type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url)
            return False
        return True

class AttachmentButtonIcon(IconClickButton):
    def __init__(self, parent):
        super(AttachmentButtonIcon, self).__init__(parent)
        self.attachment = None

    def setAttachment(self, attachment):
        self.attachment = attachment
        if attachment:
            self.setText(attachment["name"])
            self.resize(self.sizeHint().width(), self.sizeHint().height())





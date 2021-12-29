from PyQt5.QtCore import QRect, QSize, Qt, QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

from customWidgets.avatarIcon import AvatarIcon
from customWidgets.iconClickButton import IconClickButton

class MailView(QFrame):
    def __init__(self, container):
        super(MailView, self).__init__(container)
        self.mailContentView = QWebEngineView(self)
        self.avatarIcon = AvatarIcon(self)
        self.senderNameLabel = QLabel(self)
        self.senderEmailLabel = QLabel(self)
        self.dateTimeLabel = QLabel(self)
        self.subjectLabel = QLabel(self)

        self.buttonsContainer = QFrame(self)
        self.forwardButton = IconClickButton(self.buttonsContainer, "forward_unselected.svg", "forward_hover.svg", "forward_hover.svg")
        self.replyButton = IconClickButton(self.buttonsContainer, "reply_unselected.svg", "reply_hover.svg","reply_hover.svg")
        self.trashButton = IconClickButton(self.buttonsContainer, "trash_unselected.svg", "trash_hover.svg", "trash_hover.svg")
        self.starButton = IconClickButton(self, "star_view_unselected.svg", "star_view_hover.svg", "star_view_hover.svg")

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(675, 87, 745, 793))
        self.setMinimumSize(QSize(745, 793))
        self.setStyleSheet("background-color: rgb(59, 67, 80);border-radius:10px;")

        self.mailContentView.setGeometry(QRect(20, 145, 705, 647))
        self.mailContentView.setMinimumSize(QSize(705, 647))
        self.mailContentView.setStyleSheet("QWebEngineView{\n"
                                           "border-color:rgb(58, 110, 255)\n"
                                           "border:10px solid black;"
                                           "border-radius:10px};\n")
        self.mailContentView.page().setBackgroundColor(Qt.transparent)

        self.avatarIcon.setGeometry(QRect(30, 30, 50, 50))
        self.avatarIcon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 0px solid rgb(199, 199, 199);\n"
                                      "border-radius: 25px;")
        self.avatarIcon.hide()

        self.senderNameLabel.setGeometry(QRect(100, 20, 275, 30))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.senderNameLabel.setFont(font)
        self.senderNameLabel.setStyleSheet("color: rgb(255, 255, 255);")

        self.senderEmailLabel.setGeometry(QRect(100, 50, 275, 30))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.senderEmailLabel.setFont(font)
        self.senderEmailLabel.setStyleSheet("color: rgb(255, 255, 255);")

        self.dateTimeLabel.setGeometry(QRect(403, 35, 135, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.dateTimeLabel.setFont(font)
        self.dateTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")

        self.subjectLabel.setGeometry(QRect(20, 100, 705, 35))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setAlignment(Qt.AlignCenter)
        self.subjectLabel.setStyleSheet("color: rgb(255, 255, 255);")
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



    def setMailContentView(self, mailData):
        if mailData.get('body'):
            self.mailContentView.setHtml(mailData.get('body'))
        self.mailContentView.page().setBackgroundColor(Qt.transparent)
        self.avatarIcon.setImage("https://lh3.googleusercontent.com/a-/AOh14GhZ69H4K_rvAjs0P7w-2LJnhujsrAqU0RzI7n-p")
        self.avatarIcon.show()
        self.senderNameLabel.setText(mailData.get('from').get('name'))
        self.senderEmailLabel.setText(mailData.get('from').get('email'))
        self.dateTimeLabel.setText(mailData.get('date'))
        self.subjectLabel.setText(mailData.get('subject'))
        self.buttonsContainer.show()
        self.starButton.show()

        # self.mailContentView.adjustSize()

    def resizeContent(self, e: QSize):
        self.resize(QSize(self.size().width() + e.width(), self.size().height() + e.height()))
        self.mailContentView.resize(self.mailContentView.size().width() + e.width(),
                                    self.mailContentView.size().height() + e.height())
        self.dateTimeLabel.move(QPoint(self.dateTimeLabel.pos().x() + e.width(), self.dateTimeLabel.pos().y()))
        self.subjectLabel.resize(QSize(self.subjectLabel.size().width() + e.width(), self.subjectLabel.size().height()))

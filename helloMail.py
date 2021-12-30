import sys

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import QtCore, QtWidgets, QtGui

from customWidgets.iconClickButton import IconClickButton
from customWidgets.labelList import LabelList

from customWidgets.newMessageDialog import NewMessageDialog
from customWidgets.mailList import MailList
from customWidgets.mailView import MailView
from module.gmailApiService import GoogleApi
from module.settingsConfig import SettingsConfig

from customWidgets.navigationList import NavigationList

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'token/credentials.json'


class HelloMail(QMainWindow):

    def __init__(self):
        super(HelloMail, self).__init__()
        self.hasFirstResize = False

        self.googleApi = GoogleApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')
        self.settings = SettingsConfig()
        self.settings.subscribe(self)

        self.centralWidget = QtWidgets.QWidget(self)
        self.mailList = MailList(self.centralWidget)
        self.mailView = MailView(self.centralWidget)
        self.mailCover = QtWidgets.QFrame(self.centralWidget)

        self.navigation = NavigationList(self.centralWidget)
        self.navigation.setSettings(self.settings)

        # self.labelList = LabelList(self.centralWidget)

        self.newMessageButton = IconClickButton(self, "new_message.svg", "new_message.svg", "new_message.svg")
        self.newMessageButton.setPositionText(20, 156, 209, 45, " New Message",14)

        self.createLabel = QPushButton(self.centralWidget)
        self.createLabel.setGeometry(53, 688, 160, 26)
        self.createLabel.setStyleSheet("background-color: #2D3242;"
                                "color:#FFFFFF;"
                                "border-radius:10px;")

        self.createLabel.setText("+ Create new label")

        self.popup = NewMessageDialog(self.centralWidget)
        self.newMessageButton.click_signal.connect(lambda:self.popup.show())
        self.setupUi()
        self.setupStyleSheets()
        self.addMailItemsOnStartUp()

    def setupUi(self):

        self.setWindowTitle("HelloMail")
        self.resize(1440, 900)
        self.setMinimumSize(QtCore.QSize(1440, 900))
        self.setCentralWidget(self.centralWidget)

        self.mailCover.setGeometry(QtCore.QRect(244, 830, 432, 81))
        self.mailCover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mailCover.setFrameShadow(QtWidgets.QFrame.Raised)

        self.mailList.setObjectName("mailList")
        self.mailList.mailItemChange.connect(lambda mailItem: self.onMailItemChange(mailItem))
        self.mailList.setSettings(self.settings)

        self.mailView.setObjectName("mailView")
        self.mailView.setSettings(self.settings)

    def setupStyleSheets(self):
        self.setStyleSheet(self.settings.getStyleSheet("mainWindow"))
        self.mailCover.setStyleSheet(self.settings.getStyleSheet("mailCover"))

    def addMailItemsOnStartUp(self):
        mails_data = self.googleApi.get_emails_by_tags(["INBOX"], 20)
        for mail_data in mails_data:
            mailItem = self.mailList.addMailItem(mail_data)
            mailItem.star_check_signal.connect(lambda ch, mI: self.onMailItemStarChecked(ch, mI))

    @QtCore.pyqtSlot()
    def onMailItemStarChecked(self, checked, mailItem):
        if checked:
            self.googleApi.modify_labels_to_email(mailItem.mailData.get('id'), ['STARRED'], [])
            mailItem.mailData['labelIds'].append('STARRED')
        else:
            self.googleApi.modify_labels_to_email(mailItem.mailData.get('id'), [], ['STARRED'])
            mailItem.mailData['labelIds'].remove('STARRED')

    @QtCore.pyqtSlot()
    def onMailItemChange(self, mailItem):
        self.mailView.setMailContentView(mailItem.mailData)
        if 'UNREAD' in mailItem.mailData['labelIds']:
            self.googleApi.modify_labels_to_email(mailItem.mailData.get('id'), [], ['UNREAD'])
            mailItem.mailData['labelIds'].remove('UNREAD')

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        if self.hasFirstResize:
            difH = e.size().height() - e.oldSize().height()
            difW = e.size().width() - e.oldSize().width()

            self.mailList.resizeContent(QSize(difW, difH))
            self.mailCover.move(QPoint(self.mailCover.pos().x(), self.mailCover.pos().y() + difH))
            self.mailView.resizeContent(QSize(difW, difH))
            super(HelloMail, self).resizeEvent(e)

        if not self.hasFirstResize:
            self.hasFirstResize = True

    def notify(self):
        # ---------------------- get notification from settings -----------------
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

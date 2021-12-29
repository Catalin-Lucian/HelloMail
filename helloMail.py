import sys

from PyQt5.QtCore import QSize, QPoint, QRect, Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5 import QtCore, QtWidgets, QtGui
from customWidgets.mailList import MailList
from customWidgets.mailView import MailView
from customWidgets.settingsPanel import SettingsPanel
from module.gmailApiService import GoogleApi
from customWidgets.iconClickButton import IconClickButton

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'token/credentials.json'


class HelloMail(QMainWindow):

    def __init__(self):
        super(HelloMail, self).__init__()
        self.hasFirstResize = False

        self.googleApi = GoogleApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')

        self.centralWidget = QtWidgets.QWidget(self)
        self.mailList = MailList(self.centralWidget)
        self.mailView = MailView(self.centralWidget)
        self.mailCover = QtWidgets.QFrame(self.centralWidget)

        self.settingsButton=SettingsPanel(self.centralWidget)
        self.setupUi()
        self.addMailItemsOnStartUp()

    def setupUi(self):
        self.setWindowTitle("HelloMail")
        self.resize(1440, 900)
        self.setMinimumSize(QtCore.QSize(1440, 900))
        self.setStyleSheet("background-color: rgb(24, 29, 35);")
        self.setCentralWidget(self.centralWidget)

        self.mailCover.setGeometry(QtCore.QRect(244, 830, 432, 81))
        self.mailCover.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, "
                                     "stop:0.4 rgba(24, 29, 35, 255), stop:1 rgba(255, 255, 255, 0));")
        self.mailCover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mailCover.setFrameShadow(QtWidgets.QFrame.Raised)

        self.mailList.mailItemChange.connect(lambda mailItem: self.onMailItemChange(mailItem))

        self.settingsButton.setGeometry(QRect(1405, 384, 188, 59))
        self.settingsButton.setStyleSheet("background-color: rgba(20, 107, 226, 1);"
                                          "border-radius:10px;"
                                          "text-align:left;"
                                          "padding:10px;")
        self.settingsButton.setWindowFlags(Qt.WindowStaysOnTopHint)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

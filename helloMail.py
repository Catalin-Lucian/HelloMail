import sys

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from customWidgets.mailList import MailList
from customWidgets.mailView import MailView
from module.gmailApiService import GoogleApi

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

        self.setupUi()
        self.addMailItems()
        self.setupMail()

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

        self.mailList.mailItemChange.connect(lambda mail: self.onMailItemChange(mail))

    @QtCore.pyqtSlot()
    def onMailItemChange(self, mail):
        self.mailView.setMailContentView(mail.mailData)


    def setupMail(self):
        # self.googleApi.test()
        pass

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

    def addMailItems(self):
        mails = self.googleApi.getEmailByTag(["INBOX"])
        for mail in mails:
            self.mailList.addMailItem(mail)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
# from module.gmailApiService import GoogleApi
from customWidgets.mailList import MailList


# API_NAME = 'gmail'
# API_VERSION = 'v1'
# SCOPES = ['https://mail.google.com/']
# CLIENT_FILE = 'token/credentials.json'


class HelloMail(QMainWindow):

    def __init__(self, ):
        super(HelloMail, self).__init__()

        # self.googleApi = GoogleApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')

        self.centralWidget = QtWidgets.QWidget(self)
        self.mailList = MailList(self.centralWidget)

        self.setupUi()
        self.addMailItems()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowTitle("HelloMail")
        self.resize(1440, 900)
        self.setMinimumSize(QtCore.QSize(1440, 900))
        self.setStyleSheet("background-color: rgb(24, 29, 35);")
        self.setCentralWidget(self.centralWidget)

    def addMailItems(self):
        self.mailList.addMailItem("helo")
        self.mailList.addMailItem("sup")
        self.mailList.addMailItem("cio")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

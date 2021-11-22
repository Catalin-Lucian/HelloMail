import sys
from designer.uic.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from module.gmailApiService import GoogleApi

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'credentials.json'


class HelloMail(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.googleApi = GoogleApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

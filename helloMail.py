import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from module.gmailApiService import GoogleApi
from designer.uic.MainWindow import Ui_MainWindow
from designer.uic.Actions import CustomMainWindow

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'token/credentials.json'


class HelloMail(QMainWindow,CustomMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

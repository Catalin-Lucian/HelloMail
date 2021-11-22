import sys
from designer.uic.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from module.gmailApiService import GoogleApi

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'token/credentials.json'


class HelloMail(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.googleApi = GoogleApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')
        self.setupUi(self)
        message = {"id": "1798c09610cffe32"}
        # self.googleApi.read_message(message)
        html = """
        <html lang="en"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>AntenaPlay</title><meta name="description" content=""></head><body style="margin: 0;">
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; background-color: #141414; margin: 0 auto; width: 550px; padding: 0 100px 100px; color: #888; font-size: 18px; line-height: 1.44; font-weight: 300;">
        <img src="https://antenaplay.ro/img/shapes.png" style="float: right; margin-right: -20px; margin-bottom: -18px;"><a href="https://tr.nl.aplay.ro/tr/rot05219EaCzmguGrdcuxQMYovrWD21/f_nagrancynl.eb" target="_blank"><img src="https://antenaplay.ro/img/antenaplaylogo.png" style="margin-bottom: 55px;"></a>
        <p style="margin: 0 0 26px;">Salut rewards,</p>
        <p style="margin: 0 0 26px;">Ai întâmpinat probleme la plata abonamentului? Consultă secțiunea de întrebări frecvente pentru a afla toate detaliile legate de abonament <a href="https://tr.nl.aplay.ro/tr/rot0521BCULocL9knjAoAKTm3ptWD21/f_nwhgbe.nagrancynl.eb" target="_blank" style="color: #00A1E4; text-decoration: none;">ajutor.antenaplay.ro</a></p>
        <a href="https://tr.nl.aplay.ro/tr/rot0521Zx3DujW9pL4Niq3iRefuWD21/f_nagrancynl.eb/pbag/nobanzrag?u=o65p937113p26093nq8R" target="_blank" style="background-color: #00A1E4; text-transform: uppercase; font-weight: bold; color: #fff; text-decoration: none; padding: 15px 30px; border-radius: 50px; display: inline-block; letter-spacing: 1px; margin: 10px 0 0 -2px; font-size: 17px;">Înapoi la pagina abonament </a>
        <div style="height: 36px;"></div>        
        <img src="https://antenaplay.ro/email/opens/10689310/b65c937113c26093ad8E" width="1" height="1"><p style="margin: 0 0 26px;">Te aşteaptă 9 canale LIVE și peste 100.000 de ore de conținut din emisiunile și serialele tale preferate.</p>
        <p style="margin: 0 0 26px;"><strong>Mulţumim,<br>Echipa AntenaPLAY</strong></p>
        <p style="margin: 56px 0 26px; font-size: 14px;">AntenaPlay.ro este un serviciu oferit de Antena TV Group SA, București</p>
        </div>
        <img src="https://tr.nl.aplay.ro/tr/v/40aa04a4-b9c0-11eb-8aed-666ccb90f87e" width="1" height="1" alt="" />
        </body></html>
        """

        self.emailContentTextBrowser.setHtml(html)
        self.emailContentTextBrowser.setOpenExternalLinks(True)
        self.emailContentWebEngine.setHtml(html)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())
import os
import pickle
import sys
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachment MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

from designer.uic.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class HelloMail(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def Create_Service(self, client_secret_file, api_name, api_version, *scopes, prefix=''):
        self.CREDENTIALS = client_secret_file
        self.API_SERVICE_NAME = api_name
        self.API_VERSION = api_version
        self.SCOPES = [scope for scope in scopes[0]]

        cred = None
        working_dir = os.getcwd()
        token_dir = 'token'
        pickle_file = 'token.pickle'

        # Check if token dir exists first, if not, create the folder
        if not os.path.exists(os.path.join(working_dir, token_dir)):
            os.mkdir(os.path.join(working_dir, token_dir))

        if os.path.exists(os.path.join(working_dir, token_dir, pickle_file)):
            with open(os.path.join(working_dir, token_dir, pickle_file), 'rb') as token:
                cred = pickle.load(token)

        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS, SCOPES)
                cred = flow.run_local_server()

            with open(os.path.join(working_dir, token_dir, pickle_file), 'wb') as token:
                pickle.dump(cred, token)

        try:
            self.service = build(self.API_SERVICE_NAME, API_VERSION, credentials=cred)
            print(self.API_SERVICE_NAME, API_VERSION, 'service created successfully')

        except Exception as e:
            print(e)
            print(f'Failed to create service instance for {self.API_SERVICE_NAME}')
            os.remove(os.path.join(working_dir, token_dir, pickle_file))
            self.service = None










    def getLabels(self):
        results = self.service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])

    def show_chatty_threads(self, user_id='me'):
        self.threads = self.service.users().threads().list(userId=user_id).execute().get('threads', [])
        for thread in self.threads:
            tdata = self.service.users().threads().get(userId=user_id, id=thread['id']).execute()
            nmsgs = len(tdata['messages'])

            if nmsgs > 2:  # skip if <3 msgs in thread
                msg = tdata['messages'][0]['payload']
                subject = ''
                for header in msg['headers']:
                    if header['name'] == 'Subject':
                        subject = header['value']
                        break
                if subject:  # skip if no Subject line
                    print('- %s (%d msgs)' % (subject, nmsgs))


# ======================================= MAIN =============================
if __name__ == '__main__':
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    CLIENT_FILE = 'token/credentials.json'

    app = QApplication(sys.argv)
    helloMail = HelloMail()
    helloMail.Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')

    helloMail.show()
    sys.exit(app.exec())

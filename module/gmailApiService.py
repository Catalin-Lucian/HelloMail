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



class GoogleApi:
    def __init__(self, credentials_file, api_name, api_version, *scopes, prefix=''):
        self.CREDENTIALS = credentials_file
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

        print(os.path.join(working_dir, token_dir, pickle_file))
        if os.path.exists(os.path.join(working_dir, token_dir, pickle_file)):
            with open(os.path.join(working_dir, token_dir, pickle_file), 'rb') as token:
                cred = pickle.load(token)

        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS, self.SCOPES)
                cred = flow.run_local_server()

            with open(os.path.join(working_dir, token_dir, pickle_file), 'wb') as token:
                pickle.dump(cred, token)

        try:
            self.service = build(self.API_SERVICE_NAME, self.API_VERSION, credentials=cred)
            print(self.API_SERVICE_NAME, self.API_VERSION, 'service created successfully')


        except Exception as e:
            print(e)
            print(f'Failed to create service instance for {self.API_SERVICE_NAME}')
            os.remove(os.path.join(working_dir, token_dir, pickle_file))
            self.service = None

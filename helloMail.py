import logging
import os
import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QPoint, QRect, Qt

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets, QtGui

from customWidgets.actionBar import ActionBar, ACTION
from customWidgets.labelList import LabelList
from customWidgets.newMessageDialog import NewMessageDialog
from customWidgets.mailList import MailList
from customWidgets.mailView import MailView
from customWidgets.searchBar import SearchBar
from customWidgets.buttons.settingsButton import SettingsButton
from customWidgets.settingsPanel import SettingsPanel
from module.gmailApiService import GmailApi
from customWidgets.buttons.iconClickButton import IconClickButton
from module.settingsConfig import SettingsConfig

from customWidgets.navigationList import NavigationList, BUTTON

API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
CLIENT_FILE = 'token/credentials.json'

logging.basicConfig(level=logging.INFO)


class HelloMail(QMainWindow):

    def __init__(self):
        super(HelloMail, self).__init__()
        self.hasFirstResize = False

        self.gmailApi = GmailApi(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')
        self.settings = SettingsConfig()
        self.settings.subscribe(self)

        self.centralWidget = QtWidgets.QWidget(self)
        self.mailList = MailList(self.centralWidget)
        self.mailView = MailView(self.centralWidget)
        self.mailCover = QtWidgets.QFrame(self.centralWidget)
        self.searchBar = SearchBar(self.centralWidget)
        self.actionBar = ActionBar(self.centralWidget)
        # self.settingsButton = SettingsButton(self.centralWidget)

        self.navigationList = NavigationList(self.centralWidget)

        self.newMessageButton = IconClickButton(self.centralWidget, "new_message.svg", "new_message.svg",
                                                "new_message.svg")

        self.newMessageDialog = NewMessageDialog(self.centralWidget)
        self.labellist = LabelList(self.centralWidget)

        self.settingsPanel = SettingsPanel(self.centralWidget)

        # logo
        self.logoImage = QtWidgets.QLabel(self.centralWidget)
        self.logoImage.setGeometry(QtCore.QRect(3, 40, 260, 59))
        pixmap = QPixmap("customWidgets" + os.path.sep + "icons" + os.path.sep + "logo.png")
        self.logoImage.setPixmap(pixmap)

        # icon
        self.setWindowIcon(QtGui.QIcon("customWidgets" + os.path.sep + "icons" + os.path.sep + "icon.png"))

        self.setupUi()
        self.setupStyleSheets()
        self.addMailItemsOnStartUp()

    def setupUi(self):

        self.setWindowTitle("helloMail")
        self.resize(1440, 900)
        self.setMinimumSize(QtCore.QSize(1440, 900))
        self.setCentralWidget(self.centralWidget)

        self.mailCover.setGeometry(QtCore.QRect(244, 830, 432, 81))
        self.mailCover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mailCover.setFrameShadow(QtWidgets.QFrame.Raised)

        self.mailList.setObjectName("mailList")
        self.mailList.mailItemChange.connect(lambda mailItem: self.onMailItemChange(mailItem))
        self.mailList.firstLastSelectSignal.connect(lambda first: self.actionBar.setCheckButton(first))
        self.mailList.setSettings(self.settings)

        self.newMessageButton.setGeometry(QRect(20, 156, 209, 45))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newMessageButton.setFont(font)
        self.newMessageButton.setText(" New Message")
        self.newMessageButton.setFlat(True)
        self.newMessageButton.setObjectName("textButton")
        self.newMessageButton.setSettings(self.settings)

        self.mailView.setObjectName("mailView")
        self.mailView.setSettings(self.settings)
        self.mailView.star_check_signal.connect(lambda ch: self.onMailViewStarChecked(ch))

        self.navigationList.setSettings(self.settings)
        self.navigationList.label_change_signal.connect(lambda button: self.onLabelChange(button))

        self.newMessageDialog.setSettings(self.settings)
        self.newMessageButton.click_signal.connect(lambda: self.newMessageDialog.show())
        self.newMessageButton.setWindowFlags(Qt.WindowStaysOnBottomHint)

        self.searchBar.setObjectName('searchBar')
        self.searchBar.setSettings(self.settings)
        self.searchBar.search_signal.connect(lambda query: self.onSearch(query))

        self.actionBar.setObjectName("actionBar")
        self.actionBar.setSettings(self.settings)
        self.actionBar.action_signal.connect(lambda action: self.onActionBarSignal(action))

        self.settingsPanel.setObjectName("settingPanel")
        self.settingsPanel.setSettings(self.settings)

        self.labellist.setSettings(self.settings)

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        if self.hasFirstResize:
            difH = e.size().height() - e.oldSize().height()
            difW = e.size().width() - e.oldSize().width()

    def setupStyleSheets(self):
        self.setStyleSheet(self.settings.getStyleSheet("mainWindow"))
        self.mailCover.setStyleSheet(self.settings.getStyleSheet("mailCover"))

    def addMailItemsOnStartUp(self):
        mails_data = self.gmailApi.get_emails_by_tags(["INBOX"], 5)
        for mail_data in mails_data:
            mailItem = self.mailList.addMailItem(mail_data)
            mailItem.star_check_signal.connect(lambda ch, mI: self.onMailItemStarChecked(ch, mI))

    @QtCore.pyqtSlot()
    def onMailItemStarChecked(self, checked, mailItem):
        if checked:
            self.gmailApi.modify_labels_to_email(mailItem.mailData.get('id'), ['STARRED'], [])
            mailItem.mailData['labelIds'].append('STARRED')
        else:
            self.gmailApi.modify_labels_to_email(mailItem.mailData.get('id'), [], ['STARRED'])
            mailItem.mailData['labelIds'].remove('STARRED')
        self.mailView.checkStar(checked)

    @QtCore.pyqtSlot()
    def onMailViewStarChecked(self, checked):
        if checked:
            self.gmailApi.modify_labels_to_email(self.mailList.getSelected().mailData.get('id'), ['STARRED'], [])
            self.mailList.getSelected().mailData['labelIds'].append('STARRED')
        else:
            self.gmailApi.modify_labels_to_email(self.mailList.getSelected().mailData.get('id'), [], ['STARRED'])
            self.mailList.getSelected().mailData['labelIds'].remove('STARRED')
        self.mailList.getSelected().checkStar(checked)

    @QtCore.pyqtSlot()
    def onMailItemChange(self, mailItem):
        self.mailView.setMailContentView(mailItem.mailData)
        if 'UNREAD' in mailItem.mailData['labelIds']:
            self.gmailApi.modify_labels_to_email(mailItem.mailData.get('id'), [], ['UNREAD'])
            mailItem.mailData['labelIds'].remove('UNREAD')

    @QtCore.pyqtSlot()
    def onLabelChange(self, label):
        mails = None
        self.mailView.hideMail()
        self.mailList.clearMailList()
        if label == BUTTON.INBOX:
            mails = self.gmailApi.get_emails_by_tags(['INBOX'], 20)
        elif label == BUTTON.STARRED:
            mails = self.gmailApi.get_emails_by_tags(['STARRED'], 20)
        elif label == BUTTON.SENT:
            mails = self.gmailApi.get_emails_by_tags(['SENT'], 20)
        elif label == BUTTON.SPAM:
            mails = self.gmailApi.get_emails_by_tags(['SPAM'], 20)
        elif label == BUTTON.DRAFT:
            mails = self.gmailApi.get_emails_by_tags(['DRAFT'], 20)
        elif label == BUTTON.TRASH:
            mails = self.gmailApi.get_emails_by_tags(['TRASH'], 20)
        for mail_data in mails:
            mailItem = self.mailList.addMailItem(mail_data)
            mailItem.star_check_signal.connect(lambda ch, mI: self.onMailItemStarChecked(ch, mI))

    @QtCore.pyqtSlot()
    def onActionBarSignal(self, action):
        if action == ACTION.CHECKED_FLAG:
            self.mailList.selectAll()
        elif action == ACTION.UNCHECKED_FLAG:
            self.mailList.unselectAll()
        elif action == ACTION.UNREAD_FLAG:
            mailIds = []
            selectedMails = self.mailList.getSelectedMails()
            selectedMail = self.mailList.getSelected()
            for selected in selectedMails:
                if selectedMail and selected == selectedMail:
                    selectedMail.deselect()
                    self.mailView.hideMail()
                selected.unread()
                mailIds.append(selected.mailData.get('id'))
            self.mailList.clearSelectedList()
            self.actionBar.setCheckButton(False)
            self.gmailApi.modify_labels_to_emails(mailIds, ['UNREAD'], [])
        elif action == ACTION.READ_FLAG:
            mailIds = []
            selectedMails = self.mailList.getSelectedMails()
            selectedMail = self.mailList.getSelected()
            for selected in selectedMails:
                if selectedMail and selected == selectedMail:
                    selectedMail.deselect()
                    self.mailView.hideMail()
                selected.read()
                mailIds.append(selected.mailData.get('id'))
            self.mailList.clearSelectedList()
            self.actionBar.setCheckButton(False)
            self.gmailApi.modify_labels_to_emails(mailIds, [], ['UNREAD'])
        elif action == ACTION.TRASH_FLAG:
            mailIds = []
            selectedMails = self.mailList.getSelectedMails()
            selectedMail = self.mailList.getSelected()
            for selected in selectedMails:
                if selectedMail and selected == selectedMail:
                    selectedMail.deselect()
                    self.mailView.hideMail()
                self.mailList.removeMailItem(selected)
                mailIds.append(selected.mailData.get('id'))
            if self.navigationList.getLabel().replace(" ", "").upper() == "TRASH" or \
                    self.navigationList.getLabel().replace(" ", "").upper() == "SPAM":
                self.gmailApi.delete_emails(mailIds)
            else:
                self.actionBar.setCheckButton(False)
                self.gmailApi.modify_labels_to_emails(mailIds, ['TRASH'], ['INBOX', 'STARRED', 'SPAM'])
            self.mailList.clearSelectedList()
        elif action == ACTION.ARCHIVE_FLAG:
            mailIds = []
            selectedMails = self.mailList.getSelectedMails()
            selectedMail = self.mailList.getSelected()
            for selected in selectedMails:
                if selectedMail and selected == selectedMail:
                    selectedMail.deselect()
                    self.mailView.hideMail()
                self.mailList.removeMailItem(selected)
                mailIds.append(selected.mailData.get('id'))
            self.mailList.clearSelectedList()
            self.actionBar.setCheckButton(False)
            self.gmailApi.modify_labels_to_emails(mailIds, [], ['INBOX'])
        elif action == ACTION.WARNING_FLAG:
            mailIds = []
            selectedMails = self.mailList.getSelectedMails()
            selectedMail = self.mailList.getSelected()
            for selected in selectedMails:
                if selectedMail and selected == selectedMail:
                    selectedMail.deselect()
                    self.mailView.hideMail()
                self.mailList.removeMailItem(selected)
                mailIds.append(selected.mailData.get('id'))
            self.mailList.clearSelectedList()
            self.actionBar.setCheckButton(False)
            self.gmailApi.modify_labels_to_emails(mailIds, ['SPAM'], ['INBOX'])

    @QtCore.pyqtSlot()
    def onSearch(self, query):
        print(query)

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        if self.hasFirstResize:
            difH = e.size().height() - e.oldSize().height()
            difW = e.size().width() - e.oldSize().width()

            self.mailList.resizeContent(QSize(difW, difH))
            self.mailCover.move(QPoint(self.mailCover.pos().x(), self.mailCover.pos().y() + difH))
            self.mailView.resizeContent(QSize(difW, difH))

            self.searchBar.move(QPoint(self.searchBar.pos().x() + difW, self.searchBar.pos().y()))
            self.settingsPanel.resizeContent(QSize(difW, difH))

        if not self.hasFirstResize:
            self.hasFirstResize = True

        super(HelloMail, self).resizeEvent(e)

    def notify(self):
        # ---------------------- get notification from settings -----------------
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helloMail = HelloMail()

    helloMail.show()
    sys.exit(app.exec())

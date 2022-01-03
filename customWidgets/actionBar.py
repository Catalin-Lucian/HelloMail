from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame

from customWidgets.buttons.iconCheckButton import IconCheckButton
from customWidgets.buttons.iconClickButton import IconClickButton


class ActionBar(QFrame):
    def __init__(self, parent):
        super(ActionBar, self).__init__(parent)
        self.settings = None

        self.selectCheckButton = IconCheckButton(self, "circle_unselected.svg", "circle_selected.svg",
                                                 "circle_hover.svg")
        self.archiveButton = IconClickButton(self, "archive_unselected.svg", "archive_hover.svg",
                                             "archive_hover.svg")
        self.warningButton = IconClickButton(self, "warning_unselected.svg", "warning_hover.svg",
                                             "warning_hover.svg")
        self.trashButton = IconClickButton(self, "trash_unselected.svg", "trash_hover.svg", "trash_hover.svg")
        self.unreadMailButton = IconClickButton(self, "mail_unread_unselected.svg", "mail_unread_hover.svg",
                                                "mail_unread_hover.svg")
        self.readMailButton = IconClickButton(self, "mail_read_unselected.svg", "mail_read_hover.svg",
                                              "mail_read_hover.svg")

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(268, 87, 392, 42))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.selectCheckButton.setGeometry(QRect(13, 10, 20, 20))

        self.archiveButton.setGeometry(QRect(97, 10, 22, 21))
        self.warningButton.setGeometry(QRect(140, 4, 36, 36))
        self.trashButton.setGeometry(QRect(190, 4, 34, 34))
        self.unreadMailButton.setGeometry(QRect(292, 15, 26, 18))
        self.readMailButton.setGeometry(QRect(340, 8, 32, 32))

    def setSettings(self, settings):
        self.settings = settings
        if self.settings:
            self.applyStyleSheets()

    def applyStyleSheets(self):
        if self.settings:
            self.settings.applyStylesheet(self)

    def notify(self):
        self.applyStyleSheets()


class ACTION:
    CHECKED_FLAG = 0
    UNCHECKED_FLAG = 1
    ARCHIVE_FLAG = 2
    WARNING_FLAG = 3
    TRASH_FLAG = 4
    UNREAD_FLAG = 5
    READ_FLAG = 6

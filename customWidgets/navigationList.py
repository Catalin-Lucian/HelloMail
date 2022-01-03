from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from customWidgets.buttons.iconCheckButton import IconCheckButton


class NavigationList:
    def __init__(self, container):
        self.container = container
        self.settings = None
        self.selected = None

        self.navigationLabel = QLabel(container)
        self.inboxIcon = IconCheckButton(self.container, "inbox_navigation_unselected.svg",
                                         "inbox_navigation_hover.svg",
                                         "inbox_navigation_hover.svg")
        self.selected = self.inboxIcon

        self.staredIcon = IconCheckButton(self.container, "stared_navigation_unselected.svg",
                                          "stared_navigation_hover.svg",
                                          "stared_navigation_hover.svg")
        self.sentIcon = IconCheckButton(self.container, "sent_navigation_unselected.svg",
                                        "sent_navigation_hover.svg",
                                        "sent_navigation_hover.svg")
        self.warningIcon = IconCheckButton(self.container, "warning_navigation_unselected.svg",
                                           "warning_navigation_hover.svg",
                                           "warning_navigation_hover.svg")
        self.draftsIcon = IconCheckButton(self.container, "drafts_navigation_unselected.svg",
                                          "drafts_navigation_hover.svg",
                                          "drafts_navigation_hover.svg")
        self.trashIcon = IconCheckButton(self.container, "trash_navigation_unselected.svg",
                                         "trash_navigation_hover.svg",
                                         "trash_navigation_hover.svg")

        self.setupUI()

    def setupUI(self):
        self.navigationLabel.setObjectName("label")
        self.navigationLabel.setGeometry(QRect(23, 244, 148, 31))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setWeight(75)
        self.navigationLabel.setFont(font)
        self.navigationLabel.setText("Navigation")

        self.inboxIcon.setObjectName("navigationButton")
        self.inboxIcon.setGeometry(QRect(61, 296, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inboxIcon.setFont(font)
        self.inboxIcon.setText(" Inbox")
        self.inboxIcon.setFlat(True)
        self.inboxIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.inboxIcon))

        self.staredIcon.setObjectName("navigationButton")
        self.staredIcon.setGeometry(QRect(61, 331, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.staredIcon.setFont(font)
        self.staredIcon.setText(" Stared")
        self.staredIcon.setFlat(True)
        self.staredIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.staredIcon))

        self.sentIcon.setObjectName("navigationButton")
        self.sentIcon.setGeometry(QRect(61, 364, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sentIcon.setFont(font)
        self.sentIcon.setText(" Sent")
        self.sentIcon.setFlat(True)
        self.sentIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.sentIcon))

        self.warningIcon.setObjectName("navigationButton")
        self.warningIcon.setGeometry(QRect(61, 397, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.warningIcon.setFont(font)
        self.warningIcon.setText(" Spam")
        self.warningIcon.setFlat(True)
        self.warningIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.warningIcon))

        self.draftsIcon.setObjectName("navigationButton")
        self.draftsIcon.setGeometry(QRect(62, 430, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.draftsIcon.setFont(font)
        self.draftsIcon.setText(" Drafts")
        self.draftsIcon.setFlat(True)
        self.draftsIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.draftsIcon))

        self.trashIcon.setObjectName("navigationButton")
        self.trashIcon.setGeometry(QRect(62, 462, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.trashIcon.setFont(font)
        self.trashIcon.setText(" Trash")
        self.trashIcon.setFlat(True)
        self.trashIcon.check_signal.connect(lambda ch: self.onButtonCheck(self.trashIcon))

    def setSettings(self, settings):
        self.settings = settings
        if settings:
            self.inboxIcon.setSettings(settings)
            self.inboxIcon.check()
            self.staredIcon.setSettings(settings)
            self.sentIcon.setSettings(settings)
            self.warningIcon.setSettings(settings)
            self.draftsIcon.setSettings(settings)
            self.trashIcon.setSettings(settings)

            self.settings.subscribe(self)

            style = settings.getStyleSheet(self.navigationLabel.objectName(), "default")
            self.navigationLabel.setStyleSheet(style)

    def notify(self):
        style = self.settings.getStyleSheet(self.navigationLabel.objectName(), "default")
        self.navigationLabel.setStyleSheet(style)

    def onButtonCheck(self, button: IconCheckButton):
        if self.selected == button:
            button.check()
        else:
            self.selected.uncheck()
            self.selected = button



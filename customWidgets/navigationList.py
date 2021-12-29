from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QPushButton, QWidget, QVBoxLayout, QSpacerItem, QScrollArea, QFrame, \
    QLayout

from HelloMail.customWidgets.iconCheckButton import IconCheckButton


class NavigationList:
    def __init__(self, container):
        self.container = container
        self.selected = None

        self.navigationLabel = QLabel(container)
        self.inboxIcon = IconCheckButton(self.container, "inbox_navigation_unselected.svg",
                                         "inbox_navigation_hover.svg",
                                         "inbox_navigation_hover.svg")
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
        self.navigationLabel.setGeometry(QRect(23, 244, 148, 31))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setWeight(75)
        self.navigationLabel.setFont(font)
        self.navigationLabel.setText("Navigation")
        self.navigationLabel.setStyleSheet("color: #FFFFFF")

        self.inboxIcon.setGeometry(QRect(61, 296, 150, 20))

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inboxIcon.setFont(font)
        self.inboxIcon.setText(" Inbox")
        self.inboxIcon.setFlat(True)
        self.inboxIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })
        self.inboxIcon.check()
        self.currentButton = self.inboxIcon

        self.staredIcon.setGeometry(QRect(61, 331, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.staredIcon.setFont(font)
        self.staredIcon.setText(" Stared")
        self.staredIcon.setFlat(True)
        self.staredIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })

        self.sentIcon.setGeometry(QRect(61, 364, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sentIcon.setFont(font)
        self.sentIcon.setText(" Sent")
        self.sentIcon.setFlat(True)
        self.sentIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })

        self.warningIcon.setGeometry(QRect(61, 397, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.warningIcon.setFont(font)
        self.warningIcon.setText(" Spam")
        self.warningIcon.setFlat(True)
        self.warningIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })

        self.draftsIcon.setGeometry(QRect(62, 430, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.draftsIcon.setFont(font)
        self.draftsIcon.setText(" Drafts")
        self.draftsIcon.setFlat(True)
        self.draftsIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })

        self.trashIcon.setGeometry(QRect(62, 462, 150, 20))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.trashIcon.setFont(font)
        self.trashIcon.setText(" Trash")
        self.trashIcon.setFlat(True)
        self.trashIcon.setThemeStyle({
            'checked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(20, 107, 226, 255)"
            },
            'unchecked': {
                "background-color": "rgba(255, 255, 255, 0)",
                "color": "rgba(255, 255, 255, 255)"
            }
        })










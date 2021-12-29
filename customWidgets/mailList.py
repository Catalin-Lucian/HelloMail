from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QRect
from PyQt5.QtWidgets import QLayout, QFrame

from customWidgets.iconCheckButton import IconCheckButton
from customWidgets.iconClickButton import IconClickButton
from customWidgets.mailItem import MailItem


class MailList(QtWidgets.QScrollArea):
    mailItemChange = pyqtSignal(QtWidgets.QFrame)

    def __init__(self, container):
        super(MailList, self).__init__(container)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.selectedMailItem = None
        self.selectedMails = []

        self.iconsBar = QFrame(container)
        self.selectCheckButton = IconCheckButton(self.iconsBar, "circle_unselected.svg", "circle_selected.svg", "circle_hover.svg")
        self.arhiveButton = IconClickButton(self.iconsBar, "arhive_unselected.svg", "arhive_hover.svg", "arhive_hover.svg")
        self.warningButton = IconClickButton(self.iconsBar, "warning_unselected.svg", "warning_hover.svg", "warning_hover.svg")
        self.trashButton = IconClickButton(self.iconsBar, "trash_unselected.svg", "trash_hover.svg", "trash_hover.svg")
        self.unreadMailButton = IconClickButton(self.iconsBar, "mail_unread_unselected.svg", "mail_unread_hover.svg", "mail_unread_hover.svg")
        self.readMailButton = IconClickButton(self.iconsBar, "mail_read_unselected.svg", "mail_read_hover.svg","mail_read_hover.svg")

        self.setupUi()

    def setupUi(self):
        self.setEnabled(True)
        self.setGeometry(QtCore.QRect(254, 139, 422, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(422, 741))
        self.setMaximumSize(QtCore.QSize(422, 16777215))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 422, 911))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)

        self.iconsBar.setGeometry(QRect(268, 87, 392, 42))
        self.iconsBar.setStyleSheet("background-color: rgba(196, 196, 196, 0.08);\n""border-radius:10px;")
        self.iconsBar.setFrameShape(QFrame.StyledPanel)
        self.iconsBar.setFrameShadow(QFrame.Raised)

        self.selectCheckButton.setGeometry(QRect(13, 10, 20, 20))
        self.arhiveButton.setGeometry(QRect(97, 10, 22, 21))
        self.warningButton.setGeometry(QRect(140, 4, 36, 36))
        self.trashButton.setGeometry(QRect(190, 4, 34, 34))
        self.unreadMailButton.setGeometry(QRect(292, 15, 26, 18))
        self.readMailButton.setGeometry(QRect(340, 8, 32, 32))

    def addMailItem(self, mailData):
        self.verticalLayout.removeItem(self.spacerItem)

        mailItem = MailItem(self.scrollAreaWidgetContents, mailData)
        mailItem.click_signal.connect(lambda itm: self.onMailClicked(itm))
        mailItem.select_check_signal.connect(lambda ch: self.onMailChecked(ch, mailItem))
        # mailItem.star_checked.connect(lambda ch: self.onMailStartChecked(ch, mailItem))
        self.verticalLayout.addWidget(mailItem, 0, Qt.AlignHCenter)
        self.verticalLayout.addSpacerItem(self.spacerItem)

        return mailItem

    def removeMailItem(self, mailItem):
        self.verticalLayout.removeWidget(mailItem)

    @QtCore.pyqtSlot()
    def onMailClicked(self, mailItem):
        if self.selectedMailItem:
            self.selectedMailItem.deselect()
        mailItem.select()
        self.selectedMailItem = mailItem
        self.mailItemChange.emit(mailItem)

    @QtCore.pyqtSlot()
    def onMailChecked(self, checked, mailItem):
        if checked:
            self.selectedMails.append(mailItem)
        else:
            self.selectedMails.remove(mailItem)

    def resizeContent(self, e: QSize) -> None:
        self.resize(QSize(422, self.size().height() + e.height()))
        self.scrollAreaWidgetContents.resize(QSize(422, self.scrollAreaWidgetContents.size().height() + e.height()))
        print(self.size().height())
        print(e.height())

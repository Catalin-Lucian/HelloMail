from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLayout
from customWidgets.mailItem import MailItem


class MailList(QtWidgets.QScrollArea):
    def __init__(self, container):
        super(MailList, self).__init__(container)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.selectedMailItem = None

        self.setupUi()

    def setupUi(self):
        self.setEnabled(True)
        self.setGeometry(QtCore.QRect(254, 139, 422, 762))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(422, 762))
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

    def addMailItem(self, mailData):
        self.verticalLayout.removeItem(self.spacerItem)

        mailItem = MailItem(self.scrollAreaWidgetContents, mailData)
        mailItem.clicked.connect(self.mailClicked)
        self.verticalLayout.addWidget(mailItem, 0, Qt.AlignHCenter)

        self.verticalLayout.addSpacerItem(self.spacerItem)

    def removeMailItem(self, mailItem):
        self.verticalLayout.removeWidget(mailItem)

    @QtCore.pyqtSlot()
    def mailClicked(self, mailItem):
        mailItem.select()
        if self.selectedMailItem:
            self.selectedMailItem.deselect()
        self.selectedMailItem = mailItem

        print(mailItem.mailData)

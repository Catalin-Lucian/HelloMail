from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLayout, QLabel, QFrame


from customWidgets.iconCheckButton import IconCheckButton
from customWidgets.iconClickButton import IconClickButton


class LabelList(QScrollArea):
    def __init__(self, container):

        super().__init__()
        self.container = container

        self.myLabel = QLabel(container)

        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.setupUi()

    def setupUi(self):
        self.myLabel.setGeometry(QRect(23, 512, 148, 31))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setWeight(75)
        self.myLabel.setFont(font)
        self.myLabel.setText("My Labels")
        self.myLabel.setStyleSheet("color: #FFFFFF")

        self.setEnabled(True)
        self.setGeometry(QRect(23, 541, 185, 124))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(185, 741))
        self.setMaximumSize(QSize(185, 16777215))
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 185, 741))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(18)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)
        self.setStyleSheet("color: rgba(255, 255, 255)")

        self.addTagElement("aaaaaaaaaaaaaa")
        self.addTagElement( "xxxx")

    def addTagElement(self,name):
        self.verticalLayout.removeItem(self.spacerItem)

        self.tagIcon = IconClickButton(self.scrollAreaWidgetContents, "tag.svg",
                                         "tag.svg",
                                         "tag.svg")
        self.tagIcon.setPositionText(0, 0, 14, 14, name, 14)

        # self.tagIcon.setGeometry(QRect(0, 0, 14, 14))
        # font = QFont()
        # font.setFamily("Calibri")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setWeight(14)
        # self.tagIcon.setFont(font)
        # self.tagIcon.setText(f" {name}")
        # self.tagIcon.setFlat(True)

        self.verticalLayout.addWidget(self.tagIcon, 0, Qt.AlignHCenter)
        self.verticalLayout.addSpacerItem(self.spacerItem)
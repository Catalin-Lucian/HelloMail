from PyQt5.QtCore import QRect, Qt, QSize, pyqtSignal
from PyQt5.QtGui import QFont, QMouseEvent
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLayout, QLabel, QFrame, \
    QPushButton

from customWidgets.buttons.iconClickButton import IconClickButton
from customWidgets.newLabelFrame import NewLabelFrame
from module.settingsConfig import SettingsConfig


class LabelList(QScrollArea):
    click_signal = pyqtSignal(QFrame)

    def __init__(self, parent):
        super(LabelList, self).__init__(parent)
        self.settings = None


        self.myLabel = QLabel(parent)

        self.scrollAreaWidgetContents = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.createLabel = IconClickButton(parent)

        self.newLabelFrame = NewLabelFrame(parent)
        self.setupUi()

    def setupUi(self):

        self.newLabelFrame.hide()

        self.createLabel.setGeometry(56, 757, 160, 26)
        self.createLabel.setStyleSheet("background-color: #2D3242;"
                                       "color:#FFFFFF;"
                                       "border-radius:10px;")
        self.createLabel.setText("+ Create new label")


        self.myLabel.setGeometry(QRect(23, 512, 148, 31))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setWeight(75)
        self.myLabel.setFont(font)
        self.myLabel.setText("My Labels")
        self.myLabel.setStyleSheet("color: #FFFFFF")

        self.setEnabled(True)
        self.setGeometry(QRect(56, 550, 185, 176))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(185, 176))
        self.setMaximumSize(QSize(185, 176))
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignLeft)

        # self.scrollAreaWidgetContents.setStyleSheet("background-color: #FFFFFF;")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 185, 176))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)
        self.setStyleSheet("color: rgba(255, 255, 255)")

        self.addTagElement("custom 1")

        self.createLabel.click_signal.connect(lambda: self.createLabelShow())

        self.newLabelFrame.create_signal.connect(lambda name: self.addTagElement(name))

    def addTagElement(self, name):
        self.verticalLayout.removeItem(self.spacerItem)

        tagButton = IconClickButton(self.scrollAreaWidgetContents, "tag.svg",
                                         "tag.svg",
                                         "tag.svg")
        tagButton.setStyleSheet("text-align: left;")
        tagButton.setGeometry(QRect(0, 0, 185, 24))

        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        tagButton.setFont(font)
        tagButton.setText(f" {name}")
        tagButton.setFlat(True)

        self.verticalLayout.addWidget(tagButton, 0, Qt.AlignLeft)
        self.verticalLayout.addSpacerItem(self.spacerItem)

    def createLabelShow(self):
        self.newLabelFrame.show()



    def setSettings(self, settings: SettingsConfig):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.newLabelFrame.setSettings(self.settings)

            self.applyStylesheets()

    def applyStylesheets(self):
        self.settings.applyStylesheet(self)

    def notify(self):
        self.applyStylesheets()

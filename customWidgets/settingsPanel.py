from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtWidgets import QFrame, QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLayout

from customWidgets.buttons.iconClickButton import IconClickButton
from customWidgets.buttons.settingsButton import SettingsButton
from customWidgets.settingsElement import CustomStyleWindow


class SettingsPanel(QFrame):

    def __init__(self, parent):
        super(SettingsPanel, self).__init__(parent)
        self.settings = None
        self.cancelButton = IconClickButton(self, "exit_chat_unselected.svg",
                                            "exit_chat_selected.svg",
                                            "exit_chat_selected.svg")
        self.settingsButton = SettingsButton(parent)
        # self.element = SettingElement(self, 642, 251)
        self.hide()

        self.scrollArea = QScrollArea(self)
        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.elementList = []

        self.setupUI()

    def setupUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(20, 20, 1400, 860)



        self.cancelButton.setGeometry(QRect(1346, 12, 35, 35))
        self.cancelButton.click_signal.connect(self.closeSettings)

        self.settingsButton.click_signal.connect(self.openSettings)
        self.settingsButton.setObjectName("settingButton")
        self.settingsButton.setGeometry(QRect(1405, 384, 188, 59))
        self.settingsButton.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(299, 87, 1076, 751))
        # self.verticalLayout.setStyleSheet("background-color:#262B32;")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(422, 741))
        self.scrollArea.setMaximumSize(QSize(422, 16777215))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 422, 911))
        self.scrollAreaWidgetContents.setStyleSheet("background-color:#262B32;")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def setSettings(self, settings):
        self.settings = settings
        if settings:
            settings.subscribe(self)
            self.cancelButton.setSettings(settings)
            self.settingsButton.setSettings(settings)
            self.applyStyleSheets()

    def applyStyleSheets(self):
        if self.settings:
            self.settings.applyStylesheet(self)

    def uploadCustomDesignData(self):
        if self.settings:
            data = self.settings.getTheme()
            elements = data.get('elements')
            for element in elements:
                elementValue = data.get("values").get(element)
                self.addCustomStyleWindow(element, elementValue)

    def addCustomStyleWindow(self, name, value):
        self.verticalLayout.removeItem(self.spacerItem)

        customStyleWindow = CustomStyleWindow(self.scrollAreaWidgetContents)
        customStyleWindow.setObjectName("settingsWidget")
        customStyleWindow.setWindowValues(name, value)
        customStyleWindow.setSettings(self.settings)
        self.elementList.append(customStyleWindow)

        self.verticalLayout.addWidget(customStyleWindow)

        self.verticalLayout.addSpacerItem(self.spacerItem)

    def resizeContent(self, difSize):
        self.resize(difSize.width() + self.size().width(), difSize.height() + self.size().height())
        self.cancelButton.move(difSize.width() + self.cancelButton.pos().x(), self.cancelButton.pos().y())
        self.settingsButton.move(QPoint(self.settingsButton.pos().x() + difSize.width(), self.settingsButton.pos().y()))

    def openSettings(self):
        self.show()
        self.settingsButton.hide()
        self.uploadCustomDesignData()

    def closeSettings(self):
        self.hide()
        self.settingsButton.show()

    def notify(self):
        self.applyStyleSheets()

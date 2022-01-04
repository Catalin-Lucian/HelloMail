from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QLayout

from module.settingsConfig import SettingsConfig


class CustomStyleElement(QFrame):
    def __init__(self, parent):
        super(CustomStyleElement, self).__init__(parent)
        self.settings = None

        self.elementName = QLineEdit(self)
        self.elementValue = QLineEdit(self)
        self.setupUI()

    def setupUI(self):
        self.elementName.setGeometry(QRect(0, 0, 218, 39))
        # setare font
        self.elementName.setObjectName("settingsInput")

        self.elementValue.setGeometry(QRect(218, 0, 539, 39))
        # setare font
        self.elementValue.setObjectName("settingsInput")

    def setSettings(self, settings: SettingsConfig):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.applyStylesheets()

    def getInput(self):
        inputValuesJson = {"name": self.elementName.text(), "value": self.elementValue.text()}
        return inputValuesJson

    def setInput(self, inputValuesJson):
        self.elementName.setText(inputValuesJson.get("name"))
        self.elementValue.setText(inputValuesJson.get("value"))

    def applyStylesheets(self):
        self.settings.applyStylesheet(self)
        self.settings.applyStylesheet(self.elementName)
        self.settings.applyStylesheet(self.elementValue)

    def notify(self):
        self.applyStylesheets()


class CustomStyleState(QScrollArea):
    def __init__(self, parent):
        super(CustomStyleState, self).__init__(parent)
        self.settings = None

        self.stateName = QLabel(self)
        # self.scrollArea = QScrollArea(self)
        self.scrollAreaWidgetContents = QWidget(self)

        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContent)
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.elementList = []

        self.setupUI()

    def setupUI(self):
        self.stateName.setGeometry(QRect(0, 0, 125, 23))
        self.stateName.setObjectName("label")

        self.setEnabled(True)
        self.setGeometry(QRect(0, 0, 902, 115))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(902, 39))
        self.setMaximumSize(QSize(902, 303))
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QRect(125, 0, 777, 115))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)

    def setStateValue(self, stateName, stateValues):
        self.stateName.setText(stateName)

        for stateValue in stateValues:
            self.addCustomStyleElement(stateValue)

    def addCustomStyleElement(self, stateValue):
        self.verticalLayout.removeItem(self.spacerItem)

        customStyleElement = CustomStyleElement(self.scrollAreaWidgetContents)
        customStyleElement.setObjectName("settingsElement")
        customStyleElement.setInput(stateValue)
        customStyleElement.setSettings(self.settings)

        self.elementList.append(customStyleElement)

        self.verticalLayout.addSpacerItem(self.spacer)

    def setSettings(self, settings: SettingsConfig):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.applyStylesheets()

    def applyStylesheets(self):
        self.settings.applyStylesheet(self)
        self.settings.applyStylesheet(self.stateName)

    def notify(self):
        self.applyStylesheets()

    def getValues(self):
        listJson = []
        for element in self.elementList:
            listJson.append(element.getInput())
        return self.stateName.text(), listJson


class CustomStyleWindow(QScrollArea):
    def __init__(self, parent):
        super(CustomStyleWindow, self).__init__(parent)

        self.settings = None

        self.windowName = QLabel(self)
        # self.scrollArea = QScrollArea(self)
        self.scrollAreaWidgetContents = QWidget(self)

        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContent)
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.elementList = []

        self.setupUI()

    def setupUI(self):
        self.windowName.setGeometry(QRect(0, 0, 174, 40))
        self.windowName.setObjectName("label")

        self.setEnabled(True)
        self.setGeometry(QRect(0, 0, 1076, 304))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(1076, 304))
        self.setMaximumSize(QSize(1076, 458))
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(False)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(QRect(125, 0, 777, 115))

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)

    def setWindowValues(self, name, values):
        states = values.get("states")

        for state in states:
            stateValue = values[state]
            self.addCustomStyleState(state, stateValue)

    def getWindowValues(self):
        windowValues = {"states": []}

        for state in self.elementList:
            name, value = state.getValues()
            windowValues["states"].append(name)
            windowValues[name] = value
        return self.windowName.text(), windowValues

    def addCustomStyleState(self, name, value):
        self.verticalLayout.removeItem(self.spacerItem)

        customStyleState = CustomStyleState(self.scrollAreaWidgetContents)
        customStyleState.setObjectName("settingsWindowState")
        customStyleState.setStateValue(name, value)
        customStyleState.setSettings(self.settings)

        self.elementList.append(customStyleState)
        self.verticalLayout.addSpacerItem(self.spacer)

    def setSettings(self, settings: SettingsConfig):
        self.settings = settings
        if settings:
            self.settings.subscribe(self)
            self.applyStylesheets()

    def applyStylesheets(self):
        self.settings.applyStylesheet(self)
        self.settings.applyStylesheet(self.windowName)

    def notify(self):
        self.applyStylesheets()


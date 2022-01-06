import json
import os
from os import listdir
from os.path import isfile
from shlex import join

from PyQt5.QtCore import Qt, QRect, QPoint, QSize, QFileInfo
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QScrollArea, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLayout, QComboBox, \
    QLabel, QTextEdit, QTreeView, QHeaderView, QLineEdit

from customWidgets.buttons.iconClickButton import IconClickButton
from customWidgets.buttons.settingsButton import SettingsButton
from customWidgets.jsonViewer import JsonModel
from module import settingsConfig


class SettingsPanel(QFrame):

    def __init__(self, parent):
        super(SettingsPanel, self).__init__(parent)
        self.settings: settingsConfig = None
        self.cancelButton = IconClickButton(self, "exit_chat_unselected.svg",
                                            "exit_chat_selected.svg",
                                            "exit_chat_selected.svg")

        self.settingsButton = SettingsButton(parent)
        # self.element = SettingElement(self, 642, 251)
        self.languageText = QLabel(self)
        self.themeText = QLabel(self)
        self.customDesignText = QLabel(self)
        self.titleText = QLabel(self)

        self.languageSelect = QComboBox(self)
        self.themeSelect = QComboBox(self)
        # self.customEdit = QTextEdit(self)

        self.view = QTreeView(self)
        self.model = JsonModel(self)

        self.saveButton = IconClickButton(self)

        self.nameFileEdit = QLineEdit(self)

        # self.successLabelInfo = QLabel(self)
        self.applyButton = IconClickButton(self)

        self.hide()

        self.setupUI()

    def setupUI(self):

        self.languageText.setGeometry(31, 130, 235, 30)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.languageText.setFont(font)
        self.languageText.setText("Language")
        self.languageText.setObjectName("label")

        font.setPointSize(25)

        self.titleText.setGeometry(241, 32, 235, 45)
        self.titleText.setFont(font)
        self.titleText.setText("Settings")
        self.titleText.setObjectName("label")

        font.setPointSize(18)

        self.themeText.setGeometry(31, 239, 235, 30)
        self.themeText.setFont(font)
        self.themeText.setText("Theme")
        self.themeText.setObjectName("label")

        self.customDesignText.setGeometry(31, 363, 235, 30)
        self.customDesignText.setFont(font)
        self.customDesignText.setText("Custom Design")
        self.customDesignText.setObjectName("label")

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(799, 0, 648, 901)

        self.cancelButton.setGeometry(QRect(10, 10, 25, 25))
        self.cancelButton.click_signal.connect(self.closeSettings)
        self.cancelButton.setObjectName("iconClickButton")

        self.settingsButton.click_signal.connect(self.openSettings)
        self.settingsButton.setObjectName("settingButton")

        self.settingsButton.setGeometry(QRect(1405, 384, 188, 59))
        self.settingsButton.setWindowFlags(Qt.WindowStaysOnTopHint)

        font.setPointSize(13)

        self.languageSelect.setGeometry(QRect(64, 170, 515, 28))
        self.languageSelect.setFont(font)
        self.languageSelect.setObjectName("settingsComboBox")

        self.themeSelect.setGeometry(QRect(64, 288, 515, 28))
        self.themeSelect.setFont(font)
        self.themeSelect.setObjectName("settingsComboBox")

        self.uploadFiles()

        self.themeSelect.currentTextChanged.connect(lambda: self.themeEventComboBox())

        # self.customEdit.setGeometry(QRect(64, 412, 522, 346))
        # self.customEdit.setFont(font)
        # self.customEdit.setObjectName("settingsComboBox")

        self.view.setModel(self.model)
        json_path = QFileInfo(__file__).absoluteDir().filePath("styles/default.json")
        with open(json_path) as file:
            document = json.load(file)
            self.model.load(document)
        self.view.header().setSectionResizeMode(0, QHeaderView.Stretch)
        # self.view.setAlternatingRowColors(True)
        self.view.resize(522, 346)
        self.view.move(QPoint(64, 412))
        self.view.setObjectName("settingsComboBox")

        self.saveButton.setGeometry(QRect(508, 774, 78, 29))
        self.saveButton.setText("Save")
        self.saveButton.setObjectName("saveButton")
        self.saveButton.click_signal.connect(lambda: self.saveJson())

        self.nameFileEdit.setGeometry(QRect(64, 774, 232, 29))
        self.nameFileEdit.setPlaceholderText("New File Name")
        self.nameFileEdit.setObjectName("saveButton")

        self.applyButton.setGeometry(QRect(402, 774, 78, 29))
        self.applyButton.setText("Apply")
        self.applyButton.setObjectName("saveButton")
        self.applyButton.click_signal.connect(lambda: self.onApplyButton())

    def onApplyButton(self):
        if self.settings:
            themeName = self.themeSelect.currentText()
            self.settings.setTheme(themeName)

    def setSettings(self, settings):
        self.settings = settings
        if settings:
            settings.subscribe(self)
            self.cancelButton.setSettings(settings)
            self.saveButton.setSettings(settings)
            self.settingsButton.setSettings(settings)
            self.applyStyleSheets()

    def applyStyleSheets(self):
        if self.settings:
            self.settings.applyStylesheet(self)
            self.settings.applyStylesheet(self.languageText)
            self.settings.applyStylesheet(self.themeText)
            self.settings.applyStylesheet(self.customDesignText)
            self.settings.applyStylesheet(self.languageSelect)
            self.settings.applyStylesheet(self.themeSelect)
            self.settings.applyStylesheet(self.view)
            self.settings.applyStylesheet(self.nameFileEdit)
            # self.settings.applyStylesheet(self.customEdit)
            self.settings.applyStylesheet(self.titleText)
            self.settings.applyStylesheet(self.applyButton)

    def resizeContent(self, difSize):
        self.move(difSize.width() + self.pos().x(), self.pos().y())
        self.resize(self.size().width(), self.size().height() + difSize.height())
        # self.cancelButton.move(difSize.width() + self.cancelButton.pos().x(), self.cancelButton.pos().y())
        self.settingsButton.move(QPoint(self.settingsButton.pos().x() + difSize.width(), self.settingsButton.pos().y()))

    def openSettings(self):
        self.show()
        self.settingsButton.hide()
        # self.uploadCustomDesignData()

    def closeSettings(self):
        self.hide()
        self.settingsButton.show()

    def notify(self):
        self.applyStyleSheets()

    def uploadFiles(self):
        mypath = os.path.abspath(os.getcwd()) + "\customWidgets\styles"
        files = [f for f in listdir(mypath)]

        for file in files:
            self.themeSelect.addItem(file[:-5])

    def themeEventComboBox(self):
        self.view.setModel(self.model)
        json_path = QFileInfo(__file__).absoluteDir().filePath(f"styles/{self.themeSelect.currentText()}.json")
        with open(json_path) as file:
            document = json.load(file)
            self.model.load(document)
        self.view.header().setSectionResizeMode(0, QHeaderView.Stretch)
        # self.view.setAlternatingRowColors(True)
        self.view.resize(522, 346)
        self.view.move(QPoint(64, 412))
        self.view.setObjectName("settingsComboBox")

    def saveJson(self):
        if self.nameFileEdit.text() != "":
            print(QFileInfo(__file__).absoluteDir().filePath("styles/" + self.nameFileEdit.text() + ".json"))
            f = open(str(QFileInfo(__file__).absoluteDir().filePath("styles/" + self.nameFileEdit.text() + ".json")),
                     'w+')
            json.dump(self.model.to_json(), f)

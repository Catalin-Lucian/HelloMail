import json
import logging

from PyQt5.QtCore import pyqtSignal

from customWidgets.settingsPanel import SettingsPanel


class SettingsConfig:

    def __init__(self):
        self.subs = []
        self.theme = self.initTheme("default")

    def initTheme(self, filename):
        with open(f"customWidgets/styles/{filename}.json") as file_object:
            # store file data in object
            return json.load(file_object)

    def setTheme(self, newTheme):
        self.theme = self.initTheme(newTheme)
        self.notify()

    def getThemeValues(self, element):
        if self.theme:
            return self.theme.get('values').get(element)
        else:
            return None

    def getStyleSheet(self, element, state='default'):
        styleSheet = ""
        elementValues = self.getThemeValues(element)
        if elementValues:
            stateValues = elementValues.get(state)
            if stateValues:
                for elementVal in stateValues:
                    styleSheet = styleSheet + f"{elementVal.get('name')}:{elementVal.get('value')};"
        return styleSheet

    def applyStylesheet(self, widget, state="default"):
        name = widget.objectName()
        style = self.getStyleSheet(name, state)
        if style:
            widget.setStyleSheet(style)
        else:
            logging.info(f"{name} - {state} style not found.")

    def subscribe(self, element):
        self.subs.append(element)

    def unsubscribe(self, element):
        self.subs.remove(element)

    def getTheme(self):
        return self.theme

    def notify(self):
        for sub in self.subs:
            try:
                sub.notify()
            except:
                self.subs.remove(sub)

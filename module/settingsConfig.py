import json


class SettingsConfig:
    def __init__(self):
        self.subs = []
        self.theme = self.initTheme("default.json")

    def initTheme(self, filename):
        with open(f"customWidgets/styles/{filename}") as file_object:
            # store file data in object
            return json.load(file_object)

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

    def subscribe(self, element):
        self.subs.append(element)

    def unsubscribe(self, element):
        self.subs.remove(element)

    def notify(self):
        for sub in self.subs:
            sub.notify()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame


class SettingsPanel(QFrame):

    def __init__(self, parrent):
        super(SettingsPanel, self).__init__(parrent)

        self.setupUI()

    def setupUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        self.setGeometry(20, 20, 1400, 860)
        self.setStyleSheet("background-color: #fffff")

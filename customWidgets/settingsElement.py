import re

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QColorDialog

from customWidgets.buttons.iconClickButton import IconClickButton


class ElementLineEdit(QLineEdit):
    enter_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(ElementLineEdit, self).__init__(parent)
        self.setStyleSheet("background-color: #929497;")
        # self.wrongIco = IconClickButton(self, "wrong.svg",
        #                                     "wrong.svg",
        #                                     "wrong.svg")

        self.setupUI()

    def setupUI(self):
        # self.wrongIco.setGeometry(50,0, 21,21)
        # self.wrongIco.hide()

        self.enter_signal.connect(lambda: self.swapColor())

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == 16777220 or a0.key() == 16777221:  # enter key
            self.enter_signal.emit()
        super(ElementLineEdit, self).keyPressEvent(a0)

    def swapColor(self):

        str = '#'+self.text()  # Your Hex

        isColor = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)
        print(isColor)
        if isColor:
            self.setStyleSheet("background-color: #" + self.text() + ";")
        # else:
            # self.wrongIco.show()


class SettingElement(QFrame):

    def __init__(self, container, x, y):
        super(SettingElement, self).__init__(container)
        self.elementLabel = QLabel(self)
        self.elementEditor = ElementLineEdit(self)

        # self.colorSelect = QColorDialog()
        # self.colorSelect.open()

        self.setupUI(x, y)


    def setupUI(self, x, y):
        self.setGeometry(0, y, 725, 358)
        self.setStyleSheet("background-color: #FA0000;")

        self.elementLabel.setStyleSheet("color: #FFFFFF;")
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.elementLabel.setFont(font)
        self.elementLabel.setText("background-color")
        self.elementLabel.setGeometry(x, y, 168, 49)

        self.elementEditor.setStyleSheet("background-color: #929497;")
        self.elementEditor.setGeometry(x + 180, y + 5, 411, 33)






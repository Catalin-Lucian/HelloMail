from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QFont, QMouseEvent
from PyQt5.QtWidgets import QDialog, QLabel, QTextEdit, QFileDialog, QFrame, QLineEdit

from HelloMail.customWidgets.iconClickButton import IconClickButton


class NewMessageDialog(QDialog):
    def __init__(self, container):
        super().__init__(container)
        self.setWindowTitle("New Message")

        self.container = QFrame(self)

        self.titleLabel = QLabel(self.container)
        self.toLabel = QLabel(self.container)
        self.subjectLabel = QLabel(self.container)

        self.toTextEdit = QLineEdit(self.container)
        self.subjectTextEdit = QLineEdit(self.container)
        self.richTextEdit = QTextEdit(self.container)
        self.filename = ""

        self.pressed = False
        self.lastPos = None

        self.exitIcon = IconClickButton(self.container, "exit_chat_unselected.svg",
                                        "exit_chat_selected.svg",
                                        "exit_chat_selected.svg")

        self.atachmentIco = IconClickButton(self.container, "attachment_popup_unselected.svg",
                                            "attachment_popup_selected.svg",
                                            "attachment_popup_selected.svg")

        self.trashIco = IconClickButton(self.container, "trash_popup_unselected.svg",
                                        "trash_popup_selected.svg",
                                        "trash_popup_selected.svg")

        self.sendIco = IconClickButton(self.container, "send_popup_selected.svg",
                                       "send_popup_selected.svg",
                                       "send_popup_selected.svg")

        self.setupUI()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def setupUI(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setGeometry(QRect(0, 0, 601, 456))
        self.setStyleSheet("background-color: rgba(0,0,0,0);")


        self.container.setStyleSheet("background-color: #262A30;"
                                     "border-radius:10px;")
        self.container.setGeometry(QRect(0, 0, 601, 456))

        self.titleLabel.setGeometry(QRect(247, 11, 127, 22))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        self.titleLabel.setFont(font)
        self.titleLabel.setText("New Message")
        self.titleLabel.setStyleSheet("color: #FFFFFF;")

        self.toLabel.setGeometry(QRect(16, 47, 59, 19))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        self.toLabel.setFont(font)
        self.toLabel.setText("To:")
        self.toLabel.setStyleSheet("color: #FFFFFF;")

        self.subjectLabel.setGeometry(QRect(16, 86, 75, 19))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        self.subjectLabel.setFont(font)
        self.subjectLabel.setText("Subject:")
        self.subjectLabel.setStyleSheet("color: #FFFFFF;")

        self.toTextEdit.setGeometry(QRect(95, 47, 473, 25))
        self.toTextEdit.setStyleSheet("background-color: #929497;"
                                      "border-radius:10px;")

        self.subjectTextEdit.setGeometry(QRect(95, 86, 473, 25))
        self.subjectTextEdit.setStyleSheet("background-color: #929497;"
                                           "border-radius:10px;")

        self.richTextEdit.setGeometry(QRect(16, 125, 555, 262))
        self.richTextEdit.setStyleSheet("background-color: #929497;"
                                        "border-radius:10px;")

        self.exitIcon.setGeometry(QRect(574, 11, 14, 14))
        self.exitIcon.click_signal.connect(self.close)

        self.atachmentIco.setGeometry(QRect(26, 409, 20, 18))
        self.atachmentIco.click_signal.connect(self.openFileNameDialog)

        self.trashIco.setGeometry(QRect(70, 409, 20, 19))
        self.sendIco.setPositionText(469, 400, 103, 34, " Send", 12)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select a file", "",
                                                  "All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName)

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(NewMessageDialog, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(NewMessageDialog, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(NewMessageDialog, self).mouseReleaseEvent(event)

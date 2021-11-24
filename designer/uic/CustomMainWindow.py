from designer.uic.MainWindow import Ui_MainWindow


class CustomMainWindow(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        # make comenctions
        self.testPushButton.clicked.connect(self.test)

    def test(self):
        print('-' * 50)

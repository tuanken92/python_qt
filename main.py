import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSum.clicked.connect(self.sum)

    def sum(self):
        a = int(self.ui.edtA.text())
        b = int(self.ui.edtB.text())
        c = a+b
        self.ui.lbResult.setText(str(c))

if __name__ == "__main__":
    print("function _name_=_main_")
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
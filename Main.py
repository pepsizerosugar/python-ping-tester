import os.path
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Modules.Interface.InitializeUI import InitUI


# Main Class
class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ping Pong")
        self.init_ui()

    # Init UI
    def init_ui(self):
        pointer = InitUI(self)
        pointer.init_layout()


# Main
if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    basedir = os.path.dirname(__file__)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'Resource/img/icon.ico')))

    window = MainClass()

    # Set Dark Theme
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(670, 550)
    mw.show()

    sys.exit(app.exec_())

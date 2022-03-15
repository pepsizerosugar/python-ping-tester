import os.path
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.InitializeUI import InitUI
from Modules.Logger.Logger import Logger


# Main Class
class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        UIElements.main_window = self
        self.init_ui()

    # Init UI
    @staticmethod
    def init_ui():
        Logger().__init__()
        InitUI().init_layout()


# Main
if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    basedir = os.path.dirname(__file__)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'Resource/Img/icon.ico')))
    qtmodern.styles.dark(app)

    window = MainClass()
    window.setWindowTitle("Ping Pong")

    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(670, 550)
    mw.show()

    sys.exit(app.exec_())

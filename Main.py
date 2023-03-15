import os.path
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Modules import Interface
from Modules import Logger


# Main Class
class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()
        Logger.init_logger()
        Interface.UIElements.main_window = self
        Interface.InitUI().init_layout()


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
    mw.setFixedSize(755, 550)
    mw.show()

    sys.exit(app.exec_())

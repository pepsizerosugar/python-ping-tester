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
        self.logger = None
        self.init_ui()

    # Init UI
    def init_ui(self):
        self.init_logger()
        pointer = InitUI(self)
        pointer.init_layout()

    def init_logger(self):
        import logging.handlers
        import os

        os.makedirs('Logs', exist_ok=True)

        self.logger = logging.getLogger('ping_test_logger')
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.handlers.RotatingFileHandler('Logs/ping_test.log', maxBytes=1048576, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info('Start Ping Pong app')


# Main
if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    basedir = os.path.dirname(__file__)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'Resource/img/icon.ico')))

    window = MainClass()
    window.setWindowTitle("Ping Pong")

    # Set Dark Theme
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(670, 550)
    mw.show()

    sys.exit(app.exec_())

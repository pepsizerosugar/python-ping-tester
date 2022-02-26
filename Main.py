import os.path
import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QVBoxLayout, QTabWidget

from InitPingTab import InitPingTab
from InitResultTab import InitResultTab

basedir = os.path.dirname(__file__)


# Main Class
class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.logger = None
        self.ping_widget = None
        self.result_widget = None

        self.init_logger()
        self.init_ui()
        self.init_widget()
        self.move_center()

    # Init UI
    def init_ui(self):
        ping_tab = InitPingTab(self)
        ping_tab.init_layout()
        self.ping_widget = ping_tab.ping_widget

        result_tab = InitResultTab(self)
        result_tab.init_layout()
        self.result_widget = result_tab.result_widget

    # Init widget
    def init_widget(self):
        tabs = QTabWidget()
        tabs.addTab(self.ping_widget, "Ping")
        tabs.addTab(self.result_widget, "Result")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)

        self.setCentralWidget(tabs)

    # Center Window
    def move_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_logger(self):
        import logging.handlers
        self.logger = logging.getLogger('ping_test_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.handlers.RotatingFileHandler('ping_test.log', maxBytes=1048576, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info('Start Ping Pong')


# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Ping Pong")
    app.setWindowIcon(QIcon(os.path.join(basedir, 'resource/img/icon.ico')))
    window = MainClass()

    # Set Dark Theme
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(670, 550)
    mw.show()

    sys.exit(app.exec_())

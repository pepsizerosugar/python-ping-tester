import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from InitializeUI import InitUI


# Main Class
class MainClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ping Pong")
        self.setWindowIcon(QIcon('resource/img/icon.ico'))

        self.init_ui()

    # Init UI
    def init_ui(self):
        pointer = InitUI(self)
        pointer.init_layout()


# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainClass()

    # Set Dark Theme
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(600, 500)
    mw.show()

    sys.exit(app.exec_())

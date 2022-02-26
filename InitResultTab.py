from PyQt5.QtWidgets import QGridLayout, QWidget


class InitResultTab:
    def __init__(self, parent):
        self.parent = parent
        self.logger = self.parent.logger

        self.logger.info('Initialize Result Tab')

        self.result_layout = QGridLayout()
        self.result_widget = None

    # Init layout
    def init_layout(self):
        self.logger.info('Initialize Layout')

        self.result_layout.setSpacing(10)
        self.result_layout.setContentsMargins(10, 10, 10, 10)

        self.init_widget()

    # Init widget
    def init_widget(self):
        self.logger.info('Initialize widget')

        self.result_widget = QWidget()
        self.result_widget.setLayout(self.result_layout)

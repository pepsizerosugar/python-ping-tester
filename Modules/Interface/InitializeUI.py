from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QProgressBar

from Modules.Interface.DataClass.EventElements import EventElements
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Group.InitInteractionGroup import InitInteractionGroup
from Modules.Interface.Group.InitServerListGroup import InitServerListGroup


class InitUI:
    def __init__(self, parent):
        super().__init__()
        self.logger = EventElements.logger
        self.parent = parent
        self.server_analyzer = None

        self.logger.info('Initialize UI')

        self.main_layout = QGridLayout()
        self.main_widget = None

        UIElements.progress_bar = QProgressBar()

        # for ProgressHandler
        self.checked_server_list = []

    # Init layout
    def init_layout(self):
        self.logger.info('Initialize layout')

        # Set style
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Init group box
        self.init_group_box()

        # Add Widgets to layout
        self.main_layout.addWidget(UIElements.ping_btn_group_box, 0, 0)
        self.main_layout.addWidget(UIElements.server_list_group_box, 1, 0)
        self.main_layout.addWidget(UIElements.progress_bar, 2, 0)

        self.init_widget()
        self.move_center()
        self.logger.info('Initialize UI finished')

    # Init group box
    def init_group_box(self):
        InitInteractionGroup(self)
        InitServerListGroup(self)

    # Init widget
    def init_widget(self):
        self.logger.info('Initialize widget')

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.parent.setCentralWidget(self.main_widget)

    # Center Window
    def move_center(self):
        qr = self.parent.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.parent.move(qr.topLeft())

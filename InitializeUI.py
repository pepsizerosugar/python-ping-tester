from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QPushButton, QTableWidget, QWidget, QDesktopWidget, QMessageBox, \
    QHBoxLayout, QCheckBox, QTableWidgetItem, QProgressBar

from ButtonHandler import ButtonHandler


class InitUI:
    def __init__(self, parent):
        super().__init__()
        self.logger = None
        self.parent = parent

        self.init_logger()
        self.logger.info('Initialize UI')

        self.main_layout = QGridLayout()
        self.main_widget = None

        self.ping_btn_group_box = None
        self.check_all_btn = None
        self.uncheck_all_btn = None
        self.ping_btn = None
        self.clear_btn = None

        self.server_list_group_box = None
        self.server_list_table = None
        self.server_list = None

        self.progress_bar = QProgressBar()

        # for ProgressHandler
        self.checked_server_list = []
        self.button_handler = ButtonHandler(self)
        self.enable_buttons = self.button_handler.enable_buttons

        self.init_layout()
        self.init_widget()
        self.move_center()

        self.logger.info('Initialize UI finished')

    # Init layout
    def init_layout(self):
        self.logger.info('Initialize layout')

        # Set style
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Init group box
        self.init_group_box()

        # Add Widgets to layout
        self.main_layout.addWidget(self.ping_btn_group_box, 0, 0)
        self.main_layout.addWidget(self.server_list_group_box, 1, 0)
        self.main_layout.addWidget(self.progress_bar, 2, 0)

    # Init group box
    def init_group_box(self):
        self.init_ping_btn_groupbox()
        self.init_server_list_groupbox()

    # Init ping button group box
    def init_ping_btn_groupbox(self):
        self.logger.info('Initialize Ping Button Group Box')

        self.ping_btn_group_box = QGroupBox("Ping")
        self.ping_btn_group_box.setLayout(QGridLayout())

        self.check_all_btn = QPushButton("Check All")
        self.uncheck_all_btn = QPushButton("Uncheck All")
        self.ping_btn = QPushButton("Ping")
        self.clear_btn = QPushButton("Clear")

        self.ping_btn_group_box.layout().addWidget(self.check_all_btn, 0, 1)
        self.ping_btn_group_box.layout().addWidget(self.uncheck_all_btn, 0, 2)
        self.ping_btn_group_box.layout().addWidget(self.ping_btn, 0, 3)
        self.ping_btn_group_box.layout().addWidget(self.clear_btn, 0, 4)

        # Set button event handler
        self.check_all_btn.clicked.connect(self.button_handler.check_all_btn_clicked)
        self.uncheck_all_btn.clicked.connect(self.button_handler.uncheck_all_btn_clicked)
        self.ping_btn.clicked.connect(self.button_handler.ping_btn_clicked)
        self.clear_btn.clicked.connect(self.button_handler.clear_btn_clicked)

    # Init server list group box
    def init_server_list_groupbox(self):
        self.logger.info('Initialize Server List Group Box')

        self.server_list_group_box = QGroupBox("Server List")
        self.server_list_group_box.setLayout(QGridLayout())

        # Set server list table
        self.server_list_table = QTableWidget()
        self.server_list_table.setSortingEnabled(False)
        self.server_list_table.setColumnCount(7)
        self.server_list_table.setHorizontalHeaderLabels(
            ['✔', 'Server', 'Region', 'IP', 'Min(ms)', 'Max(ms)', 'Avg(ms)'])

        # First init server list table size
        self.server_list_table.setColumnWidth(0, 10)
        self.server_list_table.setColumnWidth(1, 100)
        self.server_list_table.setColumnWidth(2, 50)
        self.server_list_table.setColumnWidth(3, 120)
        self.server_list_table.setColumnWidth(4, 70)
        self.server_list_table.setColumnWidth(5, 70)
        self.server_list_table.setColumnWidth(6, 70)

        self.server_list_group_box.layout().addWidget(self.server_list_table, 0, 0)

        # Init server list
        self.server_list = self.init_server_list(self.parent)

        # Set server list table
        self.server_list_table.setRowCount(len(self.server_list))
        self.logger.info('Initialize server list table')
        for i in range(len(self.server_list)):
            self.insert_server_list_table(i, self.server_list[i])

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

    # Init server list
    def init_server_list(self, parent):
        self.logger.info('Initialize server list')

        # Load server list
        try:
            server_structure = []
            with open('server_list.json', 'r') as f:
                import json
                data = json.load(f)
                server_list = data['server_list']
                json.dumps(server_list, sort_keys=True)
                for server in server_list:
                    for ip in server_list[server]['ip_addresses']:
                        server_structure.append({
                            'server': server,
                            'region': server_list[server]['region'],
                            'ip': ip,
                        })
        except FileNotFoundError:
            server_structure = []
            self.logger.error('Server list file not found')
            QMessageBox.warning(self.parent, 'Error', 'Server list file not found')
        return server_structure

    # Insert server list table
    def insert_server_list_table(self, row, server):
        cell_widget = QWidget()
        check_box_layout = QHBoxLayout()
        check_box_layout.addWidget(QCheckBox())
        check_box_layout.setAlignment(Qt.AlignCenter)
        check_box_layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(check_box_layout)

        self.server_list_table.setCellWidget(row, 0, cell_widget)
        self.server_list_table.setItem(row, 1, QTableWidgetItem(server['server']))
        self.server_list_table.setItem(row, 2, QTableWidgetItem(server['region']))
        self.server_list_table.setItem(row, 3, QTableWidgetItem(server['ip']))

    def init_logger(self):
        import logging.handlers
        self.logger = logging.getLogger('ping_test_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.handlers.RotatingFileHandler('ping_test.log', maxBytes=1048576, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info('Start Ping Test app')

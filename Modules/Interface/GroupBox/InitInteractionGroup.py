from PyQt5.QtWidgets import QGroupBox, QGridLayout, QComboBox, QPushButton

from Modules.Analyze.ServerAnalyze import ServerAnalyze
from Modules.Handler.ButtonHandler import ButtonHandler
from Modules.Handler.ComboBoxHandler import ComboBoxHandler
from Modules.Interface.DataClass.EventElements import EventElements
from Modules.Interface.DataClass.ServerData import Server
from Modules.Interface.DataClass.UIElement import UIElements


class InitInteractionGroup:
    def __init__(self):
        self.logger = EventElements.logger

        self.button_handler = ButtonHandler(self)
        self.enable_buttons = self.button_handler.enable_interaction
        self.combobox_handler = ComboBoxHandler()

        self.init_interaction_groupbox()

    # Init ping button group box
    def init_interaction_groupbox(self):
        self.logger.info('Initialize Ping Button GroupBox Box')

        UIElements.ping_btn_group_box = QGroupBox()
        UIElements.ping_btn_group_box.setLayout(QGridLayout())
        UIElements.ping_btn_group_box.setStyleSheet(
            "QGroupBox { background-color: palette(alternate-base);  border: 1px solid palette(midlight); margin-top: 0px; }")

        self.init_combo_box()

        UIElements.check_btn = QPushButton('Check')
        UIElements.uncheck_btn = QPushButton('Uncheck')
        UIElements.ping_btn = QPushButton('Ping')
        UIElements.clear_btn = QPushButton('Clear')

        # Set button event handler
        UIElements.check_btn.clicked.connect(self.button_handler.check_btn_clicked)
        UIElements.uncheck_btn.clicked.connect(self.button_handler.uncheck_btn_clicked)
        UIElements.ping_btn.clicked.connect(self.button_handler.ping_btn_clicked)
        UIElements.clear_btn.clicked.connect(self.button_handler.clear_btn_clicked)

        UIElements.ping_btn_group_box.layout().addWidget(UIElements.check_btn, 0, 3)
        UIElements.ping_btn_group_box.layout().addWidget(UIElements.uncheck_btn, 0, 4)
        UIElements.ping_btn_group_box.layout().addWidget(UIElements.ping_btn, 0, 5)
        UIElements.ping_btn_group_box.layout().addWidget(UIElements.clear_btn, 0, 6)

    # Init combo box
    def init_combo_box(self):
        UIElements.type_combo_box = QComboBox()
        UIElements.select_combo_box = QComboBox()

        UIElements.type_combo_box.addItems(['All', 'Server', 'Region'])

        # Set combo box event handler
        UIElements.type_combo_box.currentIndexChanged.connect(self.combobox_handler.type_combo_box_changed)
        UIElements.select_combo_box.currentIndexChanged.connect(self.combobox_handler.select_combo_box_changed)

        # Init server list
        self.init_server_list()
        ServerAnalyze().collect_by_server()

        UIElements.ping_btn_group_box.layout().addWidget(UIElements.type_combo_box, 0, 0)
        UIElements.ping_btn_group_box.layout().addWidget(UIElements.select_combo_box, 0, 1)

    # Init server list
    def init_server_list(self):
        self.logger.info('Initialize server list')

        # Load server list
        try:
            Server.server_list = []
            with open('Resource/Server/server_list.json', 'r') as f:
                import json
                data = json.load(f)
                server_list = data['server_list']
                json.dumps(server_list, sort_keys=True)
                for server in server_list:
                    for ip in server_list[server]['ip_addresses']:
                        Server.server_list.append({
                            'server': server,
                            'region': server_list[server]['region'],
                            'ip': ip,
                        })
        except FileNotFoundError:
            Server.server_list = []
            self.logger.error('Server list file not found')
            from Modules.Interface.Dialog import Dialogs
            Dialogs.when_server_list_file_not_found()
        return Server.server_list

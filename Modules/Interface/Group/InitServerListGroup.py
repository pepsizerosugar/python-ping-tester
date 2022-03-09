from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QTableWidget, QGridLayout, QWidget, QHBoxLayout, QCheckBox, QTableWidgetItem

from Modules.Interface.DataClass.EventElements import EventElements
from Modules.Interface.DataClass.UIElement import UIElements


class InitServerListGroup:
    def __init__(self, parent):
        self.parent = parent
        self.logger = EventElements.logger

        self.init_server_list_groupbox()

    # Init server list group box
    def init_server_list_groupbox(self):
        self.logger.info('Initialize Server List Group Box')

        UIElements.server_list_group_box = QGroupBox()
        UIElements.server_list_group_box.setLayout(QGridLayout())
        UIElements.server_list_group_box.setStyleSheet(
            "QGroupBox { background-color: palette(alternate-base);  border: 1px solid palette(midlight); margin-top: 0px; }")

        # Set server list table
        UIElements.server_list_table = QTableWidget()
        UIElements.server_list_table.setSortingEnabled(False)
        UIElements.server_list_table.setColumnCount(8)
        UIElements.server_list_table.setHorizontalHeaderLabels(
            ['✔', 'Server', 'Region', 'IP', 'Min(ms)', 'Max(ms)', 'Avg(ms)', 'Loss(%)'])

        # First init server list table size
        UIElements.server_list_table.setColumnWidth(0, 10)
        UIElements.server_list_table.setColumnWidth(1, 100)
        UIElements.server_list_table.setColumnWidth(2, 50)
        UIElements.server_list_table.setColumnWidth(3, 120)
        UIElements.server_list_table.setColumnWidth(4, 70)
        UIElements.server_list_table.setColumnWidth(5, 70)
        UIElements.server_list_table.setColumnWidth(6, 70)
        UIElements.server_list_table.setColumnWidth(7, 70)

        UIElements.server_list_group_box.layout().addWidget(UIElements.server_list_table, 0, 0)

        # Set server list table
        from Modules.Interface.DataClass.ServerData import Server
        UIElements.server_list_table.setRowCount(len(Server.server_list))
        self.logger.info('Initialize server list table')
        for i, server in enumerate(Server.server_list):
            self.insert_server_list_table(i, server)

    # Insert server list table
    @staticmethod
    def insert_server_list_table(row, server):
        cell_widget = QWidget()
        check_box_layout = QHBoxLayout()
        check_box_layout.addWidget(QCheckBox())
        check_box_layout.setAlignment(Qt.AlignCenter)
        check_box_layout.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(check_box_layout)

        UIElements.server_list_table.setCellWidget(row, 0, cell_widget)
        UIElements.server_list_table.setItem(row, 1, QTableWidgetItem(server['server']))
        UIElements.server_list_table.setItem(row, 2, QTableWidgetItem(server['region']))
        UIElements.server_list_table.setItem(row, 3, QTableWidgetItem(server['ip']))

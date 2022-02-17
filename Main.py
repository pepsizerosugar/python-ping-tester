import sys
import json
import logging.handlers

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGridLayout, QWidget, QGroupBox, QPushButton, QTableWidget, \
    QMessageBox, QTableWidgetItem, QCheckBox, QApplication

# Server list format: [
#           {
#              'name': '',
#              'region': '',
#              'ipAddresses': [
#                  "000.000.000.000",
#                  "000.000.000.000",
#              ]
#           },
#           {
#              'name': '',
#              'region': '',
#              'ipAddresses': [
#                  "000.000.000.000",
#                  "000.000.000.000",
#              ]
#           }
# ]


# Logging setup
logger = logging.getLogger('pingTest')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.handlers.RotatingFileHandler('pingTest.log', maxBytes=1048576, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('Start Ping Test app')


# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_layout = None
        self.main_widget = None
        self.ping_btn_group_box = None
        self.server_list_group_box = None
        self.server_list_table = None
        self.server_list = None

        self.setWindowTitle("Ping Pong")
        self.setFixedSize(600, 400)

        self.init_ui()

    # Init UI
    def init_ui(self):
        logger.info('Initialize UI')
        # Init layout
        self.main_layout = QGridLayout()
        self.init_layout()

        self.center()
        self.show()

        # Set StatusBar
        self.statusBar().showMessage('Ready')
        logger.info('Initialize UI finished')

    # Center Window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Init layout
    def init_layout(self):
        logger.info('Initialize layout')

        # Init group box
        self.init_ping_btn_groupbox()
        self.init_server_list_groupbox()

        # Add Widgets to layout
        self.main_layout.addWidget(self.ping_btn_group_box, 0, 0)
        self.main_layout.addWidget(self.server_list_group_box, 1, 0)

        # Init widget
        self.init_widget()

    # Init widget
    def init_widget(self):
        logger.info('Initialize widget')

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

    # Init Ping Button Group Box
    def init_ping_btn_groupbox(self):
        logger.info('Initialize Ping Button Group Box')

        self.ping_btn_group_box = QGroupBox("Ping")
        self.ping_btn_group_box.setLayout(QGridLayout())

        self.ping_btn_group_box.layout().addWidget(QPushButton('Check All'), 0, 1)
        self.ping_btn_group_box.layout().addWidget(QPushButton('Ping'), 0, 2)
        self.ping_btn_group_box.layout().addWidget(QPushButton('Clear'), 0, 3)

    # Init Server List Group Box
    def init_server_list_groupbox(self):
        logger.info('Initialize Server List Group Box')

        self.server_list_group_box = QGroupBox("Server List")
        self.server_list_group_box.setLayout(QGridLayout())

        # Set server list table
        self.server_list_table = QTableWidget()
        self.server_list_table.setColumnCount(7)
        self.server_list_table.setHorizontalHeaderLabels(['Check', 'Server', 'Region', 'IP', 'Min', 'Max', 'Avg'])
        self.server_list_table.setColumnWidth(0, 50)
        self.server_list_table.setColumnWidth(1, 80)
        self.server_list_table.setColumnWidth(2, 50)
        self.server_list_table.setColumnWidth(3, 100)
        self.server_list_table.setColumnWidth(4, 75)
        self.server_list_table.setColumnWidth(5, 75)
        self.server_list_table.setColumnWidth(6, 75)

        self.server_list_group_box.layout().addWidget(self.server_list_table, 0, 0)

        # Init server list
        self.server_list = self.init_server_list()

        # Set server list table
        self.server_list_table.setRowCount(len(self.server_list))
        for i in range(len(self.server_list)):
            self.insert_server_list_table(i, self.server_list[i])

    # Init server list table
    logger.info('Initialize server list table')

    def init_server_list(self):
        logger.info('Initialize server list')

        # Load server list
        try:
            server_structure = []
            with open('server_list.json', 'r') as f:
                data = json.load(f)
                server_list = data['server_list']
                for i in range(len(server_list)):
                    for j in range(len(server_list[i]['ipAddresses'])):
                        server_structure.append({
                            'server': server_list[i]['name'],
                            'region': server_list[i]['region'],
                            'ip': server_list[i]['ipAddresses'][j],
                        })
        except FileNotFoundError:
            server_structure = []
            logger.error('Server list file not found')
            QMessageBox.warning(self, 'Error', 'Server list file not found')
        return server_structure

    # Insert server list table
    def insert_server_list_table(self, row, server):
        self.server_list_table.setCellWidget(row, 0, QCheckBox())
        self.server_list_table.setItem(row, 1, QTableWidgetItem(server['server']))
        self.server_list_table.setItem(row, 2, QTableWidgetItem(server['region']))
        self.server_list_table.setItem(row, 3, QTableWidgetItem(server['ip']))
        self.server_list_table.setItem(row, 4, QTableWidgetItem('-'))
        self.server_list_table.setItem(row, 5, QTableWidgetItem('-'))
        self.server_list_table.setItem(row, 6, QTableWidgetItem('-'))


# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

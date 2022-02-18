import sys
import json
import logging.handlers
import qtmodern.styles
import qtmodern.windows

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QBrush, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGridLayout, QWidget, QGroupBox, QPushButton, QTableWidget, \
    QMessageBox, QTableWidgetItem, QCheckBox, QApplication, QHBoxLayout, QHeaderView
from PingThread import PingThread

# Server list format: [
#           {
#              'name': '',
#              'region': '',
#              'ip_addresses': [
#                  "000.000.000.000",
#                  "000.000.000.000",
#              ]
#           },
#           {
#              'name': '',
#              'region': '',
#              'ip_addresses': [
#                  "000.000.000.000",
#                  "000.000.000.000",
#              ]
#           }
# ]


# Logging setup
logger = logging.getLogger('ping_test_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.handlers.RotatingFileHandler('ping_test.log', maxBytes=1048576, backupCount=5)
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

        self.check_all_btn = None
        self.uncheck_all_btn = None
        self.ping_btn = None
        self.clear_btn = None

        self.server_list_group_box = None
        self.server_list_table = None
        self.server_list = None
        self.checked_server_list = None

        self.count = 0

        self.setWindowTitle("Ping Pong")
        self.setWindowIcon(QIcon('resource/img/icon.ico'))

        self.init_ui()

    # Init UI
    def init_ui(self):
        logger.info('Initialize UI')
        # Init layout
        self.main_layout = QGridLayout()
        self.init_layout()

        self.center()

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

        # Set Style
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

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

        self.check_all_btn = QPushButton("Check All")
        self.uncheck_all_btn = QPushButton("Uncheck All")
        self.ping_btn = QPushButton("Ping")
        self.clear_btn = QPushButton("Clear")

        self.ping_btn_group_box.layout().addWidget(self.check_all_btn, 0, 1)
        self.ping_btn_group_box.layout().addWidget(self.uncheck_all_btn, 0, 2)
        self.ping_btn_group_box.layout().addWidget(self.ping_btn, 0, 3)
        self.ping_btn_group_box.layout().addWidget(self.clear_btn, 0, 4)

        # Set button event handler
        self.check_all_btn.clicked.connect(self.check_all_btn_clicked)
        self.uncheck_all_btn.clicked.connect(self.uncheck_all_btn_clicked)
        self.ping_btn.clicked.connect(self.ping_btn_clicked)
        self.clear_btn.clicked.connect(self.clear_btn_clicked)

    # check all button clicked
    def check_all_btn_clicked(self):
        logger.info('Check all button clicked')

        for row in range(self.server_list_table.rowCount()):
            check_box_widget = self.server_list_table.cellWidget(row, 0)
            check_box_widget.children()[1].setChecked(True)

    # uncheck all button clicked
    def uncheck_all_btn_clicked(self):
        logger.info('Uncheck all button clicked')

        for row in range(self.server_list_table.rowCount()):
            check_box_widget = self.server_list_table.cellWidget(row, 0)
            check_box_widget.children()[1].setChecked(False)

    # ping button clicked
    def ping_btn_clicked(self):
        logger.info('Ping button clicked')
        self.statusBar().showMessage('Pinging...')

        self.checked_server_list = []

        # Create checked server list
        for row in range(self.server_list_table.rowCount()):
            check_box_widget = self.server_list_table.cellWidget(row, 0)
            if check_box_widget.children()[1].isChecked():
                server_name = self.server_list_table.item(row, 1).text()
                server_ip = self.server_list_table.item(row, 3).text()
                ping_thread = PingThread(row, server_name, server_ip, logger)
                self.checked_server_list.append(ping_thread)

                # Change result table cell to 'Pinging...'
                for j in range(4, 7):
                    self.server_list_table.setItem(row, j, QTableWidgetItem('Pinging...'))
                    self.server_list_table.item(row, j).setForeground(QBrush(QColor(0, 150, 0)))
                self.server_list_table.repaint()

        # Start ping thread
        if len(self.checked_server_list) > 0:
            for thread in self.checked_server_list:
                thread.progress.connect(self.update_progress)
                thread.start()
        else:
            self.statusBar().showMessage('Ready')
            QMessageBox.information(self, 'Info', 'Please select server to ping.')

    # ping_thread progress
    @pyqtSlot(int, list)
    def update_progress(self, currentRow, result):
        import re
        self.count += 1
        for i in range(3):
            value = result[i]
            if value == 'Fail':
                self.server_list_table.item(currentRow, i + 4).setText(value)
                self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 0, 0)))
            else:
                int_value = int(re.findall(r'\d{1,3}', value)[0])
                self.server_list_table.item(currentRow, i + 4).setText(str(int_value))
                if 50 >= int_value >= 0:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(0, 150, 0)))
                if 100 >= int_value >= 51:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 69, 0)))
                if 150 >= int_value >= 101:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(250, 128, 114)))
                if 200 >= int_value >= 151:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(240, 128, 12)))
                if 300 >= int_value >= 201:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(220, 20, 60)))
                if int_value >= 301:
                    self.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 0, 0)))
            self.server_list_table.repaint()
        if self.count == len(self.checked_server_list):
            logger.info('Ping finished')
            self.statusBar().showMessage('Ping finished')
            self.count = 0
            # self.resize_server_list_table()

    # clear button clicked
    def clear_btn_clicked(self):
        logger.info('Clear button clicked')
        self.statusBar().showMessage('Clear')

        # clear result tabel cell
        for row in range(self.server_list_table.rowCount()):
            for j in range(4, 7):
                self.server_list_table.item(row, j).setText('-')
                self.server_list_table.item(row, j).setForeground(QBrush(QColor(180, 180, 180)))
            self.server_list_table.repaint()
        # self.resize_server_list_table()

        self.statusBar().showMessage('Clear finished')

    # Init Server List Group Box
    def init_server_list_groupbox(self):
        logger.info('Initialize Server List Group Box')

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
                server_list = sorted(server_list, key=lambda x: x['name'])
                for i in range(len(server_list)):
                    for j in range(len(server_list[i]['ip_addresses'])):
                        server_structure.append({
                            'server': server_list[i]['name'],
                            'region': server_list[i]['region'],
                            'ip': server_list[i]['ip_addresses'][j],
                        })
        except FileNotFoundError:
            server_structure = []
            logger.error('Server list file not found')
            QMessageBox.warning(self, 'Error', 'Server list file not found')
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
        self.server_list_table.setItem(row, 4, QTableWidgetItem('-'))
        self.server_list_table.setItem(row, 5, QTableWidgetItem('-'))
        self.server_list_table.setItem(row, 6, QTableWidgetItem('-'))

    # Resize server list table
    def resize_server_list_table(self):
        logger.info('Resize server list table')

        table_header = self.server_list_table.horizontalHeader()
        table_width = table_header.width()
        width = []
        for column in range(table_header.count()):
            table_header.setSectionResizeMode(column, QHeaderView.ResizeToContents)
            width.append(table_header.sectionSize(column))

        width_factor = table_width / sum(width)

        for column in range(table_header.count()):
            table_header.setSectionResizeMode(column, QHeaderView.Interactive)
            table_header.resizeSection(column, int(width[column] * width_factor))


# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Set Dark Theme
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.setFixedSize(600, 500)
    mw.show()

    sys.exit(app.exec_())

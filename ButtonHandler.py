from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from PingThread import PingThread
from ProgressHandler import ProgressHandler


class ButtonHandler:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger
        self.progress_handler = ProgressHandler(self.parent)

    # check all button clicked
    def check_all_btn_clicked(self):
        self.logger.info('Check all button clicked')

        for row in range(self.parent.server_list_table.rowCount()):
            check_box_widget = self.parent.server_list_table.cellWidget(row, 0)
            check_box_widget.children()[1].setChecked(True)

    # uncheck all button clicked
    def uncheck_all_btn_clicked(self):
        self.logger.info('Uncheck all button clicked')

        for row in range(self.parent.server_list_table.rowCount()):
            check_box_widget = self.parent.server_list_table.cellWidget(row, 0)
            check_box_widget.children()[1].setChecked(False)

    # ping button clicked
    def ping_btn_clicked(self):
        self.logger.info('Ping button clicked')

        self.parent.progress_bar.setRange(0, 0)
        self.disable_buttons()

        self.parent.checked_server_list = []

        # Create checked server list
        for row in range(self.parent.server_list_table.rowCount()):
            check_box_widget = self.parent.server_list_table.cellWidget(row, 0)
            if check_box_widget.children()[1].isChecked():
                server_name = self.parent.server_list_table.item(row, 1).text()
                server_ip = self.parent.server_list_table.item(row, 3).text()
                ping_thread = PingThread(self.parent, row, server_name, server_ip)
                self.parent.checked_server_list.append(ping_thread)

                # Change result table cell to 'Pinging...'
                for j in range(4, 7):
                    self.parent.server_list_table.setItem(row, j, QTableWidgetItem('Pinging...'))
                    self.parent.server_list_table.item(row, j).setForeground(QBrush(QColor(0, 150, 0)))
                self.parent.server_list_table.repaint()

        # Start ping thread
        if len(self.parent.checked_server_list) > 0:
            for thread in self.parent.checked_server_list:
                thread.progress.connect(self.progress_handler.handle_progress)
                thread.start()
        else:
            QMessageBox.warning(self.parent.parent, 'Warn', 'Please select server to ping.')
            self.parent.progress_bar.setRange(0, 1)
            self.enable_buttons()

    # clear button clicked
    def clear_btn_clicked(self):
        self.logger.info('Clear button clicked')

        self.parent.progress_bar.reset()

        # clear result tabel cell
        for row in range(self.parent.server_list_table.rowCount()):
            for j in range(4, 7):
                self.parent.server_list_table.setItem(row, j, QTableWidgetItem(''))

    # disable buttons
    def disable_buttons(self):
        self.logger.info('Disable buttons')
        self.parent.check_all_btn.setEnabled(False)
        self.parent.uncheck_all_btn.setEnabled(False)
        self.parent.ping_btn.setEnabled(False)
        self.parent.clear_btn.setEnabled(False)

    # enable buttons
    def enable_buttons(self):
        self.logger.info('Enable buttons')
        self.parent.check_all_btn.setEnabled(True)
        self.parent.uncheck_all_btn.setEnabled(True)
        self.parent.ping_btn.setEnabled(True)
        self.parent.clear_btn.setEnabled(True)

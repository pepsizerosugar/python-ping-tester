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

    # check button clicked
    def check_btn_clicked(self):
        self.logger.info('Check all button clicked')
        select_type = self.parent.select_type_of_first
        select_value = self.parent.select_type_of_second

        for row in range(self.parent.server_list_table.rowCount()):
            check_box_widget = self.parent.server_list_table.cellWidget(row, 0).children()[1]
            if select_type == 'All':
                check_box_widget.setChecked(True)
            if select_type == 'Server':
                if self.parent.server_list_table.item(row, 1).text() == select_value:
                    check_box_widget.setChecked(True)
            if select_type == 'Region':
                if self.parent.server_list_table.item(row, 2).text() == select_value:
                    check_box_widget.setChecked(True)

    # uncheck button clicked
    def uncheck_btn_clicked(self):
        self.logger.info('Uncheck button clicked')

        for row in range(self.parent.server_list_table.rowCount()):
            self.parent.server_list_table.cellWidget(row, 0).children()[1].setChecked(False)

    # ping button clicked
    def ping_btn_clicked(self):
        self.logger.info('Ping button clicked')

        self.parent.progress_bar.setRange(0, 0)
        self.disable_interaction()

        self.parent.checked_server_list = []

        # Create checked server list
        for row in range(self.parent.server_list_table.rowCount()):
            check_box_widget = self.parent.server_list_table.cellWidget(row, 0)
            if check_box_widget.children()[1].isChecked():
                server_name = self.parent.server_list_table.item(row, 1).text()
                server_ip = self.parent.server_list_table.item(row, 3).text()
                ping_thread = PingThread(self.parent, row, server_name, server_ip)
                self.parent.checked_server_list.append([ping_thread, row])

                # Change result table cell to 'Pinging...'
                for j in range(4, 8):
                    self.parent.server_list_table.setItem(row, j, QTableWidgetItem('Pinging...'))
                    self.parent.server_list_table.item(row, j).setForeground(QBrush(QColor(0, 150, 0)))
                self.parent.server_list_table.repaint()

        # Start ping thread
        if len(self.parent.checked_server_list) > 0:
            for thread in self.parent.checked_server_list:
                thread[0].progress.connect(self.progress_handler.handle_progress)
                thread[0].start()
        else:
            QMessageBox.warning(self.parent.parent, 'Warn', 'Please select server to ping.')
            self.parent.progress_bar.setRange(0, 1)
            self.enable_interaction()

    # clear button clicked
    def clear_btn_clicked(self):
        self.logger.info('Clear button clicked')

        self.parent.progress_bar.reset()

        # clear result tabel cell
        for row in range(self.parent.server_list_table.rowCount()):
            for j in range(4, 8):
                self.parent.server_list_table.takeItem(row, j)

    # disable buttons
    def disable_interaction(self):
        self.logger.info('Disable interaction')
        self.parent.type_combo_box.setEnabled(False)
        self.parent.select_combo_box.setEnabled(False)
        self.parent.check_btn.setEnabled(False)
        self.parent.uncheck_btn.setEnabled(False)
        self.parent.ping_btn.setEnabled(False)
        self.parent.clear_btn.setEnabled(False)

    # enable buttons
    def enable_interaction(self):
        self.logger.info('Enable interaction')
        self.parent.type_combo_box.setEnabled(True)
        self.parent.select_combo_box.setEnabled(True)
        self.parent.check_btn.setEnabled(True)
        self.parent.uncheck_btn.setEnabled(True)
        self.parent.ping_btn.setEnabled(True)
        self.parent.clear_btn.setEnabled(True)

from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from Modules.Handler.ProgressHandler import ProgressHandler
from Modules.Interface.DataClass.EventElements import EventElements
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Thread.PingThread import PingThread


class ButtonHandler:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = EventElements.logger
        self.progress_handler = ProgressHandler(self.parent)

    # check button clicked
    def check_btn_clicked(self):
        self.logger.info('Check all button clicked')
        select_type = EventElements.select_type_of_first
        select_value = EventElements.select_type_of_second

        for row in range(UIElements.server_list_table.rowCount()):
            check_box_widget = UIElements.server_list_table.cellWidget(row, 0).children()[1]
            if select_type == 'All':
                check_box_widget.setChecked(True)
            if select_type == 'Server':
                if UIElements.server_list_table.item(row, 1).text() == select_value:
                    check_box_widget.setChecked(True)
            if select_type == 'Region':
                if UIElements.server_list_table.item(row, 2).text() == select_value:
                    check_box_widget.setChecked(True)

    # uncheck button clicked
    def uncheck_btn_clicked(self):
        self.logger.info('Uncheck button clicked')

        for row in range(UIElements.server_list_table.rowCount()):
            UIElements.server_list_table.cellWidget(row, 0).children()[1].setChecked(False)

    # ping button clicked
    def ping_btn_clicked(self):
        self.logger.info('Ping button clicked')

        UIElements.progress_bar.setRange(0, 0)
        self.disable_interaction()

        self.parent.checked_server_list = []

        # Create checked server list
        for row in range(UIElements.server_list_table.rowCount()):
            check_box_widget = UIElements.server_list_table.cellWidget(row, 0)
            if check_box_widget.children()[1].isChecked():
                server_name = UIElements.server_list_table.item(row, 1).text()
                server_ip = UIElements.server_list_table.item(row, 3).text()
                ping_thread = PingThread(self.parent, row, server_name, server_ip)
                self.parent.checked_server_list.append([ping_thread, row])

                # Change result table cell to 'Pinging...'
                for j in range(4, 8):
                    UIElements.server_list_table.setItem(row, j, QTableWidgetItem('Pinging...'))
                    UIElements.server_list_table.item(row, j).setForeground(QBrush(QColor(0, 150, 0)))
                UIElements.server_list_table.repaint()

        # Start ping thread
        if len(self.parent.checked_server_list) > 0:
            for thread in self.parent.checked_server_list:
                thread[0].progress.connect(self.progress_handler.handle_progress)
                thread[0].start()
        else:
            QMessageBox.warning(self.parent.parent.parent, 'Warn', 'Please select server to ping.')
            UIElements.progress_bar.setRange(0, 1)
            self.enable_interaction()

    # clear button clicked
    def clear_btn_clicked(self):
        self.logger.info('Clear button clicked')

        UIElements.progress_bar.reset()

        # clear result tabel cell
        for row in range(UIElements.server_list_table.rowCount()):
            for j in range(4, 8):
                UIElements.server_list_table.takeItem(row, j)

    # disable buttons
    def disable_interaction(self):
        self.logger.info('Disable interaction')
        UIElements.type_combo_box.setEnabled(False)
        UIElements.select_combo_box.setEnabled(False)
        UIElements.check_btn.setEnabled(False)
        UIElements.uncheck_btn.setEnabled(False)
        UIElements.ping_btn.setEnabled(False)
        UIElements.clear_btn.setEnabled(False)

    # enable buttons
    def enable_interaction(self):
        self.logger.info('Enable interaction')
        UIElements.type_combo_box.setEnabled(True)
        UIElements.select_combo_box.setEnabled(True)
        UIElements.check_btn.setEnabled(True)
        UIElements.uncheck_btn.setEnabled(True)
        UIElements.ping_btn.setEnabled(True)
        UIElements.clear_btn.setEnabled(True)

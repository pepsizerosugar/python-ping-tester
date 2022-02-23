from PyQt5.QtCore import pyqtSlot, Qt, QObject
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from ResultAnalyze import ResultAnalyze


class ProgressHandler(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger
        self.count = 0

    # Handling ping_thread progress
    @pyqtSlot(int, list)
    def handle_progress(self, currentRow, result):
        import re
        self.count += 1
        self.parent.progress_bar.setRange(0, len(self.parent.checked_server_list))
        self.parent.progress_bar.setValue(self.count)

        for i in range(3):
            value = result[i]
            if value == 'Fail':
                self.parent.server_list_table.item(currentRow, i + 4).setText(value)
                self.parent.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 0, 0)))
            else:
                int_value = int(re.findall(r'\d{1,3}', value)[0])
                cell_item = QTableWidgetItem()
                cell_item.setData(Qt.DisplayRole, int_value)
                self.parent.server_list_table.setItem(currentRow, i + 4, cell_item)
                cell_widget = self.parent.server_list_table.item(currentRow, i + 4).tableWidget()
                while True:
                    if 50 >= int_value >= 0:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(0, 150, 0)))
                        break
                    if 100 >= int_value >= 51:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 69, 0)))
                        break
                    if 150 >= int_value >= 101:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(250, 128, 114)))
                        break
                    if 200 >= int_value >= 151:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(240, 128, 12)))
                        break
                    if 300 >= int_value >= 201:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(220, 20, 60)))
                        break
                    if int_value >= 301:
                        cell_widget.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 0, 0)))
                        break

        self.parent.server_list_table.repaint()

        if self.count == len(self.parent.checked_server_list):
            self.logger.info('Ping finished')
            self.parent.server_list_table.sortByColumn(6, Qt.AscendingOrder)
            ResultAnalyze(self.parent)

            best_server = self.parent.server_list_table.item(0, 1).text()
            best_server_ip = self.parent.server_list_table.item(0, 3).text()
            best_server_ping = self.parent.server_list_table.item(0, 6).text()
            QMessageBox.information(self.parent.parent, 'Pong',
                                    'Ping finished\n'
                                    'Best server : ' + best_server + '(' + best_server_ip + ') with ping ' + best_server_ping)

            self.parent.progress_bar.reset()
            self.parent.enable_buttons()
            self.count = 0

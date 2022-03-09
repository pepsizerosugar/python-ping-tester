from PyQt5.QtCore import pyqtSlot, Qt, QObject
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from Modules.Analyze.ResultAnalyze import ResultAnalyze
from Modules.Interface.DataObject.EventElements import EventElements
from Modules.Interface.DataObject.UIElement import UIElements


class ProgressHandler(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = EventElements.logger
        self.count = 0
        self.ping_result_model = []

    # Handling ping_thread progress
    @pyqtSlot(int, str, list)
    def handle_progress(self, currentRow, loss, result):
        self.count += 1
        UIElements.progress_bar.setRange(0, len(self.parent.checked_server_list))
        UIElements.progress_bar.setValue(self.count)
        server = UIElements.server_list_table.item(currentRow, 1).text()
        region = UIElements.server_list_table.item(currentRow, 2).text()
        ip = UIElements.server_list_table.item(currentRow, 3).text()
        loss = int(loss[0:loss.find('%')])
        self.ping_result_model.append(
            {
                'row': currentRow,
                'server': server,
                'region': region,
                'ip': ip,
                'result': result,
                'loss': loss
            }
        )

        self.set_ping_result(currentRow, result)
        self.set_ping_loss(currentRow, loss)

        # Check ping thread is finished
        if self.count == len(self.parent.checked_server_list):
            self.logger.info('Ping finished')
            UIElements.server_list_table.sortByColumn(6, Qt.AscendingOrder)
            ResultAnalyze(self.parent, self.ping_result_model).convert_result_table_to_model()

            best_server = UIElements.server_list_table.item(0, 1).text()
            best_server_ip = UIElements.server_list_table.item(0, 3).text()
            best_server_ping = UIElements.server_list_table.item(0, 6).text()
            QMessageBox.information(self.parent.parent.parent, 'Pong',
                                    'Ping finished\n'
                                    'Best server : ' + best_server + '(' + best_server_ip + ') with ping ' + best_server_ping)
            self.ping_result_model = []
            UIElements.progress_bar.reset()
            self.parent.enable_buttons()
            self.count = 0

    # Set ping result
    @staticmethod
    def set_ping_result(currentRow, result):
        # set ping result
        for i in range(3):
            value = result[i]
            if value == 'Fail':
                UIElements.server_list_table.item(currentRow, i + 4).setText(value)
                UIElements.server_list_table.item(currentRow, i + 4).setForeground(QBrush(QColor(255, 0, 0)))
            else:
                int_value = int(value[0:value.find('ms')])
                cell_item = QTableWidgetItem()
                cell_item.setData(Qt.DisplayRole, int_value)
                UIElements.server_list_table.setItem(currentRow, i + 4, cell_item)
                cell_widget = UIElements.server_list_table.item(currentRow, i + 4)
                while True:
                    if 50 >= int_value >= 0:
                        cell_widget.setForeground(QBrush(QColor(0, 150, 0)))
                        break
                    if 100 >= int_value >= 51:
                        cell_widget.setForeground(QBrush(QColor(255, 69, 0)))
                        break
                    if 150 >= int_value >= 101:
                        cell_widget.setForeground(QBrush(QColor(250, 128, 114)))
                        break
                    if 200 >= int_value >= 151:
                        cell_widget.setForeground(QBrush(QColor(240, 128, 12)))
                        break
                    if 300 >= int_value >= 201:
                        cell_widget.setForeground(QBrush(QColor(220, 20, 60)))
                        break
                    if int_value >= 301:
                        cell_widget.setForeground(QBrush(QColor(255, 0, 0)))
                        break
        UIElements.server_list_table.repaint()

    # Set ping loss
    @staticmethod
    def set_ping_loss(currentRow, loss):
        loss_item = QTableWidgetItem()
        loss_item.setData(Qt.DisplayRole, loss)
        UIElements.server_list_table.setItem(currentRow, 7, loss_item)
        loss_widget = UIElements.server_list_table.item(currentRow, 7)
        while True:
            if loss == 0:
                loss_widget.setForeground(QBrush(QColor(0, 150, 0)))
                break
            if 25 >= loss >= 1:
                loss_widget.setForeground(QBrush(QColor(255, 69, 0)))
                break
            if 50 >= loss >= 26:
                loss_widget.setForeground(QBrush(QColor(250, 128, 114)))
                break
            if 75 >= loss >= 51:
                loss_widget.setForeground(QBrush(QColor(240, 128, 12)))
                break
            if 100 >= loss >= 76:
                loss_widget.setForeground(QBrush(QColor(255, 0, 0)))
                break
        UIElements.server_list_table.repaint()

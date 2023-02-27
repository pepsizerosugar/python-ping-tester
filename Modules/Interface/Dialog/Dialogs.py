from PyQt5.QtWidgets import QMessageBox

from Modules.Interface.DataClass.UIElement import UIElements


def when_checked_server_is_empty():
    QMessageBox.warning(UIElements.main_window, 'Warn', 'Please select server to ping.')


def when_server_list_file_not_found():
    QMessageBox.critical(UIElements.main_window, 'Error', 'Server list file not found')


def when_ping_finished(best_server, best_server_ip, best_server_ping):
    QMessageBox.information(UIElements.main_window, 'Pong',
                            'Ping finished\n'
                            'Best server : ' + best_server + '(' + best_server_ip + ') with ping ' + best_server_ping)

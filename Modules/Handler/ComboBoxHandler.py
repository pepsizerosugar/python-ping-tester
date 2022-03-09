from Modules.Interface.DataObject.EventElements import EventElements
from Modules.Interface.DataObject.ServerData import Server
from Modules.Interface.DataObject.UIElement import UIElements


class ComboBoxHandler:
    def __init__(self):
        super().__init__()
        self.logger = EventElements.logger

    def type_combo_box_changed(self):
        self.logger.info('type_combo_box_changed')
        UIElements.select_combo_box.clear()
        EventElements.select_type = UIElements.type_combo_box.currentText()

        if EventElements.select_type == 'All':
            EventElements.select_type_of_first = 'All'
        if EventElements.select_type == 'Server':
            EventElements.select_type_of_first = 'Server'
            UIElements.select_combo_box.addItems(Server.collection[EventElements.select_type])
        if EventElements.select_type == 'Region':
            EventElements.select_type_of_first = 'Region'
            UIElements.select_combo_box.addItems(Server.collection[EventElements.select_type])

    def select_combo_box_changed(self):
        self.logger.info('select_combo_box_changed')
        EventElements.select_type_of_second = UIElements.select_combo_box.currentText()

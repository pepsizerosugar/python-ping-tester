class ComboBoxHandler:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger

    def type_combo_box_changed(self):
        self.logger.info('type_combo_box_changed')
        self.parent.select_combo_box.clear()
        self.parent.select_type = self.parent.type_combo_box.currentText()

        if self.parent.select_type == 'All':
            self.parent.select_type_of_first = 'All'
        if self.parent.select_type == 'Server':
            self.parent.select_type_of_first = 'Server'
            self.parent.select_combo_box.addItems(self.parent.collection[self.parent.select_type])
        if self.parent.select_type == 'Region':
            self.parent.select_type_of_first = 'Region'
            self.parent.select_combo_box.addItems(self.parent.collection[self.parent.select_type])

    def select_combo_box_changed(self):
        self.logger.info('select_combo_box_changed')
        self.parent.select_type_of_second = self.parent.select_combo_box.currentText()

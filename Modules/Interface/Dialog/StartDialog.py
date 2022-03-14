from Modules.Interface.DataClass.EventElements import EventElements


class StartDialog:
    def __init__(self, parent):
        self.logger = EventElements.logger
        self.parent = parent

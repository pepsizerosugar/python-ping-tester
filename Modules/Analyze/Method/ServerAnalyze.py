from Modules.Interface import EventElements
from Modules.Interface import Server


class ServerAnalyze:
    def __init__(self):
        super().__init__()
        self.logger = EventElements.logger
        self.servers = []
        self.regions = []

    def collect_by_server(self):
        for server in Server.server_list:
            server_name = server['server']
            server_region = server['region']

            if server_name not in self.servers:
                self.servers.append(server_name)
            if server_region not in self.regions:
                self.regions.append(server_region)
        Server.collection = {"Server": self.servers, "Region": self.regions}

    def get_server_collection(self):
        return {"Server": self.servers, "Region": self.regions}

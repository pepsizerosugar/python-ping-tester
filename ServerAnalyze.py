class ServerAnalyze:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger
        self.servers = []
        self.regions = []

    def collect_by_server(self):
        for server in self.parent.server_list:
            server_name = server['server']
            server_region = server['region']

            if server_name not in self.servers:
                self.servers.append(server_name)
            if server_region not in self.regions:
                self.regions.append(server_region)

    def get_server_collection(self):
        return {"Server": self.servers, "Region": self.regions}

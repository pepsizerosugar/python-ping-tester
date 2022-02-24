class ResultAnalyze:
    def __init__(self, parent, ping_result):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger
        self.ping_result = ping_result
        self.result_model_by_server = None
        self.result_model_by_region = None

    def convert_result_table_to_model(self):
        self.logger.info("Analyze result")
        self.result_model_by_server = {}
        self.result_model_by_region = {}

        for server in self.ping_result:
            row_server = server['server']
            row_region = server['region']
            row_avg = server['result'][2]

            if self.result_model_by_server.get(row_server) is None:
                self.result_model_by_server[row_server] = {"avg": 0, "count": 0}
            if self.result_model_by_region.get(row_region) is None:
                self.result_model_by_region[row_region] = {"avg": 0, "count": 0}

            if row_avg == "Fail":
                self.result_model_by_server[row_server]["count"] += 1
                self.result_model_by_server[row_server]["fail_count"] += 1

                self.result_model_by_region[row_region]["count"] += 1
                self.result_model_by_region[row_region]["fail_count"] += 1
            else:
                import re
                row_avg = int(re.findall(r'\d{1,3}', row_avg)[0])

                # collect data by server
                self.result_model_by_server[row_server]["avg"] += row_avg
                self.result_model_by_server[row_server]["count"] += 1

                # collect data by region
                self.result_model_by_region[row_region]["avg"] += row_avg
                self.result_model_by_region[row_region]["count"] += 1

        # calculate average by server
        for key, value in self.result_model_by_server.items():
            self.result_model_by_server[key]["avg"] = \
                round(self.result_model_by_server[key]["avg"] / self.result_model_by_server[key]["count"])
        self.logger.info("Analyze.result_model_by_server: %s", self.result_model_by_server)

        # calculate average by region
        for key, value in self.result_model_by_region.items():
            self.result_model_by_region[key]["avg"] = \
                round(self.result_model_by_region[key]["avg"] / self.result_model_by_region[key]["count"])
        self.logger.info("Analyze.result_model_by_region: %s", self.result_model_by_region)

    def get_result_model_by_server(self):
        return self.result_model_by_server

    def get_result_model_by_region(self):
        return self.result_model_by_region

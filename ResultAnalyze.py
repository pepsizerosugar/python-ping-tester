class Analyze:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.logger = self.parent.logger
        self.result_model_by_server = None
        self.result_model_by_region = None
        self.convert_result_table_to_model()

    def convert_result_table_to_model(self):
        self.logger.info("Analyze.result_table_to_model")
        self.result_model_by_server = {}
        self.result_model_by_region = {}

        for i in range(self.parent.server_list_table.rowCount()):
            row_server = self.parent.server_list_table.item(i, 1).text()
            row_region = self.parent.server_list_table.item(i, 2).text()
            row_avg = self.parent.server_list_table.item(i, 6).text()

            if self.result_model_by_server.get(row_server) is None:
                self.result_model_by_server[row_server] = {"avg": 0, "count": 0}
            if self.result_model_by_region.get(row_region) is None:
                self.result_model_by_region[row_region] = {"avg": 0, "count": 0}

            if row_avg != "Fail":
                row_avg = int(row_avg)

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
        self.logger.info("Analyze.result_table_to_model: result_model_by_server: %s", self.result_model_by_server)

        # calculate average by region
        for key, value in self.result_model_by_region.items():
            self.result_model_by_region[key]["avg"] = \
                round(self.result_model_by_region[key]["avg"] / self.result_model_by_region[key]["count"])
        self.logger.info("Analyze.result_table_to_model: result_model_by_region: %s", self.result_model_by_region)

    def get_result_model_by_server(self):
        return self.result_model_by_server

    def get_result_model_by_region(self):
        return self.result_model_by_region

from Modules.Analyze.DataClass.AnalyzeData import AnalyzeData
from Modules.Interface.DataClass.EventElements import EventElements


class ResultAnalyze:
    def __init__(self, ping_result):
        super().__init__()
        self.logger = EventElements.logger
        self.ping_result = ping_result

    def convert_result_table_to_model(self):
        self.logger.info("Analyze result")
        AnalyzeData.result_model_by_server = {}
        AnalyzeData.result_model_by_region = {}

        for server in self.ping_result:
            row_server = server['server']
            row_region = server['region']
            row_avg = server['result'][2]

            if AnalyzeData.result_model_by_server.get(row_server) is None:
                AnalyzeData.result_model_by_server[row_server] = {"avg": 0, "count": 0, "fail_count": 0}
            if AnalyzeData.result_model_by_region.get(row_region) is None:
                AnalyzeData.result_model_by_region[row_region] = {"avg": 0, "count": 0, "fail_count": 0}

            if row_avg == "Fail":
                AnalyzeData.result_model_by_server[row_server]["count"] += 1
                AnalyzeData.result_model_by_server[row_server]["fail_count"] += 1

                AnalyzeData.result_model_by_region[row_region]["count"] += 1
                AnalyzeData.result_model_by_region[row_region]["fail_count"] += 1
            else:
                import re
                row_avg = int(re.findall(r'\d{1,3}', row_avg)[0])

                # collect data by server
                AnalyzeData.result_model_by_server[row_server]["avg"] += row_avg
                AnalyzeData.result_model_by_server[row_server]["count"] += 1

                # collect data by region
                AnalyzeData.result_model_by_region[row_region]["avg"] += row_avg
                AnalyzeData.result_model_by_region[row_region]["count"] += 1

        # calculate average by server
        for key, value in AnalyzeData.result_model_by_server.items():
            AnalyzeData.result_model_by_server[key]["avg"] = \
                round(AnalyzeData.result_model_by_server[key]["avg"] / AnalyzeData.result_model_by_server[key]["count"])
        # rank by avg
        AnalyzeData.rank_by_server = sorted(AnalyzeData.result_model_by_server.items(), key=lambda x: x[1]["avg"])
        self.logger.info("Analyze.result_model_by_server: %s", AnalyzeData.result_model_by_server)
        self.logger.info("Analyze.sort_by_server: %s", AnalyzeData.rank_by_server)

        # calculate average by region
        for key, value in AnalyzeData.result_model_by_region.items():
            AnalyzeData.result_model_by_region[key]["avg"] = \
                round(AnalyzeData.result_model_by_region[key]["avg"] / AnalyzeData.result_model_by_region[key]["count"])
        # rank by avg
        AnalyzeData.rank_by_region = sorted(AnalyzeData.result_model_by_region.items(), key=lambda x: x[1]["avg"])
        self.logger.info("Analyze.result_model_by_region: %s", AnalyzeData.result_model_by_region)
        self.logger.info("Analyze.sort_by_region: %s", AnalyzeData.rank_by_region)

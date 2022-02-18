from PyQt5.QtCore import QThread, pyqtSignal


class PingThread(QThread):
    progress = pyqtSignal(int, list)

    def __init__(self, currentRow, name, ip, logger):
        QThread.__init__(self)
        self.currentRow = currentRow
        self.name = name
        self.ip = ip
        self.logger = logger

    def run(self):
        self.msleep(50)
        self.ping(self.ip)

    def ping(self, ip):
        self.logger.info('Ping server: %s(%s)', self.name, self.ip)

        import subprocess
        import re

        try:
            ping_response = subprocess.Popen("ping -n 5 -w 1000 " + str(ip), stdout=subprocess.PIPE, shell=True)
            stdout, stderr = ping_response.communicate()
            stdout = stdout.decode("cp949").split('\n')[-2].replace(" ", "")
            result = re.findall(r"\d{1,3}ms", stdout)

            if len(result) != 3:
                result = ["Fail", "Fail", "Fail"]

            self.logger.info('Ping result: %s(%s) %s', self.name, self.ip, result)
            self.progress.emit(self.currentRow, result)
        except Exception as e:
            print(e)
            self.logger.error(e)
            return

        self.quit()

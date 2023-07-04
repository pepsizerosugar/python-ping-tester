from PyQt5.QtCore import QThread, pyqtSignal

from Modules.Interface import EventElements


class PingThread(QThread):
    progress = pyqtSignal(int, str, list)

    def __init__(self, currentRow, name, ip):
        QThread.__init__(self)
        self.currentRow = currentRow
        self.name = name
        self.ip = ip
        self.logger = EventElements.logger

    def run(self):
        self.ping(self.ip)

    def ping(self, ip):
        self.logger.info('Ping server: %s(%s)', self.name, self.ip)

        import subprocess
        import re

        try:
            ping_response = subprocess.Popen("ping -n 5 -w 1000 " + str(ip), stdout=subprocess.PIPE, shell=True)
            stdout, stderr = ping_response.communicate()
            stdout = stdout.decode("cp949").split('\n')

            if len(stdout) == 11:
                result = ["Fail", "Fail", "Fail"]
                packet = stdout[-2].replace(" ", "")
                loss = re.findall(r"\d{1,3}%", packet)[0]
            else:
                packet = stdout[-4].replace(" ", "")
                loss = re.findall(r"\d{1,3}%", packet)[0]
                ping_time = stdout[-2].replace(" ", "")
                result = re.findall(r"\d{1,3}ms", ping_time)

            self.logger.info('Ping result: %s(%s) %s', self.name, self.ip, result)
            self.progress.emit(self.currentRow, loss, result)
        except Exception as e:
            print(e)
            self.logger.error(e)
            return

        self.quit()

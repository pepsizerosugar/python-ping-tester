from PyQt5.QtCore import QThread, pyqtSignal


class PingThread(QThread):
    progress = pyqtSignal(int, str, list)

    def __init__(self, parent, currentRow, name, ip):
        QThread.__init__(self)
        self.parent = parent
        self.currentRow = currentRow
        self.name = name
        self.ip = ip
        self.logger = self.parent.logger

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
            stdout = stdout.decode("cp949").split('\n')
            packet = stdout[-4].replace(" ", "")
            ping_time = stdout[-2].replace(" ", "")
            loss = re.findall(r"\d{1,3}%", packet)[0]
            result = re.findall(r"\d{1,3}ms", ping_time)

            if len(result) != 3:
                result = ["Fail", "Fail", "Fail"]

            self.logger.info('Ping result: %s(%s) %s', self.name, self.ip, result)
            self.progress.emit(self.currentRow, loss, result)
        except Exception as e:
            print(e)
            self.logger.error(e)
            return

        self.quit()

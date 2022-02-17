from PyQt5.QtCore import QThread, pyqtSignal


class PingThread(QThread):
    progress = pyqtSignal(list)

    def __init__(self, ip):
        QThread.__init__(self)
        self.ip = ip
        self.isRun = False

    def run(self):
        while self.isRun:
            self.ping(self.ip)

    def ping(self, ip):
        import subprocess
        import re

        try:
            ping_response = subprocess.Popen("ping -n 3 -w 1000 " + str(ip), stdout=subprocess.PIPE, shell=True)
            stdout, stderr = ping_response.communicate()
            stdout = stdout.decode("cp949").split('\n')[-2].replace(" ", "")
            result = re.findall(r"\d{1,3}ms", stdout)
            if len(result) != 3:
                result = ["Fail", "Fail", "Fail"]
            self.progress.emit(result)
        except Exception as e:
            print(e)
            return

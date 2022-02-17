from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox, QApplication

from PingThread import PingThread


class TestGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ip = None
        self.th = None

        self.ipField = QLineEdit("127.0.0.1", self)
        self.startBtn = QPushButton("쓰레드 시작", self)
        self.stopBtn = QPushButton("쓰레드 정지", self)
        self.resultLabel = QLabel("쓰레드 대기중", self)

        self.ipField.setAlignment(Qt.AlignCenter)
        self.resultLabel.setAlignment(Qt.AlignCenter)

        vertBox = QVBoxLayout()
        vertBox.addWidget(self.ipField)
        vertBox.addWidget(self.startBtn)
        vertBox.addWidget(self.stopBtn)
        vertBox.addWidget(self.resultLabel)

        self.setLayout(vertBox)
        self.setFixedSize(200, 150)

        self.startBtn.clicked.connect(self.threadStart)
        self.stopBtn.clicked.connect(self.threadStop)

        self.setWindowTitle('핑 쓰레드')
        self.show()

    @pyqtSlot()
    def threadStart(self):
        self.ip = self.ipField.text()
        if len(self.ip) != 0:
            self.th = PingThread(self.ip)
            self.th.progress.connect(self.pingResultUpdated)

            if not self.th.isRun:
                print('메인 : 쓰레드 시작')
                self.resultLabel.setText("Pinging...")
                self.th.isRun = True
                self.th.start()
        else:
            self.noInputIpAddress()

    @pyqtSlot()
    def threadStop(self):
        if self.th is not None:
            if self.th.isRun:
                print('메인 : 쓰레드 정지')
                self.th.isRun = False
                self.th.quit()
            else:
                self.threadIsNotRunning()
        else:
            self.threadIsNotRunning()

    @pyqtSlot(list)
    def pingResultUpdated(self, result):
        print(result)
        self.resultLabel.setText(str(result))

    def noInputIpAddress(self):
        print('메인 : 입력된 IP가 없습니다.')
        QMessageBox.about(self, "알림", "입력된 IP가 없습니다.")

    def threadIsNotRunning(self):
        print('메인 : 쓰레드가 실행 중이지 않습니다.')
        QMessageBox.about(self, "알림", "쓰레드가 실행 중이지 않습니다.")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = TestGUI()
    app.exec_()

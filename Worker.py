from PyQt6.QtCore import QThread, pyqtSignal


class Worker(QThread):
    resultReady = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, sleepTime, parent=None):
        super().__init__(parent)

        self.__sleepTime = sleepTime

    def run(self):
        result = str("Thread done!")
        if self.parent().dumm == 0:
            for i in range(1, 100):
                self.progress.emit(i)
                self.usleep(self.__sleepTime) # 100*1000=100*0,1 sec
        else:
            for i in range(self.parent().progress, 100):
                self.progress.emit(i)
                self.usleep(self.__sleepTime) # 100*1000=100*0,1 sec


        self.resultReady.emit(result)

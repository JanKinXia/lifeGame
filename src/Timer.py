import threading


class Timer(object):
    def __init__(self, time, function):
        self.time = time
        self.function = function
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True

    def start(self):
        print('start')
        self._timer = threading.Timer(self.time, self.run)
        self._timer.setDaemon(True)
        self._timer.start()

    def run(self):
        if self.__flag.isSet():
            print('run')
            try:
                self.function()
            except:
                pass
            self.start() 
        
    def pause(self):
        print('pause')
        self.__flag.clear()
        
        

import threading
import time
import logging

# реализация через метод класса
class SingleCls:
    _instance = 0
    @classmethod
    def instance(cls):
        if cls._instance == 0:
            cls.object = Figure()
            cls._instance = 1
        return cls.object

# реализация через обычный класс
class SingleObj:
    _instance = 0

    def instance(self):
        if SingleObj._instance == 0:
            SingleObj.object = Figure()
            SingleObj._instance = 1
        return SingleObj.object

class SingleStat:
    _instance = 0
    @staticmethod
    def instance():
        if SingleStat._instance == 0:
            SingleStat.object = Figure()
            SingleStat._instance = 1
        return SingleStat.object


class Figure:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.name = ''

    def square(self):
        return self.width*self.height

    def get_info(self):
        print(id(self))
        print(self.__dict__)

def thread_function(name):
    logging.info(f'Thread {name} starting')
    time.sleep(2)
    s = SingleCls.instance()
    s.name += ' '+str(name)
    s.get_info()
    logging.info(f'Thread {name} is finished.')


if __name__=='__main__':

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    threads = list()
    for  index in range(5):
        logging.info(f'before starting {index}')
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    for index,thread in enumerate(threads):
        logging.info(f'before joining {index}')
        thread.join()
        logging.info(f'after joining {index}')

    logging.info("Main    : all done")

    s = SingleCls.instance()
    s.get_info()
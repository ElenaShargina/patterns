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

    def square(self):
        return self.width*self.height

    def get_info(self):
        print(id(self))
        print(self.__dict__)


if __name__=='__main__':
    # реализация через метод класса
    s1 = SingleCls.instance()
    s1.get_info()
    s2 = SingleCls.instance()
    s2.get_info()
    s2.height = 10
    s1.get_info()

    # реализация через обычный класс(зачем?)
    s3 = SingleObj().instance()
    s3.get_info()
    s4 = SingleObj().instance()
    s4.get_info()
    s3.height = 10
    s4.get_info()

    # реализация через обычный класс(зачем?)
    s5 = SingleStat.instance()
    s5.get_info()
    s6 = SingleStat.instance()
    s6.get_info()
    s5.height = 10
    s6.get_info()

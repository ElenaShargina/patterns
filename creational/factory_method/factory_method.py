"""
паттерн, порождающий классы
определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс
инстанцировать
Для каждого нового продукта нужно создать новый подкласс создателя

"""
class AbstractHouse:
    def info(self):
        print(self.__dict__)
class AbstractDeveloper:
    def __init__(self,name):
        self.name = name
    # фабричный метод
    def work(self):
        pass

class WoodHouse(AbstractHouse):
    def __init__(self,author):
        self.type = 'Деревянный дом'
        self.author = author
class WoodDeveloper(AbstractDeveloper):
    # реализация фабричного метода
    def work(self):
        return WoodHouse(self.name)

class PanelHouse(AbstractHouse):
    def __init__(self,author):
        self.type = 'Панельный дом'
        self.author = author
class PanelDeveloper(AbstractDeveloper):
    # реализация фабричного метода
    def work(self):
        return PanelHouse(self.name)

if __name__=='__main__':
    wd = WoodDeveloper('Фирма по производству деревянных домов')
    pd = PanelDeveloper('Компания по строительству из панелей')
    for i in (pd,wd):
        house = i.work()
        house.info()
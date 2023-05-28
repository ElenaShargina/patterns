"""
FLYWEIGHT
паттерн, структурирующий объекты
использует разделение для эффективной поддержки множества мелких объектов
Ключевая идея - различие между внутренним и внешним состояниями.
Внутреннее состояние хранится в самом приспособленце и состоит из информации,
не зависящей от его контекста. Именно поэтому он может разделяться. Внешнее зависит от контекста и
изменяется с ним, поэтому не подлежит разделению.
Объекта-клиенты отвечают за передачу внешнего состояния приспособленцу, если это нужно.
Экономия памяти: уменьшение общего числа экземпляров
сокращение объема памяти, необходимого для хранения внутреннего состояния
вычисление, а не хранение внешнего состояния
например - буквы - разделяемые объекты. Шрифты и цвета хранятся в отдельной структуре
и являются внешним состоянием. А не каждая буква хранится со своим цветом и шрифтом.
"""
from abc import abstractmethod,ABCMeta
# абстрактный класс ДОМА
class House:
    __metaclass__=ABCMeta
    # количество этажей - параметр внутреннего состояния
    def __init__(self,floors):
        self.floors = floors
    @abstractmethod
    def build(self):
        pass

"""
конкретный класс Панельные дома с внутренней информацией - количеством этажей и способом стройки
"""
class PanelHouse(House):

    # широта и долгота - параметры внешнего состояния приспособленцев
    def build(self, longitude, latitude):
        print(f'Panel house of {self.floors} floors is build at ({longitude},{latitude})')

"""
конкретный класс Кирпичные дома с внутренней информацией - количеством этажей и способом стройки
"""
class BrickHouse(House):

    # широта и долгота - параметры внешнего состояния приспособленцев
    def build(self, longitude, latitude):
        print(f'Brick house of {self.floors} floors is build at ({longitude},{latitude})')

"""
Фабрика приспособленцев.
Хранит в себе пул уже существующих объектов - приспособленцев (может быть сгенерирован заранее)
и по запросу выдает существующий, а не генерит новый объект
"""
class HouseFactory:
    houses:dict={}
    @staticmethod
    def build_id(type,floors):
        return type+'_'+str(floors)

    @classmethod
    def get(cls,house_type,house_floors):
        id_house = HouseFactory.build_id(house_type,house_floors)
        if id_house not in cls.houses.keys():
            cls.houses[id_house] = globals()[house_type](house_floors)
        return cls.houses[id_house]

if __name__=='__main__':
    from random import randint
    longtitude = 12.45
    latitude = 13.78
    for i in range(10):
        longtitude+=i
        latitude+=i
        new_house = HouseFactory.get('PanelHouse', randint(1,5))
        new_house.build(longtitude,latitude)
    for i in range(10):
        longtitude+=i
        latitude+=i
        new_house = HouseFactory.get('BrickHouse', randint(1,5))
        new_house.build(longtitude,latitude)

    print(HouseFactory.houses)
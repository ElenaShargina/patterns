"""
ПАТТЕРН ПРОТОТИП
У вас есть объект, который нужно скопировать. Как это сделать?
Нужно создать пустой объект такого же класса,
а затем поочерёдно скопировать значения всех полей из старого объекта в новый.

Прекрасно! Но есть нюанс. Не каждый объект удастся скопировать таким образом,
ведь часть его состояния может быть приватной,
 а значит – недоступной для остального кода программы.

 Но есть и другая проблема. Копирующий код станет зависим от классов копируемых объектов.
 Ведь, чтобы перебрать все поля объекта, нужно привязаться к его классу.
 Из-за этого вы не сможете копировать объекты, зная только их интерфейсы, а не конкретные классы.

Решение
Паттерн Прототип поручает создание копий самим копируемым объектам.
Он вводит общий интерфейс для всех объектов, поддерживающих клонирование.
 Это позволяет копировать объекты, не привязываясь к их конкретным классам.
 Обычно такой интерфейс имеет всего один метод clone.

Реализация этого метода в разных классах очень схожа.
Метод создаёт новый объект текущего класса и копирует в него
значения всех полей собственного объекта.
Так получится скопировать даже приватные поля,
так как большинство языков программирования разрешает
доступ к приватным полям любого объекта текущего класса.

Объект, который копируют, называется прототипом
(откуда и название паттерна). Когда объекты программы содержат сотни полей
и тысячи возможных конфигураций, прототипы могут служить
своеобразной альтернативой созданию подклассов.
https://radioprog.ru/post/1467
"""
import copy

class Figure:
    def clone(self):
        pass
    def getInfo(self):
        print(id(self))
        print(self.__dict__)

class Rectangular(Figure):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.square = self.width*self.height

    def clone(self):
        return copy.deepcopy(self)

class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius
        self.square = self.radius*2*3.14

    def clone(self):
        return copy.deepcopy(self)

if __name__=='__main__':
    r1 = Rectangular(10,15)
    r1.getInfo()
    r2 = r1.clone()
    r2.getInfo()

    c1 = Circle(12)
    c1.getInfo()
    c2 = c1.clone()
    c2.getInfo()

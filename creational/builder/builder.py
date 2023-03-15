"""
ПАТТЕРН СТРОИТЕЛЬ
- Когда процесс создания нового объекта не должен зависеть от того,
из каких частей этот объект состоит и как эти части связаны между собой
- Когда необходимо обеспечить получение различных вариаций объекта в процессе его создания
https://metanit.com/sharp/patterns/2.5.php
В отличие от фабрики акцент на пошаговом создании объекта, а в фабрике - на семействе объектов
Нет абстрактного описания получаемого продукта - клиент знает, какой продукт заказывает и как с ним
обращаться. Продукты могут быть очень разными.
"""

"""
Клиент, дающий заказ распорядителю/director (пекарю) на сбор продукта (хлеба или кофе)
"""
class Bakery:
    def test_it(self):
        b = Baker()
        p1 = b.doit(WhiteBreadBuilder())
        print(p1)
        p2 = b.doit(RyeBreadBuilder())
        print(p2)
        c1 = b.doit(CoffeeArabicaBuilder())
        print(c1)
        # подразумевается, что клиент знает, что он заказывает у распорядителя
        # и поэтому знает о том, как обращаться с полученным продуктом
        c1.add_sugar()
        print(c1)
"""
Пекарь, распорядитель действий билдера
"""
class Baker:
    def doit(self,builder):
        builder.create_product()
        builder.set_salt()
        builder.set_flour()
        builder.set_additives()
        builder.set_sugar()
        builder.set_grain()
        return builder.product
"""
Продукт хлеб
"""
class Bread:
    def __init__(self):
        self.flour = ''
        self.salt = ''
        self.additives = ''
    def __repr__(self):
        return str(self.__dict__)
"""
Абстрактный билдер продукта, включающий все возможные ингредиенты (и для хлеба, и для кофе)
"""
class Builder:
    def create_product(self):
        self.product = Bread()
    def set_flour(self):
        pass
    def set_salt(self):
        pass
    def set_additives(self):
        pass
    def set_grain(self):
        pass
    def set_sugar(self):
        pass
"""
Билдер белого хлеба
"""
class WhiteBreadBuilder(Builder):
    def set_flour(self):
        self.product.flour = 'Пшеничная мука'
    def set_additives(self):
        self.product.additives = 'Улучшители вкуса для белого хлеба'
"""
Билдер ржаного хлеба
"""
class RyeBreadBuilder(Builder):
    def set_flour(self):
        self.product.flour = 'Ржаная мука'
    def set_salt(self):
        self.product.salt = 'Соль'
    def set_additives(self):
        self.product.additives = 'Изюм'

"""
другой продукт, отличающийся от хлеба дополнительным методом
"""
class Coffee:
    def __init__(self):
        self.grain = ''
        self.sugar = ''

    def add_sugar(self):
        self.sugar = 'Больше сахара'

    def __repr__(self):
        return str(self.__dict__)
"""
билдер кофе
"""
class CoffeeArabicaBuilder(Builder):
    def create_product(self):
        self.product = Coffee()
    def set_grain(self):
        self.product.grain = 'Арабика'
    def set_sugar(self):
        self.product.sugar = 'Немного сахара'


if __name__=='__main__':
    b = Bakery()
    b.test_it()
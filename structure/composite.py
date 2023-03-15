"""
COMPOSITE/компоновщик
структурирует объекты
Абстрактный класс Component, рекурсивно работающий одновременно
и с примитивами Leaf (линия),
и с контейнерами Composite (рисунок из линий).
Клиенты манипулируют объектами композиции через интерфейс Component.  Если получателем
запроса является листовой объект Leaf, то он обрабатывает запрос. Если получателем будет
составной объект Composite, то обычно он перенаправляет запрос своим потомкам Leaf,
 возможно, выполняя дополнительные операции.
"""
class Component:
    def __init__(self,name):
        self.name = name
        self.children = []

    def add(self,instance):
        self.children = self.children + [instance,]

    def delete(self, instance):
        if instance in self.children:
            self.children.remove(instance)
            return True
        else:
            result = False
            for i in self.children:
                result = i.delete(instance)
                if result == True:
                    break
            return result


    def display(self,tab=''):
        res = tab+self.name.upper()+':\n'
        for i in self.children:
            res += i.display(tab+'-')
        return res

class Leaf(Component):
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def display(self,tab=''):
        return f'{tab}Name: {self.name}, weight: {self.weight} kg\n'

    def delete(self, instance):
        return False

class Composite(Component):
    def __init__(self,name, children=[]):
        self.name = name
        self.children = children

    @property
    def weight(self):
        res = 0
        for i in self.children:
            res += i.weight
        return res

    @weight.setter
    def weight(self,new_weight):
        raise Exception('You can not assign weight to bunch of leaves.')


if __name__=='__main__':
    c = Composite('root')
    leaf = Leaf('chair',10)
    subtree = Composite('Subtree',[Leaf('table',120),Leaf('sofa',230)])
    c.add(subtree)
    subtree2 = Composite('Subtree2',[Leaf('wardrobe',400),Composite('Subtree3',[leaf,Leaf('banket',40)]),])
    c.add(subtree2)
    print(subtree2.weight)
    print(c.display())
    c.delete(leaf)
    wrong_leaf = Leaf('nothing',10)
    c.delete(wrong_leaf)
    print(c.display())

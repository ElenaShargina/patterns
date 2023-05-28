"""
ИТЕРАТОР
необходимо менять итераторы, не забираясь в код конкретного списка(итерируемого объекта)
"""
class Abstract_List:
    def create_iterator(self,iterator_cls):
        return iterator_cls(self)
    def count(self):
        pass
    def append(self,item):
        pass
    def remove(self,item):
        pass

class Abstract_Iterator:
    def __init__(self,list_obj):
        self._index = None
        self._list = list_obj
    def first(self):
        pass
    def next(self):
        pass
    def is_done(self):
        pass
    def current_item(self):
        pass

class Person_List(Abstract_List):
    def __init__(self):
        self._list = []
    def count(self):
        return len(self._list)
    def append(self,item):
        self._list.append(item)
    def remove(self,item):
        self._list.pop(self._list.index(item))
    def __getitem__(self, key):
        return self._list[key]
    def show(self):
        for i in self._list:
            print(i)

class Straight_Iterator(Abstract_Iterator):
    def first(self):
        self._index = 0
    def next(self):
        if not self.is_done():
            self._index += 1
        else:
            raise Exception('Out of range error!')
    def is_done(self):
        if self._list.count() <= self._index:
            return True
        else:
            return False
    def current_item(self):
        return self._list[self._index]

class Backward_Iterator(Abstract_Iterator):
    def first(self):
        self._index = self._list.count()-1
    def next(self):
        if not self.is_done():
            self._index -= 1
        else:
            raise Exception('Out of range error!')
    def is_done(self):
        if self._index < 0:
            return True
        else:
            return False
    def current_item(self):
        return self._list[self._index]

class House:
    def __init__(self, street, house):
        self.street = street
        self.house = house

    def __str__(self):
         return ' '.join([self.street, self.house])

class House_dict(Abstract_List):
    def __init__(self):
        self._list = []
    def count(self):
        return len(self._list)
    def append(self,item : House):
        self._list.append(item)
    def remove(self,item):
        self._list.pop(item)
    def __getitem__(self, key):
        return self._list[key]
    def show(self):
        for i in self._list:
            print(i)

if __name__=='__main__':
    mylist = Person_List()
    mylist.append('Ivan Ivanov')
    mylist.append('Sergei Sergeev')
    mylist.append('Prohor Prohorov')
    mylist.append('Anna Sergeeva')
    print('Наш начальный список людей:')
    mylist.show()
    print('Людей в списке: ',mylist.count())
    print('Удаляем Ivan Ivanov, теперь список выглядит так: ')
    mylist.remove('Ivan Ivanov')
    mylist.show()
    print('Запускаем прямой итератор по списку людей: ')
    iter1 = mylist.create_iterator(Straight_Iterator)
    iter1.first()
    while not iter1.is_done():
        print(iter1.current_item())
        iter1.next()

    print('Запускаем обратный итератор по списку людей: ')
    iter2 = mylist.create_iterator(Backward_Iterator)
    iter2.first()
    while not iter2.is_done():
        print(iter2.current_item())
        iter2.next()

    print('Запускаем одновременно прямой и обратный итераторы по списку людей: ')
    iter3 = mylist.create_iterator(Straight_Iterator)
    iter4 = mylist.create_iterator(Backward_Iterator)
    iter3.first()
    iter4.first()
    while not (iter3.is_done() and iter4.is_done()):
        print('->: '+ iter3.current_item(), ' - ', '<-: ' + iter4.current_item())
        iter3.next()
        iter4.next()

    print('Список домов')
    my_dict = House_dict()
    my_dict.append(House('Сиреневая улица','113'))
    my_dict.append(House('Ивановская улица','8'))
    my_dict.append(House('Коробковая улица','4'))
    print('Запускаем обратный итератор по списку домов: ')
    iter5 = my_dict.create_iterator(Backward_Iterator)
    iter5.first()
    while not iter5.is_done():
        print(iter5.current_item())
        iter5.next()


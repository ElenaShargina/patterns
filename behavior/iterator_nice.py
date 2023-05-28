class Abstract_iterator:
    def __init__(self,data):
        self._data = data
    def __getitem__(self, key):
        return self._data[key]
    def __iter__(self):
        pass
    def __next__(self):
        pass

class Straight_Iterator(Abstract_iterator):
    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix >= len(self._data):
            raise StopIteration
        item = self._data[self.ix]
        self.ix += 1
        return item

class Backward_iterator(Abstract_iterator):
    def __iter__(self):
        self.ix = len(self._data)-1
        return self

    def __next__(self):
        if self.ix < 0:
            raise StopIteration
        item = self._data[self.ix]
        self.ix -=1
        return item

class Abstract_List:
    def __init__(self,data):
        self._data = data

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def create_iterator(self,iterator_cls):
        return iterator_cls(self)

    def __str__(self):
        return ', '.join(str(i) for i in self._data)


if __name__=='__main__':
    print('Инициализируем список')
    x = Abstract_List([1,2,3,4,5])
    print(x)
    print('Запускаем прямой итератор')
    i1 = x.create_iterator(Straight_Iterator)
    for k in i1:
        print(k)
    print('Запускаем обратный итератор')
    i2 = x.create_iterator(Backward_iterator)
    for k in i2:
        print(k)

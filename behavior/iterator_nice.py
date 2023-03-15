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
        print('initialize iter')
        self.ix = 0
        return self

    def __next__(self):
        # print('next->')
        if self.ix >= len(self._data):
            raise StopIteration
        item = self._data[self.ix]
        self.ix += 1
        return item

class Backward_iterator(Abstract_iterator):
    def __iter__(self):
        print('initialize back iter')
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



if __name__=='__main__':
    # x = Backward_iterator(Abstract_List([1,2,3,4,5]))
    # x = Abstract_List([1,2,3,4]).create_iterator(Straight_Iterator)
    #
    # for i in x:
    #     print(i, end=' | ')

    x = Abstract_List([1,2,3,4,5])
    i1 = x.create_iterator(Straight_Iterator)
    i2 = x.create_iterator(Backward_iterator)
    for i in i1:
        for j in i2:
            print(str(i)+'-'+str(j))
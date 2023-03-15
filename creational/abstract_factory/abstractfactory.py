from maze import *
from random import Random
"""
PATTERN abstract factory
"""
"""
абстрактный интерфейс для продукта фабрики - лабиринта
"""
class AbstractMaze:
    def draw(self):
        pass
    def add_room(self, r):
        pass
    def add_door(self,r1,r2):
        pass

"""
абстрактная фабрика для изготовления лабиринтов вне зависимости от их реализации,
главное, чтобы их продукт удовлетворял интерфейсу абстрактного продукта
"""
class MazeFactory:
    def make_maze(self):
        pass
    def make_room(self):
        pass

"""
класс, использующий абстрактную фабрику лабиринтов. На вход нужно дать только указание о том,
какую конкретную реализацию лабиринтов использовать
"""
class MazeGame:
    def create_maze(self,maze_factory:MazeFactory):
        m = maze_factory.make_maze()
        r1 = maze_factory.make_room()
        r2 = maze_factory.make_room()
        r3 = maze_factory.make_room()
        r4 = maze_factory.make_room()
        m.add_room(r1)
        m.add_room(r2)
        m.add_room(r3)
        m.add_room(r4)

        m.add_door(r1,r2)
        m.add_door(r2,r3)

        print(m.draw())
        return m

"""
класс конкретной фабрики, реализующей интерфейс абстрактной
"""
class SimpleMazeFactory(MazeFactory):
    def make_maze(self):
        return SimpleMaze()
    def make_room(self):
        return SimpleRoom()
"""
класс конкретного продукта, реализующий интерфейс абстрактного
(Maze наследуем для удобства, чтобы не переносить сюда весь код)
"""
class SimpleMaze(Maze,AbstractMaze):
    pass
class SimpleRoom(Room):
    pass

"""
класс конкретной фабрики, реализующей интерфейс абстрактной
"""
class NumberMazeFactory(MazeFactory):
    def make_maze(self):
        return NumberMaze()
    def make_room(self):
        return NumberRoom()

"""
класс конкретного продукта NumberMaze 
 соответствует интерфейсу абстрактного продукта
"""
class NumberMaze(AbstractMaze):
    _data:list
    def __init__(self):
        self._data = list()

    def draw(self):
        res = ''
        for i in self._data:
            if type(i)==NumberRoom:
               res += ' '+str(i.index)+' '
            else:
                res += str(i)
        return res

    def add_room(self, r):
        self._data.append(r)

    def add_door(self,r1,r2):
        index_r1 = self._data.index(r1)
        index_r2 = self._data.index(r2)
        self._data = self._data[:index_r1+1]+['->']+self._data[index_r2:]

class NumberRoom():
    all_indexes = []
    index:int
    def __init__(self):
        new_index = 0
        while new_index in NumberRoom.all_indexes or new_index==0:
            new_index = random.randint(1,10**6)
        self.index = new_index

if __name__=='__main__':
    print('SIMPLE!')
    ms = MazeGame().create_maze(SimpleMazeFactory())
    ms.draw()

    print('ENCHANTED!')

    me = MazeGame().create_maze(NumberMazeFactory())
    me.draw()
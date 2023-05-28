"""
MEMENTO/token
не нарушая инкапсуляции фиксирует и выносит за пределы объекта его внутреннее состояние так,
чтобы позднее можно было восстановить в нем обьект
"""
import random
import shelve

# базовые классы графических объектов
class Point:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

class Graphic:
    def __init__(self,x:int,y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self,delta:Point):
        self.x += delta.x
        self.y += delta.y

    def draw(self):
        print(f'({self.x},{self.y+self.height})'.ljust(20,'-'),f'({self.x+self.width,self.y+self.height})')
        print('|'.ljust(20,'-'),'|')
        print(f'({self.x},{self.y})'.ljust(20,'-'),f'({self.x+self.width},{self.y})')

# класс команды на движение графического объекта
class MoveCommand:
    def __init__(self,target: Graphic, delta: Point):
        self._target = target
        self._delta = delta
        self._state = None

    def execute(self):
        # обращаемся к классу за хранителем
        solver = ConstraintSolver.get_solver()
        # получаем хранителя, описывающего текущее состояние внутренних уравнений и переменных ConstraintSolver
        self._state = solver.create_memento()
        self._target.move(self._delta)
        # классу связей надо пересчитать линии
        solver.solve()

    def unexecute(self):
        solver = ConstraintSolver.get_solver()
        self._target.move(Point(self._delta.x*(-1),self._delta.y*(-1)))
        #восстановление состояния хозяина - возвращаем ConstraintSolver хранящуюся в хранителе инофрмацию
        solver.set_memento(self._state)
        # основываясь на переданной информации, ConstraintSolver изменяет свои внутренние структуры,
        # возвращая уравнения и переменные (линии) в начальное состояние
        solver.solve()

# хранитель. Сохраняет внутреннее состояние объекта ConstraintSolver.
class SolverState:
    def __init__(self,obj):
        self._key = str(hash(obj)+random.randint(0,10**6))
        with shelve.open('memento_files/memento') as db:
            db[self._key] = obj

    def get_info(self):
        with shelve.open('memento_files/memento') as db:
            # print(self._key)
            return db[self._key]

class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print(f'({self.x1},{self.y1}) ----> ({self.x2},{self.y2})')

# класс, отвечающий за связи между графическими объектами
# класс-хозяин, создает хранитель, содержащий снимок текущего внутреннего состояния
# использует хранитель для восстановления внутреннего состояния
# регистрирует линии, соединяющие графические объекты Graphic
# реализован с помощью Singleton
class ConstraintSolver:
    _instance = None
    # список связей между парами графических объектов
    _constraints = []
    _another = None
    @classmethod
    def get_solver(cls):
        if cls._instance == None:
            cls._instance = ConstraintSolver()
        return cls._instance

    def __init__(self):
        pass

    def add_constraint(self,a:Graphic,b:Graphic):
        self._constraints.append((a,b))
        self.solve()

    def remove_constraint(self):
        pass

    def draw(self):
        for i in self._lines:
            i.draw()

# пересчитываем все линии для списка связей
# если сеть переданная информация от хранителя, то просто загружаем ее
    def solve(self):
        if self._another!=None:
            print('Загружаем старое сохранение!')
            self._lines = self._another._lines
            self._constraints = self._another._constraints
            self._another = None
        else:
            self._lines = []
            for i in self._constraints:
                a = i[0]
                b = i[1]
                self._lines.append(Line(a.x + a.width // 2, a.y + a.height, b.x + b.width // 2, b.y))


# создаем снимок текущего состояния объекта и возвращаем его
    def create_memento(self):
        return SolverState(self)

# получаем снимок прошлого состояния объекта и обрабатываем его
    # здесь - просто запоминаем
    def set_memento(self, state:SolverState):
        self._another = state.get_info()

# служебная функция для отрисовки всей картинки
def draw_everything(*args):
    for i in args:
        i.draw()

if __name__=='__main__':
    g1 = Graphic(0,0,10,5)
    g2 = Graphic(20,20,10,5)
    cs = ConstraintSolver.get_solver()
    cs.add_constraint(g1,g2)
    draw_everything(g1,g2,cs)
    # даем команду на движение объекта
    my_command = MoveCommand(target=g1,delta=Point(10,0))
    my_command.execute()
    draw_everything(g1,g2,cs)
    my_command1 = MoveCommand(target=g1,delta = Point(3,3))
    my_command1.execute()
    draw_everything(g1,g2,cs)
    # отменяем команды
    my_command1.unexecute()
    draw_everything(g1, g2, cs)
    my_command.unexecute()
    draw_everything(g1,g2,cs)







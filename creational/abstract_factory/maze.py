import random
from enum import Enum
from random import Random

class DrawException(Exception):
    pass

class Direction(Enum):
    north='N'
    south='S'
    east='E'
    west = 'W'

class Incline(Enum):
    vertical = 'V'
    horizontal = 'H'

class MapSite:
    width=5
    vertical_symbol = '|'
    horizontal_symbol = '--'
    corner_symbol = '.'
    empty_symbol = '  '
    door_symbol = '+'
    def enter(self):
        pass
    def draw(self):
        pass

class Room(MapSite):
    all_numbers: list=[]
    def __init__(self):
        new_index = 0
        while new_index in Room.all_numbers or new_index==0:
            new_index = random.randint(1,10**6)
        Room.all_numbers.append(new_index)
        self.number = new_index
        self.sides = {}
        for i in Direction:
            self.set_side(Wall(),i)

    number: int = None
    sides: dict

    def set_side(self,side,direction:Direction):
        if side.incline == None:
            if direction in (direction.north, direction.south):
                side.incline = Incline.horizontal
            elif direction in (direction.east, direction.west):
                side.incline = Incline.vertical
        self.sides[direction.value] = side

    def set_door(self,direction:Direction):
        self.set_side(Door(),direction)

    def draw(self):
        """
        .------.
        |      |
        |      |
        |      |
        .------.
        """
        res = self.corner_symbol
        if self.sides[Direction.north.value]:
            res += self.sides[Direction.north.value].draw()
        else:
            res += Wall(incline=Incline.horizontal).draw()
        res += self.corner_symbol+'\n'
        vert_res = ''
        if self.sides[Direction.west.value]:
            vert_res += self.sides[Direction.west.value].draw()
        else:
            vert_res += Wall(incline=Incline.vertical).draw()
        if self.sides[Direction.east.value]:
            vert_res += self.sides[Direction.east.value].draw()
        else:
            vert_res += Wall(incline=Incline.vertical).draw()
        vert_res = vert_res.strip().split('\n')
        for i in range(0,len(vert_res)//2):
            res += vert_res[i]+self.empty_symbol*self.width+vert_res[len(vert_res)//2+i]+'\n'
        res += self.corner_symbol
        if self.sides[Direction.south.value]:
            res += self.sides[Direction.south.value].draw()
        else:
            res += Wall(incline=Incline.horizontal).draw()
        res += self.corner_symbol+'\n'
        return res

class Wall(MapSite):
    incline:Incline = None
    def __init__(self, incline=None):
        self.incline = incline

    def draw(self):
        if self.incline == Incline.vertical:
            return f'{self.vertical_symbol}\n'*self.width
        elif self.incline == Incline.horizontal:
            return self.horizontal_symbol*self.width
        else:
            raise DrawException(f'Can not draw wall {self}, no incline is specified.')

class Door(Wall):
    is_open: bool = False
    # room_1: Room = None
    # room_2: Room = None

    def draw(self):
        if self.incline == Incline.vertical:
            wall_height = self.width//3
            door_height = self.width- 2*wall_height
            return f'{self.vertical_symbol}\n'*wall_height+f'{self.door_symbol}\n'*door_height+f'{self.vertical_symbol}\n'*wall_height
        elif self.incline == Incline.horizontal:
            wall_width = self.width // 3
            door_width = self.width - 2 * wall_width
            return self.vertical_symbol * wall_width + self.door_symbol * door_width + self.vertical_symbol * wall_width
        else:
            raise DrawException(f'Can not draw door {self}, no incline is specified.')

class Maze:
    data: list = []
    def add_room(self, room: dict(type=Room,help='help string'))->None:
        self.data.append(room)

    def add_door(self,room1:Room,room2:Room):
        room1.set_door(Direction.east)
        room2.set_door(Direction.west)

    def draw(self):
        res = ''
        res_list = []
        number_of_rooms = len(self.data)
        for r in self.data:
            res_list.append(list(r.draw().splitlines()))
        i = 0
        room_height = len(res_list[0])
        while i<room_height:
            for r in res_list:
                res += r[i]
            res += '\n'
            i+=1
        return res


if __name__=='__main__':
    m = Maze()

    r1 = Room()
    m.add_room(r1)
    r2 = Room()
    m.add_room(r2)

    m.add_door(r1,r2)

    r3 = Room()
    m.add_room(r3)
    m.add_door(r2,r3)

    r4 = Room()
    m.add_room(r4)
    print(m.draw())
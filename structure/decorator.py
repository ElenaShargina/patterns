"""
DECORATOR/WRAPPER
динамически добавляет объекту новые обязанности.
"""
from colorama import init,Fore
from colorama import Back
from colorama import Style

class Component:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def draw(self):
        return self.name+' '+self.surname

class Decorator(Component):
    def __init__(self,component:Component):
        self._component = component

    def draw(self):
        return self._component.draw()

class PlusDecorator(Decorator):
    def draw(self):
        return '++++\n'+self._component.draw()+'\n++++'

class MinusDecorator(Decorator):
    def draw(self):
        return '----\n' + self._component.draw() + '\n----'

class GreenDecorator(Decorator):
    def draw(self):
        return Fore.GREEN+self._component.draw()+'\n'

if __name__=='__main__':
    init(autoreset=True)
    c = Component('Ivan', 'Ivanov')
    print(c.draw())
    pdc = PlusDecorator(c)
    print(pdc.draw())
    mdc = MinusDecorator(c)
    print(mdc.draw())
    greendc = GreenDecorator(c)
    print(greendc.draw())
    w = PlusDecorator(MinusDecorator(MinusDecorator(Component('Erast','Fandorin'))))
    print(w.draw())
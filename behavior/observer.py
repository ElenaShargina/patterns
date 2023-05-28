"""
Observer / publish-subscribe / dependents
К данным прикреплены диаграмма и таблица. Они не знают друг о друге, но когда пользователь
работает с таблицей, то изменений отражаются и на диаграмме, и наоборот.
И таблица, и диаграмма зависят от данных объекта и поэтому должны уведомляться о любы изменениях
в его состоянии.
Субъект - может быть сколько угодно зависимых от него наблюдателей.
Все наблюдатели уведомляются об изменениях в состоянии субъекта. Получив уведомление,
наблюдатель опрашивает субъекта, чтобы синхронизировать с ним свой состояние.
Субъект не имеет информации о том, какие объекты являются подписчиками.
"""
import datetime, time
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self,observer):
        self._observers.append(observer)

    def detach(self,observer):
        index = self._observers.index(observer)
        if index!=None:
            self._observers.pop(index)

    def notify(self):
        for i in self._observers:
            i.update(self)

    def get_info(self):
        pass

class Observer:
    def __init__(self,subject:Subject):
        subject.attach(self)
        self.update(subject)

    def update(self,subject:Subject):
        pass

class Timer(Subject):
    def tick(self):
        self.time = datetime.datetime.now()
        print(self.time)
        self.notify()

    def get_info(self):
        return (self.time.hour, self.time.minute, self.time.second)

class DigitalClock(Observer):
    def update(self,subject:Subject):
        self.represent = 'DIGI' + ':'.join([str(i) for i in subject.get_info()])

    def draw(self):
        print(self.represent)

class AnalogClock(Observer):
    def update(self,subject:Subject):
        self.represent = 'ANALOG' + ':'.join([str(i) for i in subject.get_info()])

    def draw(self):
        print(self.represent)


if __name__=='__main__':
    timer = Timer()
    timer.tick()
    aclock = AnalogClock(timer)
    dclock = DigitalClock(timer)
    aclock.draw()
    dclock.draw()
    time.sleep(5)
    timer.tick()
    aclock.draw()
    dclock.draw()

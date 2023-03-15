"""
Adapter/Wrapper
Преобразует интерфейс одного класса в интерфейс другого, который ожидают клиенты
Обеспечивает совместную работу классов, которая без него была бы невозможна
"""
class TransportAdapter:
    def go(self):
        pass

class AutoAdapter(TransportAdapter):
    def go(self):
        self.drive()

class Auto(AutoAdapter):
    def drive(self):
        print('Машина едет!')

class CamelAdapter(TransportAdapter):
    def go(self):
        self.run()

class Camel(CamelAdapter):
    def run(self):
        print('Верблюд едет!')

class Driver:
    def travel(self,transport: TransportAdapter):
        transport.go()

if __name__=='__main__':
    d = Driver()
    auto = Auto()
    d.travel(auto)
    camel = Camel()
    d.travel(camel)


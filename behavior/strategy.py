"""
Strategy / Policy

определяет семейство алгоритмов, инкапсулирует их и делает их взаимонезависимыми.
Стратегия позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.

При этом конкретные стратегии могут пользоваться не всей информацией, которую им передает Контекст.
Интерфейс Контекста должен быть спроектирован, чтобы покрыть все возможные потребности стратегий,
которые могут добавляться в будущем. Также должен быть спроектирован интерфейс
абстрактного класса Strategy
"""
class Strategy:
    def __init__(self,context):
        self._context = context
    def algorithm(self,data):
        pass

class ConcreteStrategy1(Strategy):
    def algorithm(self,data):
        print('Starting concrete strategy 1 with data', data, ' and params', self._context.params[1])

class ConcreteStrategy2(Strategy):
    def algorithm(self, data):
        print('Starting concrete strategy 2 with data', data, ' and params', self._context.params[0])


class Context:
    def __init__(self,params):
        self.params = params

    def doit(self,strategy,data):
        strategy(self).algorithm(data)

if __name__=='__main__':
    my_context = Context(['param1','param2'])
    my_context.doit(ConcreteStrategy1,'some specific data')
    my_context.doit(ConcreteStrategy2,'another specific data')
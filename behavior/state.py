"""
State
позволяет объекту варьировать свое поведение в зависимости от внутреннего состояния.
Извне создается впечатление, что изменился класс объекта.

Применяется, когда в коде операций встречаются состоящие из многих ветвей условные
операторы, в которых выбор ветви зависит от состояния.
"""
# класс Context, через который работают клиенты
class Connection:
    def __init__(self,port):
        self._state = TCPClosed(port)

    def open(self):
        print('Open the connection...')
        self._state.open(self)

    def close(self):
        print('Close the connection...')
        self._state.close(self)

    def change_state(self,state):
        self._state = state

    def acknowledge(self):
        self._state.acknowledge()

# class State - в этом примере о смене состояний знают ConcreteStates, то есть
# введены связи между этими подклассами
class TCPState:
    def __init__(self,port):
        self._port = port
    def open(self,connection):
        pass
    def close(self,connection):
        pass
    def acknowledge(self):
        pass

# class ConcreteState
class TCPEstablished(TCPState):
    def open(self,connection):
        pass
    def close(self,connection):
        connection.change_state(TCPClosed(self._port))
    def acknowledge(self):
        print(f'Connection is in established state at {self._port} port')

class TCPClosed(TCPState):
    def open(self,connection):
        connection.change_state(TCPEstablished(self._port))
    def close(self,connection):
        pass
    def acknowledge(self):
        print(f'Connection is in closed state at {self._port} port')

if __name__=='__main__':
    connect = Connection(port=123)
    connect.acknowledge()
    connect.open()
    connect.acknowledge()
    connect.close()
    connect.acknowledge()


"""
    В ЭТОМ ПРИМЕРЕ РЕШЕНИЕ О СМЕНЕ ПОДКЛАССА СОСТОЯНИЯ будет принимать
    класс контекста
"""
class Context:
    def __init__(self,port):
        self._port = port
        self._state = ClosedState(self._port)

    def open(self):
        self._state.__class__ = OpenedState
        # self._state = OpenedState(self._port)

    def close(self):
        self._state = ClosedState(self._port)
        # new_class = type('MyClosed',(ClosedState,),self._state.__dict__)
        # self._state = new_class(self._port)

        # self._state.__class__ = type('MyClosed', (ClosedState,), self._state.__dict__)

        # self._state.__class__ = ClosedState

    def send(self,message):
        self._state.send(message)

    def acknowledge(self):
        self._state.acknowledge()

class State:
    def __init__(self,port):
        self._port = port
    def open(self):
        pass
    def close(self):
        pass
    def acknowledge(self):
        print(self.__class__.__name__,end=' -> ')
        self._acknowledge()
    def send(self,message):
        pass

class ClosedState(State):
    def open(self):
        print('The state is Closed.')
    def close(self):
        pass
    def _acknowledge(self):
        print(f'The state is closed at {self._port} port.')
    def send(self,message):
        print('Cant send message to closed state')

class OpenedState(State):
    def open(self):
        pass
    def close(self):
        pass
    def _acknowledge(self):
        print(f'The state is opened at {self._port} port.')
    def send(self,message):
        print(f'Message {message} is successfully sent.')

if __name__=='__main__':
    print('------------')
    context = Context(port=123)
    context.acknowledge()
    context.open()
    context.acknowledge()
    context.send('Hello')
    context.close()
    context.acknowledge()
    context.send('Hi')
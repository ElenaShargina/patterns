"""
Паттерн Command/Action/Transaction
Инкапсулирует запрос как объект, позволяя тем самым задавать параметры клиентов для обработки
соответствующих запросов, ставить запросы в очередь или протоколировать их,
а также поддерживать отмену операций.
Например - кнопки и меню не знают, кто будет обрабатывать их запросы. В реализации кнопок и меню
нет действий, которые они должны инициировать.
Команда может состоять из нескольких команд, направленных в разные места. ТОгда нужен класс
MacroCommand, реализующий последовательность команда Command.

"""
# абстрактный класс команды
class Command():
    history = []
    def __init__(self,application):
        self._app = application
    def execute(self):
        pass

# класс конкретной команды
# определяет связь между объектом-получателем команды (Document) и действием
class OpenCommand(Command):
    def execute(self):
        name = input('Enter the name of new document...\n')
        if hash(name) not in self._app.docs:
            self._app.add_doc(Document(name))
            print(f'New document {name} is created!')
            self._app.docs[hash(name)].rewrite()
            self._app.docs[hash(name)].show()
        else:
            self._app.docs[hash(name)].open()
            self._app.docs[hash(name)].show()
        self._app.current_doc = self._app.docs[hash(name)]

# класс конкретной команды
class RewriteCommand(Command):
    def execute(self):
        if self._app.current_doc == None:
            print('Error: open some document!')
        else:
            self._app.current_doc.rewrite()

# класс конкретной команды
class DeleteCommand(Command):
    def execute(self):
        if self._app.current_doc == None:
            print('Error: open some document!')
        else:
            # удаляем из списка документов приложения
            self._app.delete_doc(self._app.current_doc.name)
            # удаляем сам объект документа
            self._app.current_doc.delete()
            self._app.current_doc = None

# получатель команды, располагает информацией о способах выполнения операций,
# необходимых для удовлетворения запроса
class Document:
    def __init__(self,name):
        self.name = name
        self.text = ''

    def open(self):
        print(f'Document {self.name} is opened!')

    def rewrite(self):
        text = input('Write some text...\n')
        self.text = text
        print(f'Document {self.name} is rewritten: {text}')

    def show(self):
        print(f'Content of document {self.name}:\n{self.text}')

    def close(self):
        print(f'Document {self.name} is closed!')

    def delete(self):
        print(f'Document {self.name} is deleted!')
        del(self)

# инициатор команды, обращается к команде для выполнения запросы
class MenuItem:
    def __init__(self,command):
        self._command = command

    def click(self):
        self._command.execute()

# создает объект класса конкретной команды и устанавливает его получателя
class Application:
    def __init__(self):
        self.docs = {}
        self.menu_items={'open':MenuItem(OpenCommand(self)),
                         'rewrite':MenuItem(RewriteCommand(self)),
                         'del':MenuItem(DeleteCommand(self))}
        self.current_doc = None

    def add_doc(self,document):
        self.docs[hash(document.name)]=document

    def delete_doc(self,name):
        self.docs.pop(hash(name))

    def show_all(self):
        res = ('All documents: ')
        res += ', '.join(list(map(lambda i: i.name, self.docs.values())))
        res += '.'
        print(res)

if __name__=='__main__':
    # клиент создает объект конкретной команды и устанавливает для него получателя
    my_app = Application()
    command = input('PRINT COMMAND (open/rewrite/del/exit)\n')
    while command!='exit':
        my_app.menu_items[command].click()
        my_app.show_all()
        command = input('PRINT COMMAND (open/rewrite/del/exit)\n')
    print('Good bye!')




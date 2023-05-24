"""
Chain of responsibility
Есть более одного объекта, способного обработать запрос, причем настоящий обработчик заранее не известен
Нужно отправить запрос одному из обработчиков, причем заранее не известно, кому именно
Набор объектов, способных обработать запрос, изменяется динамически.
https://www.geeksforgeeks.org/chain-of-responsibility-python-design-patterns/
"""
"""
Подмешиваемый в виджеты класс, содержащий текст подсказки и ссылку на родительский виджет - где будет
искать текст помощи в случае отсутствия текста помощи у себя
"""
class HelpHandler:
    # def __init__(self,next=None,text=''):
    #     self._next = next
    #     self.text = text

    @property
    def has_text(self):
        if self.text!=None:
            return True
        else:
            return False

    def help(self):
        if self.has_text:
            print('HELP:' + str(self.text))
        else:
            if self._next!=None:
                self._next.help()
            else:
                print('No Help is found =(')

class Widget(HelpHandler):
    def __init__(self,type,name,parent=None,help_text=None):
        self.type = type
        self.name = name
        self._next = parent
        self.text = help_text

if __name__=='__main__':
    window = Widget('window','main',help_text='some main help text')
    column1 = Widget('window','column1',window, help_text='some column help text')
    button = Widget('button','button1',column1)
    button.help()
    column2 = Widget('window','column2')
    button2 = Widget('button','button2',column2)
    button2.help()

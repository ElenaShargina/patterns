"""
Паттерн МЕДИАТОР
определяет объект, инкапсулирующий способ взаимодействия множества объектов.
Посредник обеспечивает слабую связанность системы, избавляя объекты
от необходимости явно ссылаться друг на друга и позволяя тем самым независимо
изменять взаимодействия между ними.
"""
from pynput import keyboard

class DialogDirector:
    def __init__(self):
        self._widgets = {}
    def widget_changed(self,widget):
        pass
    def create_widgets(self):
        pass
    def show(self):
        for i in self._widgets.values():
            i.show()

class Widget:
    def __init__(self, director:DialogDirector):
        self._director = director

    def changed(self):
        self._director.widget_changed(self)
    def handle_event(self,event):
        pass
    def show(self):
        pass

class ListBox(Widget):
    def set_items(self,items:list):
        self._items = items
        self.selected_index = None

    def show(self):
        print('-'*25)
        for i,value in enumerate(self._items):
            if i == self.selected_index:
                value = value.upper()
            print(value, end=' | ')
        print('\n'+'-'*25)

    def handle_event(self,event):
        self.selected_index  = self._items.index(event)
        self.changed()

    def get_selected_text(self):
        if self.selected_index!=None:
            return self._items[self.selected_index]
        else:
            return None

class TextField(Widget):
    def set_text(self,text):
        self.text = text

    def show(self):
        print('====>'+self.text+'<=====')

class Button(Widget):
    def set_text(self,text):
        self.text = text
    def set_active(self):
        self.text = self.text.upper()
    def set_inactive(self):
        self.text = self.text.capitalize()
    def show(self):
        print('-'*10)
        print('|'+self.text.center(8,' ')+'|')
        print('-'*10)
    def handle_event(self,event):
        if event==True:
            self.set_active()
        else:
            self.set_inactive()
        self.changed()

class MyDialog(DialogDirector):
    def create_widgets(self,listbox:ListBox,textfield:TextField,button:Button):
        self._widgets['listbox'] = listbox
        self._widgets['textfield'] = textfield
        self._widgets['button'] = button

    def widget_changed(self,widget:Widget):
        if widget == self._widgets['listbox']:
            print('list!')
            self._widgets['textfield'].set_text(widget.get_selected_text())
        elif widget == self._widgets['button']:
            print('button!')

        self.show()

if __name__=='__main__':
    d = MyDialog()

    lb = ListBox(d)
    lb.set_items(['first', 'second', 'third'])

    tf = TextField(d)
    tf.set_text('sample')

    b = Button(d)
    b.set_text('Okey')

    d.create_widgets(lb,tf,b)
    d.show()

    lb.handle_event('second')

    b.handle_event(True)

    b.handle_event(False)

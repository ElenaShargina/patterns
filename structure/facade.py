"""
FACADE
класс, организующий работу с разветвленной подсистемой(например, с компилятором)
класс знает каким подсистемам адресовать запрос
Классы подсистемы реализуют функциональность подсистемы,
ничего не знают о существовании фасада, не хранят ссылок на него
"""
class Compiler:
    def compile(self):
        print('Компилирование кода')

class TextEditor:
    def textit(self):
        print('Набор кода')
    def checkit(self):
        print('Проверка кода')

class Debugger:
    def debug(self):
        print('Дебаг кода')

class IDE:
    def __init__(self):
        self.compiler = Compiler()
        self.texteditor = TextEditor()
        self.debugger = Debugger()

    def text_and_debug(self):
        self.texteditor.textit()
        self.texteditor.checkit()
        self.debugger.debug()

    def debug_and_compile(self):
        self.debugger.debug()
        self.compiler.compile()


if __name__ == '__main__':
    x = IDE()
    x.text_and_debug()
    x.debug_and_compile()
    x.debugger.debug()

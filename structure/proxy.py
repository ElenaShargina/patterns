"""
Когда надо осуществлять взаимодействие по сети, а объект-проси должен имитировать поведения
объекта в другом адресном пространстве. Использование прокси позволяет снизить
накладные издержки при передачи данных через сеть.
Подобная ситуация еще называется удалённый заместитель (remote proxies)

Когда нужно управлять доступом к ресурсу, создание которого требует больших затрат.
Реальный объект создается только тогда, когда он действительно может понадобится,
а до этого все запросы к нему обрабатывает прокси-объект.
Подобная ситуация еще называется виртуальный заместитель (virtual proxies)

Когда необходимо разграничить доступ к вызываемому объекту в зависимости
от прав вызывающего объекта. Подобная ситуация еще называется
защищающий заместитель (protection proxies)

Когда нужно вести подсчет ссылок на объект или обеспечить
потокобезопасную работу с реальным объектом.
Подобная ситуация называется "умные ссылки" (smart reference)
"""
import random
import string

class Page:
    def __init__(self,number,text):
        self.number = number
        self.text = text

"""
класс с обращением к базе данных либо тяжелой генерацией контента
"""
class RealBook:
    def get_page(self,number):
        print('Generating new page...')
        text = ''.join([random.choice(string.ascii_letters+string.punctuation+' ') for x in range(120)])
        return Page(number,text)
"""
класс-прокси, решающий, нужно ли запускать тяжелую генерацию или обращение к БД.
Фактически - кеш страниц.
"""
class BookProxy(RealBook):
    def __init__(self):
        self._pages = {}
        self._book = RealBook()

    def get_page(self,number):
        if number not in self._pages.keys():
            self._pages[number] = self._book.get_page(number)
        return self._pages[number]

"""
класс, с которым работает клиент. Клиент не видит прокси
"""
class Book:
    def __init__(self):
        self._proxy = BookProxy()

    def get_page(self,number):
        return self._proxy.get_page(number)


if __name__=='__main__':
    b = Book()
    # обращаемся каждый раз к новой странице, они будут генерироваться
    for n in range(1,10):
        p = b.get_page(n)
        print(p.text)
    # обращаемся к уже запрошенной когда-то странице,
    # она не будет генерироваться заново, а возьмется из кеша
    p = b.get_page(3)
    print(p.text)
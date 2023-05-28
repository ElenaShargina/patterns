"""
Template Method
определяет основу алгоритма и позволяет подклассам переопределить некоторые шаги алгоритма,
не изменяя его структуру в целом
"""

class Application:
    def __init__(self):
        self._docs = []

    def add_document(self,doc):
       self._docs.append(doc)

    def open_document(self,path):
        if self.can_open_document(path):
            doc = PDFDocument(path)
            doc.open()
            self.add_document(doc)
            doc.do_read()
        else:
            self.about_to_create_document(path)
            doc = self.do_create_document(path)
            self.add_document(doc)
            doc.do_read()



    # абстрактный метод, должен быть переопределен
    def do_create_document(self,doc):
        pass

    # абстрактный метод, должен быть переопределен
    def can_open_document(self,doc):
        pass

    # абстрактный метод, должен быть переопределен
    def about_to_create_document(self, doc):
        pass

class MyApplication(Application):
    def do_create_document(self,path):
        print('MyApplication creates document.')
        doc = PDFDocument(path)
        doc.save()
        return doc

    def can_open_document(self,path):
        if 'notexist' in path:
            return False
        else:
            return True

    def about_to_create_document(self, path):
        print('Document is not found. I will create it.')

class Document:
    def __init__(self,path):
        self.path = path
    def save(self):
        print(f'Saving document {self.path}')

    def open(self):
        print(f'Opening document {self.path}')

    def close(self):
        print(f'Closing document {self.path}')

    # абстрактный метод, должен быть переопределены
    def do_read(self):
        pass

class PDFDocument(Document):
    def do_read(self):
        print(f'Special reading from PDF file {self.path}.')

if __name__=='__main__':
    myapp = MyApplication()
    myapp.open_document('folder/notexist.txt')
    myapp.open_document('folder/exist.txt')

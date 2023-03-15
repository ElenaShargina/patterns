"""
BRIDGE/HANDLE/BODY
Связь агрегации между классами Abstraction и Implementor фактически
и представляет некоторый мост между двумя параллельными иерархиями классов.

"""
# имплементатор
class ILanguage:
    def build(self,product):
        pass
    def execute(self,product):
        pass

# конкретный имплементатор 1
class CPPLanguage(ILanguage):
    def build(self,product):
        print(f'Пишем на C++ программу {product}.')
    def execute(self,product):
        print(f'Компилируем программу {product} на C++.')

# конкретный имплементатор 2
class PythonLanguage(ILanguage):
    def build(self,product):
        print(f'Пишем на Python программу {product}.')
    def execute(self,product):
        print(f'Запускаем программу {product} на Python.')

# Абстракция
class Programmer:
    def __init__(self,language: ILanguage,project:str):
        self.language = language
        self.project = project
    def work(self):
        pass
    def earn(self):
        pass

# Уточненная абстракция 1
class FreelanceProgrammer(Programmer):
    def work(self):
        print('Начинаем работу как фрилансер.')
        self.language.build(self.project)
        self.language.execute(self.project)
    def earn(self):
        print(f'Получаем деньги за заказ {self.project}.')

# Уточненная абстракция 2
class CorporateProgrammer(Programmer):
    def work(self):
        print('Работаем в корпорации.')
        self.language.build(self.project)
        self.language.execute(self.project)
    def earn(self):
        print('Получаем зарплату в конце месяца.')

if __name__=='__main__':
    fr = FreelanceProgrammer(CPPLanguage(), 'AAA игра')
    fr.work()
    fr.earn()
    cp = CorporateProgrammer(PythonLanguage(), 'САЙТ МАГАЗИНА')
    cp.work()
    cp.earn()
    
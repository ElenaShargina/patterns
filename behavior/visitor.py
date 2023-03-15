"""
Visitor
описывает операцию с каждым объектом из некоторой структуры. Позволяет определить новую операцию,
не изменяя классы этих объектов.
Выполняемые операции зависят и от типа посещаемого объекта, и от типа посетителя.
"""
class Equipment:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    def accept(self,equipment_visitor):
        pass

class CompositeEquipment:
    def __init__(self,name):
        self.name = name
        self._items = []

    def add(self,item:Equipment):
        self._items.append(item)

    def iterator(self):
        return iter(self._items)

class EquipmentVisitor:
    def visit_chair(self,equipment):
        pass
    def visit_table(self,equipment):
        pass
    def visit_computer(self,equipment):
        pass

class EquipmentCountingVisitor(EquipmentVisitor):
    def __init__(self):
        self._total = 0

    def get_total(self, composite_equipment: CompositeEquipment):
        for i in composite_equipment.iterator():
            i.accept(self)
        return self._total

class Chair(Equipment):
    def accept(self,equipment_visitor):
        equipment_visitor.visit_chair(self)

class Table(Equipment):
    def accept(self,equipment_visitor):
        equipment_visitor.visit_table(self)

class Computer(Equipment):
    def accept(self,equipment_visitor):
        equipment_visitor.visit_computer(self)

class PriceVisitor(EquipmentCountingVisitor):
    def visit_chair(self,equipment):
        print('Counting price of chairs')
        self._total += equipment.price
    def visit_computer(self,equipment):
        print('Counting price of computer')
        self._total += equipment.price
    def visit_table(self,equipment):
        print('Counting price of table')
        self._total += equipment.price

class WeightVisitor(EquipmentCountingVisitor):
    def visit_chair(self,equipment):
        print('Counting weight of chairs')
        self._total += equipment.weight
    def visit_computer(self,equipment):
        print('Counting weight of computer')
        self._total += equipment.weight
    def visit_table(self,equipment):
        print('Counting weight of table')
        self._total += equipment.weight

class ListVisitor(EquipmentVisitor):
    def __init__(self):
        self.res = []

    def work(self,composite_equipment):
        for i in composite_equipment.iterator():
            i.accept(self)
        return ';\n'.join(self.res)

    def visit_table(self,equipment):
        self.res.append('Table: '+ ', '.join([f'{str(j)} : {equipment.__dict__[j]}' for j in equipment.__dict__]))

    def visit_chair(self,equipment):
        self.res.append('Chair: '+ ', '.join([f'{str(j)} : {equipment.__dict__[j]}' for j in equipment.__dict__]))

    def visit_computer(self,equipment):
        self.res.append('Computer: '+ ', '.join([f'{str(j)} : {equipment.__dict__[j]}' for j in equipment.__dict__]))

if __name__=='__main__':
    mytable = Table('very good table',100,20)
    mychair = Chair('old chair',50,5)
    mycomp = Computer('new notebook',200,1)
    my_workarea = CompositeEquipment('My work_area')
    my_workarea.add(mycomp)
    my_workarea.add(mychair)
    my_workarea.add(mytable)

    my_price_visitor = PriceVisitor()
    print(my_price_visitor.get_total(my_workarea))

    my_weight_visitor = WeightVisitor()
    print(my_weight_visitor.get_total(my_workarea))

    my_list_visitor = ListVisitor()
    print(my_list_visitor.work(my_workarea))

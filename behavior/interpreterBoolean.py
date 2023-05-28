"""
ИНТЕРПРЕТАТОР
для заданного языка определяет представление его грамматики, а также
интерпретатор предложений этого языка
Предложение этого языка можно представить в виде абстрактного синтаксического дерева.

"""
class Context:
    def __init__(self):
        self.values = {}

    def look_up(self, name):
        if name in self.values:
            return self.values[name]
        else:
            raise Exception(f'No variable {name} is assigned in current context.')

    def assign(self, a, b:bool):
        self.values[a.name] = b
        pass

class BooleanExpression:
    def evaluate(self,context:Context):
        pass
    def replace(self, value, a):
        pass
    def copy(self):
        pass

# nonterminal expression
class AndExpression(BooleanExpression):
    def __init__(self,a:BooleanExpression,b:BooleanExpression):
        self.a = a
        self.b = b

    def evaluate(self,context:Context):
        return self.a.evaluate(context) & self.b.evaluate(context)

    def copy(self):
        return AndExpression(self.a.copy(), self.b.copy())

    def replace(self, name, a:BooleanExpression):
        return AndExpression(self.a.replace(name,a),self.b.replace(name,a))

# nonterminal expression
class OrExpression(BooleanExpression):
    def __init__(self,a:BooleanExpression,b:BooleanExpression):
        self.a = a
        self.b = b

    def evaluate(self,context:Context):
        return self.a.evaluate(context) or self.b.evaluate(context)

    def replace(self, name, a:BooleanExpression):
        return OrExpression(self.a.replace(name,a),self.b.replace(name,a))

class NotExpression(BooleanExpression):
    def __init__(self,a:BooleanExpression):
        self.a = a

    def evaluate(self,context:Context):
        return not self.a.evaluate((context))

    def replace(self, name, a:BooleanExpression):
        return NotExpression(self.a.replace(name,a))

# terminal expression
# 'true' | 'false'
class ConstSequence(BooleanExpression):
    def __init__(self):
        pass

# именованная переменная
# 'A' | 'B' | 'C' | ...
class VariableExpression(BooleanExpression):
    def __init__(self, name):
        self.name = name

    def evaluate(self,context:Context):
        return context.look_up(self.name)

    def copy(self):
        return VariableExpression(self.name)

    def replace(self, name, a:BooleanExpression):
        if (name == self.name):
            return a.copy()
        else:
            return VariableExpression(name)

if __name__=='__main__':
    c = Context()
    x = VariableExpression('X')
    y = VariableExpression('Y')

    exp = AndExpression(NotExpression(x),y)

    c.assign(x,False)
    c.assign(y,True)

    print(exp.evaluate(c))

    z = VariableExpression('Z')
    new_exp = exp.replace('Y',z)
    print(new_exp)
    c.assign(z,False)

    print(new_exp.evaluate(c))
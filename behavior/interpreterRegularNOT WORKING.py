"""
ИНТЕРПРЕТАТОР
для заданного языка определяет представление его грамматики, а также
интерпретатор предложений этого языка
Предложение этого языка можно представить в виде абстрактного синтаксического дерева.

expression ::=literal | alternation | sequence | reperirion | '(' expression ')'
alternation ::= expression '|' expression
sequence ::= expression '&' expression
repetition ::= expression '*'
literal ::= 'a' | 'b' | 'c'| ... {'a' | 'b' |...}*
где expression это начальный символ, а literal - терминальный символ, определяющий простые слова
"""
class RegularExpression:
    def match(self, input_state):
        pass

    def big_match(self,another):
        print(f'Nodes: {another}')
        result = self.match([another,])
        print(f'inner_state: {result}')
        answer = False
        for i in result:
            if i == []:
                answer = True
                break
        return answer

# terminal expression
# literal ::= 'a' | 'b' | 'c'| ... {'a' | 'b' |...}*
class LiteralExpression(RegularExpression):
    def __init__(self,value):
        self.value = value

    def match(self, input_state):
        result_state = []
        for  i in input_state:
            if i[0].match(self.value):
                result_state.append(i[1:])
        return result_state

# nonterminal expression
# sequence ::= expression '&' expression
class SequenceExpression(RegularExpression):
    def __init__(self,a:RegularExpression,b:RegularExpression):
        self.a = a
        self.b = b

    def match(self, input_state):
        result_state = []


# nonterminal expression
class AlternationExpression(RegularExpression):
    def __init__(self,a:RegularExpression, b:RegularExpression):
        self.a = a
        self.b = b

    def match(self, input_state):
        pass

# nonterminal expression
class RepetitionSequence(RegularExpression):
    def __init__(self, a:RegularExpression):
        self.a = a

    def match(self, input_state):
        result_state = []
        for i in input_state:
            print(i)
            stop = False
            while stop != True:
                if self.a.match([[i[0],]]):
                    result_state.append(i[1:])
                else:
                    stop = True
        return result_state

class Node:
    def __init__(self,value):
        self.value = value

    def match(self,another):
        if self.value == another:
            return True
        else:
            return False
    @staticmethod
    def construct(s):
        res = list(map(lambda x: Node(x), s.split(' ')))
        return res

    def __repr__(self):
        return self.value


if __name__=='__main__':
    # exp = SequenceExpression(LiteralExpression('dog'),LiteralExpression('cat'))
    # exp = RepetitionSequence(LiteralExpression('dog'))
    exp = LiteralExpression('dog')
    print(exp.big_match(Node.construct('dog')))
    print(exp.big_match(Node.construct('dog fff')))
    print(exp.big_match(Node.construct('fff')))

    # exp = RepetitionSequence(LiteralExpression('dog'))
    # print(exp.big_match(Node.construct('dog')))
    # print(exp.big_match(Node.construct('dog fff')))
    # print(exp.big_match(Node.construct('dog dog')))
    # print(exp.big_match(Node.construct('fff')))
import unittest

def interpret(expression):
    tokens = tokenize(expression)
        
    while '(' in tokens:
        start = tokens.index('(')
        end = tokens.index(')', start)
        subexpression = tokens[start + 1:end]
        result = interpret(' '.join(subexpression))
        tokens = tokens[:start] + [str(result)] + tokens[end + 1:]
    
    result = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == '+':
            result += operand 
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
    return result
    
def tokenize(expression):
    return expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(',' ( ').replace(')', ' ) ').split()

class TestIntrepreter(unittest.TestCase):
    def test_addition(self):    
        self.assertEqual(interpret("3 + 5"), 8)
        
    def test_subtraction(self):
        self.assertEqual(interpret("7 - 2"), 5)
        
    def test_multiplication(self):
        self.assertEqual(interpret("(4 + 3) * 2"), 14)
        
    def test_division(self):
        self.assertEqual(interpret("(6 + 2) / 2"), 4)
        
if __name__ == "__main__":
    unittest.main()
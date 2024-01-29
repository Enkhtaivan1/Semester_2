import unittest

def interpret(expression):
    tokens = tokenize(expression)

    while '*' in tokens:
        index = tokens.index('*');
        product = int(tokens[index - 1]) * int(tokens[index + 1]);
        tokens[index - 1] = str(product);
        del tokens[index:index + 2];

    while '/' in tokens:
        index = tokens.index('/');
        product = int(tokens[index - 1] / tokens[index + 1]);
        tokens[index - 1] = str(product);
        del tokens[index:index + 2];

    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand

    return result

def tokenize(expression):
    return expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()

class TestInterpreter(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(interpret("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(interpret("7 - 5"), 2)

    def test_complex_expression(self):
        self.assertEqual(interpret("(2 * 4) + 4"), 12)


if __name__ == "__main__":
    unittest.main()

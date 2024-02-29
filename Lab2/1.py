class ProductionRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class CFG:
    def __init__(self, start_symbol):
        self.start_symbol = start_symbol
        self.production_rules = []

    def add_rule(self, left, right):
        self.production_rules.append(ProductionRule(left, right))


def initialize_palindrome_cfg():
    cfg = CFG('S') # 'S' n ehleliin symbol(temdeg)
    cfg.add.rule('S', ['a', 'S', 'a'])
    cfg.add.rule('S', ['b', 'S', 'b'])
    cfg.add.rule('S', ['a'])
    cfg.add.rule('S', ['b'])
    cfg.add.rule('S', [''])
    
from rply import ParserGenerator
from ast import Add, Sub, Mul, Div, Number, Print

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
        'FLOAT', 'INT', 'OPEN_PARENS', 'CLOSE_PARENS',
        'PLUS', 'MINUS', 'MUL', 'DIV',
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)

env = []

class ExpressionParser:
        
    @pg.production('expression : FLOAT')
    @pg.production('expression : INT')
    def expression_number(p):
        number = p[0]
        if number.gettokentype() == 'FLOAT':
            return Number(float(number.getstr()))
        return Number(int(number.getstr()))
        
    @pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    def expression_parens(p):
        return p[1]    

    @pg.production('expression : expression PLUS expression')
    @pg.production('expression : expression MINUS expression')
    @pg.production('expression : expression MUL expression')
    @pg.production('expression : expression DIV expression')
    def expression_binop(p):
        pass
        left = p[0]
        right = p[2]
        if p[1].gettokentype() == 'PLUS':
            return Add(left, right)
        elif p[1].gettokentype() == 'MINUS':
            return Sub(left, right)
        elif p[1].gettokentype() == 'MUL':
            return Mul(left, right)
        elif p[1].gettokentype() == 'DIV':
            return Div(left, right)
        else:
            raise AssertionError('Invalid operation!')    

    def parse(self, tokens):
        parser = pg.build()
        parsed_code = parser.parse(tokens)
        return parsed_code.eval()
            

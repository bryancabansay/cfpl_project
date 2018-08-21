from rply import ParserGenerator
from ast import Assignment
from ast import Add, Sub, Mul, Div, Number
from global_vars import *

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
        'FLOAT', 'INT', 'CHAR', 'BOOL', 'OPEN_PARENS', 'CLOSE_PARENS',
        'PLUS', 'MINUS', 'MUL', 'DIV', 'EQUAL', 'IDENTIFIER'
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
)

class AssignParser:
        
    @pg.production('var_assign : IDENTIFIER EQUAL expression')
    def var_decl(p):

        return Assignment(
            identifier = p[0].getstr(),
            value      = p[2]
        )
    
    @pg.production('expression : INT')
    @pg.production('expression : FLOAT')
    @pg.production('expression : CHAR')
    @pg.production('expression : BOOL')
    def number(p):
        if p[0].gettokentype() == "INT":
            return int(p[0].getstr())
        if p[0].gettokentype() == "FLOAT":
            return float(p[0].getstr())
        if p[0].gettokentype() == "CHAR":
            return float(p[0].getstr())
        if p[0].gettokentype() == "BOOL":
            value = p[0].getstr().replace("\"","")
            if value == "TRUE":
              return True
            else:
              return False

    @pg.production('expression : math_expression')
    def math_expression(p):
        return p[0]

    @pg.production('math_expression : number')
    def number(p):
        return p[0]

    @pg.production('math_expression : IDENTIFIER')
    def identifier(p):
        return Number(variables[p[0].getstr()])

    @pg.production('number : FLOAT')
    @pg.production('number : INT')
    def expression_number(p):
        number = p[0]
        if number.gettokentype() == 'FLOAT':
            return Number(float(number.getstr()))
        return Number(int(number.getstr()))
        
    @pg.production('math_expression : OPEN_PARENS math_expression CLOSE_PARENS')
    def expression_parens(p):
        return p[1]    

    @pg.production('math_expression : math_expression PLUS math_expression')
    @pg.production('math_expression : math_expression MINUS math_expression')
    @pg.production('math_expression : math_expression MUL math_expression')
    @pg.production('math_expression : math_expression DIV math_expression')
    def expression_binop(p):
        left  = p[0]
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
        parser      = pg.build()
        parsed_code = parser.parse(tokens)
        return parsed_code.eval()


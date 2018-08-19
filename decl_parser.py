from rply import ParserGenerator
from ast import Assignment

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
        'VAR', 'IDENTIFIER', 'AS_INT', 'AS_FLOAT', 'EQUAL',
        'INT', 'FLOAT'
    ]
)

class DeclarationParser:
        
    @pg.production('var_decl : VAR IDENTIFIER EQUAL number data_type')
    def var_decl(p):
        return Assignment(p[1].getstr(), p[3][0].getstr(), p[4][0].gettokentype())

    @pg.production('number : INT')
    @pg.production('number : FLOAT')
    def number(p):
        return p

    @pg.production('data_type : AS_INT')
    @pg.production('data_type : AS_FLOAT')
    def data_type(p):
        return p 

    def parse(self, tokens):
        parser = pg.build()
        parsed_code = parser.parse(tokens)
        return parsed_code.eval()
            

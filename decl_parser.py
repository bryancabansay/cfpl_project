from rply import ParserGenerator
from ast import Assignment

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    [
        'VAR', 'IDENTIFIER', 'AS_INT', 'AS_FLOAT', 'EQUAL',
        'INT', 'FLOAT', 'COMMA', 'AS_CHAR', 'AS_BOOL', 'CHAR', 'BOOL'
    ]
)

class DeclarationParser:
        
    @pg.production('var_decl : VAR assignment data_type')
    def var_decl(p):
        return Assignment(
            data      = p[1],
            data_type = p[2].gettokentype()
        )

    @pg.production('number : INT')
    @pg.production('number : FLOAT')
    @pg.production('number : CHAR')
    @pg.production('number : BOOL')
    def number(p):
        return p[0]

    @pg.production('data_type : AS_INT')
    @pg.production('data_type : AS_FLOAT')
    @pg.production('data_type : AS_CHAR')
    @pg.production('data_type : AS_BOOL')
    def data_type(p):
        return p[0]

    @pg.production('assignment : IDENTIFIER')
    def identifier_only(p):
        data = dict()
        data['identifier'] = p[0].getstr()
        data['value']      = "0"
        lst                = []
        lst.append(data)
        return lst

    @pg.production('assignment : IDENTIFIER EQUAL number')
    def identifier_with_number(p):
        data = dict()
        data['identifier'] = p[0].getstr()
        data['value']      = p[2].getstr()
        lst = []
        lst.append(data)
        return lst

    @pg.production('assignment : assignment COMMA IDENTIFIER')
    def another_identifier(p):
        data = dict()
        data['identifier'] = p[2].getstr()
        data['value']      = "0"
        lst = p[0]
        lst.append(data.copy())
        return lst

    @pg.production('assignment : assignment COMMA IDENTIFIER EQUAL number')
    def another_identifier(p):
        data = dict()
        data['identifier'] = p[2].getstr()
        data['value']      = p[4].getstr()
        lst                = p[0]
        lst.append(data.copy())
        return lst

    def parse(self, tokens):
        parser      = pg.build()
        parsed_code = parser.parse(tokens)
        return parsed_code.eval()


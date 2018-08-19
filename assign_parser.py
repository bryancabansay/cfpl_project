from rply import ParserGenerator
from ast import Assignment

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

    def parse(self, tokens):
        parser      = pg.build()
        parsed_code = parser.parse(tokens)
        return parsed_code.eval()


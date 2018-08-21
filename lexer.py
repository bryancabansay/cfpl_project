from rply import LexerGenerator

lg = LexerGenerator()

lg.add('FLOAT', r'[-+]?\d*\.\d+')
lg.add('INT', r'[-+]?[0-9]+')
lg.add('OUTPUT', r'OUTPUT:')
lg.add('PRINT', r'print')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('NEW_LINE', r'\n')

# Variable Declaration tokens
lg.add('VAR', r'VAR')
lg.add('EQUAL', r'=')
lg.add('CHAR', r'\'[a-zA-Z]{1}\'')
lg.add('BOOL', r'("TRUE"|"FALSE")')
lg.add('COMMA', r',')
lg.add('AS_INT', r'AS INT')
lg.add('AS_FLOAT', r'AS FLOAT')
lg.add('AS_CHAR', r'AS CHAR')
lg.add('AS_BOOL', r'AS BOOL')

lg.add('IDENTIFIER', r'[A-Za-z][A-Za-z0-9_]*')

lg.ignore('\s+')

lexer = lg.build()
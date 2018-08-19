from rply import LexerGenerator

lg = LexerGenerator()

lg.add('OUTPUT', r'OUTPUT:')
lg.add('PRINT', r'print')
lg.add('FLOAT', r'[-+]?\d*\.\d+')
lg.add('INT', r'[-+]?[0-9]+')
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')
lg.add('MUL', r'\*')
lg.add('DIV', r'/')
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('NEW_LINE', r'\n')
lg.add('VAR', r'VAR')
lg.add('AS_INT', r'AS INT')
lg.add('EQUAL', r'=')
lg.add('AS_INT', r'AS INT')
lg.add('AS_FLOAT', r'AS FLOAT')
lg.add('IDENTIFIER', r'[A-Za-z][A-Za-z0-9_]*')

lg.ignore('\s+')

lexer = lg.build()
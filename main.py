from lexer import lexer
from decl_parser import DeclarationParser
from global_vars import *

text_input = """
VAR XYZ = 123.0 AS FLOAT
VAR test = 321 AS INT
"""

parser = DeclarationParser()

for text in text_input.splitlines():
    if text:
        tokens = lexer.lex(text)    
        # for token in tokens:
        #     print(token)
        parser.parse(tokens)
        print(variables)
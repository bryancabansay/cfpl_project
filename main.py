from lexer import lexer
from decl_parser import DeclarationParser
from global_vars import *

text_input = """
VAR abc, b, c AS INT
VAR x, w_23='w' AS CHAR
VAR t="TRUE", f = "FALSE" AS BOOL
"""

parser = DeclarationParser()

for text in text_input.splitlines():
    if text:
        tokens = lexer.lex(text)    
        # for token in tokens:
        #     print(token)
        parser.parse(tokens)
        print(variables)
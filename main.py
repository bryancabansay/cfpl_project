from lexer         import lexer
from decl_parser   import DeclarationParser
from assign_parser import AssignParser
from global_vars   import *

text_input = """
VAR abc, b, c AS INT
VAR x, w_23='x' AS CHAR
VAR t="TRUE", f = "FALSE", z AS BOOL
abc = 1111
t = "FALSE"
z = "TRUE"
t = "TRUE"
"""

dcl_parser = DeclarationParser()
ass_parser = AssignParser()

for text in text_input.splitlines():
    if text:
        tokens = lexer.lex(text)
        if "VAR" in text:
            # for token in tokens:
            #     print(token)
            dcl_parser.parse(tokens)
            print(variables)
        else:
            # for token in tokens:
            #     print(token)
            ass_parser.parse(tokens)
            print(variables)
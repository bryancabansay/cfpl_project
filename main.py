from lexer         import lexer
from decl_parser   import DeclarationParser
from assign_parser import AssignParser
from global_vars   import *

text_input = """
VAR xyz, abc=100 AS INT
xyz= ((100 *5)/10 + 10) * -1
xyz = abc
xyz = (100 *5)
abc = -1
abc = xyz + 1
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
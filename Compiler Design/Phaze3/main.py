#Ahmad Asadi 99463107
#Golestan Mohammadi 97463150
from myLexer import *
from myParser import *

lexer = lex()
parser = yacc()

ast = parser.parse('2 * 3 + 4 * (5 - x)')
print(ast)
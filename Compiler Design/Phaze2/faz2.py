#Ahmad Asadi 99463107
#Golestan Mohammadi 97463150
import ply.lex as lex
 
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'do' : 'DO',
    'while' : 'WHILE',
    'boolean' : 'BOOLEAN',
    'int' : 'INT',
    'double' : 'DOUBLE',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'char' : 'CHAR',
    'class' : 'CLASS',
    'true' : 'TRUE_BOOOLEAN',
    'false' : 'FALSE_BOOLEAN',
    'null' : 'NULL',
    'new' : 'NEW',
    'private' : 'PPRIVATE',
    'public' : 'PUBLIC',
    'extends' : 'extends',
    'protected' : 'PROTECTED',
    'return' : 'RETURN',
    'static' : 'STATIC',
    'this' : 'THIS',
    'void' : 'VOID',
    'main' : 'MAIN',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'switch' : 'SWITCH',
    'case' : 'CASE',
    'default' : 'DEFAULT',
    'for' : 'FOR',
    'println' : 'PRINTLN',
    'enum' : 'ENUM',
    'import' : 'IMPORT',
    'or' : 'OR',
    'and' : 'AND',
}

tokens = [
    'PRINT',
    'DECREMENT',
    'ID_ERROR',
    'NUM_ERROR',
    'NUMBER',
    'ID',
    'INCREMENT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULUS',
    'OPEN_PAR',
    'CLOSE_PAR',
    'LBRACKET',
    'RBRACKET',
    'ASSIGN_OP',
    'EQUAL_OP',
    'LOGICAL_NOT',
    'NOT_EQUAL_OP',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_OR_EQUAL_TO',
    'LESS_THAN_OR_EQUAL_TO',
    'DOLLAR_SIGN',
    'SEMICOLON',
    'COMMAS',
    'DOT'
] + list(reserved.values())
 
t_DECREMENT = r'\-\-'
t_INCREMENT = r'\+\+'
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MODULUS = r'\%'
t_OPEN_PAR  = r'\('
t_CLOSE_PAR  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUAL_OP = r'\='
t_LOGICAL_NOT = r'\!'
t_NOT_EQUAL_OP = r'\!\='
t_ASSIGN_OP = r'\=\='
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LOGICAL_AND = r'\&\&'
t_LOGICAL_OR = r'\|\|'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_OR_EQUAL_TO = r'\>\='
t_LESS_THAN_OR_EQUAL_TO = r'\<\='
t_DOLLAR_SIGN = r'\$'
t_SEMICOLON = r'\;'
t_COMMAS = r'\,'
t_DOT = r'\.'

def t_PRINT(t):
    r'System.out.println'
    return t

def t_ID_ERROR(t):
    r'[0-9][0-9]*[a-zA-Z_][a-zA-Z_0-9]*|_[a-zA-Z_0-9]*|-[a-zA-Z_]+[a-zA-Z_0-9]*|[a-zA-Z_0-9]+-[a-zA-Z_0-9]*|-[0-9][a-zA-Z_]+'
    t.type = 'ID_ERROR'
    return t

def t_NUM_ERROR(t):
    r'[0][0-9]*'
    return t

def t_NUMBER(t):
    r'(-1|-2|-3|-4|-5|-6|-7|-8|-9|1|2|3|4|5|6|7|8|9)[0-9]*'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
t_ignore  = ' \t'
 
def t_error(t):
    t.type = "undifined char"
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

def getBigestLen(mylist):
    num = 0
    for temp in mylist:
        if len(temp) >= num:
            num = len(temp)
    return num

def printTable(list1, list2):
    str = ""
    for count in range(len(list1)):
        str += list1[count]
        
        for count2 in range(getBigestLen(list1) - len(list1[count])):
            str += " "
        str += "|"
        str += list2[count]
        str += "\n"
        str += "-------------------------------------"
        str += "\n"
    return str

data2 = '''
while(id == unix) {
    if (not impl) then {
        num = num % 10
    while (false) {
        -print()
    }
} != = == ! ++ --
&&false
System.out.println
[] .
-5
import
'''

def runi(data):
    lexer = lex.lex()
    
    lexer.input(data)

# Tokenize
    list1 = []
    list2 = []
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        list1.append(tok.type)
        list2.append(str(tok.value))

    str3 = printTable(list1, list2)
    return str3

#runi()


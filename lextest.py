import ply.lex as lex
input_file = open("newfile.txt","r")

tokens = (
    'DIGIT',
    'NUMBER',
    'GLOBAL_VARIABLE_ID',
    'LOCAL_VARIABLE_ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'MODULE',
    'COMMA',
    'RET',
    'ALLOCA',
    'ALIGN',
    'STORE',
    'LOAD',
    'MUL',
    'I32',
    'p_I32',
    'NSW' #poisoned variable
)

t_DIGIT = r'[0-9]'  #riconosce un digit

#IGNORE
t_ignore_TAB = r' \t'
t_ignore_COMMENT = r'\#.*'
t_ignore_SPACE = r'\ +'

##Punteggiatura
t_COMMA = r'\,'

##Operazioni
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MODULE = r'\%'
t_EQUALS = r'\='

#LLVM IR MOST USED FUNCTION
t_ALLOCA = r'alloca'
t_STORE = r'store'
t_LOAD = r'load'
t_ALIGN = r'align'
t_MUL = r'mul'
t_RET = r'ret'

#LLVM IR VARIABLES TYPES
t_I32 = r'i32'
t_p_I32 = r'i32\*'

#LLVM IR OTHERS
t_NSW = r'nsw'

def t_LOCAL_VARIABLE_ID(t):
    r'%[0-9]+'
    t.value = int(t.value[1:len(t.value)])
    return t

def t_GLOBAL_VARIABLE_ID(t):
    r'@[0-9]+'
    t.value = int(t.value[1:len(t.value)])
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def eof(t):
    return None

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()
lexer.input(input_file.read())

input_file.close()

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

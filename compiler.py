import string
import ply.lex as lex
import ply.yacc as yacc

programm = [100]

## SUPPORT FUNCTIONS
def VAR_decoder(string,addend_obj):
    addend_obj.type = string[0]
    addend_obj.val = int(string[1:])

## INSTRUCTION CLASS

class info_instruction():
    def __init__(self,instr):
        self.operation = instr[0]
        self.var0 = instr[1]
        self.var1 = instr[2]
        self.var2 = instr[3]
        self.var3 = instr[4]


## INPUT MAKER
#def input_maker(c_programm)


input_file = open("newfile.txt","r")

##LEXER

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
    'LPAR',
    'RPAR',
    'COMMA',
    'SEMICOLON',
    'OPERATION',
    'VARTYPE',
    'NSW' #poisoned variable
)

t_DIGIT = r'[0-9]'  #riconosce un digit

#IGNORE
t_ignore_TAB = r' \t'
t_ignore_COMMENT = r'\#.*'
t_ignore_SPACE = r'\ +'
t_ignore_NSW = r'nsw'

##Punteggiatura
t_COMMA = r'\,'
t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMICOLON = r';'

##Operazioni
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MODULE = r'\%'
t_EQUALS = r'\='

#LLVM IR MOST USED FUNCTION
t_OPERATION = r'[a-z][a-z]+'


#LLVM IR VARIABLES TYPES
t_VARTYPE = r'[a-z][\d+]+\**'

#LLVM IR OTHERS

def t_LOCAL_VARIABLE_ID(t):
    r'%[0-9]+'
    #t.value = int(t.value[1:len(t.value)])
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


##PARSER##PARSER##PARSER##PARSER##PARSER##PARSER##PARSER##PARSER

##SUPPORT CLASSES

def VAR_decoder(string,addend_obj):
    addend_obj.type = string[0]
    addend_obj.val = int(string[1:])

programm = []
instr00 = [0,0,0,0,0]
input_file = open("newfile.txt","r")

def p_error(p):
    print("ERROR")

def p_instr0(p):
    '''instr0 : instr1
              | func '''

def p_instr1(p):
    'instr1 : operand1 EQUALS func'

def p_func(p):
    '''func : OPERATION operand0
            | OPERATION operand1'''
    instr00[0] = p[1]

def p_operand0(p):  #operando per variabili non per costanti
    '''operand0 : operand3 COMMA operand3
                | operand4 COMMA operand3
                | operand3 COMMA operand4'''
    p[0] = p[1] + p[3]
    instr00[3] = p[1]
    instr00[4] = p[3]

def p_operand1(p):
    '''operand1 : operand3
                | operand4 '''
    p[0] = p[1]
    
    if(instr00[1] == 0):
        instr00[1] = p[1]
    else:
        instr00[2] = p[1]

def p_operand3(p):
    '''operand3 : VARTYPE LOCAL_VARIABLE_ID
                | VARTYPE NUMBER '''
    p[0] = p[1] + str(p[2])  ## la funzione str converte int in string

def p_operand4(p):
    '''operand4 : VARTYPE
                | LOCAL_VARIABLE_ID
                | NUMBER '''
    p[0] = str(p[1])


parser = yacc.yacc()
tmpstring = input_file.readline()

while (tmpstring != ";;"):
    
    parser.parse(tmpstring)
    tmpstring = input_file.readline()
    programm.append(instr00)    
    instr00 = [0,0,0,0,0]

input_file.close()
print("\n#########################################")
for j in range(len(programm)):
    print(programm[j])



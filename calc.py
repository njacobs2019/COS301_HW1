#-------------------------------------------------------------
# Example from PLY docs.
# calc.py
# 
# A simple calculator with variables.  This is from O'Reilly's
# "Lex and Yacc", p. 63.
#-------------------------------------------------------------

import sys
sys.path.insert(0, "../..")
if sys.version_info[0] >=3:
    raw_input = input

# This defines non-literal tokens
# the tokens
tokens = ('NAME', 'NUMBER')

# This defines literal tokens
# simple tokens
literals = ['=', '+', '-', '*', '/', '(', ')', '%']

# tokens
# REGEX of what defines a name
# objects that start with t_ are special
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'  # needs to have this name to match the tokens list

# The docstring defines the REGEX that corresponds to the token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   # originally set to part of input string that matches the regex
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")   # helps for reporting syntax errors

# for skipping over illegal characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build lexer
import ply.lex as lex
lex.lex()

# Parsing rules

# left and right means evaluate going from that direction
precedence = (  ('left', '+', '-'),   # lowest precedence
                ('left', '*', '/', '%'),
                ('right', 'UMINUS'))  # highest


# dictionary of names
names = {}

# p_ is special
def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '%' expression'''
    # LHS is at position 0, then increments from there
    if p[2] == '+':
        p[0] = p[1]+p[3]
    elif p[2] == '-':
        p[0] = p[1]-p[3]
    elif p[2] == '*':
        p[0] = p[1]*p[3]
    elif p[2] == '/':
        p[0] = p[1]/p[3]
    elif p[2] == '%':
        p[0] = p[1]%p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0]=0

def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()
while 1:
    try:
        s = raw_input('calc > ')  # prints prompt and get user input
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)




# Nicholas Jacobs
# UMaine COS 301 - Programming Languages
# HW1

# This code is a derivation of:
#-------------------------------------------------------------
# Example from PLY docs.
# calc.py
# 
# A simple calculator with variables.  This is from O'Reilly's
# "Lex and Yacc", p. 63.
#-------------------------------------------------------------
from vector import vector
import ply.lex as lex
import ply.yacc as yacc

# This defines non-literal tokens
# the tokens
tokens = ('NAME', 'NUMBER', 'DIV')

# This defines literal tokens
# simple tokens
literals = ['=', '+', '-', '*', '/', '(', ')', '%', ',']

# tokens
# REGEX of what defines a name
# objects that start with t_ are special
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'  # needs to have this name to match the tokens list

t_DIV = r'//'

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
lex.lex()

# Parsing rules

# left and right means evaluate going from that direction
precedence = (  ('left', '+', '-'),   # lowest precedence
                ('left', '*', '/', '%', 'DIV'),
                ('right', 'UMINUS'))  # highest

# dictionary of names
names = {}

# p_ is special
def p_statement_assign_s(p):
    'statement : NAME "=" s_expression'
    names[p[1]] = p[3]

def p_statement_expr_s(p):
    'statement : s_expression'
    print(p[1])

def p_statement_assign(p):
    'statement : NAME "=" vec'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : vec'
    print(p[1])

def p_vec_binop(p):
    '''vec : vec "+" vec
           | vec "-" vec
           | vec "*" vec
           | vec "/" vec
           | vec "%" vec
           | vec DIV vec'''
    if p[2] == "+":
        p[0] = p[1].add(p[3])
    elif p[2] == "-":
        p[0] = p[1].subtract(p[3])
    elif p[2] == "*":
        p[0] = p[1].multiply(p[3])
    elif p[2] == "/":
        p[0] = p[1].divide(p[3])
    elif p[2] == "%":
        p[0] = p[1].mod(p[3])
    elif p[2] == "//":
        p[0] = p[1].div(p[3])

def p_vec_uminus(p):
    "vec : '-' vec %prec UMINUS"
    p[0] = p[2].negate()

def p_vec_group(p):
    "vec : '(' vec ')'"
    p[0] = p[2]

def p_vec_empty(p):
    "vec : '(' ')'"
    p[0] = vector()

def p_vec_end1(p):
    "vec : Lvec s_expression ')'"
    p[0] = p[1].append(p[2])

def p_vec_end2(p):
    "vec : Lvec ')'"
    p[0] = p[1]

#Left vector
def p_vec_start(p):
    "Lvec : '(' s_expression ','"
    p[0] = vector([p[2]])

def p_vec_continue(p):
    "Lvec : Lvec s_expression ','"
    p[0] = p[1].append(p[2])

def p_expression_binop(p):
    '''s_expression : s_expression '+' s_expression
                  | s_expression '-' s_expression
                  | s_expression '*' s_expression
                  | s_expression '/' s_expression
                  | s_expression '%' s_expression
                  | s_expression DIV s_expression'''
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
    elif p[2] == '//':
        p[0] = p[1]//p[3]

def p_expression_uminus(p):
    "s_expression : '-' s_expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "s_expression : '(' s_expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "s_expression : NUMBER"
    p[0] = p[1]

def p_vec_name(p):
    "vec : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0]=0

def p_expression_name(p):
    "s_expression : NAME"
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

yacc.yacc()

if __name__ == "__main__":
    while 1:
        try:
            s = input('')  # prints prompt and get user input
        except EOFError:
            break
        if not s:
            continue
        yacc.parse(s)
import ply.lex as lex
import ply.yacc as yacc
import arithmetic as arm

# Non-literal token definitions
tokens = ('NAME', 'NUMBER', 'DIV')

# Literal token definitions
literals = ['=', '+', '-', '*', '/', '(', ')', '%', ',']

# Regular expression of what defines a name
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Regular expression of what defines DIV operator
t_DIV = r'//'

# Definition of a number
# The docstring defines the regular expression that corresponds to the token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Characters to ignore
t_ignore = " \t"

# Definition of newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")   # helps for reporting syntax errors

# For skipping over illegal characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build lexer
lex.lex()

# Parsing rules
# left and right means evaluate going from that direction
precedence = (  ('left', '+', '-'),                # lowest precedence
                ('left', '*', '/', '%', 'DIV'),
                ('right', 'UMINUS'))               # highest precedence

# Dictionary of names
# This stores variable assignment during execution to memory
names = {}

# Grammar and logic for assignment
def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

# Grammar and logic for identity of expressions
def p_statement_expr(p):
    'statement : expression'
    print(p[1])

# Grammar and logic for binary operations
def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '%' expression
                  | expression DIV expression'''
    # Need to make sure it checks the types of the variables
    # LHS is at position 0, then increments from there
    if p[2] == '+':
        p[0] = arm.add(p[1],p[3])
    elif p[2] == '-':
        p[0] = arm.subtract(p[1],p[3])
    elif p[2] == '*':
        p[0] = arm.multiply(p[1],p[3])
    elif p[2] == '/':
        p[0] = arm.divide(p[1],p[3])
    elif p[2] == '%':
        p[0] = arm.mod(p[1],p[3])
    elif p[2] == '//':
        p[0] = arm.div(p[1],p[3])

# Grammar and logic for negation
def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = arm.negate(p[2])

# Grammar and logic for grouping with parenthesis
def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

# Grammar and logic for parsing a number
def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

# Grammar and logic for parsing a variable name
def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0]=0

# Grammar and logic for converting vector/list to expression
def p_expression_vec(p):
    "expression : vec"
    p[0] = p[1]

# Vector/list productions

# Grammar and logic for empty vectors
def p_vec_empty(p):
    "vec : '(' ')'"
    p[0] = tuple()

# Grammar and logic for terminating a vector
def p_vec_end1(p):
    "vec : Lvec expression ')'"
    assert isinstance(p[1],tuple), "List must be a tuple"
    assert isinstance(p[2], int) or isinstance(p[2],float), "Lists can only contain ints and floats"
    p[0] = p[1] + (p[2],)

# Grammar and logic for terminating a vector
def p_vec_end2(p):
    "vec : Lvec ')'"
    assert isinstance(p[1],tuple), "List must be a tuple"
    p[0] = p[1]

#Left vector
# Beginning of vector before it terminates

# Grammar and logic for starting a vector
def p_vec_start(p):
    "Lvec : '(' expression ','"
    assert isinstance(p[2], int) or isinstance(p[2],float), "Lists can only contain ints and floats"
    p[0] = (p[2],)

# Grammar and logic for continuing a vector
def p_vec_continue(p):
    "Lvec : Lvec expression ','"
    assert isinstance(p[1],tuple), "List must be a tuple"
    assert isinstance(p[2], int) or isinstance(p[2],float), "Lists can only contain ints and floats"
    p[0] = p[1] + (p[2],)

# Grammar and logic for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at {p.value}")
    else:
        print("Syntax error at EOF")

# Create the parser
yacc.yacc()

# Loop for user input
if __name__ == "__main__":
    while True:
        try:
            s = input('')  # prints prompt and get user input
        except EOFError:
            break
        if not s:
            continue
        yacc.parse(s)
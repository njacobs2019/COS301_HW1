# This file defines the logic and calculations for the calculator

# Adds the two expressions
def add(a,b):    
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]+x[1] for x in zip(a,b)])
    return a+b

# Subtracts the two expressions
def subtract(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]-x[1] for x in zip(a,b)])
    return a-b

# Multiplies the two expressions
def multiply(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]*x[1] for x in zip(a,b)])
    return a*b

# Divides the two expressions
def divide(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]/x[1] for x in zip(a,b)])
    return a/b

# Applies modulo to the two expressions
def mod(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]%x[1] for x in zip(a,b)])
    return a%b

# Applies integer division to the two expressions
def div(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]//x[1] for x in zip(a,b)])
    return a//b

# Negates the expression
def negate(a):
    is_expression(a)
    if isinstance(a,tuple):
        return tuple([-1*x for x in a])
    return -1*a

# Checks that a and be are compatible types
def compatible_type(a,b):
    # Compatible types:
    # int a, int b
    # int a, float b
    # float a, int b
    # float a, float b
    # tuple a, tuple b
    if isinstance(a,int) and isinstance(b,int):
        return True
    if isinstance(a,int) and isinstance(b,float):
        return True
    if isinstance(a,float) and isinstance(b,int):
        return True
    if isinstance(a,float) and isinstance(b,float):
        return True
    if isinstance(a,tuple) and isinstance(b,tuple):
        if len(a)==len(b):
            return True
    return False

# Checks that x is a valid expression.  If not, throws an error
def is_expression(x):
    assert isinstance(x, int) or isinstance(x, float) or isinstance(x, tuple), "Error:  invalid expression"
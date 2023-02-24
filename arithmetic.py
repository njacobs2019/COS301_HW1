import sys

def add(a,b):    
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]+x[1] for x in zip(a,b)])
    return a+b

def subtract(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]-x[1] for x in zip(a,b)])
    return a-b

def multiply(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]*x[1] for x in zip(a,b)])
    return a*b

def divide(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]/x[1] for x in zip(a,b)])
    return a/b

def mod(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]%x[1] for x in zip(a,b)])
    return a%b

def div(a,b):
    is_expression(a)
    is_expression(b)
    assert compatible_type(a,b), "Expressions are incompatible types"

    if isinstance(a,tuple):
        return tuple([x[0]//x[1] for x in zip(a,b)])
    return a//b

def negate(a):
    is_expression(a)
    if isinstance(a,tuple):
        return tuple([-1*x for x in a])
    return -1*a

def compatible_type(a,b):
    "Checks that a and be are compatible types"
    ## int a, int b
    ## int a, float b
    ## float a, int b
    ## float a, float b
    ## tuple a, tuple b
    if isinstance(a,int) and isinstance(b,int):
        return True
    if isinstance(a,int) and isinstance(b,float):
        return True
    if isinstance(a,float) and isinstance(b,int):
        return True
    if isinstance(a,float) and isinstance(b,float):
        return True
    if isinstance(a,tuple) and isinstance(b,tuple):
        return True
    return False

def is_expression(x):
    "Checks that x is a valid expression"
    assert isinstance(x, int) or isinstance(x, float) or isinstance(x, tuple), "Error:  invalid expression"

def is_list(x):
    "Checks that x is a valid list"
    assert isinstance(x, tuple), "Error:  Invalid list"

def is_scalar(x):
    "Checks that x is a scalar"
    assert isinstance(x, int) or isinstance(x, float), "Error:  invalid scalar"
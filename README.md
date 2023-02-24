# About PLY Calcx
PLY Calcx was written by Nicholas Jacobs.  This was completed for a homework assignment for UMaine's Programming Languages class COS 301.  It uses the PLY library (Python Lex Yacc) to specify how to tokenize and parse input from standard input, then executes the calculations for a standard calculator with the running Python instance.  PLY is a Python alternative to Lex and Yacc (Yet another compiler compiler) which are the Unix alternatives to the more popular [GNU Flex](https://www.gnu.org/software/flex/) and [GNU Bison](https://www.gnu.org/software/bison/).  Flex is a lexical analyzer for tokenizing input and Bison is a parser generator.

# Installation
This program was developed in the Anaconda distribution of Python 3.9.

To install the PLY package in your environment run:
```
$ pip install -r requirements.txt
```

# Running PLY Calcx
Just run the `calcx.py` file and type into the terminal.

## Supported Types:
**Scalars:**  Only integer input is supported, but a float might be returned.  
**Lists:**  Comma separated lists of integers are supported as input surrounded by "()".  Lists can contain any arbitrary number of elements or as few as one.  They can optionally be terminated by a trailing comma except lists of length one which must be contain a trailing comma.  PLY Calcx does not support embedded lists.  Here are some examples of lists:  
```
(1,)
(1,2)
(1,2,)
(1,2,3)
```

## Supported Operations:
PLY Calcx only supports operations between two scalars or two lists of equal length.  List operations are applied element-wise.  Scalar expression may be evaluated inside a list.  It supports assignment with duck typing (a variable can at first be assigned a scalar value, but later be reassigned to a list).  Variable names can contain numbers, capital letters, lowercase letters, or underscores, but cannot start with a number.  Here are the supported operations:  
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Integer division (//)
- Modulo (%)
- Negation (-)
- Associativity of scalar and list operations with parenthesis
- Assignment (variable = scalar or list)

# Testing
To test the program run `test.py` which runs the test cases from `test_cases.txt`.

# BNF Grammar
Here is the formal grammar for the calculator program:
```
<statement> ::= <name> "=" <expression>
             |  <expression>

<expression> ::= <expression> "+" <expression>
              |  <expression> "-" <expression>
              |  <expression> "*" <expression>
              |  <expression> "/" <expression>
              |  <expression> "%" <expression>
              |  <expression> "//" <expression>
              |  "-" <expression>
              |  "(" <expression> ")"
              |  <number>
              |  <name>
              |  <vec>

<vec> ::= "(" ")"
       |  <lvec> <expression> ")"
       |  <lvec> ")"

<lvec> ::= "(" <expression> ","
        |  <lvec> <expression> ","

```

# Attributions
PLY Calcx is an extension of the [calculator example](https://github.com/dabeaz/ply/blob/master/example/calc/calc.py) in the PLY docs.
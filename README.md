# This is The Grammar

```
statement : NAME "=" expression
          | expression

expression : expression "+" expression
           | expression "-" expression
           | expression "*" expression
           | expression "/" expression
           | expression "%" expression
           | expression DIV expression
           | "-" expression                    # High precedence
           | "(" expression ")"
           | NUMBER
           | NAME
           | vec

vec : "(" ")"                        # Empty list
    | Lvec expression ")"
    | Lvec ")"

# Left Vector
Lvec : "(" expression ","
     | Lvec expression ","

```
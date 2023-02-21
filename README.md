# This is The Grammar

```
statement : NAME "=" s_expression
          | s_expression
          | NAME "=" vec
          | vec

vec : vec "+" vec
    | vec "-" vec
    | vec "*" vec
    | vec "/" vec
    | vec "%" vec
    | vec DIV vec
    | "-" vec                        # High precedence
    | "(" vec ")"
    | "(" ")"                        # Empty list
    | Lvec s_expression ")"
    | Lvec ")"

# Left Vector
Lvec : "(" s_expression ","
     | Lvec s_expression ","

s_expression : s_expression "+" s_expression
           | s_expression "-" s_expression
           | s_expression "*" s_expression
           | s_expression "/" s_expression
           | s_expression "%" s_expression
           | s_expression DIV s_expression
           | "-" s_expression                    # High precedence
           | "(" s_expression ")"
           | NUMBER
           | NAME

```
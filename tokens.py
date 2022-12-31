from enum import Enum
import pdb

all_tokens={
    ' ':'SPACE',
    '/n':'NEXT_LINE',
    '(' :'STARTPARE',
    ')':'ENDPARE',
    '{':'STARTBRACE',
    '}':'ENDBRACE',
    ':':'COLON',
    '*':'MUL',
    '+':'PLUS',
    '-':'MINUS',
    '=':'EQUAL',
    '/':'DIV',
    '==':'LOGICAL_EQUAL',
    '>':'GREATER',
    '<':'LOWER',
    '>=':'GREATER_EQUAL',
    '<=':'LOWER_EQUAL',
    '||':'OR',
    '&&':'AND',
    'void':'VOID',
    'class':'CLASS',
    'for':'FOR',
    'while':'WHILE',
    'int':'INT',
    'float':'FLOAT',
    'double':'DOUBLE',
    'string':'STRING',
    'return':'RETURN'
}


compare_tokens={
    '>':'GREATER',
    '<':'LOWER',
    '=':'EQUAL',
}

line_specifire={';':'SEMI_COLON'}
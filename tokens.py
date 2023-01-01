from enum import Enum
import pdb

all_tokens={
    '#include':'INCLUDE',
    'using':'USING',
    'namespace':'NAMESPACE',
    '[':'START_BRAKET',
    ']':'END_BRAKET',
    '"':'QUETU',
    ' ':'SPACE',
    '\n':'NEXT_LINE',
    '(' :'STARTPARE',
    ')':'ENDPARE',
    '{':'STARTBRACE',
    '}':'ENDBRACE',
    ':':'COLON',
    ';':'SEMI_COLON',
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
    '<<':"DOUBLE_LW",
    '>>':"DOUBLE_GT",
    '&&':'AND',
    'void':'VOID',
    'class':'CLASS',
    'for':'FOR',
    'while':'WHILE',
    'int':'INT',
    'float':'FLOAT',
    'double':'DOUBLE',
    'string':'STRING',
    'return':'RETURN',
    '.':'DOT',
    ',':'COMMA',
    'main':'MAIN',
    'cout':"COUT"
}


double_operator_tokens={
    '>':'GREATER',
    '<':'LOWER',
    '=':'EQUAL',
    '|':'OR',
    '&':'AND',
    '/':'SLASH',
    '*':'STAR'
}

block_start_list=['{','[','(']

block_end_list=['}',']',')']
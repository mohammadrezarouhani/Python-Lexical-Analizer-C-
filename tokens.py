from enum import Enum
import pdb

class DelimiterTokens(Enum):
    STARTPARE='('
    ENDPARE=')'
    STARTBRACE='{'
    ENDBRACE='}'
    COLON=':'


class OpertorTokens(Enum):
    MUL='*'
    PLUS='+'
    MINUS='-'
    EQUAL='='
    DIV='/'


class LogicalTokens(Enum):
    LOGICAL_EQUAL='=='
    GREATER='>'
    LOWER='<'
    GREATER_EQUAL='>='
    LOWER_EQUAL='<='
    

class ScopeKeyWordTokens(Enum):
    DEF='def'
    CLASS='class'
    FOR='for'
    WHILE='while'


class SimpleKeyWordTokens(Enum):
    RETURN='return'


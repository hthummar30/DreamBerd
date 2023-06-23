import ply.lex as lex

tokens = (
    'CONST',
    'VAR',
    'DELETE',
    'REVERSE',
    'ASYNC',
    'FUNCT',
    'USE',
    'NEW',
    'CLASS',
    'CLASSNAME',
    'PRINT',
    'EQUALS',
    'PREVIOUS',
    'NEXT',
    'AFTER',
    'AWAIT',
    'NOOP',
    'EXCLAMATION',
    'IDENTIFIER',
    'NUMBER',
    'STRING',
)

# Regular expression rules for simple tokens
t_CONST = r'const'
t_VAR = r'var'
t_DELETE = r'delete'
t_REVERSE = r'reverse'
t_ASYNC = r'async'
t_FUNCT = r'funct'
t_USE = r'use'
t_NEW = r'new'
t_CLASS = r'class'
t_CLASSNAME = r'className'
t_PRINT = r'print'
t_EQUALS = r'='
t_PREVIOUS = r'previous'
t_NEXT = r'next'
t_AFTER = r'after'
t_AWAIT = r'await'
t_NOOP = r'noop'
t_EXCLAMATION = r'!'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = str(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
const var name = "Hello"!
delete "Hello"!
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break    # No more input
    print(tok)

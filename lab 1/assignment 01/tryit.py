import re

# Function to check if a string is a keyword
def is_keyword(word):
    keywords = ["auto", "break", "case", "char", "const", "continue", "default",
                "do", "double", "else", "enum", "extern", "float", "for", "goto",
                "if", "int", "long", "register", "return", "short", "signed",
                "sizeof", "static", "struct", "switch", "typedef", "union",
                "unsigned", "void", "volatile", "while"]
    return word in keywords

# Function to check if a string is an identifier
def is_identifier(word):
    return bool(re.match(r'^[a-zA-Z_]\w*$', word))

# Function to check if a string is a constant
def is_constant(word):
    return bool(re.match(r'^\d+$', word))

# Function to check if a string is an arithmetic operator
def is_arithmetic_operator(char):
    return char in "+-*/%="

# Function to check if a string is a logical operator
def is_logical_operator(word):
    return word in [">", ">=", "<", "<=", "==", "!="]

# Function to check if a string is a punctuation
def is_punctuation(char):
    return char in ";:,"

# Function to check if a string is a parenthesis
def is_parenthesis(char):
    return char in "(){}[]"

def analyze_lexical(filename):
    key_string = set()
    iden_string = set()
    con_string = set()
    arith_string = set()
    log_string = set()
    pun_string = set()
    paren_string = set()

    with open(filename, 'r') as file:
        j = 0
        com_flag = 0
        log_flag = 0
        comment = ''
        log = '$'
        for line in file:
            for ch in line:
                # Comment
                if ch == '/':
                    com_flag += 1
                    if com_flag == 1:
                        comment = '/'
                        continue
                if com_flag == 1:
                    arith_string.add(comment)
                    comment = ''
                    com_flag = 0
                elif com_flag == 2 and ch == '\n':
                    com_flag = 0
                    comment = ''
                    continue
                elif com_flag == 2:
                    continue

                # Logical operator
                if ch in ('>', '<', '=', '!') and log == '$':
                    log_flag += 1
                    log = ch
                    continue
                if log_flag == 1 and ch != '=':
                    log_flag = 0
                    log = '$'
                if log_flag == 1 and ch == '=':
                    log_string.add(log + ch)
                    log_flag = 0
                    log = '$'

                # Parenthesis
                if ch in "(){}[]":
                    paren_string.add(ch)

                # Punctuation
                if ch in ";:,":
                    pun_string.add(ch)

                # Arithmetic operator
                if ch in "+-*/%=":
                    arith_string.add(ch)

                # Word or character
                if ch.isalnum() or ch in "+-*/":
                    j += 1
                elif ch == ' ' or ch == '\n':
                    word = line.strip()
                    if is_keyword(word):
                        key_string.add(word)
                    elif is_identifier(word):
                        iden_string.add(word)
                    elif is_constant(word):
                        con_string.add(word)
                    j = 0

    print("Keyword [{}]: {}".format(len(key_string), ", ".join(key_string)))
    print("Identifier [{}]: {}".format(len(iden_string), ", ".join(iden_string)))
    print("Arithmetic operator [{}]: {}".format(len(arith_string), ", ".join(arith_string)))
    print("Logical operator [{}]: {}".format(len(log_string), ", ".join(log_string)))
    print("Constant [{}]: {}".format(len(con_string), ", ".join(con_string)))
    print("Punctuation [{}]: {}".format(len(pun_string), ", ".join(pun_string)))
    print("Parenthesis [{}]: {}".format(len(paren_string), ", ".join(paren_string)))

# Analyze lexical
analyze_lexical("input.txt")

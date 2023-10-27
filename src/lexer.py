import json
from enum import Enum
from collections import deque
class TokenType(Enum):
    Number          = 0
    Identifier      = 1
    Let             = 2
    OpenParen       = 3
    CloseParen      = 4
    Equals          = 5
    BinaryOperator  = 6
    EOF             = 7

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type

    def __str__(self):
        return f"{{ value: '{self.value}', type: {self.type.value} }}"

def getSourceCode() -> str:
    res = ''
    try:
        with open("../test/source_code.txt", "r") as file:
            res = file.read()
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f"An error occured: {e}")
    return res
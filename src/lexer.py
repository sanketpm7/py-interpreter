from enum import Enum

class TokenType(Enum):
    Number = 1
    Identifie = 2
    Let = 3
    OpenParen = 4
    CloseParen = 5
    Equals = 6
    BinaryOperato = 7
    EOF = 8

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type

    def __str__(self):
        return f"{{ {self.value} : {self.type} }}"


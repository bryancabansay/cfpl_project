from rply.token import BaseBox
from global_vars import *

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class Assignment():
    def __init__(self, identifier, value, data_type):
        self.identifier =identifier.strip()
        self.value = value
        self.data_type = data_type.strip()

    def eval(self):
        if 'AS_INT' in self.data_type:
            variables[self.identifier] = int(self.value)
        elif 'AS_FLOAT' in self.data_type:
            variables[self.identifier] = float(self.value)
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
    def __init__(self, data, data_type):
        self.data      = data
        self.data_type = data_type.strip()

    def eval(self):        
        for item in self.data:                
            if 'AS_INT' in self.data_type:
                variables[item['identifier']] = int(item['value'])
            elif 'AS_FLOAT' in self.data_type:
                variables[item['identifier']] = float(item['value'])
            elif 'AS_CHAR' in self.data_type:
                value = item['value'].replace("'", "")
                if value == '0':
                    variables[item['identifier']] = ''
                elif len(value) > 1:
                    raise Exception("Improper char value.")
                else:
                    variables[item['identifier']] = value
            elif 'AS_BOOL' in self.data_type:
                value = item['value'].replace("\"","")
                if value == "TRUE":                    
                    variables[item['identifier']] = True
                elif value == "FALSE":
                    variables[item['identifier']] = False
                else:
                    raise Exception("Improper boolean value.")
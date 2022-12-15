import math

def multi(*args):
    mult = 1
    for i in args:
        mult = mult * i
    print(mult)

multi(20,20,10)
import random #For testing sortAr
import numpy #Used for math functions
import os
import sys
import time
from libs.Parser import parse

def random_sign():
    num = random.randrange(0, 4)

    if num == 1:
        return '-'
    if num == 2:
        return '*'
    if num == 3:
        return '/'
    if num == 4:
        return '^'

    return '+'

def testing():
    equation = ''
    random.seed(time.time())
    equation += str(random.randrange(-400, 0))
    index = 0
    for index in range(random.randrange(1, 15)):
        equation += random_sign()
        equation += str(random.randrange(-200, 200))
    
    print('equation: ' + equation)

    result = parse(equation)
    return result

test = False

#if this is the main script
if __name__ == "__main__":
    alive = True
    args = sys.argv
    if((len(args) > 1 and args[1] == "test") or test == True):
        print(testing())
        alive = False
        input('press enter key to coninue...')
    
    while alive:
        print("Write your equation:")
        val = input()
        result = parse(val)

        print(f'result = {result}')
        input('press enter key to continue...')
        os.system('clear')

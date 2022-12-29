import random #For testing sortAr
import numpy #Used for math functions
import os

parserId = 0

#return parserId and increment it by 1
def getId():
    global parserId
    id = parserId
    parserId += 1
    return id


def sum(i, tks):
    val = float(tks[i-1][1]) + float(tks[i+1][1])
    return (2, val)

def sub(i, tks):
    val = float(tks[i-1][1]) - float(tks[i+1][1])
    return (2, val)

def mul(i, tks):
    val = float(tks[i-1][1]) * float(tks[i+1][1])
    return (2, val)

def div(i, tks):
    x = tks[i-1][1]
    y = tks[i+1][1]
    val = float(tks[i-1][1]) / float(tks[i+1][1])
    return (2, val)

def pow(i, tks):
    val = numpy.float_power(float(tks[i-1][1]), float(tks[i+1][1]))
    return (2, val)

#inverse sort based on priority of sign tokens. Returns number of iterations
def sortAr(array):
    #index is the pointer of the array, using it to get x element of the array
    index = 0
    #number of iterations in the array for measuring performance
    iterations = 0
    #while pointer of array is within the array size
    while index < len(array):
        #Need to skip index 0 because getting "last" from array would be getting "array[-1]"
        if(index == 0):
            index += 1
            continue
        last = array[index-1]
        actual = array[index]

        #if priority of actual sign is greater than the last, swap last sign with actual and decrement 1 position of the array pointer variable(index)
        if(actual[1] > last[1]):
            array[index-1] = actual
            array[index] = last
            index -= 1
            iterations += 1
            continue
        index += 1

    return iterations

#(token_type, value, id)
tokens = []
#(sign, func, priority)
signs = [('+', sum, 0), ('-', sub, 0), ('*', mul, 1), ('/', div, 1), ('^', pow, 2)]

#returns index from an array tokens from an "id" variable(int). Returns index or -1 if not found
def find_id(id):
    index = 0
    for index in range(len(tokens)):
        if(tokens[index][0] == 2):
            continue
        if(tokens[index][2] == id):
            return index
    return -1

#Check if "val" is a number by "catching" a "ValueError". Returns bool
def is_int(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False

#Check list of signs looking for a sign string match, and return the ftuple of said sign. Returns tuple(string, func, priority) or 0 if none found
def parse_sign(sign):
    for elem in signs:
        if(sign == elem[0]):
            return elem
    return 0

#Parse the equation (string)"text" attributing tokens for each numbers and signs into (array)"tokens"
def parse(text):
    #index is the pointer for getting each character from text
    index = 0
    #0 - none, 1 - sign, 2 - number
    token_type = 0

    #parsed_text is the value of the current to-be token
    parsed_text = ""

    for index in range(len(text)):
        actual = text[index]
        try:
            last = text[index-1]
        except:
            last = '/0'

        try:
            next = text[index+1]
        except:
            next = '/0'

        isNum = is_int(text[index])

        #Check if number has decimals, if it has then just skip checking for sign.
        if(actual == '.'):
            parsed_text += actual
            continue

        #Check if "actual" is a minus sign and if it is to represent a negative number
        if(actual == '-' and not is_int(last) and is_int(next)):
            #if the current token type is a sign then saves it
            if(token_type == 1):
                tokens.append((token_type, parsed_text, getId()))
                parsed_text = ""
            
            #Start to record the new token and skip other checks
            token_type = 2
            parsed_text += text[index]
            continue

        #Check if current to-be token is sign and current character is a number or vice-versa
        if((token_type == 1 and isNum) or (token_type == 2 and not isNum)):
            #save current token and continue
            if(token_type == 1):
                tokens.append((token_type, parsed_text, getId()))
            else:
                tokens.append((token_type, parsed_text))
            token_type = 0
            parsed_text = ""

        #if current to-be token is NULL then verify if "actual" is a number or sign, then attribue it to the "token_type"
        if(token_type == 0):
            if(isNum):
                token_type = 2
                #print('setting up tokentype as number')
            else:
                token_type = 1
                #print('setting up tokentype as sign')

        #adds the current character to the value of current to-be token
        parsed_text += text[index]

    #Add the last token to the list(Necessary because this function only add to the token list when the next token_type is different from the actual, and the loop ends without
    #adding the last token)
    if(token_type == 1):
        tokens.append((token_type, parsed_text, getId()))
    else:
       tokens.append((token_type, parsed_text))

    solve()

def solve():
    #signsInstances -> list that will be populated with the index and priorities of "tokens"'s signs
    #index -> pointer that will iterate through "tokens"
    signsInstances = []
    index = 1

    #loop through tokens
    while index < len(tokens):
        #if the token's type equals the "sign type(1)"
        if(tokens[index][0] == 1):
            parsedSign = parse_sign(tokens[index][1])
            
            #if the sign doesn't exist in the list 
            if(parsedSign == 0):
                print(f'Error trying to parse {tokens[index]}')
                return -1

            #append to the "signsInstances" list a tuple that contais an "id" and the priority of the sign
            signsInstances.append((tokens[index][2], parsedSign[2]))
        #increment 1 to the token's pointer
        index += 1

    iterations = sortAr(signsInstances)
    print(f'sorted array with {iterations} iterations')

    print(f'array before solving: {tokens}')

    #reset index to iterate through "signsInstances"
    index = 0
    #loop until "tokens" length equals 1
    while len(tokens) != 1:
        #get pointed sign position at "tokens" array
        SignIndex = find_id(signsInstances[index][0])
        print(f'array: {tokens}')

        #get token from "tokens" array using SignIndex
        SIElem = tokens[SignIndex]
        print(f'working at token: {SIElem}')

        #get the function of the sign and run it
        func = parse_sign(SIElem[1])[1]
        result = func(SignIndex, tokens)
        print(f'result: {result}')

        #set the result to the left number of the sign
        tokens[SignIndex-1] = result
        
        print(f'removing tokens[1-{tokens[SignIndex]}, 2-{tokens[SignIndex+1]}')
        #remove the sign and right number from "tokens"
        tokens.pop(SignIndex+1)
        tokens.pop(SignIndex)

        index += 1
    return

#if this is the main script
if __name__ == "__main__":
    while 1:
        print("Write your equation:")
        tokens = []
        val = input()
        parse(val)

        print(f'result = {tokens[0]}')
        input('press any key to continue...')
        os.system('clear')

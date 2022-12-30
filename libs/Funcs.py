import numpy

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

#(sign, func, priority)
signs = [('+', sum, 0), ('-', sub, 0), ('*', mul, 1), ('/', div, 1), ('^', pow, 2)]

#Check list of signs looking for a sign string match, and return the tuple of said sign. Returns tuple(string, func, priority) or 0 if none found
def signExists(sign):
    for elem in signs:
        if(sign == elem[0]):
            return elem
    return 0

#iterates through tokens and copy all signs into another array. Return tuple(id, priority) of sign array
def getSigns(tokens):
    #signsInstances -> list that will be populated with the index and priorities of "tokens"'s signs
    #index -> pointer that will iterate through "tokens"
    signsInstances = []
    index = 1

    #loop through tokens
    while index < len(tokens):
        #if the token's type equals the "sign type(1)"
        if(tokens[index][0] == 1):
            parsedSign = signExists(tokens[index][1])
            
            #if the sign doesn't exist in the list 
            if(parsedSign == 0):
                print(f'Error trying to parse {tokens[index]}')
                return -1

            #append to the "signsInstances" list a tuple that contais an "id" and the priority of the sign
            signsInstances.append((tokens[index][2], parsedSign[2]))
        #get next tokens
        index += 1
    return signsInstances

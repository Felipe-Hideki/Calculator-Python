from . import Utilities, Funcs, Id

#Parse the equation (string)"text" attributing tokens for each numbers and signs into (array)"tokens"
def parse(text):
    #(token_type, value, id)
    tokens = []
    #index is the pointer for getting each character from text
    index = 0
    #0 - none, 1 - sign, 2 - number
    token_type = 0

    #parsed_text is the value of the current to-be token
    parsed_text = ""

    for index in range(len(text)):
        actual = text[index]

        if(index == 0):
            last = '\0'
        else:
            last = text[index-1]

        if(index == len(text)-1):
            next = '\0'
        else:
            next = text[index+1]

        isNum = Utilities.is_int(text[index])

        #Check if number has decimals, if it has then just skip checking for sign.
        if(actual == '.'):
            parsed_text += actual
            continue

        #Check if "actual" is a minus sign and if it is to represent a negative number
        if(actual == '-' and not Utilities.is_int(last) and Utilities.is_int(next)):
            #if the current token type is a sign then saves it
            if(token_type == 1):
                tokens.append((token_type, parsed_text, Id.getId()))
                parsed_text = ""
            
            #Start to record the new token and skip other checks
            token_type = 2
            parsed_text += text[index]
            continue

        #Check if current to-be token is sign and current character is a number or vice-versa
        if((token_type == 1 and isNum) or (token_type == 2 and not isNum)):
            #save current token and continue
            if(token_type == 1):
                tokens.append((token_type, parsed_text, Id.getId()))
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
        tokens.append((token_type, parsed_text, Id.getId()))
    else:
       tokens.append((token_type, parsed_text))

    solve(tokens)
    return tokens[0]

#Solve equations contained in tokens
def solve(tokens):
    #signsInstances -> list that will be populated with the index and priorities of "tokens"'s signs
    #index -> pointer that will iterate through "tokens"
    signsInstances = Funcs.getSigns(tokens)

    if(signsInstances == -1):
        return -1
    
    iterations = Utilities.sortAsc(signsInstances)

    #print(f'sorted array with {iterations} iterations')

    #print(f'array before solving: {tokens}')

    #reset index to iterate through "signsInstances"
    index = 0
    #loop until "tokens" length equals 1
    while len(tokens) != 1:
        #get pointed sign position at "tokens" array
        SignIndex = Id.find_id(tokens, signsInstances[index][0])
        #print(f'array: {tokens}')

        #get token from "tokens" array using SignIndex
        SIElem = tokens[SignIndex]
        #print(f'working at token: {SIElem}')

        #get the function of the sign and run it
        func = Funcs.signExists(SIElem[1])[1]
        result = func(SignIndex, tokens)
        #print(f'result: {result}')

        #set the result to the left number of the sign
        tokens[SignIndex-1] = result
        
        #print(f'removing tokens[1-{tokens[SignIndex]}, 2-{tokens[SignIndex+1]}')
        #remove the sign and right number from "tokens"
        tokens.pop(SignIndex+1)
        tokens.pop(SignIndex)

        index += 1

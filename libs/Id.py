parserId = 0

#returns index from an array tokens from an "id" variable(int). Returns index or -1 if not found
def find_id(tokens, id):
    index = 0
    for index in range(len(tokens)):
        if(tokens[index][0] == 2):
            continue
        if(tokens[index][2] == id):
            return index
    return -1

#return parserId and increment it by 1
def getId():
    global parserId
    id = parserId
    parserId += 1
    return id
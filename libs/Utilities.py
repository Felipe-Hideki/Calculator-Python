#Check if "val" is a number by "catching" a "ValueError". Returns bool
def is_int(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False

#inverse sort based on priority of sign tokens. Returns number of iterations
##May be removed later, substituting it with sort function from array
def sortAsc(array):
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
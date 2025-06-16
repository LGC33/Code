values = [5,3,7,9,2]
def min_index(values):
    minval = values[0]
    idx= 0
    for i in range(0, len(values)):
        if values[i] < minval:
            minival = values[i]
            idx = i
    return i 

hello = min_index(values)

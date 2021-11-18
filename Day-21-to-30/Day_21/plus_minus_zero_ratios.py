
def plusMinusRatio(arr):
    pos, neg, zeros = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zeros += 1
    return pos/len(arr), neg/len(arr), zeros/len(arr)

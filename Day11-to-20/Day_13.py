#jump search algorithm
from math import sqrt
def jumpSearch( arr, x , n ):
    # Computing the size to be jumped
    step = sqrt(n)   
    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += sqrt(n)
        if prev >= n:
            return -1
    # Doing a linear search for x in 
    # block beginning with prev.
    while arr[int(prev)] < x:
        prev += 1
        # If we reached next block or end 
        # of array, element is not present.
        if prev == min(step, n):
            return -1

#Day 13

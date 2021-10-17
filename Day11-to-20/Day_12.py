# binary search algorithm
def binary_search(list, find_value):
    low = 0
    high = len(list)
    # starting the loop to find the value
    while low <= high:
        # finding the middle index of the list
        mid = (low + high)//2
        '''If the element to be searched 
is smaller than the element present at the mid
index, move end to mid-1, and all RHS will get
discarded.'''
        if list[mid] < find_value:
            low = mid
        '''If the element to be searched
 is greater than the element present at the mid
 index, move beg to mid+1, and all LHS will get 
 discarded.
        elif list[mid] > find_value:
            high = mid
        #if they match return the index.
        else:
            return mid


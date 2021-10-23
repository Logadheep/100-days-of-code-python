#bubble sort
#slowest sorting algorithm
#complexity == О(n**2)
#complexity is О(n) when t list is already sorted.
def bubbleSort(arr):
    #computing no of elements in the array
    n = len(arr)
    # starting the loop
    for i in range(n):
        # nesting loop based on i value...
        for j in range(0, n-i-1):
            #swapping values if the values are
            # not in the order
        
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    #return sorted array
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
 
print(bubbleSort(arr))

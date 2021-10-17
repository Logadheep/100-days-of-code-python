# Fibonacci search...
# similar to binary
def fibonaccianSearch(arr, x, n):
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
    """fibM is going to store the smallest Fibonacci
 Number greater than or equal to n"""
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    # Marks the eliminated range from front
    offset = -1
    while (fibM > 1):
        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)
        """If x is greater than the value at index fibMm2, 
cut the subarray array from offset to i""" 
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        """If x is less than the value at index fibMm2, 
cut the subarray after i+1"""
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        # element found. return index
        else:
            return i
    # comparing the last element with x 
    if(fibMMm1 and arr[n-1] == x):
        return n-1
    # element not found. return -1
    return -1

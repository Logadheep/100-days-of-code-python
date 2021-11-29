'''
Function Description:-

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
'''
"""
Input Format
A single integer, , denoting the size of the staircase.

Constraints
Output Format
Print a staircase of size  using # symbols and spaces.
Note: The last line must have  spaces in it.
"""
def staircase(n):
    i = 0
    while i <= n:
        if i == 0:
            i += 1
            continue
        print(' ' * (n - i) + '#' * i)
        i += 1

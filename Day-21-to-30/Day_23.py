#############################
######## MIN MAX SUM ########
#############################

"""
Function Description

Complete the miniMaxSum function in the editor below.
miniMaxSum has the following parameter(s):
arr: an array of  integers

Print
Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
"""
'''
Input Format
A single line of five space-separated integers.

Constraints

Output Format
Print two space-separated long integers denoting the 
respective minimum and maximum values that can be 
calculated by summing exactly four of the five integers. 
(The output can be greater than a 32 bit integer.)
''''
def miniMaxSum(arr):
    x = sum(arr)
    print(x-max(arr), x-min(arr))

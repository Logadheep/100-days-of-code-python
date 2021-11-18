# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''
Function description:-
	Complete the  function in the editor below.
	diagonalDifference takes the following parameter:
		int arr[n][m]: an array of integers
Return:-
	int: the absolute diagonal difference
'''
"""
Input Format:-
	The first line contains a single integer, , the number of rows and columns in the square matrix .
	Each of the next  lines describes a row, , and consists of  space-separated integers .
Output Format:-
	Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
"""


def diagonalDifference():
    N = int(input())
    total = 0
    for i in range(N):
        row = input().split()
        total += int(row[i])-int(row[-(i+1)])
    return abs(total)

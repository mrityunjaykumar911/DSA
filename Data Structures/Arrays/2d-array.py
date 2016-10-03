# coding=utf-8

"""
    Created by mrityunjayk on 3/10/16.

    Website: 
    
    -----------------------------------------------------------------
    Problem Statement: 
        
            Context  Given a  2D Array, :  1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:  a b c   d e f g There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.  Task  Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
     
    Example:
            nput Format  There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .  Constraints  Output Format  Print the largest (maximum) hourglass sum found in .    Sample Input  1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0  Sample Output  19 
    
    -----------------------------------------------------------------
    Category: Array

"""


class Solution:
    def __init__(self):
        self.class_name = "2d-array"

    def __str__(self):
        return self.class_name

    def findSolution(self):
        arr = []
        for arr_i in xrange(6):
            arr_temp = map(int, raw_input().strip().split(' '))
            arr.append(arr_temp)
        from sys import maxint
        max_sum = -maxint - 2
        for i in xrange(4):
            for j in xrange(4):
                sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
                if sum > max_sum:
                    max_sum = sum
        return max_sum


s = Solution()
print s.findSolution()
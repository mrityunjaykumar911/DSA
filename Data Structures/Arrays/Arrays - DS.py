# coding=utf-8

"""
    Created by mrityunjayk on 3/10/16.

    Website: https://www.hackerrank.com/challenges/arrays-ds
    
    -----------------------------------------------------------------
    Problem Statement: 
        
            An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  (you may also see it written as ).  Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.
     
    Example:
            Sample Input  4 1 4 3 2 Sample Output  2 3 4 1
    
    -----------------------------------------------------------------
    Category: Arrays

"""

# Hackerrank
class Solution:
    def __init__(self):
        self.class_name = "Arrays - DS"

    def __str__(self):
        return self.class_name

    def findSolution(self):
        # TODO adding raw input source
        n = int(raw_input().strip())
        arr = raw_input().strip().split()
        arr.reverse()
        return ' '.join(arr)


s = Solution()
print s.findSolution()
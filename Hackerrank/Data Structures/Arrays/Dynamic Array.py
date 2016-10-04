# coding=utf-8

"""
    Created by mrityunjayk on 3/10/16.

    Website: https://www.hackerrank.com/challenges/dynamic-array
    
    -----------------------------------------------------------------
    Problem Statement: 
        
            Create a list, , of  empty sequences, where each sequence is indexed from  to . The elements within each of the  sequences also use -indexing. Create an integer, , and initialize it to . The  types of queries that can be performed on your list of sequences () are described below: Query:  Find the sequence, , at index  in . Append integer  to sequence . Query:  Find the sequence, , at index  in . Find the value of element  in  (where  is the size of ) and assign it to . Print the new value of  on a new line Task  Given , , and  queries, execute each query.
     
    Example:
            Input Format  The first line contains two space-separated integers,  (the number of sequences) and  (the number of queries), respectively.  Each of the  subsequent lines contains a query in the format defined above. Sample Input  2 5 1 0 5 1 1 7 1 0 3 2 1 0 2 1 1 Sample Output  7 3
    
    -----------------------------------------------------------------
    Category: Array

"""


class Solution:
    def __init__(self):
        self.class_name = "Dynamic Array"

    def __str__(self):
        return self.class_name

    def take_input(self, number_of_input_rows=1, input_type=int):
        taken_input = []
        for i in xrange(number_of_input_rows):
            try:
                arr_temp = map(input_type, raw_input().strip().split(' '))
            except:
                arr_temp = list()
            taken_input.extend(arr_temp)
        return taken_input

    def findSolution(self):
        N, Q = self.take_input()
        seq0 = []
        seq1 = []
        lastAns = 0
        while Q:
            a, x, y = self.take_input()
            seq = (x ^ lastAns) % N
            print seq
            if a == 1:
                if seq == 0:
                    seq0.append(y)
                    print seq0
                elif seq == 1:
                    seq1.append(y)
                    print seq1
            elif a == 2:
                lastAns = seq0[seq] % len(seq1)
                print '\n', lastAns
            else:
                continue
            Q -= 1
        return None


s = Solution()
print s.findSolution()

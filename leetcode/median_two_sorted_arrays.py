# coding=utf-8
"""Problem Statement

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


Approach #1 Recursive Approach [Accepted]
To solve this problem, we need to understand "What is the use of median". In statistics, the median is used for:

Dividing a set into two equal length subsets, that one subset is always greater than the other.

If we understand the use of median for dividing, we are very close to the answer.

First let's cut \text{A}A into two parts at a random position ii:

          left_A             |        right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
Since \text{A}A has mm elements, so there are m+1m+1 kinds of cutting (i = 0 \sim mi=0∼m).


"""


class Solution(object):
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
            nums1 = [1, 2]
            nums2 = [3, 4]
            The median is (2 + 3)/2 = 2.5

            nums1 = [1, 3]
            nums2 = [2]
            The median is 2.0
        """

        return self.NaiveSolution(nums1, nums2)

    def NaiveSolution(self, nums1, nums2):
        """
            Naive solution:
                Merge the array, sort it and find the median
        """
        # merged array
        merged = nums1 + nums2

        # sort array
        merged = sorted(merged)

        return self.findMedian(merged)

    def findMedian(self, merged):
        # if len is even
        n = len(merged)
        if not n:
            raise Exception("Empty list")
        if n % 2 == 0:
            return (merged[n / 2 - 1] + merged[n / 2]) / 2.0
        else:
            return merged[n / 2]
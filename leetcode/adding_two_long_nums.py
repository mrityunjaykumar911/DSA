"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = int(x)
        self.next = None

    def __iter__(self):
        temp = self
        while temp is not None:
            yield temp.val
            temp = temp.next

    def __eq__(self, other):
        temp = self
        temp2 = other
        while temp is not None and temp2 is not None:
            if temp.val == temp2.val:
                temp = temp.next
                temp2 = temp2.next
                continue
            else:
                return False
        if temp is not None:
            return False
        if temp2 is not None:
            return False
        return True

    @staticmethod
    def create(number):
        list_of_nums = list(str(number))
        if len(list_of_nums) is 0:
            return ListNode(-1)
        # get start node
        start = list_of_nums[0]
        start_node = ListNode(start)
        start_node_save = start_node.copy()
        for each in list_of_nums[1:]:
            this_node = ListNode(each)
            start_node.next = this_node
            start_node = this_node

        return start_node_save

    def copy(self):
        return self


class Solution(object):
    def get_last(self, answer):
        temp = answer
        while temp.next:
            temp = temp.next
        return temp

    def addTwoNumbers(self, l, r):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        answer = None

        while l and r:

            sum = carry + l.val + r.val
            carry = sum / 10
            if not answer:
                answer = ListNode(sum % 10)
            else:
                temp = self.get_last(answer)
                temp.next = ListNode(sum % 10)
            l = l.next
            r = r.next

        while l:
            each = l.val + carry
            carry = each / 10
            each = each % 10
            if not answer:
                answer = ListNode(each)
            else:
                temp = self.get_last(answer)
                temp.next = ListNode(each)
            l = l.next

        while r:
            each = r.val + carry
            carry = each / 10
            each = each % 10
            if not answer:
                answer = ListNode(each)
            else:
                temp = self.get_last(answer)
                temp.next = ListNode(each)
            r = r.next
        if carry != 0:
            temp = self.get_last(answer)
            temp.next = ListNode(carry)

        return answer


if __name__ == "__main__":
    ex = ListNode.create(12345)
    for each in ex:
        print(each)

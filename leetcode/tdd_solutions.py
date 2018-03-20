# import section
from leetcode.adding_two_long_nums import ListNode, Solution as additive
from leetcode.jewels_and_stones import Solution as jewels
from median_two_sorted_arrays import Solution as median


def test_case_1():
    # Median of two sorted arrays
    list1 = [1, 3]
    list2 = [2]
    answer = median().findMedianSortedArrays(nums1=list1, nums2=list2) == 2.0
    assert answer is True


def test_case_2():
    # addition of two numbers
    num1 = ListNode.create(8765432100)
    num2 = ListNode.create(1234567890)
    answer_here = additive().addTwoNumbers(num1, num2)
    answer = answer_here == ListNode.create(9999999990)
    assert answer is True


def test_case_3():
    # jewels and stones
    J = "aA"
    S = "aaZZ~!`A"
    answer = jewels().numJewelsInStones(J, S) == 3
    assert answer is True


def test_case_4():
    pass


def test_case_5():
    pass


def test_case_6():
    pass


def test_case_7():
    pass


def test_case_8():
    pass


if __name__ == "__main__":
    pass

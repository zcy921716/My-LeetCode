"""
You are given two non-empty linked lists representing two non-negative
integers.

The digits are stored in reverse order and each of their nodes contain a single
 digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        flag = 0
        p = l1
        q = l2
        k = ListNode(0)
        kk = k

        while p or q:

            if p:
                x = p.val
                p = p.next
            else:
                x = 0

            if q:
                y = q.val
                q = q.next
            else:
                y = 0

            tmp = flag + x + y
            flag = int(tmp / 10)
            kk.next = ListNode(tmp - flag * 10)

            kk = kk.next

        else:
            if flag == 1:
                kk.next = ListNode(1)

            return k.next

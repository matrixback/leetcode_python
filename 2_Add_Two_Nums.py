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
        curry = 0
        result = ListNode(0)   # 哑节点
        ahead = result
        while l1 and l2:
            sum = l1.val + l2.val + curry
            remainder = sum % 10
            curry = sum // 10
            node = ListNode(remainder)
            ahead.next = node
            ahead = node
            l1, l2 = l1.next, l2.next

        if l2:    # 此时 l1 为 None。
            l1 = l2

        while l1:
            sum = l1.val + curry
            remainder = sum % 10
            curry = sum // 10
            node = ListNode(remainder)
            ahead.next = node
            ahead = node
            l1 = l1.next

        if curry:
            node = ListNode(curry)
            ahead.next = node

        return result.next
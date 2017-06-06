# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def list_size(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        # 开始处理
        if not head:
            return True  
        length = list_size(head)
        middle = length / 2
		# 创建一个哑节点，方便处理
        h1 = ListNode(0)
        while middle:
            next = head.next
            head.next = h1
            h1 = head
            head = next
            middle -= 1
        # 一半之后的链表  
        h2 = head        
        if length % 2 != 0:
            h2 = h2.next
        middle = length / 2
        while middle:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
            middle -= 1
        else:
            return True
        
    
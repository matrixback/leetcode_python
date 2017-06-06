"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

**思路：**典型的快慢指针问题。
"""
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution(object):
	    def hasCycle(self, head):
	        """
	        :type head: ListNode
	        :rtype: bool
	        """
	        if not head:
	            return False
	            
	        quick = head
	        slow = head
	        while True:
	            if (not quick.next) or (not quick.next.next):
	                return False
	            quick = quick.next.next
	            slow = slow.next
	            if quick == slow:
	                return True
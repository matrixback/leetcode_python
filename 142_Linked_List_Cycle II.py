"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

**思路：**这道题需要一点数学推导。假设换的入口距 head 的距离为 M，环的大小为 C，快慢指针相遇处距离环入口处为 N。那么根据快慢指针的性质，2（M + N） = M + N + nC，得到：M = （n-1)C + (C-N)。这意味着如果快指针再走 M 步，那么一定在环的入口处。 为了简便，不计算 M 的大小，再次利用两个指针，让新指针从 head 处走 M，快指针再走 M 步，他们会在入口处相遇的。

"""
	# Definition for singly-linked list.
	# class ListNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	
	class Solution(object):
	    def detectCycle(self, head):
	        """
	        :type head: ListNode
	        :rtype: ListNode
	        """
	        if not head:
	            return
	        
	        quick = slow = head
	        while True:
	            if (not quick.next) or (not quick.next.next):
	                return 
	            quick = quick.next.next
	            slow = slow.next
	            if quick == slow:
	                break
	        # 如果能到此处，那么必定有环。
	        slow = head
	        while slow != quick:
	            slow = slow.next
	            quick = quick.next
	        return slow
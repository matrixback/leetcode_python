# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  链表的插入排序，思路是新开一个表头，就旧链的节点依次插入新头
#  用了一个哑节点，可以不用，判断一下 parent is None 即可。
#
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        new_head = ListNode(0)    
        while head is not None:
            node = head
            head = head.next
            current = new_head.next
            parent = new_head

            while current is not None and current.val < node.val:
                parent = current
                current = current.next
            parent.next = node
            node.next = current

        return new_head.next
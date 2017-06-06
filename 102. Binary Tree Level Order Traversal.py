Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

**思路：**层次遍历需要用一个队列保存前面已经访问过的节点的左右子树。

	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution(object):
	    def levelOrder(self, root):
	        """
	        :type root: TreeNode
	        :rtype: List[List[int]]
	        """
	        if not root:
	            return []
	            
	        from collections import deque
	        nums = []
	        cur_nums = []
	        q = deque()
	        q.append(root)
	        cur_cnt = 1
	        next_level_cnt = 0
	        while len(q)>0:
	            root = q.popleft()
	            cur_cnt -= 1
	            cur_nums.append(root.val)
	            if root.left:
	                next_level_cnt += 1
	                q.append(root.left)
	            if root.right:
	                next_level_cnt += 1
	                q.append(root.right)
	            
	            if cur_cnt <= 0:
	                nums.append(cur_nums)
	                cur_nums = []
	                cur_cnt = next_level_cnt
	                next_level_cnt = 0
	        return nums
            
        
        
        
        
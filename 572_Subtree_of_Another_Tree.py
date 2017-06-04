Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Given tree s:

	     3
	    / \
	   4   5
	  / \
	 1   2
Given tree t:

	   4 
	  / \
	 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

	     3
	    / \
	   4   5
	  / \
	 1   2
	    /
	   0
Given tree t:

	   4
	  / \
	 1   2
Return false.

**思路：**一棵树是不是另一棵树的子树。注意，是子树，而不是子结构。子树要求和另一棵树的子树完全相同，而不是另一棵树的一部分。


	# Definition for a binary tree node.
	# class TreeNode(object):
	#     def __init__(self, x):
	#         self.val = x
	#         self.left = None
	#         self.right = None
	
	class Solution(object):
	    def isSubtree(self, s, t):
	        """
	        :type s: TreeNode
	        :type t: TreeNode
	        :rtype: bool
	        """
	        def isSameTree(t1, t2):
	            # t2 遍历结束则结束 
	            if (not t1) and (not t2):
	                return True
	            if t1 and t2:
	                return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
	            return False
	        
	        if not t:
	            return True
	        if not s:
	            return False
	            
	        if isSameTree(s, t):
	            return True
	        if self.isSubtree(s.left, t):
	            return True
	        elif self.isSubtree(s.right, t):
	            return True
	        else:
	            return False

如果是一部分：

	class Solution(object):
	    def isSubtree(self, s, t):
	        """
	        :type s: TreeNode
	        :type t: TreeNode
	        :rtype: bool
	        """
	        def doesHasTree(t1, t2):
	            # 主要的区别在这儿，t2 结束则整个判断结束 
	            if not t2:
	                return True
	            if t1:
	                return t1.val == t2.val and doesHasTree(t1.left, t2.left) and doesHasTree(t1.right, t2.right)
	            return False
	        
	        if not t:
	            return True
	        if not s:
	            return False
	            
	        if doesHasTree(s, t):
	            return True
	        if self.isSubtree(s.left, t):
	            return True
	        elif self.isSubtree(s.right, t):
	            return True
	        else:
	            return False
    
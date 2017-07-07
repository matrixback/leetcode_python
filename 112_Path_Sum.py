# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		def inorder(node, cursum):
			if not node:
				return False
			cursum += node.val
			if (not node.left) and (not node.right) and (cursum == sum):
				return True
			left = False
			right = False
			if node.left:
				left = inorder(node.left, cursum)
			if node.right:
				right = inorder(node.right, cursum)
			return left or right
		return inorder(root, 0)
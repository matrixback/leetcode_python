# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def post_order(node):
            if not node:
                return True, 0
            
            left_result, left_depth = (True, 0)
            right_result, right_depth = (True, 0)
            if node.left:
                left_result, left_depth = post_order(node.left)
            if node.right:
                right_result, right_depth = post_order(node.right)
            cur_result = left_result and right_result and (-1<= left_depth - right_depth <= 1)
            cur_max_depth = max(left_depth, right_depth) + 1
            return cur_result, cur_max_depth
        result, _ = post_order(root)
        return result
        
                
                
        
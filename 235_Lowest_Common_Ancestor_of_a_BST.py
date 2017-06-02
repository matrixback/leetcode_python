# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        def post_order(root):
            if not root:
                return None

            left, right = None, None
            if root.left:
                left = post_order(root.left)
            if root.right:
                right = post_order(root.right)

            if (root in [p, q]) or (left and right) :
                return root
            elif (not left) and (not right):
                return None
            else:
                return left if left else right

        return post_order(root)
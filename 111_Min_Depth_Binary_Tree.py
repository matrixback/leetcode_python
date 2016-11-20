# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 思路：
# 可以用层次遍历做，效率最好。用一个变量记录深度，当碰到没有儿子的节点时，返回当前深度。
# 当前为了方便，用了递归的方法，左右子树碰到第一个没有儿子的节点时返回，然后比较谁小。

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        return self.minDepthRecu(root, depth)

    def minDepthRecu(self, root, depth):
        if root is None:
            return depth
        elif root.left is None and root.right is None:
            return depth+1
        elif root.left is None:
            return self.minDepthRecu(root.right, depth+1)
        elif root.right is None:
            return self.minDepthRecu(root.left, depth+1)
        else:
            return min(self.minDepthRecu(root.left, depth+1), \
                       self.minDepthRecu(root.right, depth+1))

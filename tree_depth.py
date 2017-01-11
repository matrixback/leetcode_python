# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        
        child_depth = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
        return child_depth + 1
test it
这道题用递归做的话比较简单，注意递归时，怎么抽象。
一般二叉树的题目将每个节点看做一个抽象单元。

用递归的方法，时间复杂度太大，可以用层次遍历的方法，这样时间复杂度为O(n), n 为根节点数。

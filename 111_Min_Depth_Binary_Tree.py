# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# ˼·��
# �����ò�α�������Ч����á���һ��������¼��ȣ�������û�ж��ӵĽڵ�ʱ�����ص�ǰ��ȡ�
# ��ǰΪ�˷��㣬���˵ݹ�ķ�������������������һ��û�ж��ӵĽڵ�ʱ���أ�Ȼ��Ƚ�˭С��

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

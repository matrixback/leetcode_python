# coding: utf-8
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        cols = len(array[0])

        right = cols - 1
        top = 0
        while right >= 0 and top < rows:
            if array[top][right] == target:
                return True
            elif array[top][right] < target:
                top += 1
            else:
                right -= 1
        else:
            return False
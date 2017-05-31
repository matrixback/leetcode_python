class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x *= -1

        res = 0
        while x != 0:
            mod = x % 10
            x = x / 10
            res = res * 10 + mod
        res *= flag
        if (res > 2147483647) or (res < -2147483647):
            return 0
        return res
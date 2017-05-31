class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        cnt = 1
        while cnt < n:
            a, b = b, a+b
            cnt += 1
        return b`

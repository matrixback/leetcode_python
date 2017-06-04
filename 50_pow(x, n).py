Implement pow(x, n).

**思路：**利用幂的性质，pow(x, n) = pow(x, n/2) * pow(x, n/2)，进行递归计算，因为分解后的两个因子相等，所以可计算计算次数。

	class Solution(object):
	    def myPow(self, x, n):
	        """
	        :type x: float
	        :type n: int
	        :rtype: float
	        """       
	        def positive_pow(x, n):
	            if n <= 1:
	                return x
	                
	            half = n/2
	            half_pow = positive_pow(x, half)
	            
	            if n % 2 == 0:
	                return half_pow * half_pow
	            else:
	                return half_pow * half_pow * x
	
	        if n == 0:
	            return 1
	        elif n < 0:
	            return 1/positive_pow(x, n*(-1))
	        else:
	            return positive_pow(x, n)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        
        str = str.strip()
        flag = 1
        if str[0] == '-':
            flag = -1
        if str[0] in ['-', '+']:
            str = str[1:]
        
        res = 0
        for num in str:
            if not num.isdigit():
                break
            res = res*10 + int(num)
            
        res *= flag
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648
        return res
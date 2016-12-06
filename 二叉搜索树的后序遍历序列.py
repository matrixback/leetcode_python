class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False     # ���Ϊ�գ��򷵻�False�����Ժ����ж���������ʱ���������ж��Ƿ�Ϊ�գ�����֤������ݹ���ȥ����False��

        pivot = sequence[-1]
        low = []
        high = []
        
        bi = 0
        for i, v in enumerate(sequence):
            if v < pivot:
                low.append(v)
            else:
                bi = i
                break
            
        for v in sequence[bi:len(sequence) - 1]:
            if v > pivot:
                 high.append(v)
            else:
                return False

        left = True
        if low:
            left = self.VerifySquenceOfBST(low)
            
        right = True
        if high:
            right = self.VerifySquenceOfBST(high)
            
        return left and right

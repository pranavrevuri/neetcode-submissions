class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        
        temp = 1

        while temp <= n:
            temp *= 2
            if temp == n:
                return True
        

        return False

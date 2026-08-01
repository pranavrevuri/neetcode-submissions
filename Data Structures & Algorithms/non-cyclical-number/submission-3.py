class Solution:
    import math
    def isHappy(self, n: int) -> bool:
        total_count = set()

        def check(current):
            if current == 1:
                return True
            
            if current in total_count:
                return False
            
            total_count.add(current)
        
            total = 0
            for i in str(current):
                num = int(i)
                total += num**2
            
            return check(total)
        
        return check(n)
            
        
        
        


        

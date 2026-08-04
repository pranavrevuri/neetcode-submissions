class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k) -> int:
            return sum(math.ceil(p / k) for p in piles)
        
        low, high = 1, max(piles)

        while low < high:
            k = (low + high) // 2

            if hours_needed(k) <= h:
                high = k
            else:
                low = k + 1
        
        return low


            


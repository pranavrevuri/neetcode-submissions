class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(mid):
            return sum(math.ceil(p / mid) for p in piles)
        
        lo, high = 1, max(piles)

        while lo < high:
            mid = (lo + high) // 2
            
            if hours_needed(mid) <= h:
                high = mid
            else:
                lo = mid + 1
        
        return lo
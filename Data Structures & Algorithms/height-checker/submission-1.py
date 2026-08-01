class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorts = sorted(heights)
        res = 0
        
        for i in range(len(heights)):
            if heights[i] != sorts[i]:
                res += 1
        
        return res
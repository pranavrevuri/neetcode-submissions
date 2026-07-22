class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0

        while l < r:
            vol = (r-l)*min(heights[l],heights[r])
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            most = max(most, vol)
        
        return most
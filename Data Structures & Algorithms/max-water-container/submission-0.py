class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most_stored = 0

        while left < right:
            can_store = (right - left) * min(heights[left], heights[right])
            if can_store > most_stored:
                most_stored = can_store
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return most_stored

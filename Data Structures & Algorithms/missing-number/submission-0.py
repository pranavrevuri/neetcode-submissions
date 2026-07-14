class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        needed = (n*(n+1)) / 2

        for i in nums:
            total += i
        
        return int(needed - total)


        

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = 0
        cur = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] <= nums[i-1]:
                cur = 0
            cur += nums[i]

            best = max(cur, best)
            

        return best
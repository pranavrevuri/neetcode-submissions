class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = n * [0]
        suffix = n * [0]
        res = n * [0]
        
        prod = 1
        for i in range(n):
            prefix[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(n-1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]
            res[i] = prefix[i] * suffix[i]
        
        return res
        

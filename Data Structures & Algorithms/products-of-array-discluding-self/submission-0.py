class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        result = []
        n = len(nums)
        running = 1
        for i in range(n):
            prefix.append(running)
            running = running * nums[i]
        
        back_run = 1
        for i in range(n - 1, -1, -1):
            suffix.insert(0, back_run)
            back_run = back_run * nums[i]
        
        for i in range(n):
            result.append(prefix[i] * suffix[i])
        
        return result

        
        

            
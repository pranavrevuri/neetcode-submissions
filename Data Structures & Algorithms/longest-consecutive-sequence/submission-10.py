class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)

        for num in nums:
            if num-1 not in nums:
                seq = 1
                while num+1 in nums:
                    seq += 1
                    num = num + 1
                best = max(seq, best)
        
        return best
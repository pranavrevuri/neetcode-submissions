class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                seq = 1
                while i+1 in nums:
                    seq += 1
                    i += 1
                longest = max(seq, longest)
        
        return longest
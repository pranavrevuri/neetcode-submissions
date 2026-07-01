class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                seq = 1
                while num+1 in nums:
                    seq += 1
                    num += 1

                if seq > longest:
                    longest = seq
        
        return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        curr_seq_len = 1
        max_seq = curr_seq_len
        for i in nums:
            if i-1 not in nums:
                start = i
                curr_seq_len = 1
                while start+1 in nums:
                    curr_seq_len += 1
                    start += 1
                    if curr_seq_len > max_seq:
                        max_seq = curr_seq_len
        return max_seq
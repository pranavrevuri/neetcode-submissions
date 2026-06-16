class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_ss = 0
        left = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            window_len = right-left+1

            if window_len - max(count.values()) <= k:
                if window_len > longest_ss:
                    longest_ss = window_len
            else:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1

        return longest_ss


                

        
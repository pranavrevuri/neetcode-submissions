class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_substring = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            window_length = right - left + 1

            if window_length > longest_substring:
                longest_substring = window_length
        
        return longest_substring
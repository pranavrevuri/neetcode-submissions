class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            win_len = r - l + 1

            if win_len - max(freq.values()) <= k:
                if win_len > longest:
                    longest = win_len
            else:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1
        
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        best = 0

        for right in range(len(s)):
            if s[right] in window:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
                    
            
            window.add(s[right])
            
            length = right - left + 1
            if length > best:
                best = length
        
        return best
            


        

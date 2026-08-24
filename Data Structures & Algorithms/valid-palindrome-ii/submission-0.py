class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(inp):
            l = 0
            r = len(inp) - 1

            while l < r:
                if inp[l] != inp[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        if isPalindrome(s):
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                check1str = s[:left] + s[left+1:]
                if isPalindrome(check1str):
                    return True
                
                check2str = s[:right] + s[right+1:]
                if isPalindrome(check2str):
                    return True
                
            
            left += 1
            right -= 1
        
        return False

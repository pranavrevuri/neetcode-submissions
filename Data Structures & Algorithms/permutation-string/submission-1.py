class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26

        for char in s1:
            num = ord(char) - ord('a')
            s1_freq[num] += 1
        
        s2_freq = [0] * 26
        for i in range(len(s1)):
            num = ord(s2[i])- ord('a')
            s2_freq[num] += 1
        
        if s1_freq == s2_freq:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            s2_freq[ord(s2[left]) - ord('a')] -= 1
            left += 1
            s2_freq[ord(s2[right]) - ord('a')] += 1
            if s1_freq == s2_freq:
                return True
        
        return False
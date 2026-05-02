class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        n = len(s)

        for i in range(n):
            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1
            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1

        for char in s:
            if s_freq[char] != t_freq.get(char, 0):
                return False

        return True
        
            

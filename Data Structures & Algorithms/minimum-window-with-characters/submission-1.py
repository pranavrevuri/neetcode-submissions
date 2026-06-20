class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_count = {}
        need = set()
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
            need.add(c)
        
        l = 0
        window = {}
        shortest = len(s)
        have = 0
        start = -1

        for r in range(len(s)):
            if s[r] in t_count:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == t_count[s[r]]:
                    have += 1
            
            while have == len(need):
                if r-l+1 <= shortest:
                    shortest = r-l+1
                    start = l

                if s[l] in t_count:
                    window[s[l]] -= 1
                    if window[s[l]] < t_count[s[l]]:
                        have -= 1
                l += 1

        
        return s[start:start+shortest] if start != -1 else ""
            




        

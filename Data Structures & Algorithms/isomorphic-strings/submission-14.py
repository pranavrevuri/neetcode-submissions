class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_dict = {}

        for i in range(len(s)):
            if s[i] not in my_dict and t[i] not in my_dict.values():
                my_dict[s[i]] = t[i]
            else:
                if s[i] in my_dict and my_dict[s[i]] != t[i]:
                    return False
        
        mapped_str = ""

        for i in s:
            if i in my_dict:
                mapped_str += my_dict[i]
        
        return mapped_str == t
                

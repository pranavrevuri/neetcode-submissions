class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag_dict = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
        
            key = tuple(count)

            if key not in ag_dict:
                ag_dict[key] = []
            
            ag_dict[key].append(word)
        
        return list(ag_dict.values())
        
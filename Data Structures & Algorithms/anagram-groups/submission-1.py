class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag_map = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            
            if key not in ag_map:
                ag_map[key] = []
            
            ag_map[key].append(word)
        
        return list(ag_map.values())
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        res = []

        for word in strs:
            freq = [0] * 26
            for char in word:
                num = ord(char) - ord('a')
                freq[num] += 1
            
            key = tuple(freq)

            if key not in my_dict:
                my_dict[key] = []
        
            my_dict[key].append(word)
        
        return list(my_dict.values())
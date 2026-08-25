class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        res = []

        for word in strs:
            char_freq = [0] * 26
            for char in word:
                ind = ord(char) - ord('a')
                char_freq[ind] += 1

            tup = tuple(char_freq)
            if tup not in my_dict:
                my_dict[tup] = [word]
            else:
                my_dict[tup].append(word)
        
        for value in my_dict.values():
            res.append(value)
        
        return res
        

        


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        my_dict = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            freq_conv = tuple(freq)
            if freq_conv not in my_dict:
                my_dict[freq_conv] = [word]
            else:
                my_dict[freq_conv].append(word)
        

        return list(my_dict.values())
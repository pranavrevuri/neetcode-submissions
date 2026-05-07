class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag_map = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)

            if key not in ag_map:
                ag_map[key] = []
            
            ag_map[key].append(word)
            
        return list(ag_map.values())

# Logic
# 1) Create a hash map for key(frequency of characters in string) and values (words that match that frequency)
# 2) Iterate through each word in the given list of strings
# 3) Create a 0 array of size 26 for frequency of each letter in string
# 4) Iterate through each char in word
# 5) For values in the array, use ord(char) - ord("a"), this adds 1 in exact position in array
# 6) Convert that array to tuple because lisst cant be keys in dictionaries
# 7) Check if key is in map, otherwise add key to map
# 8) Append word to that key
# 9) Convert map values to list and return it
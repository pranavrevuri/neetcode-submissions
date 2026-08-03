class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True

        my_dict = {}
        
        for word in words:
            for char in word:
                my_dict[char] = my_dict.get(char, 0) + 1
        
        for val in my_dict.values():
            if val % len(words) != 0:
                return False
        
        return True
        
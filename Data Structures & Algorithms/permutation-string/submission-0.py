class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        my_dict = {}

        freq_s1 = [0] * 26
        for char in s1:
            char_num = ord(char) - ord('a')
            freq_s1[char_num] += 1
        
        freq_s1 = tuple(freq_s1)
        my_dict[freq_s1] = 1
        
        window_size = len(s1)
        for i in range(len(s2) - window_size + 1):
            j = i
            win_freq = [0] * 26
            end = j + window_size
            while j < end:
                j_num = ord(s2[j]) - ord('a')
                win_freq[j_num] += 1
                j += 1
            win_freq = tuple(win_freq)
            if win_freq in my_dict:
                return True
        
        return False
        

                


        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []       
        freq = [[] for _ in range(len(nums) + 1)]
        my_dict = {}

        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        for key, value in my_dict.items():
            freq[value].append(key)
        
        n = 0
        for i in range(len(freq)-1, 0, -1):
            if freq[i] != []:
                for num in freq[i]:
                    if n == k:
                        break
                    res.append(num)
                    n += 1
                    
        
        return res




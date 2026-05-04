class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            if nums[i] not in my_map:
                my_map[nums[i]] = 1
            else:
                my_map[nums[i]] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for key, count in my_map.items():
            freq[count].append(key)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

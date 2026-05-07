class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for key, count in my_dict.items():
            freq[count].append(key)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
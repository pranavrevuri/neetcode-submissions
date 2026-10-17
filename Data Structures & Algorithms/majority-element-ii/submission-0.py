class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        needed = len(nums) // 3

        ht = {}

        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        
        res = []

        for key, value in ht.items():
            if value > needed:
                res.append(key)
        
        return res


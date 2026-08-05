class Solution:
    def findLucky(self, arr: List[int]) -> int:
        my_dict = {}
        res = 0

        for num in arr:
            my_dict[num] = my_dict.get(num, 0) + 1

        cur = 0
        for key, value in my_dict.items():
            if key == value:
                cur = value
            res = max(cur, res)

        return res if res != 0 else -1
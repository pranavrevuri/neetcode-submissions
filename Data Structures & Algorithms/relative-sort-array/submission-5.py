class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for num in arr2:
            while num in arr1:
                res.append(num)
                arr1.remove(num)
        
        arr1.sort()
        for num in arr1:
            res.append(num)
        return res
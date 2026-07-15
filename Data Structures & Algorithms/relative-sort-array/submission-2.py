class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for num in arr2:
            temp_num = arr1.count(num)
            for i in range(temp_num):
                res.append(num)
        
        temp = []
        for num in arr1:
            if num not in set(res):
                temp.append(num)
        
        temp.sort()

        res.extend(temp)

    
        
        return res
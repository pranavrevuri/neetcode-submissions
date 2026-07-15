class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for num in arr2:
            temp_num = arr1.count(num)
            for i in range(temp_num):
                res.append(num)
                arr1.remove(num)
        
    
        res.extend(sorted(arr1))

    
        
        return res
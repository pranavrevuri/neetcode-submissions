class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] <= target:
                left = mid + 1
                if target <= matrix[mid][-1]:
                    return self.binarySearch(matrix[mid], target)
            else:
                right = mid - 1
        
        return False
                
        
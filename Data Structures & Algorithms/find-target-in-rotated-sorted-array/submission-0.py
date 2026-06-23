class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left != right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
        
        pivot_pos = left

        if target == nums[pivot_pos]:
            return pivot_pos
        elif target >= nums[pivot_pos] and nums[-1] >= target:
            left = pivot_pos
            right = len(nums) - 1
        else:
            left = 0
            right = pivot_pos
        
        while (left < right):
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        if nums[left] == target:
            return left
        
        return -1
                

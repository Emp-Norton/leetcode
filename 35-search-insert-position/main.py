# Naive solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
             return 0
        vals = {num:index for (index, num) in enumerate(nums)}
        lowest_matched_index = 0
        for num in vals:
            if target == num:
                return vals[num]
            else:
                if target > num:
                    lowest_matched_index = vals[num]
        return lowest_matched_index + 1



# Optimized binary-search (iterative):
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

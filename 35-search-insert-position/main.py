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

# TODO:
	# Potential optimization:
	        # divide and conquer to achieve logN runtime
        # set search_ind = len(nums)/2
        # if num > nums[search_ind]
            # repeat with right-split array
        # else
            # repeat with left-split_Array

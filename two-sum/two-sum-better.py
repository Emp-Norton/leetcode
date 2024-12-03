class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_copy = sorted(nums)
        low_idx = 0
        high_idx = len(nums) - 1
        for i in range(len(nums_copy)):
            low_val = nums_copy[low_idx]
            high_val = nums_copy[high_idx]
            sum = low_val + high_val
            if sum > target:
                high_idx -= 1
            elif sum < target:
                low_idx += 1
            else:
                target_low = nums_copy[low_idx]
                target_high = nums_copy[high_idx]
                
        first_idx, second_idx = None, None
        for i in range(len(nums)):
            print(i)
            if nums[i] == target_low:
                if first_idx is None:
                    first_idx = i
                    continue
            if nums[i] == target_high:
                if second_idx is None:
                    second_idx = i
                    continue
        return [first_idx, second_idx]


# Note: This beats 57% of submissions, it can absolutely be improved. It's also a mess. 

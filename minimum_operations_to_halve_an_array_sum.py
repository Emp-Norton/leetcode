class Solution(object):
    def halveArray(self, nums):
        nums = sorted(map(float, nums), reverse=True)
        total_sum = sum(nums)
        target = total_sum / 2
        leftovers = []
        tally = 0
        ops = 0
        idx_nums, idx_leftovers = 0, 0
        while tally < target:
            if idx_leftovers >= len(leftovers) or (idx_nums < len(nums) and leftovers[idx_leftovers] < nums[idx_nums]):
                item_to_eat = nums[idx_nums]
                idx_nums += 1
            else:
                item_to_eat = leftovers[idx_leftovers]
                idx_leftovers += 1
            eaten = item_to_eat / 2
            tally += eaten
            ops += 1
            leftovers.append(eaten)
        return ops

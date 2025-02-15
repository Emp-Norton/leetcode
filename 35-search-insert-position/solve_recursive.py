class Solution:
	def searchInsert(nums, target):
	    def binary_search(left, right):
	        if left > right:
	            return left
	            
	        mid = (left + right) // 2
	        
	        if nums[mid] == target:
	            return mid
	        elif nums[mid] < target:
	            return binary_search(mid + 1, right)
	        else:
	            return binary_search(left, mid - 1)
	            
	    return binary_search(0, len(nums) - 1)

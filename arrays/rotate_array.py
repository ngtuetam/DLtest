class Solution:
    def rotate(nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if k > len(nums):
        #     k = k - len(nums)

        k = k % len(nums)
            
        def reverse(nums, left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # Reverse the whole array
        reverse(nums, 0, len(nums) - 1)
		# Reverse the first part
        reverse(nums, 0, k-1)
		# Reverse the second part
        reverse(nums, k, len(nums)-1)
		# Reverse the whole array
        # reverse(nums, 0, len(nums) - 1)
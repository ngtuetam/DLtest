class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] !=0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j+=1
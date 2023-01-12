# find pivot then search
class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        l = 0
        r = n -1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l = 0
        r = n -1
        if target <= nums[r]:
            l = pivot
        else:
            r = pivot

        while (l<=r):
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if target > nums[m]:
                l = m +1
            else:
                r = m -1
        return -1



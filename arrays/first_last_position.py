# Given a sorted array of integers, return the low and high index of the given element.
class Solution:
    def searchRange(self, nums, target: int):
        def first(nums, target: int) -> int:
            n = len(nums)
            l = 0
            r = n - 1
            res = -1
            while (l<=r):
                m = l + (r-l)//2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    res = m
                    r = m - 1
            return res
        def last(nums, target: int) -> int:
            n = len(nums)
            l = 0
            r = n - 1
            res = -1
            while (l<=r):
                m = l + (r-l)//2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    res = m
                    l = m + 1
            return res
        res = []
        res.append(first(nums,target))
        res.append(last(nums,target))
        return res
        

"""
Problem: https://leetcode.com/problems/search-insert-position/?envType=study-plan&id=algorithm-i
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = l + ((r-l)//2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
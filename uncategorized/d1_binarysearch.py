"""
Problem: https://leetcode.com/problems/binary-search/?envType=study-plan&id=algorithm-i
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
            else: 
                return m
        return -1
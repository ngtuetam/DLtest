"""
Problem: https://leetcode.com/problems/squares-of-a-sorted-array/?envType=study-plan&id=algorithm-i
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        res = []
        while i <= j:
            if nums[i]**2 <= nums[j]**2:
                num = nums[j]*nums[j]
                res = [num] + res
                j-=1
            else:
                num = nums[i]*nums[i]
                res = [num] + res
                i+=1
        return res

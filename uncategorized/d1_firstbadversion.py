"""
Problem: https://leetcode.com/problems/first-bad-version/description/
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n):
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            mid = l + ((r-l)//2)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
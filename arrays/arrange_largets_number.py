# create a custom sort, edge case is when all element is 0
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        def cmp(a,b):
            if a+b >= b+a:
                return 1
            else:
                return -1
        nums = map(str,nums)
        res = "".join(sorted(nums, key=cmp_to_key(cmp), reverse=True))
        if res[0] == "0":
            return "0"
        return res
        
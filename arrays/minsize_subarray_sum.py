# sliding window

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        l = 0
        sub_sum = 0
        res = n + 1 
        for r in range(len(nums)):
            sub_sum += nums[r]
            while sub_sum >= target:
                res = min(res, (r-l+1))
                sub_sum -= nums[l]
                l+=1
        return 0 if res == n+1 else res
